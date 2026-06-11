
import asyncio, asyncpg

async def check():
    conn = await asyncpg.connect(
        host="192.168.0.160", port=5433, database="meridia_core",
        user="meridia", password="Ethanj2020##"
    )
    rows = await conn.fetch(
        "SELECT table_schema, table_name FROM information_schema.tables WHERE table_name='census_tracts'"
    )
    print(f"census_tracts found in {len(rows)} schema(s):")
    for r in rows:
        print(f"  {r['table_schema']}.{r['table_name']}")
        cnt = await conn.fetchval(f"SELECT COUNT(*) FROM {r['table_schema']}.census_tracts")
        print(f"  rows: {cnt:,}")

    # Create it in public if missing
    if not any(r['table_schema'] == 'public' for r in rows):
        print("\nCreating census_tracts in public schema...")
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS census_tracts (
                geoid               VARCHAR(20) PRIMARY KEY,
                state_code          VARCHAR(2),
                county_code         VARCHAR(5),
                tract_name          VARCHAR(100),
                msa_name            VARCHAR(100),
                is_distressed       BOOLEAN DEFAULT FALSE,
                is_underserved      BOOLEAN DEFAULT FALSE,
                is_lmi              BOOLEAN DEFAULT FALSE,
                ffiec_income_pct    NUMERIC(6,2),
                median_hh_income    INTEGER,
                poverty_rate        NUMERIC(5,2),
                population          INTEGER,
                pct_minority        NUMERIC(5,2),
                opportunity_score   NUMERIC(5,2),
                msa_code            VARCHAR(10),
                data_year           INTEGER,
                updated_at          TIMESTAMPTZ DEFAULT NOW()
            )
        """)
        await conn.execute("CREATE INDEX IF NOT EXISTS idx_ct_state ON census_tracts(state_code)")
        await conn.execute("CREATE INDEX IF NOT EXISTS idx_ct_lmi ON census_tracts(is_lmi)")
        print("census_tracts created in public schema")

    await conn.close()

asyncio.run(check())
