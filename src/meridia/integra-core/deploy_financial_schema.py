
import asyncio

DB_URL = "postgresql+asyncpg://meridia:Ethanj2020##@192.168.0.160:5433/meridia_core"

# Just the Meridia financial tables — clean deployment
SCHEMA = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS entities (
    entity_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name            VARCHAR(255) NOT NULL,
    tier            VARCHAR(20) NOT NULL CHECK (tier IN ('renaissance','core','edge','crown','institutional')),
    entity_type     VARCHAR(50) NOT NULL,
    geography_state VARCHAR(2),
    geography_msa   VARCHAR(50),
    census_tract    VARCHAR(20),
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS positions (
    position_id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id           UUID REFERENCES entities(entity_id) ON DELETE CASCADE,
    period              VARCHAR(10) NOT NULL,
    fps_score           NUMERIC(5,2),
    net_position        NUMERIC(5,2),
    liquidity_coverage  NUMERIC(5,2),
    dscr_score          NUMERIC(5,2),
    runway_score        NUMERIC(5,2),
    distribution_align  NUMERIC(5,2),
    fps_direction       VARCHAR(20),
    fps_narrative       TEXT,
    raw_data            JSONB,
    calculated_at       TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_id, period)
);

CREATE TABLE IF NOT EXISTS trust_scores (
    trust_id                    UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id                   UUID REFERENCES entities(entity_id) ON DELETE CASCADE,
    period                      VARCHAR(10) NOT NULL,
    trust_index                 NUMERIC(5,2),
    behavioral_consistency      NUMERIC(5,2),
    governance_adherence        NUMERIC(5,2),
    communication_reliability   NUMERIC(5,2),
    commitment_fulfillment      NUMERIC(5,2),
    direction                   VARCHAR(20),
    calculated_at               TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_id, period)
);

CREATE TABLE IF NOT EXISTS relationships (
    rel_id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    institution_id      UUID REFERENCES entities(entity_id),
    client_id           UUID REFERENCES entities(entity_id),
    product_type        VARCHAR(50),
    exposure_amount     NUMERIC(15,2),
    risk_direction      VARCHAR(20) CHECK (risk_direction IN ('toward_institution','toward_client','bilateral','sound')),
    risk_score          NUMERIC(5,2),
    status              VARCHAR(20) DEFAULT 'active',
    opened_at           DATE,
    updated_at          TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS relationship_signals (
    signal_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rel_id          UUID REFERENCES relationships(rel_id) ON DELETE CASCADE,
    signal_type     VARCHAR(50),
    severity        VARCHAR(20) CHECK (severity IN ('info','watch','review','critical')),
    message         TEXT,
    resolved        BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cra_activity (
    event_id        UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    institution_id  UUID REFERENCES entities(entity_id),
    entity_id       UUID REFERENCES entities(entity_id),
    activity_type   VARCHAR(50),
    amount          NUMERIC(15,2),
    census_tract    VARCHAR(20),
    is_lmi          BOOLEAN,
    is_distressed   BOOLEAN,
    is_underserved  BOOLEAN,
    activity_date   DATE,
    reportable_year INTEGER,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS compliance_events (
    event_id        UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id       UUID REFERENCES entities(entity_id),
    regulation      VARCHAR(20),
    event_type      VARCHAR(50),
    status          VARCHAR(20),
    description     TEXT,
    due_date        DATE,
    resolved_at     TIMESTAMPTZ,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS fred_series (
    series_id           VARCHAR(30),
    observation_date    DATE,
    value               NUMERIC(15,6),
    series_name         VARCHAR(255),
    frequency           VARCHAR(20),
    units               VARCHAR(100),
    updated_at          TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (series_id, observation_date)
);

CREATE TABLE IF NOT EXISTS hmda_loans (
    loan_id             VARCHAR(50) PRIMARY KEY,
    institution_name    VARCHAR(255),
    lei                 VARCHAR(20),
    state_code          VARCHAR(2),
    census_tract        VARCHAR(20),
    action_taken        INTEGER,
    loan_purpose        INTEGER,
    loan_type           INTEGER,
    loan_amount         INTEGER,
    income              INTEGER,
    applicant_race      VARCHAR(10),
    applicant_ethnicity VARCHAR(10),
    applicant_sex       INTEGER,
    activity_year       INTEGER,
    created_at          TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS fdic_branches (
    id              SERIAL PRIMARY KEY,
    institution_name VARCHAR(255),
    rssd_id         INTEGER,
    cert            INTEGER,
    branch_name     VARCHAR(255),
    city            VARCHAR(100),
    state_code      VARCHAR(2),
    zip             VARCHAR(10),
    census_tract    VARCHAR(20),
    deposits        NUMERIC(15,2),
    data_year       INTEGER,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cfpb_complaints (
    complaint_id        VARCHAR(50) PRIMARY KEY,
    product             VARCHAR(255),
    sub_product         VARCHAR(255),
    issue               VARCHAR(255),
    company             VARCHAR(255),
    state_code          VARCHAR(2),
    zip                 VARCHAR(5),
    submitted_via       VARCHAR(50),
    date_received       DATE,
    company_response    VARCHAR(100),
    timely_response     BOOLEAN,
    consumer_disputed   BOOLEAN,
    created_at          TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS data_pull_log (
    id              SERIAL PRIMARY KEY,
    source          VARCHAR(50),
    pull_type       VARCHAR(20),
    status          VARCHAR(20),
    records_inserted INTEGER DEFAULT 0,
    records_updated  INTEGER DEFAULT 0,
    error_message   TEXT,
    started_at      TIMESTAMPTZ DEFAULT NOW(),
    completed_at    TIMESTAMPTZ
);

-- Seed demo entities with fixed UUIDs
INSERT INTO entities (entity_id, name, tier, entity_type, geography_state, geography_msa)
VALUES
  ('a1b2c3d4-0001-0001-0001-000000000001', 'Vantage Financial Partners', 'institutional', 'institution', 'GA', '12054'),
  ('a1b2c3d4-0002-0002-0002-000000000002', 'Hargrove Family Office', 'crown', 'household', 'GA', '12054'),
  ('a1b2c3d4-0003-0003-0003-000000000003', 'Cornerstone AME Collective', 'core', 'nonprofit', 'GA', '12054'),
  ('a1b2c3d4-0004-0004-0004-000000000004', 'Gulf South Properties LLC', 'edge', 'business', 'GA', '12054'),
  ('a1b2c3d4-0005-0005-0005-000000000005', 'Marcus Thompson', 'renaissance', 'individual', 'GA', '12054')
ON CONFLICT (entity_id) DO NOTHING;

-- Seed demo position for Hargrove
INSERT INTO positions (entity_id, period, fps_score, net_position, liquidity_coverage, dscr_score, runway_score, distribution_align, fps_direction, fps_narrative)
VALUES (
  'a1b2c3d4-0002-0002-0002-000000000002',
  '2026-Q1', 78.4, 82.0, 75.0, 71.0, 80.0, 84.0,
  'improving',
  'Hargrove Family Office holds a strong financial position at 78.4/100. Liquidity coverage and distribution alignment are leading indicators. The trust corpus is performing above benchmark.'
) ON CONFLICT (entity_id, period) DO NOTHING;

-- Seed demo trust score for Hargrove
INSERT INTO trust_scores (entity_id, period, trust_index, behavioral_consistency, governance_adherence, communication_reliability, commitment_fulfillment, direction)
VALUES (
  'a1b2c3d4-0002-0002-0002-000000000002',
  '2026-Q1', 84.2, 88.0, 79.0, 86.0, 84.0, 'improving'
) ON CONFLICT (entity_id, period) DO NOTHING;
"""

async def deploy():
    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy import text
    engine = create_async_engine(DB_URL, echo=False)

    statements = [s.strip() for s in SCHEMA.split(';') if s.strip() and not s.strip().startswith('--')]
    ok = skip = warn = 0

    for i, stmt in enumerate(statements):
        try:
            async with engine.begin() as conn:
                await conn.execute(text(stmt))
            ok += 1
        except Exception as e:
            msg = str(e)
            if any(x in msg for x in ['already exists', 'duplicate', 'unique']):
                skip += 1
            else:
                print(f"  WARN [{i+1}]: {msg[:120]}")
                warn += 1

    print(f"Done: {ok} ok, {skip} skipped, {warn} warnings")

    # Verify
    async with engine.connect() as conn:
        r = await conn.execute(text(
            "SELECT table_name FROM information_schema.tables "
            "WHERE table_schema='public' AND table_name IN "
            "('entities','positions','trust_scores','relationships','fred_series','hmda_loans','data_pull_log','cra_activity') "
            "ORDER BY table_name"
        ))
        tables = [row[0] for row in r.fetchall()]
        print(f"Financial tables deployed: {tables}")

        r2 = await conn.execute(text("SELECT name, tier FROM entities ORDER BY tier"))
        entities = r2.fetchall()
        print(f"Demo entities seeded ({len(entities)}):")
        for e in entities:
            print(f"  {e[1]:15} {e[0]}")

    await engine.dispose()

asyncio.run(deploy())
