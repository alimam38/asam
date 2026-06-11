
import asyncio

DB_URL = "postgresql+asyncpg://meridia:Ethanj2020##@192.168.0.160:5433/meridia_core"

SEED_SQL = [
    """INSERT INTO entities (entity_id, name, tier, entity_type, geography_state, geography_msa)
    VALUES
      ('a1b2c3d4-0001-0001-0001-000000000001'::uuid, 'Vantage Financial Partners', 'institutional', 'institution', 'GA', '12054'),
      ('a1b2c3d4-0002-0002-0002-000000000002'::uuid, 'Hargrove Family Office', 'crown', 'household', 'GA', '12054'),
      ('a1b2c3d4-0003-0003-0003-000000000003'::uuid, 'Cornerstone AME Collective', 'core', 'nonprofit', 'GA', '12054'),
      ('a1b2c3d4-0004-0004-0004-000000000004'::uuid, 'Gulf South Properties LLC', 'edge', 'business', 'GA', '12054'),
      ('a1b2c3d4-0005-0005-0005-000000000005'::uuid, 'Marcus Thompson', 'renaissance', 'individual', 'GA', '12054')
    ON CONFLICT (entity_id) DO NOTHING""",

    """INSERT INTO positions (entity_id, period, fps_score, net_position, liquidity_coverage,
      dscr_score, runway_score, distribution_align, fps_direction, fps_narrative)
    VALUES (
      'a1b2c3d4-0002-0002-0002-000000000002'::uuid,
      '2026-Q1', 78.4, 82.0, 75.0, 71.0, 80.0, 84.0, 'improving',
      'Hargrove Family Office holds a strong financial position at 78.4/100. Liquidity coverage and distribution alignment are leading indicators. The trust corpus is performing above benchmark.'
    ) ON CONFLICT (entity_id, period) DO NOTHING""",

    """INSERT INTO positions (entity_id, period, fps_score, net_position, liquidity_coverage,
      dscr_score, runway_score, distribution_align, fps_direction, fps_narrative)
    VALUES (
      'a1b2c3d4-0001-0001-0001-000000000001'::uuid,
      '2026-Q1', 71.2, 68.0, 74.0, 70.0, 72.0, 72.0, 'stable',
      'Vantage Financial Partners maintains a stable institutional position at 71.2/100. Portfolio distribution is balanced. Three bilateral risk flags require governance attention.'
    ) ON CONFLICT (entity_id, period) DO NOTHING""",

    """INSERT INTO trust_scores (entity_id, period, trust_index, behavioral_consistency,
      governance_adherence, communication_reliability, commitment_fulfillment, direction)
    VALUES (
      'a1b2c3d4-0002-0002-0002-000000000002'::uuid,
      '2026-Q1', 84.2, 88.0, 79.0, 86.0, 84.0, 'improving'
    ) ON CONFLICT (entity_id, period) DO NOTHING""",

    """INSERT INTO trust_scores (entity_id, period, trust_index, behavioral_consistency,
      governance_adherence, communication_reliability, commitment_fulfillment, direction)
    VALUES (
      'a1b2c3d4-0001-0001-0001-000000000001'::uuid,
      '2026-Q1', 76.8, 80.0, 72.0, 78.0, 78.0, 'stable'
    ) ON CONFLICT (entity_id, period) DO NOTHING""",

    """INSERT INTO relationships (rel_id, institution_id, client_id, product_type,
      exposure_amount, risk_direction, risk_score, status)
    VALUES
      ('b1c2d3e4-0001-0001-0001-000000000001'::uuid,
       'a1b2c3d4-0001-0001-0001-000000000001'::uuid,
       'a1b2c3d4-0002-0002-0002-000000000002'::uuid,
       'wealth_management', 2850000.00, 'sound', 84.2, 'active'),
      ('b1c2d3e4-0002-0002-0002-000000000002'::uuid,
       'a1b2c3d4-0001-0001-0001-000000000001'::uuid,
       'a1b2c3d4-0003-0003-0003-000000000003'::uuid,
       'commercial_deposit', 425000.00, 'toward_institution', 58.0, 'active'),
      ('b1c2d3e4-0003-0003-0003-000000000003'::uuid,
       'a1b2c3d4-0001-0001-0001-000000000001'::uuid,
       'a1b2c3d4-0004-0004-0004-000000000004'::uuid,
       'commercial_loan', 1200000.00, 'bilateral', 42.0, 'active'),
      ('b1c2d3e4-0004-0004-0004-000000000004'::uuid,
       'a1b2c3d4-0001-0001-0001-000000000001'::uuid,
       'a1b2c3d4-0005-0005-0005-000000000005'::uuid,
       'checking', 4200.00, 'sound', 71.0, 'active')
    ON CONFLICT (rel_id) DO NOTHING""",

    """INSERT INTO compliance_events (entity_id, regulation, event_type, status, description, due_date)
    VALUES
      ('a1b2c3d4-0001-0001-0001-000000000001'::uuid, 'CRA', 'exam', 'open',
       'Annual CRA examination scheduled. Portfolio must demonstrate qualified activity in LMI tracts.', '2026-06-30'),
      ('a1b2c3d4-0002-0002-0002-000000000002'::uuid, 'HMDA', 'certification', 'in_progress',
       'HMDA LAR certification for prior year activity. 47 reportable transactions pending review.', '2026-03-31')""",
]

async def seed():
    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy import text
    engine = create_async_engine(DB_URL, echo=False)

    ok = skip = warn = 0
    for i, stmt in enumerate(SEED_SQL):
        try:
            async with engine.begin() as conn:
                await conn.execute(text(stmt))
            ok += 1
        except Exception as e:
            msg = str(e)
            if any(x in msg for x in ['already exists', 'duplicate', 'unique', 'conflict']):
                skip += 1
            else:
                print(f"  WARN [{i+1}]: {msg[:120]}")
                warn += 1

    print(f"Seed: {ok} ok, {skip} skipped, {warn} warnings")

    # Verify
    async with engine.connect() as conn:
        r = await conn.execute(text("SELECT name, tier FROM entities ORDER BY tier"))
        rows = r.fetchall()
        print(f"\nEntities ({len(rows)}):")
        for row in rows:
            print(f"  {row[1]:15} {row[0]}")

        r2 = await conn.execute(text("SELECT COUNT(*) FROM relationships"))
        print(f"\nRelationships: {r2.scalar()}")

        r3 = await conn.execute(text("SELECT COUNT(*) FROM compliance_events"))
        print(f"Compliance events: {r3.scalar()}")

    await engine.dispose()

asyncio.run(seed())
