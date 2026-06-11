# AIA Corpus Architecture — Deployment & Ingestion Guide

**Document:** EIG-CORPUS-2026-001  
**Date:** February 21, 2026  
**Target:** Synology DS925+ / PostgreSQL Container  

---

## What This Is

This is the filing system for the AIA's permanent brain. Every document, every decision, every framework, every concept that constitutes Eden Intelligence Group's institutional knowledge gets structured here. Once deployed, any AI session that connects to this database inherits the full intelligence state — not a 15-line memory summary, not a conversation transcript, but the actual classified, indexed, searchable corpus.

---

## Schema Overview

The corpus lives in its own PostgreSQL schema (`corpus`) alongside the existing education tables. Nothing is disturbed. Six core tables plus supporting infrastructure:

### Core Tables

| Table | Purpose |
|-------|---------|
| `corpus.documents` | Every file in the corpus — classified by status, origin, domain, era |
| `corpus.extracts` | Distilled knowledge pulled from documents — decisions, principles, definitions, frameworks |
| `corpus.lineage` | How documents relate: supersedes, evolves from, splits into, merges with |
| `corpus.tags` | Flexible tagging beyond the fixed classification enums |
| `corpus.sessions` | Record of every ingestion or classification session |
| `corpus.decisions` | Permanent architectural decision records with rationale |

### Supporting Tables

| Table | Purpose |
|-------|---------|
| `corpus.naming_registry` | Tracks name evolution (Aegis → Sentiarch → Meridia → WayPoint) |
| `corpus.document_tags` | Many-to-many join for flexible tagging |
| `corpus.session_documents` | Links sessions to documents they created/modified |

### Key Views & Functions

| Function | What It Does |
|----------|-------------|
| `corpus.search('query')` | Full-text search across all documents (title, summary, content) |
| `corpus.get_lineage(doc_id)` | Returns full evolution tree for any document |
| `corpus.domain_state('waypoint_core')` | Current canon + foundational docs for a product domain |
| `corpus.active_decisions()` | All active architectural decisions, optionally filtered by domain |
| `corpus.current_canon` | Materialized view of all canon documents with tags |

---

## Classification System

### Document Status (Most Important)

Every document gets exactly one status. This is how the AIA knows what's current vs historical:

- **canon** — This is the current truth. The latest version. What the AIA operates on.
- **superseded** — Was canon, but has been replaced. Kept for lineage tracking.
- **foundational** — Historical document that shaped current thinking. Not current but still relevant context.
- **exploratory** — Ideas that were explored but not committed to. May be revisited.
- **retired** — Explicitly abandoned. Kept for record but marked as no longer applicable.
- **raw** — Just ingested, not yet classified. Default state for new documents.

### Document Origin

Where the document came from:

- **dropbox** — Historical archive (the years of accumulated material)
- **claude_session** — Output from Claude conversations
- **gemini_session** — Output from Gemini conversations
- **gpt_session** — Legacy GPT work (historical reference only, not ongoing)
- **manual** — Created directly by the architect
- **generated** — Produced by AIA pipeline (reports, analyses)
- **external** — Third-party material (research papers, regulations, competitor info)

### Product Domain

Which part of the ecosystem this relates to:

- waypoint_core, waypoint_crown, waypoint_edge
- crowns_eye, integra, kingdom_soundworks
- eden_corporate (legal, structure, IP)
- aia_methodology (the AIA itself)
- cross_domain, general

### Era

When in the evolution timeline this was created:

- **pre_meridia** — Aegis/Sentiarch naming era
- **transition** — Period when naming was shifting
- **meridia_v1** — Current Meridia framework
- **eden_formation** — Corporate structure phase (now)

---

## Ingestion Workflow

### How Documents Flow In

The ingestion process is designed to work naturally across sessions, exactly like the MCR report emerged from the ecosystem assessment:

**Step 1: Session starts.** A new session record is created in `corpus.sessions` documenting what model is being used and what the session aims to accomplish.

**Step 2: Documents are loaded.** Files from Dropbox (or any source) are read. Text is extracted. A `corpus.documents` record is created with status = 'raw'.

**Step 3: Classification happens conversationally.** The AI reads the document and proposes classification — status, domain, era, tags, summary, key concepts. The architect confirms or corrects. Classification is stored with confidence level ('verified' if architect confirmed, 'inferred' if AI-classified).

**Step 4: Extracts are distilled.** Key decisions, principles, definitions, and frameworks are pulled from the document and stored as `corpus.extracts`. These are what the AIA actually operates on day-to-day.

**Step 5: Lineage is mapped.** If this document supersedes, evolves from, or relates to existing documents, those relationships are recorded in `corpus.lineage`.

**Step 6: Session closes.** Session record is updated with counts and summary.

### The Natural Organization Principle

You don't need to pre-classify everything before ingestion. The schema handles documents arriving in any order:

- A document arrives as 'raw'
- Over subsequent sessions, it gets classified
- As related documents arrive, lineage connections form
- The materialized view `corpus.current_canon` always reflects the latest classified state
- The search function works on raw documents too — classification improves retrieval but doesn't block it

This means you can ingest 50 Dropbox files in one session, classify 10 of them, and come back to the rest later. The corpus grows organically. Structure emerges from the intelligence layer, not from pre-organization.

---

## Deployment Steps

### 1. Connect to PostgreSQL on NAS

```bash
# SSH into Synology (or use Docker exec)
docker exec -it <postgres_container_name> psql -U postgres
```

### 2. Create Database (if not exists)

```sql
CREATE DATABASE meridia;
\c meridia
```

### 3. Run Schema

```bash
psql -U postgres -d meridia -f aia_corpus_schema.sql
```

### 4. Verify

```sql
-- Check tables created
\dt corpus.*

-- Check seed data
SELECT * FROM corpus.naming_registry;
SELECT * FROM corpus.decisions;
SELECT * FROM corpus.tags;
```

---

## How This Changes Everything

### Before (Current State)
- Claude gets 15 lines of memory + whatever transcripts are attached
- New sessions start with partial context
- A month of work is invisible
- Years of Dropbox material is inaccessible
- Every model interaction reinvents the wheel

### After (Corpus Live)
- Any session can query `corpus.search('governance cascade')` and get every relevant document
- `corpus.active_decisions()` returns every architectural decision with rationale
- `corpus.domain_state('waypoint_core')` shows current canon for any product
- `corpus.get_lineage(doc_id)` traces how any concept evolved
- The naming registry resolves "is it Aegis or Meridia or WayPoint" instantly
- New documents are classified against existing corpus, not in isolation

### For Keith
He can see the architecture behind the architecture. Not just Index8's frontend, not just 24 API endpoints — the actual intelligence layer that makes the system know what it knows. The corpus schema IS the proof that this isn't middleware.

### For Andre
When the system produces four audience-differentiated reports from the same underlying data, the corpus is what gives those reports depth. The AIA doesn't generate reports from a prompt — it generates them from classified institutional knowledge with full lineage tracking and decision history.

---

## Next Steps After Deployment

1. **Deploy schema** on NAS PostgreSQL
2. **Begin Dropbox ingestion** — start with the most foundational documents (Appendices D, H, K, L; architecture briefs; the documents that shaped the core concepts)
3. **Classify over sessions** — each conversation with Claude can ingest and classify a batch of documents
4. **Build retrieval API** — a simple endpoint that lets any AI session query the corpus
5. **Connect to Integra** — the API layer reads from corpus instead of session context

The corpus grows with every session. The intelligence compounds. The AIA becomes real.

---

*Eden Intelligence Group — R&D Division*  
*Classification: Internal — Operational*
