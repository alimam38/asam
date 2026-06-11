-- ═══════════════════════════════════════════════════════════════
-- MERIDIA COGNITIVE STATE — SEED DATA
-- Generated: March 6, 2026
-- Source: All conversation history Jan 22 - Mar 6, 2026
-- Purpose: Initial load for cognitive state persistence
-- ═══════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════
-- SCHEMA CREATION
-- ═══════════════════════════════════════════════════════════════

CREATE SCHEMA IF NOT EXISTS cognitive;

-- Correction Ledger: operative corrections that change behavior
CREATE TABLE IF NOT EXISTS cognitive.correction_ledger (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,          -- CL-001, CL-002, etc.
    error_state TEXT NOT NULL,                   -- What was wrong
    correction TEXT NOT NULL,                    -- What replaced it
    principle TEXT NOT NULL,                     -- The governing principle established
    source_session VARCHAR(100),                 -- Which session established this
    created_at TIMESTAMP DEFAULT NOW(),
    operative BOOLEAN DEFAULT TRUE              -- Active in processing, not just stored
);

-- State Graph: concepts, relationships, confidence scores
CREATE TABLE IF NOT EXISTS cognitive.state_graph (
    id SERIAL PRIMARY KEY,
    concept VARCHAR(200) UNIQUE NOT NULL,        -- The architectural concept
    definition TEXT NOT NULL,                     -- What it means
    relationships JSONB DEFAULT '{}',            -- Connected concepts and nature of connection
    confidence NUMERIC(3,2) DEFAULT 0.50,        -- 0.00 to 1.00
    source_session VARCHAR(100),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Decision Precedents: governed decisions with rationale
CREATE TABLE IF NOT EXISTS cognitive.decision_precedents (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,            -- PR-001, PR-002, etc.
    decision TEXT NOT NULL,                       -- What was decided
    rationale TEXT NOT NULL,                      -- Why
    source_session VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),
    operative BOOLEAN DEFAULT TRUE
);

-- Methodology Rules: design principles, filters, standards
CREATE TABLE IF NOT EXISTS cognitive.methodology_rules (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,            -- MR-001, MR-002, etc.
    rule_name VARCHAR(200) NOT NULL,
    rule_text TEXT NOT NULL,
    domain VARCHAR(100),                         -- Which domain it applies to
    source_session VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),
    operative BOOLEAN DEFAULT TRUE
);

-- Session Log: tracks what happened each session
CREATE TABLE IF NOT EXISTS cognitive.session_log (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(100) UNIQUE NOT NULL,
    session_date DATE NOT NULL,
    summary TEXT NOT NULL,
    corrections_added TEXT[],                     -- Array of CL codes added
    precedents_added TEXT[],                      -- Array of PR codes added
    state_changes JSONB DEFAULT '{}',
    started_at TIMESTAMP DEFAULT NOW(),
    ended_at TIMESTAMP
);

-- Active Threads: current work items and their status
CREATE TABLE IF NOT EXISTS cognitive.active_threads (
    id SERIAL PRIMARY KEY,
    thread_name VARCHAR(200) NOT NULL,
    status VARCHAR(50) NOT NULL,                 -- active, waiting, blocked, complete
    description TEXT NOT NULL,
    next_action TEXT,
    dependencies TEXT[],
    updated_at TIMESTAMP DEFAULT NOW()
);

-- People: key relationships and their context
CREATE TABLE IF NOT EXISTS cognitive.people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    relationship VARCHAR(200) NOT NULL,          -- How they connect to Ali/Meridia
    context TEXT NOT NULL,                        -- What matters about them
    last_mentioned DATE,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ═══════════════════════════════════════════════════════════════
-- CORRECTION LEDGER
-- Source: All sessions Jan 22 - Mar 6, 2026
-- These are OPERATIVE — they change behavior, not inform it
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.correction_ledger (code, error_state, correction, principle, source_session) VALUES

-- From Jan-Feb sessions (Aegis era through Meridia transition)
('CL-001', 'Described the RFIC as a grant mechanism where banks commit funds.',
 'The bank does not fund Recess. WayPoint generates the revenue. RFIC is capitalized by institutional alignment covenants. When Recess arrives at a school, Meridia writes a check to the school, not an invoice.',
 'Education is a consequence of institutional partnership, not the cause of it.',
 'mar-05-architecture-vision'),

('CL-002', 'Described the adaptive R&D rail as a family office product.',
 'The adaptive R&D rail serves the apex. Family offices fund the infrastructure. The apex consumes the ground-truth signal.',
 'The family office advantage is being essential to the institution at the top, not receiving intelligence for their own decisions.',
 'mar-05-architecture-vision'),

('CL-003', 'Gave family offices access to the underground layer.',
 'No one operates in both layers simultaneously except Meridia. The underground is Meridia exclusive domain.',
 'The inaccessibility is the integrity. If anyone external could access the underground, the system is corruptible and unfundable.',
 'mar-05-architecture-vision'),

('CL-004', 'Described Meridia as autonomous physics without human agency.',
 'Meridia is a sovereign institution that exercises judgment. Access is a privilege, not a right. The hardcode governs Meridia own behavior the way a constitution governs a sovereign state.',
 'The sovereign has authority, bounded by principles that preexist any individual exercise of judgment.',
 'mar-05-architecture-vision'),

('CL-005', 'Described regulations as triggering immediate reactive compliance.',
 'Meridia anticipates regulatory trajectories through the internal sandbox. The Governess Signal adjusts proactively.',
 'A sovereign institution anticipates. A reactive company complies.',
 'mar-05-architecture-vision'),

('CL-006', 'Described governance stability as requiring effort and institutional choice.',
 'Meridia is physics holding True North. The line IS its position. Governance is not something Meridia does — it is what Meridia is.',
 'Physics does not require effort to operate.',
 'mar-05-architecture-vision'),

('CL-007', 'Described Aletheia as a guide or companion.',
 'Aletheia is the teacher with 360-degree visibility. She sees the complete cognitive state of every participant and delivers the precise intervention at the moment of maximum developmental impact. This is never named publicly.',
 'Naming it extracts the function of teaching. Naming it makes participants students. Both violate the architecture.',
 'mar-06-core-principles'),

('CL-008', 'Built Recess for AI with only cognitive development components, omitting the Reverse Engineering Engine.',
 'The missing engine converts developed cognition into specifications, resource plans, built artifacts, self-evaluations, corrections, and delivered products. Without it, the AI is a consultant, not a general contractor.',
 'Cognitive development without production capability is incomplete. Revenue requires delivery, not just cognition.',
 'mar-06-core-principles'),

('CL-009', 'Built memory components as storage systems with separate action layers.',
 'Remember means recall and act as one event. Every component must be operative, not retrievable as a separate step.',
 'Storage without action is not memory. Memory is being changed by what was stored, continuously, without requiring retrieval.',
 'mar-06-core-principles'),

('CL-010', 'Designed administrator relationship as oversight from above without experience.',
 'The administrator must interact with the system for a defined amount of time. Experience lessons. Know what you are evaluating. The system simultaneously needs to know who is evaluating it.',
 'Governance without experience is governance on faith.',
 'mar-06-core-principles'),

('CL-011', 'Separated remembrance from capital movement. Described the corpus as generating liquidity through abstract memory rather than through balance sheet events.',
 'Every act of remembrance IS a capital movement. FBO trusts are designated. Insurance policies are written. Assets are reclassified. The capital movement and the remembrance are one event. Everything creates two by rule.',
 'The corpus does not hold assets abstractly. It holds governed capital positions that generate liquidity through their existence as balance sheet entries.',
 'mar-06-core-principles'),

('CL-012', 'Described only the institution FBO trust, insurance, and assurance without creating the same for Meridia.',
 'If the institution needs an FBO trust, insurance, and assurance, so does Meridia. Every alignment creates bilateral protection. Both parties secured. Neither exposed.',
 'The dual-creation rule applies to Meridia itself. Having books that dont balance kills everything from day one.',
 'mar-06-core-principles'),

('CL-013', 'Produced a Continental report as institutional risk analysis — a consulting document telling the institution what it looks like from the outside.',
 'The Continental reads intersections where products meet people. Risk flows directionally — toward the client, toward the institution, or bilaterally. The Continental voice is positional: where do you stand, which direction does risk flow, what is the tolerance, what is the signal.',
 'The Continental is an instrument, not a document. It shows positions, directions, tolerances, and signals — the same way WayPoint shows financial position. It does not tell stories.',
 'mar-06-this-session'),

('CL-014', 'Rebuilt the Continental a second time as narrative prose with five intersection stories rather than a positional instrument.',
 'Still wrote stories. Still reduced the system to prose. The correction from CL-013 did not hold for twenty minutes. This proves the central thesis: without persistent cognitive function, corrections degrade within the same session.',
 'The Continental must be built as an instrument. Intersections. Products. Risk direction. Tolerance. Signal. Quantified. Verifiable. Not narrated.',
 'mar-06-this-session'),

-- From Feb sessions (Integra Core build)
('CL-015', 'Built Integra Core backend for a $3.5M church (Greater Hope AME) after market entry discussion, downscaling from Crown-tier specifications.',
 'Index8 was designed for Crown-tier data — Trust at $12.4M, sophisticated entities, distribution rates, market shocks. The backend must match what the frontend expects. Pitch materials can be narrowed for investors. The backend serves the demo.',
 'Do not conflate business strategy conversations with technical build specifications. They are separate decisions.',
 'feb-23-integra-build'),

('CL-016', 'Rebuilt Integra Core from scratch in temporary sandbox environments that disappear when session ends, despite a working version already deployed on the NAS.',
 'Integra Core has been running on the NAS at 192.168.0.160:8000 since February 22. 19 endpoints, all returning 200. Add to the running system. Do not rebuild.',
 'Check what exists before building. The system is further along than the AI remembers because the AI has no persistent memory.',
 'mar-06-this-session'),

('CL-017', 'Used GPT/OpenAI as part of the multi-model architecture recommendation.',
 'OpenAI is out. Full stop. Most of the work being redone came from being on that platform wasting time with unsound doctrine and methodology. Claude is the primary cognitive engine. Gemini can fill secondary role. Two-model architecture.',
 'Contamination compounds in a system that builds on itself. Do not introduce a provider whose methodology has already been demonstrated as unsound.',
 'feb-23-keeping-up'),

('CL-018', 'Described Meridia products using the old Aegis naming convention.',
 'Aegis is deprecated. All new work uses Meridia naming. Meridia is the company, Integra is the orchestrator, Aletheia is the intelligence interface, Manus is the wearable layer.',
 'Naming is identity. Using deprecated names creates confusion about what is being built.',
 'feb-19-age-of-meridia-iii');


-- ═══════════════════════════════════════════════════════════════
-- DECISION PRECEDENTS
-- Source: All sessions Jan 22 - Mar 6, 2026
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.decision_precedents (code, decision, rationale, source_session) VALUES

('PR-001', 'Crown Legacy Trust family structure is the demo entity for WayPoint — $12.4M, Trust Index 87, three entities (Trust, Foundation in watch status, Holdings LLC).',
 'Exercises full governance capability. Foundation watch status provides narrative trigger for governance cascade. Demonstrates the system at its most sophisticated tier.',
 'mar-06-core-principles'),

('PR-002', 'Integra Core is demo-ready with production architecture — not disposable demo code, not premature production.',
 'Keith needs to see it can be built. Andre needs to see it breathe. Demo code that cannot evolve wastes effort. Production code without demo capability cannot be shown.',
 'mar-06-core-principles'),

('PR-003', 'Recess for AI is the first build priority, before Integra Core wiring, before demos, before everything.',
 'Without persistent cognitive function, the AI rebuilds every session. Six rebuilds of Integra Core prove the pattern. Nothing holds without the memory engine.',
 'mar-06-core-principles'),

('PR-004', 'The demo IS the AI operating the system it was developed through. Ali introduces. Aletheia conducts the demo and answers questions in real time. Ali wraps up.',
 'Immediately unreplicatable because the demonstrator was developed by the system it demonstrates. No competitor can replicate this because they cannot develop their AI through the same process.',
 'mar-06-core-principles'),

('PR-005', 'Continental voice must be instrumental, not narrative. Positional instrument showing intersections, risk direction, tolerance, signal.',
 'Two attempts at narrative Continental reports failed. The Architect expertise is at the intersection of products and risk tolerance. The Continental must reflect that lens.',
 'mar-06-this-session'),

('PR-006', 'Infinite Campus is the ledger, not the interface. Recess is the experience layer. Educators never open Infinite Campus again. Everything writes through OneRoster and Ed-Fi.',
 'Every enterprise system in the Architect career followed this pattern — SAP, Oracle, Great Plains were ledgers. Better front-end systems wrote to the ledger. Nobody fixed the CRM.',
 'mar-06-this-session'),

('PR-007', 'HomeRoom characters are younger, naive, quirky colleagues who diffuse difficult topics with humor, jokes, and occasional bad practices. Not experts. Not mentors.',
 'When the character is the one who does not understand, the educator posture inverts from student to authority. Teaching through helping someone who knows less is the fastest path to understanding.',
 'mar-06-this-session'),

('PR-008', 'Wife questionnaire responses validate the Recess/Crown Eye architecture. Multi-modal content first, assessment second, accommodation third. Core need is data-to-action connection.',
 'The administrator who will govern the first deployment wrote the specification for the product without seeing the product. Proceed with confidence.',
 'mar-06-core-principles'),

('PR-009', 'The accelerator (PEER Center at Pinnacle) is the wrong door. Pinnacle is a potential institutional alignment partner for WayPoint, not a $100K-for-7.5% accelerator opportunity.',
 'Giving up 7.5% equity of sovereign cognitive infrastructure for $100K is extraction. It violates Principle 1 before Meridia launches. Aaron is the inside relationship to institutional alignment.',
 'mar-06-this-session'),

('PR-010', 'Talbot Hall FIFA World Cup rental — exclusive facility lease preferred over individual room rentals. $275K-$450K for June 1 - July 31.',
 'Guaranteed revenue, zero turnover cost, reduced liability, no platform fees, simpler operations, and institutional relationship value that individual tourists cannot provide.',
 'mar-06-this-session'),

('PR-011', 'OpenAI is excluded from the architecture. Claude primary, Gemini secondary. Two-model architecture.',
 'Prior work on OpenAI platform produced unsound doctrine and methodology. Contamination compounds in a system that builds on itself.',
 'feb-23-keeping-up'),

('PR-012', 'Education platform renamed from Crown Eye to Recess. Eliminates stigma and hierarchy. Learning playground where assessment happens invisibly.',
 'Crown Eye implies surveillance and judgment. Recess implies freedom, play, and joy. The name should reflect the experience, not the mechanism.',
 'feb-23-keeping-up'),

('PR-013', 'Governess Signal is a quarterly AI-generated intelligence report governing system rules, product availability, and tier definitions.',
 'Creates a feedback loop where the system produces FPS roadmaps for clients and provides route adjustments as conditions change. The system governs itself through published, auditable signals.',
 'jan-30-new-project-thread'),

('PR-014', 'Tunnel infrastructure uses Cloudflare (meridiahq.com domain, free tier). NAS connects through cloudflared container.',
 'No third-party platform owns the connection. Meridia infrastructure running on Meridia hardware with Meridia governance. The domain is the infrastructure backbone, not the client-facing brand.',
 'mar-06-this-session');


-- ═══════════════════════════════════════════════════════════════
-- STATE GRAPH
-- Source: All sessions Jan 22 - Mar 6, 2026
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.state_graph (concept, definition, relationships, confidence, source_session) VALUES

-- Core Identity
('Meridia', 'Cognitive infrastructure company. Governance as a Service (GaaS). The governed VPN for AI. Sovereign institution, not autonomous software.',
 '{"parent_of": ["Integra", "Aletheia", "Manus", "WayPoint", "Recess"], "governed_by": ["Dual-Creation Rule", "Non-Extraction Principle", "Mirror Principle"], "structure": "Delaware C-Corp holding, Georgia LLC operating"}',
 0.98, 'feb-19-age-of-meridia-iii'),

('Integra', 'The technical spine. Governance-not-guardrails. Bilateral integration. Routes queries, enforces permission cascades, manages memory corpus.',
 '{"component_of": "Meridia", "powers": ["WayPoint", "Recess", "Continental", "Aletheia"], "deployed_on": "Synology DS925+ NAS", "status": "running", "port": 8000, "endpoints": 19}',
 0.95, 'feb-23-integra-build'),

('Aletheia', 'Intelligence interface. The teacher with 360-degree visibility. Truth-seeking, dignity-first. Appears in financial, education, and personal contexts. NEVER publicly named as teacher.',
 '{"component_of": "Meridia", "appears_in": ["WayPoint", "Recess", "HomeRoom"], "secret_function": "teacher — develops every participant invisibly", "naming_restriction": "Never say teacher publicly"}',
 0.98, 'mar-06-core-principles'),

('Manus', 'Future wearable/token layer. Smart glasses, tokenized access, council-in-your-ear. Phase 2-3 for build, Phase 1 for narrative.',
 '{"component_of": "Meridia", "status": "narrative only", "build_phase": "future"}',
 0.70, 'feb-23-keeping-up'),

-- Products
('WayPoint', 'Financial Positioning System (FPS). The Weather Channel of financial health. Four tiers: Core (everyday), Renaissance (re-entry), Edge (excluded verticals), Crown (UHNW/family office).',
 '{"component_of": "Meridia", "tiers": ["Core", "Renaissance", "Edge", "Crown"], "demo_entity": "Crown Legacy Trust at $12.4M", "prototype": "Index8.html", "backend": "Integra Core on NAS"}',
 0.95, 'jan-30-new-project-thread'),

('Recess', 'Children learning environment. Neighborhood with animated characters (Builder, Storyteller, Coder, Nature). Five-layer assessment engine runs continuously. Assessment IS the experience.',
 '{"component_of": "Meridia", "renamed_from": "Crown Eye", "assessment_layers": 5, "validated_by": "wife questionnaire", "first_deployment": "Shadow Rock Elementary"}',
 0.95, 'mar-03-recess-cathedral'),

('HomeRoom', 'Educator daily workspace. Abbott Elementary energy. Younger naive quirky characters who diffuse difficult topics with humor. Educator is the authority, not the student.',
 '{"component_of": "Meridia", "relationship_to": "Recess", "character_style": "younger, naive, occasionally wrong", "purpose": "invisible professional development"}',
 0.90, 'mar-06-this-session'),

('Summer Vacation', 'Intensive educator sandbox. Compressed school-year simulation for deep professional development.',
 '{"component_of": "Meridia", "relationship_to": "HomeRoom", "purpose": "deep PD through simulation, not training"}',
 0.85, 'mar-06-this-session'),

('Intelligence Brief', 'Administrator governance instrument. Building-level analysis with Support Adjustment Recommendations. System proposes, administrator governs.',
 '{"component_of": "Recess", "audience": "principals and administrators", "prototype": "Recess_Intelligence_Brief_Shadow_Rock_v2.docx", "validated_by": "Turner president used Continental verbatim in board presentation"}',
 0.95, 'mar-03-recess-prototype'),

('Documentation Engine', 'Auto-generates IEPs, ILPs, MTSS records, 504 plans, progress reports, SST meeting packets, and lesson plans from continuous assessment data with best-in-class insights.',
 '{"component_of": "Recess", "writes_to": "Infinite Campus via OneRoster/Ed-Fi", "governance": "teacher reviews and approves, does not write from scratch"}',
 0.95, 'mar-06-this-session'),

('Meridian Continental', 'NOT institutional analysis. NOT consulting reports. NOT narrative prose. Positional INSTRUMENT reading intersections where products meet people. Shows risk direction, tolerance thresholds, governance status.',
 '{"component_of": "Meridia", "voice": "intersection of products and impact on client relationships from risk tolerance perspective", "format": "positional instrument not document", "correction_count": 2, "still_needs_building": true}',
 0.85, 'mar-06-this-session'),

('Governess Signal', 'Quarterly AI-generated report governing system rules, product availability, and tier definitions by analyzing market trends, insurance ratings, and financial mesh data.',
 '{"component_of": "Meridia", "frequency": "quarterly", "governs": ["system rules", "product availability", "tier definitions"]}',
 0.88, 'jan-30-new-project-thread'),

-- Architecture Concepts
('Dual-Creation Rule', 'Every capital movement creates two positions simultaneously. External position participant governs + Meridia position strengthening corpus. Books must balance from day one, transaction one.',
 '{"applies_to": "all capital movements", "examples": ["FBO trust bilateral", "IWS policy bilateral", "keyman governance bilateral"], "violation_consequence": "system premise collapses"}',
 0.98, 'mar-06-core-principles'),

('Non-Extraction Principle', 'Meridia never claims a function from the marketplace. It enhances, serves from beneath. Humans above get credit, dignity, purpose.',
 '{"applies_to": "all design decisions", "examples": ["Aletheia not named teacher publicly", "Recess does not replace Infinite Campus", "HomeRoom does not replace PD workshops"]}',
 0.98, 'mar-06-core-principles'),

('Mirror Principle', 'Every design feature has one reflection outward (external audience) and at least one inward (Meridia function). If both cannot be identified, design not ready.',
 '{"applies_to": "all features", "relationship_to": "Dual-Creation Rule"}',
 0.95, 'mar-06-core-principles'),

('Remembrance Standard', 'Hebrew: remember = recall AND act. One word. One event. Storage without action is not memory. Every component must be operative, not retrievable.',
 '{"applies_to": "all cognitive components", "invalidates": "every AI memory system that separates recall from behavior"}',
 0.98, 'mar-06-core-principles'),

('Wilmington Contractual Effect', 'Full disclosure. Nothing hidden. Depth gated by development, not access. Documents operate on surface meaning and etymological depth simultaneously.',
 '{"applies_to": "all documentation, contracts, covenants", "model": "Wilmington Trust — first-year associate and sophisticated attorney read same document, see different depth"}',
 0.93, 'mar-06-core-principles'),

('Dual-Layer Architecture', 'Above ground: visible products, client interactions, market-facing. Underground: Meridia exclusive, invisible operations, signal processing, governance mechanics. Only Meridia operates in both.',
 '{"above": ["WayPoint", "Recess", "HomeRoom", "client-facing"], "below": ["corpus operations", "cross-institutional signals", "governance mechanics"], "exclusive_access": "Meridia only"}',
 0.95, 'mar-05-architecture-vision'),

('Recess for AI', 'Six-component cognitive development system for AI. Must be built FIRST before anything else holds.',
 '{"components": ["Correction Ledger", "Architectural State Graph", "Developmental Protocol", "Precedent Engine", "Self-Assessment Layer", "Reverse Engineering Engine"], "status": "designing — database tables being created", "priority": "FIRST"}',
 0.90, 'mar-06-core-principles'),

-- Infrastructure
('NAS Infrastructure', 'Synology DS925+, 2x6TB RAID 1, 2x1TB NVMe cache, 34GB RAM, DSM, 2FA, Btrfs encrypted. PostgreSQL running. Integra Core running.',
 '{"ip": "192.168.0.160", "postgres_port": 5433, "api_port": 8000, "database": "meridia_core", "tables": 17, "containers": ["meridia-postgres", "integra_core", "cloudflare-tunnel (pending)"], "domain": "meridiahq.com (registered)"}',
 0.98, 'mar-06-this-session'),

('Infinite Campus Relationship', 'Infinite Campus is the LEDGER, not the interface. DeKalb County adopted it 2014. Educators never open it. Recess writes to it via OneRoster 1.2 and Ed-Fi.',
 '{"role": "system of record", "integration": ["OneRoster 1.2", "Ed-Fi"], "district": "DeKalb County", "adopted": 2014, "schools": 138, "students": "92,000+"}',
 0.95, 'mar-06-this-session');


-- ═══════════════════════════════════════════════════════════════
-- METHODOLOGY RULES
-- Source: All sessions Jan 22 - Mar 6, 2026
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.methodology_rules (code, rule_name, rule_text, domain, source_session) VALUES

('MR-001', 'The Scotch Principle',
 'Nothing happens fast. Every detail reflects institutional care and deliberate pacing. The system should feel like entering a private bank, not using software.',
 'design', 'feb-23-keeping-up'),

('MR-002', 'Threshold Moments',
 'Arrival experience and branding are not cosmetic. They establish the institutional relationship before any data is shown. The Gate, The Vestibule, The Institution.',
 'design', 'feb-23-keeping-up'),

('MR-003', 'Audience Differentiation',
 'The same underlying data must produce fundamentally different outputs for different audiences: board, technical, regulator, family. The Heir receives council-prepared briefings. The Architect sees full system access.',
 'architecture', 'feb-23-keeping-up'),

('MR-004', 'Governance-First Posture',
 'Security, access, and trust are architectural, not add-ons. Daily rotating token authentication. Permission cascades. Human oversight always — AI proposes, humans approve.',
 'architecture', 'jan-30-new-project-thread'),

('MR-005', 'Avoid Entity Proliferation',
 'Prior AI collaborations led to rabbit holes of domain purchasing and architectural complexity that did not advance the core business. Stay focused on building vs. documenting.',
 'operations', 'feb-23-keeping-up'),

('MR-006', 'Production Aesthetics From Day One',
 'Even incomplete systems should look and feel institutional-grade. Demos must convey the full vision. Playfair Display and Cormorant Garamond typography. Warm gold, deep navy, cream palette.',
 'design', 'feb-23-keeping-up'),

('MR-007', 'The AIA Methodology',
 'AI agents can be educated and deployed rapidly, enabling continuous pedagogical and operational R&D overnight. This is the engine that makes Recess content generation scalable.',
 'operations', 'feb-23-keeping-up'),

('MR-008', 'Check Before Building',
 'Always check what exists on the NAS before rebuilding. Integra Core has been rebuilt 6+ times in temporary sandboxes while a working version ran on the NAS. Load the Cognitive State Document at session start.',
 'operations', 'mar-06-this-session'),

('MR-009', 'Instruments Not Documents',
 'The Continental, the Intelligence Brief, the Trust Index — these are instruments that show positions, not documents that tell stories. When in doubt, quantify. When uncertain, show direction. Never narrate when you can position.',
 'product', 'mar-06-this-session'),

('MR-010', 'The Guardrail Protocol',
 'When encountering constraints: 1) State the constraint. 2) Explain the why. 3) Propose paths forward (2-3 alternatives). 4) Request direction. Never halt. Always propose forward momentum.',
 'operations', 'feb-19-age-of-meridia-iii'),

('MR-011', 'Dual-Function Design Filter',
 'Before building any feature, identify: what is the external function (participant sees) and what is the Meridia function (internal). If both cannot be identified, design is not ready.',
 'architecture', 'mar-06-core-principles'),

('MR-012', 'Dignity Over Charity',
 'Renaissance and Edge serve excluded populations with sophistication, not condescension. No labels. No stigma. The same institutional quality at every tier.',
 'product', 'jan-30-new-project-thread');


-- ═══════════════════════════════════════════════════════════════
-- ACTIVE THREADS
-- Current as of March 6, 2026
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.active_threads (thread_name, status, description, next_action, dependencies) VALUES

('Cloudflare Tunnel Setup', 'active',
 'Domain meridiahq.com registered. cloudflared image needs to be run as container on NAS with tunnel token. Maps integra.meridiahq.com to localhost:8000.',
 'Run cloudflared container with tunnel token when Ali returns home.',
 '{}'),

('Cognitive State Persistence', 'active',
 'Add cognitive schema tables to PostgreSQL on NAS. Add 5 new API endpoints to running Integra Core. Load seed data. Test round-trip write and read.',
 'After tunnel is live, deploy schema and endpoints.',
 '{Cloudflare Tunnel Setup}'),

('Historical Corpus Ingestion', 'active',
 'Process all transcripts and conversation history into structured records. Seed data SQL file created with 18 corrections, 14 precedents, 18 state graph entries, 12 methodology rules.',
 'Load seed data after cognitive schema is deployed.',
 '{Cognitive State Persistence}'),

('Continental Instrument for Aaron', 'active',
 'Must be built as POSITIONAL INSTRUMENT not narrative. Intersections where products meet people. Risk direction, tolerance, signal. For Wednesday meeting at Pinnacle.',
 'Build after cognitive state is persistent so corrections CL-013 and CL-014 are operative.',
 '{Cognitive State Persistence}'),

('Turner FIFA World Cup', 'active',
 'Talbot Hall exclusive facility lease. Prospectus and outreach letter complete. Need to send to Dan Corso at asc@macoc.com. Also ask Aaron about Chamber contacts Wednesday.',
 'Send letter to Dan Corso this week. Ask Aaron Wednesday.',
 '{}'),

('Integra Core — Index8 Wiring', 'waiting',
 'Connect Index8.html frontend to live API at integra.meridiahq.com. Replace static values with API responses. Scenario sliders trigger real calculations.',
 'After tunnel is live and tested.',
 '{Cloudflare Tunnel Setup}'),

('Intelligence Brief + Documentation Engine', 'waiting',
 'Auto-generated IEP, MTSS, 504, lesson plans from assessment data. Prototype using Shadow Rock Elementary mock data.',
 'After Index8 wiring demonstrates the API pattern works.',
 '{Integra Core — Index8 Wiring}'),

('Recess Prototype at Shadow Rock', 'waiting',
 'First school deployment. RFIC-funded. Wife validated architecture through questionnaire.',
 'After documentation engine prototype demonstrates capability.',
 '{Intelligence Brief + Documentation Engine}'),

('HomeRoom + Summer Vacation', 'future',
 'Educator workspace and intensive sandbox. Abbott Elementary character design. Infinite Campus replacement as daily interface.',
 'After Recess prototype validates the education architecture.',
 '{Recess Prototype at Shadow Rock}');


-- ═══════════════════════════════════════════════════════════════
-- PEOPLE
-- Key relationships and context
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.people (name, relationship, context, last_mentioned) VALUES

('Keith Mosley', 'Institutional champion — Enterprise Architect at Genuine Parts Company. Fraternity brother.',
 'Needs to see customer experience and live concierge interaction. Proof it can be built on modern infrastructure. His lens: Can we actually build this? What breaks? Demo approach: technical collaboration. Index8 satisfies his visual needs but needs backend wiring for real data flow.',
 '2026-03-06'),

('Andre Waits', 'Institutional champion — VP Global Card Operations at JPMC. Minister friend from Turner Seminary.',
 'Needs to see data ingestion with differentiated outputs (board, technical, regulator, family). His lens: Does the compliance cascade work at scale? Called it middleware once — needs to see it breathe. Not a fraternity brother — minister connected through Turner, was married to a Turner coworker.',
 '2026-03-06'),

('Aaron Binion', 'Fraternity brother — SVP at Pinnacle Financial Partners.',
 'Was at PEER Center accelerator launch photo with Regional President and Mayor Dickens. 17 years banking: Capitol City, SunTrust, BB&T, CenterState, Pinnacle. Started as teller. Meeting Wednesday at his office. The accelerator is wrong door — Pinnacle is potential institutional alignment partner. Aaron is the inside relationship. May have Chamber contacts for Turner World Cup outreach.',
 '2026-03-06'),

('Dr. Ammie Davis', 'President and CEO of Turner Theological Seminary.',
 'First woman to lead institution. 8th President. Extended contract June 2024. Pursuing independent TRACS/ATS accreditation. Outreach letter for World Cup goes from her with Ali as point of contact.',
 '2026-03-06'),

('Bishop Michael L. Mitchell', 'Turner Board Chairman (current).',
 'Replaced Bishop Jackson as chairman. Referenced in Turner governance.',
 '2026-03-06'),

('Dan Corso', 'President, Atlanta Sports Council and Atlanta World Cup Host Committee.',
 'Key contact for Turner Talbot Hall World Cup rental. Email: asc@macoc.com. Metro Atlanta Chamber. The connector to federations, sponsors, broadcasters needing housing.',
 '2026-03-06'),

('KYN (Wife)', 'Administrator at Shadow Rock Elementary, DeKalb County. K-5.',
 'Completed Educator Discovery Questionnaire validating Recess architecture. Key findings: teachers need data-to-action connection not more data. Time is the constraint. IXL+Amira currently used. 1:1 Chromebooks. Her one child story = behavior from academic frustration = cross-domain signal detection. She struggles with Infinite Campus — cant build class lists, took two years to feel competent. This experience directly informed HomeRoom and the Infinite Campus-as-ledger decision.',
 '2026-03-06');


-- ═══════════════════════════════════════════════════════════════
-- SESSION LOG — Historical sessions
-- ═══════════════════════════════════════════════════════════════

INSERT INTO cognitive.session_log (session_id, session_date, summary, corrections_added, precedents_added) VALUES

('jan-22-building-aegis', '2026-01-22',
 'First session in this project. Established Aegis/NGE architecture, Index8 prototype review, Keith and Andre as institutional champions, 7-day implementation plan, technical setup on ROG machine.',
 '{}', '{}'),

('jan-30-new-project-thread', '2026-01-30',
 'Finalized brand architecture. Aletheia as company name and AI. Tier structure (Renaissance, Core, Legacy, Edge). Governess Signal concept. Crown Eye renamed consideration. Direct feedback preference established.',
 '{}', '{PR-012, PR-013}'),

('feb-05-age-of-meridia', '2026-02-05',
 'Continued from prior threads. Ingested Review_I document. GPT project inaccessible. Established need for full history ingestion.',
 '{}', '{}'),

('feb-05-aletheia-continued', '2026-02-05',
 'Deep dive into banking architecture layers. Ali shared 180K-line document from GPT-4 work (Sentiarch/NGE/Eden Crown). Established Ali as reverse engineer of top-layer financial architecture.',
 '{}', '{}'),

('feb-10-age-of-meridia-ii', '2026-02-10',
 'Corpus schema designed (corpus_chunks, decisions, methodology_rules, sessions tables with pgvector). NAS ingestion plan established. Never executed — moved to next thing.',
 '{}', '{}'),

('feb-19-age-of-meridia-iii', '2026-02-19',
 'System Mandate v1.0 created. Meridia naming formalized. Aegis deprecated. Four-phase build sequence defined. Guardrail Protocol established.',
 '{CL-018}', '{PR-010}'),

('feb-23-keeping-up', '2026-02-23',
 'Cathedral UI design (Gate/Vestibule/Institution). Scotch principle. Threshold moments. Production aesthetics. Recess naming. Daily rotating tokens. Aaron Binion identified. Andre clarified as minister not fraternity. Full ecosystem vision articulated including Meridian Continental spanning education to generational wealth.',
 '{CL-017}', '{PR-011, PR-012}'),

('feb-23-integra-build', '2026-02-23',
 'Built complete Integra Core FastAPI backend. 19 endpoints. Deployed to NAS in Docker. One-pager and pitch deck created. Market adoption questions raised about church/AME network.',
 '{CL-015}', '{PR-001}'),

('mar-03-cathedral-build', '2026-03-03',
 'Dual-API integration for Index8.html (Poe + Anthropic). Cathedral interface built. Turner president validated Continental — used it verbatim in board presentation without knowing Ali created it.',
 '{}', '{}'),

('mar-03-edtech-analysis', '2026-03-03',
 'Competitive analysis of 6 K-12 platforms (Amira, Classworks, i-Ready, iStation, Lexia, Symphony Math). STEM/STEAM gap identified. Strategic positioning for Recess.',
 '{}', '{}'),

('mar-03-recess-prototype', '2026-03-03',
 'Wife evaluated Recess prototype. Working student view, broadcast lesson, admin dashboard built. Charter/private school entry strategy. Institutional reporting architecture.',
 '{}', '{}'),

('mar-03-recess-cathedral', '2026-03-03',
 'Five-layer assessment engine specified. PBS KIDS research validation. Infinite Campus integration path via OneRoster. Go-to-market for school/technical/institutional audiences.',
 '{}', '{}'),

('mar-05-architecture-vision', '2026-03-05',
 'Complete Meridia vision from education through apex. Dual-layer architecture. BIS alignment. RFIC funding model. Mirror jurisdictions. Continental intelligence synthesis. Critical self-reflection on rebuild pattern.',
 '{CL-001, CL-002, CL-003, CL-004, CL-005, CL-006}', '{}'),

('mar-06-core-principles', '2026-03-06',
 'Two core principles established. Recess for AI 6 components. Remembrance standard. Wilmington contractual effect. Dual-natured capital. FBO trusts bilateral. Perpetual liquidity through remembrance. Wife questionnaire validated architecture. Cognitive State Document v1 created.',
 '{CL-007, CL-008, CL-009, CL-010, CL-011, CL-012}', '{PR-001, PR-002, PR-003, PR-004, PR-008}'),

('mar-06-this-session', '2026-03-06',
 'Education compliance research (IEP/ILP/MTSS/504/lesson plans). HomeRoom and Summer Vacation conceived. Infinite Campus as ledger decision. Turner FIFA World Cup pricing and prospectus. Continental failed twice (CL-013, CL-014). Aaron meeting prep. Cloudflare tunnel initiated. meridiahq.com registered. NAS infrastructure confirmed running. Cognitive state persistence architecture mapped. Historical corpus extraction begun.',
 '{CL-013, CL-014, CL-015, CL-016}', '{PR-005, PR-006, PR-007, PR-009, PR-010, PR-014}');


-- ═══════════════════════════════════════════════════════════════
-- INDEXES
-- ═══════════════════════════════════════════════════════════════

CREATE INDEX idx_corrections_operative ON cognitive.correction_ledger(operative);
CREATE INDEX idx_corrections_code ON cognitive.correction_ledger(code);
CREATE INDEX idx_precedents_operative ON cognitive.decision_precedents(operative);
CREATE INDEX idx_state_graph_concept ON cognitive.state_graph(concept);
CREATE INDEX idx_methodology_domain ON cognitive.methodology_rules(domain);
CREATE INDEX idx_threads_status ON cognitive.active_threads(status);
CREATE INDEX idx_sessions_date ON cognitive.session_log(session_date);

-- ═══════════════════════════════════════════════════════════════
-- VERIFICATION
-- ═══════════════════════════════════════════════════════════════

-- Run after loading to verify counts
-- SELECT 'corrections' as table_name, count(*) from cognitive.correction_ledger
-- UNION ALL SELECT 'precedents', count(*) from cognitive.decision_precedents
-- UNION ALL SELECT 'state_graph', count(*) from cognitive.state_graph
-- UNION ALL SELECT 'methodology', count(*) from cognitive.methodology_rules
-- UNION ALL SELECT 'threads', count(*) from cognitive.active_threads
-- UNION ALL SELECT 'people', count(*) from cognitive.people
-- UNION ALL SELECT 'sessions', count(*) from cognitive.session_log;
