import os, requests
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# ── Step 1: pull top 20 LEIs from the DB ─────────────────
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)
cur = conn.cursor()
cur.execute("""
    SELECT lei, COUNT(*) as loan_count
    FROM hmda_loans
    GROUP BY lei
    ORDER BY loan_count DESC
    LIMIT 20
""")
rows = cur.fetchall()
cur.close(); conn.close()

leis = [r[0] for r in rows]
counts = {r[0]: r[1] for r in rows}

# ── Step 2: batch GLEIF lookup ────────────────────────────
url = "https://api.gleif.org/api/v1/lei-records"
params = {
    "filter[lei]": ",".join(leis),
    "page[size]": 20,
}
resp = requests.get(url, params=params, timeout=30)
resp.raise_for_status()
payload = resp.json()

# ── Step 3: parse names from JSON:API response ────────────
resolved = {}
for record in payload.get("data", []):
    lei_val = record["attributes"]["lei"]
    name = record["attributes"]["entity"]["legalName"]["name"]
    resolved[lei_val] = name

# ── Step 4: show results ──────────────────────────────────
print(f"{'LEI':<25} {'LOAN COUNT':>10}  INSTITUTION NAME")
print("-" * 90)
missing = []
for lei, count in rows:
    name = resolved.get(lei, "NOT FOUND")
    if name == "NOT FOUND":
        missing.append(lei)
    print(f"{lei:<25} {count:>10}  {name}")

print(f"\nResolved: {len(resolved)}/20   Not found: {len(missing)}")
if missing:
    print("Missing LEIs:", missing)

# ── Step 5: create table and insert ──────────────────────
conn2 = psycopg2.connect(
    host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)
cur2 = conn2.cursor()

cur2.execute("""
    CREATE TABLE IF NOT EXISTS institutions (
        lei        VARCHAR(20) PRIMARY KEY,
        legal_name TEXT        NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW()
    )
""")

insert_data = [(lei, resolved[lei]) for lei, _ in rows if lei in resolved]
cur2.executemany(
    "INSERT INTO institutions (lei, legal_name) VALUES (%s, %s) ON CONFLICT (lei) DO NOTHING",
    insert_data,
)
conn2.commit()

cur2.execute("SELECT COUNT(*) FROM institutions")
count = cur2.fetchone()[0]
print(f"\n=== CONFIRMED: {count} rows in institutions table ===")
