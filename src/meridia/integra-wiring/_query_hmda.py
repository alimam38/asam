import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)
cur = conn.cursor()

print("=== HMDA_LOANS COLUMNS ===")
cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='hmda_loans' ORDER BY ordinal_position")
for r in cur.fetchall():
    print(" ", r[0], "-", r[1])

print("\n=== Q1a: NULL CHECK ON institution_name ===")
cur.execute("SELECT COUNT(*) FROM hmda_loans WHERE institution_name IS NULL OR institution_name = ''")
print("  null/empty institution_name rows:", cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM hmda_loans WHERE institution_name IS NOT NULL AND institution_name != ''")
print("  populated institution_name rows:", cur.fetchone()[0])

print("\n=== Q1b: SAMPLE lei VALUES ===")
cur.execute("SELECT DISTINCT lei FROM hmda_loans WHERE lei IS NOT NULL LIMIT 10")
for r in cur.fetchall():
    print(" ", r[0])

print("\n=== Q1: LEI + LOAN COUNTS (institution_name is unpopulated) ===")
cur.execute("""
    SELECT lei, COUNT(*) as loan_count
    FROM hmda_loans
    GROUP BY lei
    ORDER BY loan_count DESC
    LIMIT 20
""")
rows = cur.fetchall()
if rows:
    for r in rows:
        print(f"  {str(r[0]):<55} {r[1]:>6}")
else:
    print("  (no rows)")

print("\n=== Q2: CENSUS TRACTS WITH ZERO HMDA ACTIVITY ===")
cur.execute("""
    SELECT COUNT(*) as zero_activity_tracts
    FROM census_tracts ct
    LEFT JOIN hmda_loans h ON h.census_tract = ct.geoid
    WHERE h.census_tract IS NULL
""")
print(" ", cur.fetchone()[0])

print("\n=== Q3: LMI OR DISTRESSED TRACTS WITH NO LOANS ===")
cur.execute("""
    SELECT COUNT(*) as lmi_or_distressed_no_loans
    FROM census_tracts ct
    LEFT JOIN hmda_loans h ON h.census_tract = ct.geoid
    WHERE h.census_tract IS NULL
    AND (ct.is_lmi = true OR ct.is_distressed = true)
""")
print(" ", cur.fetchone()[0])

cur.close()
conn.close()
