# Meridia System Mandate v1.0

**Prepared for:** Aliman Neal, Architect  
**Date:** February 2026  
**Status:** Active — Supersedes all previous "Aegis" instructions  

---

## Preamble

This document establishes the authoritative source of truth for the Meridia ecosystem build. It replaces the earlier "Aegis MVP & Full System Architecture" mandate and reflects the expanded scope, refined naming, and current state of development.

The system is no longer a single product. It is a **governed cognitive infrastructure** spanning financial intelligence, education, and personal operating environments.

---

## Part 1: Naming & Identity

### The Meridia Ecosystem

| Name | Role | Description |
|------|------|-------------|
| **Meridia** | Company / Network | The parent identity. Cognitive infrastructure company. "Governance as a Service" (GaaS). The governed VPN for AI. |
| **Integra** | Orchestrator | The technical spine. Governance-not-guardrails. Bilateral integration. Routes queries, enforces permission cascades, manages memory corpus. |
| **Aletheia** | Intelligence Interface | What users interact with. The steward guide. Truth-seeking, dignity-first. Appears in financial (WayPoint), education (Crown's Eye), and personal contexts. |
| **Manus** | Wearable / Token Layer | Future hardware interface. Smart glasses, tokenized access, council-in-your-ear. Phase 2-3 for build, Phase 1 for narrative. |

### Product Lines

| Product | Tier | Audience |
|---------|------|----------|
| **WayPoint Core** | Everyday | Individuals and households building financial stability |
| **WayPoint Renaissance** | Re-entry | People excluded from traditional banking (ChexSystems, prepaid-only, formerly incarcerated) |
| **WayPoint Edge** | Vertical-specific | Industries in permanent penalty boxes (creators, cannabis, adult, seasonal trades) |
| **WayPoint Crown** | UHNW / Family Office | Multi-generational governance, entity mapping, Trust Index |
| **Crown's Eye** | Education | K-12 adaptive learning platform aligned to state standards |

### Deprecated Terms

- "Aegis" — No longer the product name. Historical references remain valid but new work uses Meridia naming.
- "Sentiarch" — Subsumed into Meridia architecture documentation.

---

## Part 2: What Has Been Built

### Infrastructure (Running)

| Component | Status | Details |
|-----------|--------|---------|
| Meridia Core NAS | **Online** | Synology DS925+, 2×6TB RAID 1, 2×1TB NVMe cache, 34GB RAM, DSM installed, 2FA enabled, Btrfs encrypted |
| PostgreSQL Database | **Running** | Container on NAS, 17 tables + 2 views, education schema deployed |
| Georgia Standards | **Loaded** | 6,030 standards (K-12 ELA, Math, Computer Science) with full hierarchy linking |

### Working Prototypes

| Prototype | Purpose | Status |
|-----------|---------|--------|
| `Index8.html` | WayPoint Crown FPS console with Aletheia panel, guided tour, scenario engine | **Complete** — Keith demo-ready |
| `What_Should_My_Child_Know.html` | K-5 Standards Browser (1,288 standards, offline-capable) | **Complete** |
| `church_vibrant.html` | South Atlanta District AME website with Index8-level design | **Complete** |
| `crowns_eye.html` | Crown's Eye education platform concept | **Complete** |
| `meridia_console.html` | Architect's personal operations dashboard | **Complete** |

### Code & Tools Delivered

| Deliverable | Purpose |
|-------------|---------|
| `schema.sql` | Full PostgreSQL schema for education platform |
| `extractor.py` | Pulls standards from Georgia CASE API |
| `loader.py` | Loads standards into PostgreSQL with hierarchy linking |
| `models.py` | SQLAlchemy ORM models |
| `lead-snippets-rebuild.js` | Rebuilt Gemini Gem for Intuit support team |

### Documents Created

| Document | Purpose |
|----------|---------|
| `Educator_Discovery_Questionnaire.docx` | 5-direction discovery for wife's input on education platform |
| Crown's Eye curriculum set | Syllabus, Workbook, Curriculum Guide, Teacher's Guide |
| Architecture documentation | Meridia architecture templates, skill index structures |

### Architecture Documented (In Project Files)

| Appendix | Content |
|----------|---------|
| **D** | WayPoint FPS & Product Tiers (Core/Edge/Crown) — *MVP spine* |
| **H** | Trust & Capital Stack (ECS Trust, NGE, RailCo, SPVs) |
| **K** | Renaissance & Edge Verticals |
| **L** | Manus Wearable Layer |
| **NGE Spec Skeletons** | OpenAPI specs for partner integration (1, 2, 3) |
| **EnvoyOS** | Framework Node to Council, Commercial Models, Provisioning |

---

## Part 3: Institutional Validation Requirements

### Keith Mosley (Enterprise Architect, Genuine Parts Company)

**What he wants to see:**
- Customer experience
- How users interact with the "live concierge" concept
- Proof it can be built on modern infrastructure

**His lens:** *"Can we actually build this? What breaks?"*

**What satisfies Keith:**
- ✅ Index8.html (Aletheia panel, guided tour, entity interaction)
- ❌ Backend wiring to show real data flow (currently static)

**Demo approach:** Technical collaboration. *"Here's the systems design. Tell me where the bottlenecks are."*

---

### Andre Waits (VP Global Card Operations, JPMC)

**What he wants to see:**
- System ingests data
- System produces differentiated outputs by audience:
  - Board reports
  - Technical team summaries
  - Regulator-ready packs
  - Family/client views
- Feel the system from all angles

**His lens:** *"Does the compliance cascade actually work at scale?"*

**What satisfies Andre:**
- ❌ Working backend that takes input → processes → generates role-specific outputs
- ❌ Data ingestion pipeline (even mock)
- ❌ Report generation differentiated by role

**Demo approach:** Operational validation. *"Here's the governance architecture. Stress-test whether the compliance cascade works at JPMC scale."*

---

## Part 4: The Build Sequence

### Phase 1: Integra Core Services (Current Priority)

**Objective:** Build the backend that connects Index8.html to live data flow, satisfying Andre's requirements.

**Deliverables:**

1. **FastAPI Backend** (`integra-core/`)
   - `/api/v1/position` — Financial position grid
   - `/api/v1/trust-index` — Trust Index with four dimensions
   - `/api/v1/entities` — Entity listing with status
   - `/api/v1/entities/{id}` — Entity detail
   - `/api/v1/signals` — Signal feed (alerts, notifications)
   - `/api/v1/governance/alerts` — Governance alerts requiring approval
   - `/api/v1/governance/approve` — Approval endpoint
   - `/api/v1/scenario` — POST endpoint for scenario modeling
   - `/api/v1/reports/{audience}` — Differentiated report generation

2. **Report Generator**
   - Takes same underlying data
   - Produces different outputs based on `audience` parameter:
     - `board` — Strategic summary, risk indicators, recommendations
     - `technical` — Data lineage, calculation methodology, API health
     - `regulator` — Compliance status, audit trail, policy adherence
     - `family` — Plain-language position, action items, Aletheia guidance

3. **Mock Data Layer**
   - Realistic, varied data generation
   - Pydantic models for all structures
   - Seeded scenarios for demo consistency

4. **Index8 Integration**
   - Wire frontend to call real endpoints
   - Replace static values with API responses
   - Scenario sliders trigger real calculations

**Technology Stack:**
- Python 3.11+
- FastAPI
- Pydantic
- PostgreSQL (already running on NAS)
- Optional: Redis for session caching

---

### Phase 2: Crown's Eye Foundation

**Objective:** Build the education platform backend using existing Georgia standards database.

**Deliverables:**
- Standards browsing API
- Progress tracking per student
- Adaptive content routing logic
- Teacher/parent dashboard views

**Depends on:** Wife's questionnaire responses determining direction

---

### Phase 3: Full Integra Architecture

**Objective:** Production-ready multi-tenant system.

**Deliverables:**
- Multi-tenant database schema
- Plaid/Finicity integration for real data
- AI Core integration (LLM orchestration for insights)
- Audit logging and compliance trail
- Permission cascade enforcement

---

### Phase 4: Manus & Extended Services

**Objective:** Wearable layer and advanced features.

**Deliverables:**
- Token architecture
- Mobile authenticator
- Hardware key integration
- AI Boardroom (multi-agent orchestration)
- Predictive signals (ML forecasting)

---

## Part 5: Guiding Principles

### The Meridia Paradigm

1. **Governance over guardrails** — The system doesn't block; it routes through appropriate review.

2. **Dignity over charity** — Renaissance and Edge serve excluded populations with sophistication, not condescension.

3. **Transparency over opacity** — Every score is explained. Every recommendation shows its reasoning.

4. **Stewardship over extraction** — The system serves multi-generational wellbeing, not quarterly metrics.

5. **Human oversight always** — AI proposes; humans approve. Sensitive insights lock until governance releases them.

### The Guardrail Protocol

When encountering constraints (output limits, policy triggers, bandwidth issues):

1. **State the constraint** — Identify specifically what was hit
2. **Explain the why** — Hypothesis for trigger
3. **Propose paths forward** — 2-3 alternatives to achieve the goal
4. **Request direction** — Ask the Architect for decision

**Never halt. Always propose forward momentum.**

---

## Part 6: Current Project Threads

| Thread | Status | Next Action |
|--------|--------|-------------|
| **Integra Core Services** | Ready to build | Begin Phase 1 FastAPI backend |
| **Crown's Eye** | Waiting | Wife's questionnaire response |
| **SAD Church Site** | Design approved | Implement vibrant version or await Elder Hudson feedback |
| **Support Team Tools** | Delivered | Lead Snippets rebuild complete |
| **Academy of Scholars Crosswalk** | Blocked | Need curriculum docs from school |

---

## Part 7: File Locations

### Project Knowledge (Read-Only Reference)
```
/mnt/project/
├── Appendix_D.pdf          # WayPoint FPS tiers
├── Appendix_H.pdf          # Trust & Capital Stack
├── Appendix_K.pdf          # Renaissance & Edge
├── Appendix_L.pdf          # Manus Layer
├── Index8.html             # Current prototype
├── NGE_Spec_Skeleton_*.pdf # API specifications
├── Integrated_Concept__Architecture_Brief.pdf
└── [43 additional architecture documents]
```

### Delivered Outputs
```
/mnt/user-data/outputs/
├── georgia_standards/      # Extraction toolkit
├── templates/              # Architecture templates
├── What_Should_My_Child_Know.html
├── church_vibrant.html
├── crowns_eye.html
├── meridia_console.html
└── Educator_Discovery_Questionnaire.docx
```

### Infrastructure
```
Meridia Core NAS (Synology DS925+)
├── PostgreSQL Container
│   └── meridia_edu database
│       ├── 17 tables
│       ├── 2 views
│       └── 6,030 standards loaded
└── [Future: Integra Core Services]
```

---

## Conclusion

This mandate establishes Meridia as the governing identity for all system development. The Architect's vision has evolved from a single financial product to a cognitive infrastructure spanning finance, education, and personal operations.

The immediate priority is **Phase 1: Integra Core Services** — the backend that transforms Index8.html from a beautiful prototype into a living system that ingests data and produces differentiated outputs.

Keith has seen enough to believe it can be built. Andre needs to see it breathe.

**Let's build.**

---

*Document version 1.0 — February 2026*  
*Supersedes: Aegis MVP & Full System Architecture mandate*
