-- ============================================================
-- MERIDIA MARKET SCHEMA
-- Meridia · Traverse Code Inc. · March 2026
-- Run once against your PostgreSQL instance
-- psql -U postgres -d meridia -f schema.sql
-- ============================================================

-- Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "postgis"; -- optional for geo queries

-- Drop existing tables (safe re-run)
DROP TABLE IF EXISTS compliance_events CASCADE;
DROP TABLE IF EXISTS cra_activity CASCADE;
DROP TABLE IF EXISTS relationship_signals CASCADE;
DROP TABLE IF EXISTS relationships CASCADE;
DROP TABLE IF EXISTS trust_scores CASCADE;
DROP TABLE IF EXISTS positions CASCADE;
DROP TABLE IF EXISTS entities CASCADE;
DROP TABLE IF EXISTS census_tracts CASCADE;
DROP TABLE IF EXISTS hmda_loans CASCADE;
DROP TABLE IF EXISTS fdic_branches CASCADE;
DROP TABLE IF EXISTS cfpb_complaints CASCADE;
DROP TABLE IF EXISTS fred_series CASCADE;
DROP TABLE IF EXISTS data_pull_log CASCADE;

-- ── ENTITIES ──────────────────────────────────────────────
CREATE TABLE entities (
    entity_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name            VARCHAR(255) NOT NULL,
    tier            VARCHAR(20) NOT NULL CHECK (tier IN ('renaissance','core','edge','crown','institutional')),
    entity_type     VARCHAR(50) NOT NULL, -- individual, household, business, nonprofit, institution
    geography_state VARCHAR(2),
    geography_msa   VARCHAR(50),
    census_tract    VARCHAR(20),           -- FIPS code
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_entities_tier ON entities(tier);
CREATE INDEX idx_entities_tract ON entities(census_tract);

-- ── POSITIONS (FPS history) ────────────────────────────────
CREATE TABLE positions (
    position_id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id           UUID REFERENCES entities(entity_id) ON DELETE CASCADE,
    period              VARCHAR(10) NOT NULL,  -- e.g. '2026-Q1'
    fps_score           NUMERIC(5,2),
    net_position        NUMERIC(5,2),          -- component score 0-100
    liquidity_coverage  NUMERIC(5,2),
    dscr_score          NUMERIC(5,2),
    runway_score        NUMERIC(5,2),
    distribution_align  NUMERIC(5,2),
    fps_direction       VARCHAR(20),           -- improving, declining, stable
    fps_narrative       TEXT,
    raw_data            JSONB,                 -- full inputs for audit trail
    calculated_at       TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_id, period)
);
CREATE INDEX idx_positions_entity ON positions(entity_id);
CREATE INDEX idx_positions_period ON positions(period);

-- ── TRUST SCORES ──────────────────────────────────────────
CREATE TABLE trust_scores (
    trust_id                UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id               UUID REFERENCES entities(entity_id) ON DELETE CASCADE,
    period                  VARCHAR(10) NOT NULL,
    trust_index             NUMERIC(5,2),
    behavioral_consistency  NUMERIC(5,2),
    governance_adherence    NUMERIC(5,2),
    communication_reliability NUMERIC(5,2),
    commitment_fulfillment  NUMERIC(5,2),
    direction               VARCHAR(20),
    calculated_at           TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_id, period)
);

-- ── RELATIONSHIPS (bilateral mapping) ─────────────────────
CREATE TABLE relationships (
    rel_id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    institution_id      UUID REFERENCES entities(entity_id),
    client_id           UUID REFERENCES entities(entity_id),
    product_type        VARCHAR(50),           -- mortgage, commercial, deposit, etc
    exposure_amount     NUMERIC(15,2),
    risk_direction      VARCHAR(20) CHECK (risk_direction IN ('toward_institution','toward_client','bilateral','sound')),
    risk_score          NUMERIC(5,2),
    status              VARCHAR(20) DEFAULT 'active',
    opened_at           DATE,
    updated_at          TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_rel_institution ON relationships(institution_id);
CREATE INDEX idx_rel_client ON relationships(client_id);

-- ── RELATIONSHIP SIGNALS ──────────────────────────────────
CREATE TABLE relationship_signals (
    signal_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rel_id          UUID REFERENCES relationships(rel_id) ON DELETE CASCADE,
    signal_type     VARCHAR(50),   -- position_change, governance_flag, compliance_event
    severity        VARCHAR(20) CHECK (severity IN ('info','watch','review','critical')),
    message         TEXT,
    resolved        BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_signals_rel ON relationship_signals(rel_id);
CREATE INDEX idx_signals_severity ON relationship_signals(severity);

-- ── CRA ACTIVITY ──────────────────────────────────────────
CREATE TABLE cra_activity (
    event_id        UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    institution_id  UUID REFERENCES entities(entity_id),
    entity_id       UUID REFERENCES entities(entity_id),
    activity_type   VARCHAR(50),  -- small_business_loan, cd_investment, service_activity
    amount          NUMERIC(15,2),
    census_tract    VARCHAR(20),
    is_lmi          BOOLEAN,
    is_distressed   BOOLEAN,
    is_underserved  BOOLEAN,
    activity_date   DATE,
    reportable_year INTEGER,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_cra_institution ON cra_activity(institution_id);
CREATE INDEX idx_cra_tract ON cra_activity(census_tract);
CREATE INDEX idx_cra_year ON cra_activity(reportable_year);

-- ── COMPLIANCE EVENTS ─────────────────────────────────────
CREATE TABLE compliance_events (
    event_id        UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id       UUID REFERENCES entities(entity_id),
    regulation      VARCHAR(20),  -- CRA, HMDA, ECOA, BSA, UDAAP
    event_type      VARCHAR(50),  -- finding, remediation, certification, exam
    status          VARCHAR(20),  -- open, in_progress, resolved
    description     TEXT,
    due_date        DATE,
    resolved_at     TIMESTAMPTZ,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_compliance_entity ON compliance_events(entity_id);
CREATE INDEX idx_compliance_regulation ON compliance_events(regulation);

-- ── CENSUS TRACTS (FFIEC + ACS overlay) ───────────────────
CREATE TABLE census_tracts (
    geoid               VARCHAR(20) PRIMARY KEY,  -- FIPS: state+county+tract
    state_code          VARCHAR(2),
    county_code         VARCHAR(5),
    tract_name          VARCHAR(100),
    msa_name            VARCHAR(100),
    -- FFIEC fields
    is_distressed       BOOLEAN DEFAULT FALSE,
    is_underserved      BOOLEAN DEFAULT FALSE,
    is_lmi              BOOLEAN DEFAULT FALSE,
    ffiec_income_pct    NUMERIC(6,2),  -- tract median income / MSA median income %
    -- Census ACS fields
    median_hh_income    INTEGER,
    poverty_rate        NUMERIC(5,2),
    population          INTEGER,
    pct_minority        NUMERIC(5,2),
    -- Calculated
    opportunity_score   NUMERIC(5,2),  -- our composite opportunity rating
    data_year           INTEGER,
    updated_at          TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_tracts_state ON census_tracts(state_code);
CREATE INDEX idx_tracts_lmi ON census_tracts(is_lmi);
CREATE INDEX idx_tracts_distressed ON census_tracts(is_distressed);

-- ── HMDA LOANS ────────────────────────────────────────────
CREATE TABLE hmda_loans (
    loan_id             VARCHAR(50) PRIMARY KEY,
    institution_name    VARCHAR(255),
    lei                 VARCHAR(20),  -- Legal Entity Identifier
    state_code          VARCHAR(2),
    census_tract        VARCHAR(20),
    action_taken        INTEGER,      -- 1=originated, 2=approved not accepted, 3=denied
    loan_purpose        INTEGER,      -- 1=home purchase, 2=refinance, 31=home improvement
    loan_type           INTEGER,      -- 1=conventional, 2=FHA, etc
    loan_amount         INTEGER,      -- thousands
    income              INTEGER,      -- thousands
    applicant_race      VARCHAR(10),
    applicant_ethnicity VARCHAR(10),
    applicant_sex       INTEGER,
    denial_reason_1     INTEGER,
    activity_year       INTEGER,
    created_at          TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_hmda_tract ON hmda_loans(census_tract);
CREATE INDEX idx_hmda_institution ON hmda_loans(lei);
CREATE INDEX idx_hmda_year ON hmda_loans(activity_year);
CREATE INDEX idx_hmda_action ON hmda_loans(action_taken);

-- ── FDIC BRANCHES ─────────────────────────────────────────
CREATE TABLE fdic_branches (
    branch_id       SERIAL PRIMARY KEY,
    institution_name VARCHAR(255),
    rssd_id         INTEGER,
    cert            INTEGER,
    branch_name     VARCHAR(255),
    state_code      VARCHAR(2),
    county          VARCHAR(100),
    city            VARCHAR(100),
    zip             VARCHAR(10),
    census_tract    VARCHAR(20),
    latitude        NUMERIC(9,6),
    longitude       NUMERIC(9,6),
    deposits        NUMERIC(15,3),  -- millions
    data_year       INTEGER,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_fdic_state ON fdic_branches(state_code);
CREATE INDEX idx_fdic_tract ON fdic_branches(census_tract);

-- ── CFPB COMPLAINTS ───────────────────────────────────────
CREATE TABLE cfpb_complaints (
    complaint_id        VARCHAR(20) PRIMARY KEY,
    product             VARCHAR(100),
    sub_product         VARCHAR(100),
    issue               VARCHAR(255),
    company             VARCHAR(255),
    state_code          VARCHAR(2),
    zip                 VARCHAR(5),
    submitted_via       VARCHAR(50),
    date_received       DATE,
    date_sent_to_company DATE,
    company_response    VARCHAR(100),
    timely_response     BOOLEAN,
    consumer_disputed   BOOLEAN,
    created_at          TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_cfpb_product ON cfpb_complaints(product);
CREATE INDEX idx_cfpb_state ON cfpb_complaints(state_code);
CREATE INDEX idx_cfpb_company ON cfpb_complaints(company);
CREATE INDEX idx_cfpb_date ON cfpb_complaints(date_received);

-- ── FRED SERIES ───────────────────────────────────────────
CREATE TABLE fred_series (
    series_id       VARCHAR(30),
    observation_date DATE,
    value           NUMERIC(15,6),
    series_name     VARCHAR(255),
    frequency       VARCHAR(20),
    units           VARCHAR(100),
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (series_id, observation_date)
);
CREATE INDEX idx_fred_series ON fred_series(series_id);
CREATE INDEX idx_fred_date ON fred_series(observation_date);

-- ── DATA PULL LOG ─────────────────────────────────────────
CREATE TABLE data_pull_log (
    log_id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source          VARCHAR(30),  -- ffiec, hmda, fred, census, fdic, cfpb
    pull_type       VARCHAR(30),  -- full, incremental
    status          VARCHAR(20),  -- success, failed, partial
    records_inserted INTEGER DEFAULT 0,
    records_updated  INTEGER DEFAULT 0,
    error_message   TEXT,
    started_at      TIMESTAMPTZ DEFAULT NOW(),
    completed_at    TIMESTAMPTZ
);

-- ── SEED: Demo entities ───────────────────────────────────
INSERT INTO entities (entity_id, name, tier, entity_type, geography_state, geography_msa, census_tract)
VALUES
  ('a1b2c3d4-0001-0001-0001-000000000001', 'Vantage Financial Partners', 'institutional', 'institution', 'GA', 'Atlanta-Sandy Springs', '13121010100'),
  ('a1b2c3d4-0002-0002-0002-000000000002', 'Hargrove Family Office', 'crown', 'household', 'GA', 'Atlanta-Sandy Springs', '13121010200'),
  ('a1b2c3d4-0003-0003-0003-000000000003', 'Cornerstone AME Collective', 'core', 'nonprofit', 'GA', 'Atlanta-Sandy Springs', '13121010300'),
  ('a1b2c3d4-0004-0004-0004-000000000004', 'Gulf South Properties LLC', 'edge', 'business', 'GA', 'Atlanta-Sandy Springs', '13121010400'),
  ('a1b2c3d4-0005-0005-0005-000000000005', 'Marcus Thompson', 'renaissance', 'individual', 'GA', 'Atlanta-Sandy Springs', '13121010500');

-- ── SEED: Relationships ───────────────────────────────────
INSERT INTO relationships (institution_id, client_id, product_type, exposure_amount, risk_direction, risk_score, status, opened_at)
VALUES
  ('a1b2c3d4-0001-0001-0001-000000000001', 'a1b2c3d4-0002-0002-0002-000000000002', 'wealth_management', 12400000, 'sound', 82, 'active', '2022-03-15'),
  ('a1b2c3d4-0001-0001-0001-000000000001', 'a1b2c3d4-0003-0003-0003-000000000003', 'commercial_deposit', 620000, 'sound', 76, 'active', '2021-06-01'),
  ('a1b2c3d4-0001-0001-0001-000000000001', 'a1b2c3d4-0004-0004-0004-000000000004', 'commercial_real_estate', 4200000, 'toward_institution', 24, 'active', '2020-11-20'),
  ('a1b2c3d4-0001-0001-0001-000000000001', 'a1b2c3d4-0005-0005-0005-000000000005', 'renaissance_deposit', 1240, 'sound', 58, 'active', '2025-01-10');
