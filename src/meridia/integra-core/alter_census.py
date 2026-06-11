
import asyncio, asyncpg

DB = dict(host="192.168.0.160", port=5433, database="meridia_core",
          user="meridia", password="Ethanj2020##")

ALTER_STMTS = [
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS income_level VARCHAR(20)",
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS ffiec_income_pct NUMERIC(6,2)",
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS msa_code VARCHAR(10)",
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS msa_mfi INTEGER",
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS tract_mfi INTEGER",
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS opportunity_score NUMERIC(5,2)",
    "ALTER TABLE census_tracts ADD COLUMN IF NOT EXISTS msa_name VARCHAR(100)",
    "CREATE INDEX IF NOT EXISTS idx_ct_msa ON census_tracts(msa_code)",
    "CREATE INDEX IF NOT EXISTS idx_ct_dist ON census_tracts(is_distressed)",
]

async def main():
    conn = await asyncpg.connect(**DB)
    for stmt in ALTER_STMTS:
        try:
            await conn.execute(stmt)
            print(f"  OK: {stmt[:60]}")
        except Exception as e:
            print(f"  SKIP: {str(e)[:60]}")

    # Verify columns
    cols = await conn.fetch(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_name='census_tracts' AND table_schema='public' ORDER BY ordinal_position"
    )
    print(f"\ncensus_tracts columns ({len(cols)}):")
    print("  " + ", ".join(r['column_name'] for r in cols))
    await conn.close()

asyncio.run(main())
