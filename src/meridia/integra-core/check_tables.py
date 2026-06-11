
import asyncio
DB_URL = "postgresql+asyncpg://meridia:Ethanj2020##@192.168.0.160:5433/meridia_core"

async def check():
    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy import text
    engine = create_async_engine(DB_URL, echo=False)
    async with engine.connect() as conn:
        r = await conn.execute(text(
            "SELECT table_schema, table_name FROM information_schema.tables "
            "WHERE table_schema NOT IN ('pg_catalog','information_schema') "
            "ORDER BY table_schema, table_name"
        ))
        rows = r.fetchall()
        schemas = {}
        for row in rows:
            schemas.setdefault(row[0], []).append(row[1])
        for schema, tables in schemas.items():
            print(f"Schema: {schema} ({len(tables)} tables)")
            for t in tables:
                print(f"  {t}")
    await engine.dispose()

asyncio.run(check())
