-- ═══════════════════════════════════════════════════════════════════
-- AIA CORPUS SCHEMA — Eden Intelligence Group
-- Persistent Intelligence Layer for the Architected Intelligence Asset
-- 
-- Target: Synology DS925+ NAS / PostgreSQL Container
-- Deploys alongside existing education schema (GA Standards)
-- 
-- Document: EIG-CORPUS-2026-001
-- Date: February 21, 2026
-- ═══════════════════════════════════════════════════════════════════

-- Create dedicated schema to keep corpus separate from education data
CREATE SCHEMA IF NOT EXISTS corpus;

-- Enable full-text search
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ─── ENUMS ──────────────────────────────────────────────────────────

CREATE TYPE corpus.document_status AS ENUM (
    'canon',           -- Current authoritative version
    'superseded',      -- Replaced by a newer document
    'foundational',    -- Historical context that shaped current thinking
    'exploratory',     -- Ideas explored but not committed to
    'retired',         -- Explicitly abandoned
    'raw'              -- Newly ingested, not yet classified
);

CREATE TYPE corpus.document_origin AS ENUM (
    'dropbox',         -- Historical archive
    'claude_session',  -- Claude conversation output
    'gemini_session',  -- Gemini conversation output
    'gpt_session',     -- Legacy GPT work (historical only)
    'manual',          -- Created directly by architect
    'generated',       -- Produced by AIA pipeline
    'external'         -- Third-party sources (research, regulations, etc.)
);

CREATE TYPE corpus.product_domain AS ENUM (
    'waypoint_core',       -- Financial positioning (individual/small business)
    'waypoint_crown',      -- Family office governance
    'waypoint_edge',       -- Excluded-vertical banking
    'crowns_eye',          -- K-12 education
    'integra',             -- AI orchestration
    'kingdom_soundworks',  -- Music/creative platform
    'eden_corporate',      -- Corporate structure, legal, IP
    'aia_methodology',     -- The AIA itself
    'cross_domain',        -- Spans multiple products
    'general'              -- Not product-specific
);

CREATE TYPE corpus.era AS ENUM (
    'pre_meridia',     -- Before Meridia naming (Aegis/Sentiarch era)
    'transition',      -- Naming evolution period
    'meridia_v1',      -- Current Meridia framework
    'eden_formation'   -- Corporate structure phase (current)
);

CREATE TYPE corpus.confidence_level AS ENUM (
    'verified',        -- Architect confirmed classification
    'inferred',        -- AI-classified, awaiting confirmation
    'uncertain'        -- Needs human review
);


-- ─── CORE TABLES ────────────────────────────────────────────────────

-- The primary document registry
CREATE TABLE corpus.documents (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Identity
    title           TEXT NOT NULL,
    filename        TEXT,                          -- Original filename
    file_type       TEXT,                          -- pdf, docx, md, html, json, etc.
    file_size_bytes BIGINT,
    checksum_sha256 TEXT,                          -- Deduplication + integrity
    
    -- Classification
    status          corpus.document_status NOT NULL DEFAULT 'raw',
    origin          corpus.document_origin NOT NULL DEFAULT 'manual',
    domain          corpus.product_domain NOT NULL DEFAULT 'general',
    era             corpus.era NOT NULL DEFAULT 'meridia_v1',
    confidence      corpus.confidence_level NOT NULL DEFAULT 'uncertain',
    
    -- Content
    summary         TEXT,                          -- AI-generated or manual summary
    full_text       TEXT,                          -- Extracted text content for search
    key_concepts    TEXT[],                        -- Array of key concepts/terms
    
    -- Temporal
    created_date    DATE,                          -- When the document was originally created
    ingested_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    classified_at   TIMESTAMPTZ,
    last_reviewed   TIMESTAMPTZ,
    
    -- Source tracking
    source_path     TEXT,                          -- Original file path (Dropbox, etc.)
    source_session  TEXT,                          -- Conversation ID if from AI session
    ingestion_notes TEXT,                          -- Context from ingestion session
    
    -- Storage
    nas_path        TEXT,                          -- Path on NAS filesystem
    
    -- Search optimization
    search_vector   TSVECTOR                       -- Full-text search index
);

-- Automatic search vector update
CREATE OR REPLACE FUNCTION corpus.update_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector := 
        setweight(to_tsvector('english', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.summary, '')), 'B') ||
        setweight(to_tsvector('english', COALESCE(NEW.full_text, '')), 'C');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_documents_search_vector
    BEFORE INSERT OR UPDATE OF title, summary, full_text
    ON corpus.documents
    FOR EACH ROW
    EXECUTE FUNCTION corpus.update_search_vector();

CREATE INDEX idx_documents_search ON corpus.documents USING GIN(search_vector);
CREATE INDEX idx_documents_status ON corpus.documents(status);
CREATE INDEX idx_documents_domain ON corpus.documents(domain);
CREATE INDEX idx_documents_era ON corpus.documents(era);
CREATE INDEX idx_documents_created ON corpus.documents(created_date);
CREATE INDEX idx_documents_checksum ON corpus.documents(checksum_sha256);


-- ─── TAXONOMY ───────────────────────────────────────────────────────

-- Flexible tagging system beyond the fixed enums
CREATE TABLE corpus.tags (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL UNIQUE,
    category    TEXT,                              -- e.g. 'concept', 'entity', 'person', 'technology'
    description TEXT,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE corpus.document_tags (
    document_id UUID REFERENCES corpus.documents(id) ON DELETE CASCADE,
    tag_id      INTEGER REFERENCES corpus.tags(id) ON DELETE CASCADE,
    confidence  corpus.confidence_level NOT NULL DEFAULT 'inferred',
    PRIMARY KEY (document_id, tag_id)
);


-- ─── LINEAGE (Document Evolution) ───────────────────────────────────

-- Tracks how documents relate to each other over time
CREATE TABLE corpus.lineage (
    id              SERIAL PRIMARY KEY,
    source_id       UUID REFERENCES corpus.documents(id) ON DELETE CASCADE,
    target_id       UUID REFERENCES corpus.documents(id) ON DELETE CASCADE,
    relationship    TEXT NOT NULL,                  -- 'supersedes', 'evolves_from', 'splits_into', 
                                                   -- 'merges_with', 'references', 'contradicts',
                                                   -- 'implements', 'expands'
    notes           TEXT,
    confidence      corpus.confidence_level NOT NULL DEFAULT 'inferred',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    UNIQUE(source_id, target_id, relationship)
);

CREATE INDEX idx_lineage_source ON corpus.lineage(source_id);
CREATE INDEX idx_lineage_target ON corpus.lineage(target_id);


-- ─── EXTRACTS (Key Passages & Concepts) ─────────────────────────────

-- Distilled knowledge from documents — what the AIA actually operates on
CREATE TABLE corpus.extracts (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id     UUID REFERENCES corpus.documents(id) ON DELETE CASCADE,
    
    extract_type    TEXT NOT NULL,                  -- 'decision', 'principle', 'definition',
                                                   -- 'architecture', 'requirement', 'insight',
                                                   -- 'metric', 'quote', 'framework'
    content         TEXT NOT NULL,                  -- The actual extracted knowledge
    context         TEXT,                           -- Surrounding context / why this matters
    domain          corpus.product_domain,
    
    is_current      BOOLEAN NOT NULL DEFAULT TRUE,  -- Still valid?
    superseded_by   UUID REFERENCES corpus.extracts(id),
    
    confidence      corpus.confidence_level NOT NULL DEFAULT 'inferred',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    search_vector   TSVECTOR
);

CREATE TRIGGER trg_extracts_search_vector
    BEFORE INSERT OR UPDATE OF content, context
    ON corpus.extracts
    FOR EACH ROW
    EXECUTE FUNCTION corpus.update_search_vector_extracts();

CREATE OR REPLACE FUNCTION corpus.update_search_vector_extracts()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector := 
        setweight(to_tsvector('english', COALESCE(NEW.content, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.context, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE INDEX idx_extracts_search ON corpus.extracts USING GIN(search_vector);
CREATE INDEX idx_extracts_document ON corpus.extracts(document_id);
CREATE INDEX idx_extracts_type ON corpus.extracts(extract_type);
CREATE INDEX idx_extracts_current ON corpus.extracts(is_current);


-- ─── SESSIONS (Ingestion & Work Sessions) ───────────────────────────

-- Tracks every session where corpus was modified
CREATE TABLE corpus.sessions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    session_type    TEXT NOT NULL,                  -- 'ingestion', 'classification', 'synthesis',
                                                   -- 'strategic', 'technical', 'review'
    model_used      TEXT,                           -- 'claude_opus_4.5', 'claude_opus_4.6', 'gemini', etc.
    
    title           TEXT,
    summary         TEXT,                           -- What was accomplished
    
    documents_added     INTEGER DEFAULT 0,
    documents_modified  INTEGER DEFAULT 0,
    extracts_created    INTEGER DEFAULT 0,
    
    started_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    ended_at        TIMESTAMPTZ,
    
    -- Link to transcript if available
    transcript_path TEXT,
    
    metadata        JSONB                          -- Flexible additional data
);

CREATE TABLE corpus.session_documents (
    session_id  UUID REFERENCES corpus.sessions(id) ON DELETE CASCADE,
    document_id UUID REFERENCES corpus.documents(id) ON DELETE CASCADE,
    action      TEXT NOT NULL,                      -- 'added', 'classified', 'reviewed', 'superseded'
    PRIMARY KEY (session_id, document_id)
);


-- ─── DECISIONS (Architectural Decision Records) ─────────────────────

-- Permanent record of strategic and architectural decisions
CREATE TABLE corpus.decisions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    title           TEXT NOT NULL,
    decision        TEXT NOT NULL,                  -- What was decided
    rationale       TEXT,                           -- Why
    alternatives    TEXT,                           -- What was considered and rejected
    consequences    TEXT,                           -- Expected impact
    
    domain          corpus.product_domain NOT NULL DEFAULT 'general',
    status          TEXT NOT NULL DEFAULT 'active', -- 'active', 'revised', 'reversed'
    
    decided_at      DATE NOT NULL,
    decided_in      UUID REFERENCES corpus.sessions(id), -- Which session
    revised_by      UUID REFERENCES corpus.decisions(id), -- If superseded
    
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_decisions_domain ON corpus.decisions(domain);
CREATE INDEX idx_decisions_status ON corpus.decisions(status);


-- ─── NAMING REGISTRY ────────────────────────────────────────────────

-- Tracks the evolution of names across the system
CREATE TABLE corpus.naming_registry (
    id              SERIAL PRIMARY KEY,
    current_name    TEXT NOT NULL,
    previous_names  TEXT[] NOT NULL DEFAULT '{}',
    context         TEXT NOT NULL,                  -- What this name refers to
    domain          corpus.product_domain,
    effective_date  DATE,
    notes           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


-- ─── CORPUS STATE (Quick-Access Current State) ──────────────────────

-- Materialized view of current canon documents per domain
CREATE MATERIALIZED VIEW corpus.current_canon AS
SELECT 
    d.id,
    d.title,
    d.domain,
    d.era,
    d.summary,
    d.created_date,
    d.ingested_at,
    d.key_concepts,
    array_agg(DISTINCT t.name) FILTER (WHERE t.name IS NOT NULL) AS tags
FROM corpus.documents d
LEFT JOIN corpus.document_tags dt ON d.id = dt.document_id
LEFT JOIN corpus.tags t ON dt.tag_id = t.id
WHERE d.status = 'canon'
GROUP BY d.id, d.title, d.domain, d.era, d.summary, d.created_date, d.ingested_at, d.key_concepts
ORDER BY d.domain, d.created_date DESC;

CREATE UNIQUE INDEX idx_current_canon_id ON corpus.current_canon(id);


-- ─── SEED DATA ──────────────────────────────────────────────────────

-- Pre-populate the naming registry with known evolution
INSERT INTO corpus.naming_registry (current_name, previous_names, context, domain, notes) VALUES
('Eden Intelligence Group', '{}', 'Parent holding company (Delaware C-Corp)', 'eden_corporate', 'Owns all IP. Investor vehicle.'),
('Meridia', '{Aegis,Sentiarch}', 'Operating ecosystem / technology brand', 'cross_domain', 'Evolved from Aegis through Sentiarch to Meridia'),
('WayPoint', '{Aegis FPS}', 'Financial Positioning System product line', 'waypoint_core', 'Core/Crown/Edge tiers'),
('Integra', '{SentiarchOS,Sentiarch OS}', 'AI orchestration layer', 'integra', 'Multi-model routing and governance'),
('Aletheia', '{}', 'Steward guide / user-facing AI persona', 'integra', 'Truth • Stewardship • Elevation'),
('Crown''s Eye', '{}', 'K-12 education platform', 'crowns_eye', 'Graduation Project for heir stewardship'),
('Kingdom Soundworks', '{}', 'Music/creative platform', 'kingdom_soundworks', 'Separate brand, may spin out'),
('AIA', '{Architected Intelligence Asset}', 'The methodology itself — persistent corpus that makes AI operative', 'aia_methodology', 'The real product. Everything else is proof case.');

-- Pre-populate core tags
INSERT INTO corpus.tags (name, category, description) VALUES
-- Concepts
('governance-cascade', 'concept', 'Multi-party permission system for insight release'),
('trust-index', 'concept', 'Quantified governance assessment across 4 dimensions'),
('financial-positioning', 'concept', 'Interpretive framework normalizing financial reality'),
('stewardship', 'concept', 'Governance-based ethical accountability'),
('dignity-first', 'concept', 'Design philosophy for excluded populations'),
('renaissance', 'concept', 'Re-entry banking pathway'),

-- Architecture
('permission-cascade', 'architecture', 'RBAC + context-aware routing'),
('multi-model', 'architecture', 'Claude primary, Gemini secondary orchestration'),
('audit-trail', 'architecture', 'Immutable logging for compliance'),
('nas-infrastructure', 'architecture', 'Synology DS925+ persistent storage'),
('docker', 'architecture', 'Container packaging for deployment'),

-- Entities & People
('keith-mosley', 'person', 'Enterprise Architect, Genuine Parts — champion'),
('andre-waits', 'person', 'VP Global Card Ops, JPMC — champion'),

-- Products
('waypoint-core', 'product', 'Individual/small business financial positioning'),
('waypoint-crown', 'product', 'Family office governance'),
('waypoint-edge', 'product', 'Excluded-vertical banking'),
('crowns-eye', 'product', 'K-12 education'),
('integra', 'product', 'AI orchestration'),

-- Strategy
('lean-execution', 'strategy', '$12K budget constraint'),
('delaware-c-corp', 'strategy', 'Standard venture-backable structure'),
('difc-innovation', 'strategy', 'UAE international footprint'),
('provisional-patents', 'strategy', 'Protect methodology before visible');

-- Pre-populate key decisions from today's session
INSERT INTO corpus.decisions (title, decision, rationale, alternatives, consequences, domain, decided_at) VALUES
(
    'Corporate Structure',
    'Delaware C-Corp (Eden Intelligence Group) as holding company + Georgia LLC (Meridia) as operating subsidiary',
    'Standard YC-recommended structure. Delaware for investor expectations, Court of Chancery, established case law. Georgia for operational presence, low cost, Atlanta fintech ecosystem access.',
    'Single LLC, S-Corp, direct Georgia C-Corp — all rejected due to investor friction or tax inefficiency',
    'Two entities to maintain. Annual DE franchise tax ($175 min). GA annual registration ($50). Enables clean investor rounds, IP protection, subsidiary flexibility.',
    'eden_corporate',
    '2026-02-21'
),
(
    'IP Ownership Architecture',
    'All IP owned by Eden Intelligence Group (parent), licensed to Meridia (subsidiary) via intercompany license agreement',
    'Protects IP from operating entity risk. Standard holding company practice. Enables future licensing to additional subsidiaries or international entities.',
    'IP at operating level — rejected due to exposure risk',
    'Requires IP assignment agreement and intercompany license. Attorney session needed. IP survives any single subsidiary restructuring.',
    'eden_corporate',
    '2026-02-21'
),
(
    'AI Model Architecture',
    'Claude as primary cognitive engine. Gemini as secondary for multimodal/bulk. NO OpenAI/GPT in AIA infrastructure.',
    'Direct negative experience with OpenAI — unsound doctrine, wasted time, unreliable outputs. Contamination risk: bad reasoning entering corpus compounds through every subsequent session.',
    'Three-model architecture including GPT — rejected based on direct experience and contamination risk',
    'Limits fallback options. Acceptable tradeoff for corpus integrity. Integra can still offer GPT to customers who want it — just not in Eden''s own infrastructure.',
    'aia_methodology',
    '2026-02-21'
),
(
    'NAS as AIA Sovereign Infrastructure',
    'Synology DS925+ serves as AIA persistent corpus — not product hosting. All institutional knowledge lives here.',
    'Platform memory systems are inadequate (15 lines, 200 chars). Session boundaries reset context. Month of intellectual development inaccessible. Corpus must be sovereign.',
    'Cloud-hosted corpus — rejected due to sovereignty concerns and cost',
    'Requires corpus schema deployment, ingestion pipeline, and retrieval layer. Hardware already operational. PostgreSQL already running.',
    'aia_methodology',
    '2026-02-21'
);


-- ─── HELPER FUNCTIONS ───────────────────────────────────────────────

-- Search corpus by natural language query
CREATE OR REPLACE FUNCTION corpus.search(query TEXT, limit_n INTEGER DEFAULT 20)
RETURNS TABLE (
    id UUID,
    title TEXT,
    domain corpus.product_domain,
    status corpus.document_status,
    era corpus.era,
    summary TEXT,
    rank REAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        d.id, d.title, d.domain, d.status, d.era, d.summary,
        ts_rank(d.search_vector, websearch_to_tsquery('english', query)) AS rank
    FROM corpus.documents d
    WHERE d.search_vector @@ websearch_to_tsquery('english', query)
    ORDER BY rank DESC
    LIMIT limit_n;
END;
$$ LANGUAGE plpgsql;

-- Get full lineage tree for a document
CREATE OR REPLACE FUNCTION corpus.get_lineage(doc_id UUID)
RETURNS TABLE (
    document_id UUID,
    document_title TEXT,
    related_id UUID,
    related_title TEXT,
    relationship TEXT,
    direction TEXT
) AS $$
BEGIN
    RETURN QUERY
    -- Documents this one evolved from
    SELECT 
        l.target_id, dt.title, l.source_id, ds.title, l.relationship, 'predecessor'::TEXT
    FROM corpus.lineage l
    JOIN corpus.documents dt ON l.target_id = dt.id
    JOIN corpus.documents ds ON l.source_id = ds.id
    WHERE l.target_id = doc_id
    
    UNION ALL
    
    -- Documents that evolved from this one
    SELECT 
        l.source_id, ds.title, l.target_id, dt.title, l.relationship, 'successor'::TEXT
    FROM corpus.lineage l
    JOIN corpus.documents ds ON l.source_id = ds.id
    JOIN corpus.documents dt ON l.target_id = dt.id
    WHERE l.source_id = doc_id
    
    ORDER BY direction, relationship;
END;
$$ LANGUAGE plpgsql;

-- Get current state of a domain
CREATE OR REPLACE FUNCTION corpus.domain_state(target_domain corpus.product_domain)
RETURNS TABLE (
    id UUID,
    title TEXT,
    status corpus.document_status,
    summary TEXT,
    created_date DATE,
    tags TEXT[]
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        d.id, d.title, d.status, d.summary, d.created_date,
        array_agg(DISTINCT t.name) FILTER (WHERE t.name IS NOT NULL)
    FROM corpus.documents d
    LEFT JOIN corpus.document_tags dt ON d.id = dt.document_id
    LEFT JOIN corpus.tags t ON dt.tag_id = t.id
    WHERE d.domain = target_domain
    AND d.status IN ('canon', 'foundational')
    GROUP BY d.id, d.title, d.status, d.summary, d.created_date
    ORDER BY d.status, d.created_date DESC;
END;
$$ LANGUAGE plpgsql;

-- Get all active decisions for a domain
CREATE OR REPLACE FUNCTION corpus.active_decisions(target_domain corpus.product_domain DEFAULT NULL)
RETURNS TABLE (
    id UUID,
    title TEXT,
    decision TEXT,
    rationale TEXT,
    domain corpus.product_domain,
    decided_at DATE
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        dc.id, dc.title, dc.decision, dc.rationale, dc.domain, dc.decided_at
    FROM corpus.decisions dc
    WHERE dc.status = 'active'
    AND (target_domain IS NULL OR dc.domain = target_domain)
    ORDER BY dc.decided_at DESC;
END;
$$ LANGUAGE plpgsql;


-- ─── REFRESH CANON VIEW ─────────────────────────────────────────────

CREATE OR REPLACE FUNCTION corpus.refresh_canon()
RETURNS VOID AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY corpus.current_canon;
END;
$$ LANGUAGE plpgsql;


-- ═══════════════════════════════════════════════════════════════════
-- DEPLOYMENT NOTES
-- 
-- 1. Connect to PostgreSQL container on Synology DS925+
-- 2. Run this script: psql -U postgres -d meridia -f aia_corpus_schema.sql
--    (or whatever database name is configured)
-- 3. Existing education schema tables are untouched
-- 4. All corpus tables live in the 'corpus' schema namespace
-- 5. To query: SELECT * FROM corpus.documents WHERE status = 'canon';
-- 6. To search: SELECT * FROM corpus.search('governance cascade');
-- 7. To refresh materialized view: SELECT corpus.refresh_canon();
-- ═══════════════════════════════════════════════════════════════════
