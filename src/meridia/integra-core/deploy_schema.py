
import asyncio
import sys
sys.path.insert(0, r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring')

DB_URL = "postgresql+asyncpg://meridia:Ethanj2020##@192.168.0.160:5433/meridia_core"

async def deploy():
    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy import text

    engine = create_async_engine(DB_URL, echo=False)
    schema_file = r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\schema.sql'

    with open(schema_file, encoding='utf-8') as f:
        sql = f.read()

    # Remove postgis line — not installed on this postgres
    sql = sql.replace("CREATE EXTENSION IF NOT EXISTS \"postgis\"; -- optional for geo queries", "-- postgis skipped")

    # Split and filter
    statements = [s.strip() for s in sql.split(';') if s.strip() and not s.strip().startswith('--')]

    print(f"Deploying {len(statements)} statements...")
    ok = 0
    skip = 0
    warn = 0

    for i, stmt in enumerate(statements):
        # Each statement in its own connection/transaction
        try:
            async with engine.begin() as conn:
                await conn.execute(text(stmt))
            ok += 1
        except Exception as e:
            msg = str(e)
            if any(x in msg for x in ['already exists', 'duplicate', 'does not exist']):
                skip += 1
            else:
                print(f"  WARN [{i+1}]: {msg[:120]}")
                warn += 1

    print(f"Done: {ok} ok, {skip} skipped (already exist), {warn} warnings")

    # Verify tables
    async with engine.connect() as conn:
        result = await conn.execute(text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name"
        ))
        tables = [r[0] for r in result.fetchall()]
        print(f"\nAll tables ({len(tables)}):")
        for t in tables:
            print(f"  {t}")

    await engine.dispose()

asyncio.run(deploy())
