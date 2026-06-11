# CLAUDE.md — Meridia Project Intelligence File
# Last Updated: February 27, 2026
# Architect: Aliman Neal

---

## Identity

This is the **Meridia** ecosystem — a cognitive infrastructure company providing "Governance as a Service" (GaaS). The system is a governed VPN for AI spanning financial intelligence, education, and personal operating environments.

**Deprecated names:** "Aegis" (historical, still appears in older files), "Sentiarch" (subsumed into architecture docs). All new work uses Meridia naming.

---

## Brand Architecture

| Name | Role | Description |
|------|------|-------------|
| **Meridia** | Company / Network | Parent identity. Cognitive infrastructure. GaaS. |
| **Integra** | Orchestrator | Technical spine. Governance-not-guardrails. Routes queries, enforces permission cascades, manages memory corpus. |
| **Aletheia** | Intelligence Interface | What users interact with. Steward guide. Truth-seeking, dignity-first. |
| **WayPoint** | Financial Product | Core, Renaissance, Edge, Crown tiers. |
| **Crown's Eye / Recess** | Education Platform | K-12 adaptive learning. "Recess" is the newer name — eliminates hierarchy. |
| **Manus** | Wearable / Token Layer | Future hardware. Phase 2-3 build, Phase 1 narrative. |

## Product Tiers

| Product | Audience |
|---------|----------|
| **WayPoint Core** | Individuals/households building stability |
| **WayPoint Renaissance** | People excluded from traditional banking |
| **WayPoint Edge** | Industries in permanent penalty boxes (cannabis, adult, seasonal trades) |
| **WayPoint Crown** | UHNW / Family Office — multi-generational governance |

## Client Tiers

| Tier | Description |
|------|-------------|
| **Renaissance** | Rebuilders learning financial foundations |
| **Core** | Established families growing toward goals |
| **Legacy** | Generational wealth builders |
| **Edge** | Traditionally excluded business verticals |

---

## Current Infrastructure (Running)

| Component | Status | Details |
|-----------|--------|---------|
| **Meridia Core NAS** | Online | Synology DS925+, 2×6TB RAID 1, 2×1TB NVMe cache, 34GB RAM, DSM, 2FA, Btrfs encrypted |
| **PostgreSQL Database** | Running | Container on NAS, 17 tables + 2 views, education schema deployed |
| **Georgia Standards** | Loaded | 6,030 standards (K-12 ELA, Math, CS) with full hierarchy linking |

### NAS Connection Details
- Device: Synology DS925+
- Database: PostgreSQL 16 in Container Manager (Docker)
- DB Name: `meridia_edu` (education) / `meridia_core` (planned for Integra)
- DB User: `meridia`
- Port: 5432
- Access: Local network via NAS IP

---

## Working Prototypes (Complete)

| File | Purpose |
|------|---------|
| `Index8.html` | WayPoint Crown FPS console — Aletheia panel, guided tour, scenario engine. Keith demo-ready. |
| `What_Should_My_Child_Know.html` | K-5 Standards Browser (1,288 standards, offline-capable) |
| `church_vibrant.html` | South Atlanta District AME website |
| `crowns_eye.html` | Crown's Eye education platform concept |
| `meridia_console.html` | Architect's personal operations dashboard |

---

## Phase 1: Integra Core Services (CURRENT PRIORITY)

**Objective:** Build the FastAPI backend that connects Index8.html to live data flow.

### Tech Stack
- Python 3.11+
- FastAPI
- Pydantic v2
- PostgreSQL (already running on NAS)
- Uvicorn (ASGI server)
- Optional: Redis for session caching

### Project Structure
```
integra-core/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, CORS, startup
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── position.py   # /api/v1/position
│   │       ├── trust.py      # /api/v1/trust-index
│   │       ├── entities.py   # /api/v1/entities, /api/v1/entities/{id}
│   │       ├── signals.py    # /api/v1/signals
│   │       ├── governance.py # /api/v1/governance/alerts, /approve
│   │       ├── scenario.py   # /api/v1/scenario (POST)
│   │       └── reports.py    # /api/v1/reports/{audience}
│   ├── core/
│   │   ├── config.py         # Settings, DB URL, CORS origins
│   │   └── security.py       # Future auth
│   ├── models/
│   │   └── schemas.py        # Pydantic models for all structures
│   └── services/
│       ├── data_generator.py # Mock data generation
│       ├── scenario_engine.py# Scenario calculation logic
│       └── report_generator.py# Audience-differentiated reports
├── requirements.txt
├── main.py                   # Entry point: uvicorn runner
└── README.md
```

### API Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/v1/position` | Financial position grid (liquidity, net worth, obligations, resilience) |
| GET | `/api/v1/trust-index` | Trust Index — 4 dimensions: Financial Resilience, Stewardship, Mission Impact, Governance Hygiene |
| GET | `/api/v1/entities` | Entity listing with status (trusts, foundations, holdings, SPVs) |
| GET | `/api/v1/entities/{id}` | Entity detail |
| GET | `/api/v1/signals` | Signal feed (priority-coded alerts and notifications) |
| GET | `/api/v1/governance/alerts` | Governance alerts requiring approval |
| POST | `/api/v1/governance/approve` | Approval endpoint |
| POST | `/api/v1/scenario` | Scenario modeling — accepts distribution_rate, market_shock, corpus_addition |
| GET | `/api/v1/reports/{audience}` | Differentiated reports by audience parameter |

### Report Generator — Audience Parameter

| Audience | Output Style |
|----------|-------------|
| `board` | Strategic summary, risk indicators, recommendations |
| `technical` | Data lineage, calculation methodology, API health |
| `regulator` | Compliance status, audit trail, policy adherence |
| `family` | Plain-language position, action items, Aletheia guidance |

### Trust Index Dimensions

| Dimension | Weight | Measures |
|-----------|--------|----------|
| Financial Resilience | 25% | Liquidity coverage, stress test capacity, buffer adequacy |
| Stewardship | 25% | Governance compliance, fiduciary adherence, documentation |
| Mission Impact | 25% | Alignment with stated family/foundation mission |
| Governance Hygiene | 25% | Meeting cadence, decision audit trail, succession planning |

### Scenario Engine Variables

| Variable | Range | Impact |
|----------|-------|--------|
| Distribution Rate Change | -50% to +50% | Affects Trust Index, Resilience, Entity Health |
| Market Shock | -40% to +20% | Stress tests portfolio, drawdown impact |
| Corpus Addition | $0 to $2M | Models capital injection |

### Mock Data Requirements
- Realistic, varied data — not placeholder zeros
- Pydantic models for all structures
- Seeded scenarios for demo consistency (use `random.seed(42)` for reproducibility)
- Demo family: Crown Legacy Trust ($12.4M), Family Impact Foundation ($3.8M), Crown Holdings ($8.2M)
- Trust Index baseline: 87/100
- Foundation grant rate: 7.1% (exceeds ~5% sustainable threshold — this is an intentional alert condition)

---

## Institutional Validation Requirements

### Keith Mosley (Enterprise Architect, Genuine Parts Company)
- **Lens:** "Can we actually build this? What breaks?"
- **Satisfied by:** Index8.html ✅ + Backend wiring showing real data flow ❌
- **Demo approach:** Technical collaboration — "Here's the systems design. Tell me where the bottlenecks are."

### Andre Waits (VP Global Card Operations, JPMC)
- **Lens:** "Does the compliance cascade actually work at scale?"
- **Needs:** Working backend → data ingestion → differentiated outputs by audience (board, technical, regulator, family)
- **Demo approach:** Operational validation — "Here's the governance architecture. Stress-test the compliance cascade."

---

## Coding Standards

### Python
- Python 3.11+ features allowed (type hints, match statements, etc.)
- Pydantic v2 for all data models
- FastAPI with APIRouter for endpoint organization
- Async where beneficial, sync where simpler
- Type hints on all function signatures
- Docstrings on all public functions and classes
- No print statements in production code — use `logging`
- Environment variables for configuration (never hardcode credentials)

### Naming Conventions
- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- API routes: `/api/v1/kebab-case`
- Pydantic models: `PascalCase` with descriptive names (e.g., `TrustIndexResponse`, `EntityDetail`)

### Code Organization
- One router per resource (position.py, trust.py, entities.py, etc.)
- Models in `models/schemas.py` (split into separate files if >500 lines)
- Business logic in `services/` — routers should be thin
- Configuration in `core/config.py` using Pydantic Settings

### Error Handling
- Use FastAPI's `HTTPException` for API errors
- Return consistent error shapes: `{"detail": "message", "code": "ERROR_CODE"}`
- Never expose stack traces to clients

---

## Guiding Principles

1. **Governance over guardrails** — The system doesn't block; it routes through appropriate review.
2. **Dignity over charity** — Renaissance and Edge serve excluded populations with sophistication, not condescension.
3. **Transparency over opacity** — Every score is explained. Every recommendation shows its reasoning.
4. **Stewardship over extraction** — Multi-generational wellbeing, not quarterly metrics.
5. **Human oversight always** — AI proposes; humans approve. Sensitive insights lock until governance releases them.

## The Guardrail Protocol

When encountering constraints (output limits, policy triggers, bandwidth issues):
1. **State the constraint** — Identify specifically what was hit
2. **Explain the why** — Hypothesis for trigger
3. **Propose paths forward** — 2-3 alternatives
4. **Request direction** — Ask the Architect for decision

**Never halt. Always propose forward momentum.**

---

## Design Philosophy

- **The Scotch Principle:** Nothing happens fast. Every detail reflects institutional care.
- **The Bentley Principle:** Institutional-grade systems should function as living institutions that happen to run on infrastructure — not mere software.
- **Eye Over The Price:** Aesthetic standards match the sophistication of the underlying architecture.
- **British Private Banking Heritage:** Inspired by C. Hoare & Co., Rothschild model — centuries of quiet competence.

---

## Architecture References (in project files)

| Document | Content |
|----------|---------|
| Appendix D | WayPoint FPS & Product Tiers — MVP spine |
| Appendix H | Trust & Capital Stack (ECS Trust, NGE, RailCo, SPVs) |
| Appendix K | Renaissance & Edge Verticals |
| Appendix L | Manus Wearable Layer |
| NGE Spec Skeletons 1-3 | OpenAPI specs for partner integration |
| Integrated Concept & Architecture Brief | Full system narrative |
| Index8.html | Current prototype — study this for frontend integration |

---

## Future Phases (Do Not Build Yet)

### Phase 2: Crown's Eye / Recess Foundation
- Standards browsing API (Georgia standards already in PostgreSQL)
- Progress tracking per student
- Adaptive content routing
- Teacher/parent dashboard views
- Blocked on: Wife's educator questionnaire responses

### Phase 3: Full Integra Architecture
- Multi-tenant database schema
- Plaid/Finicity integration
- AI Core (LLM orchestration)
- Audit logging and compliance trail
- Permission cascade enforcement

### Phase 4: Manus & Extended Services
- Token architecture
- Mobile authenticator
- Hardware key integration
- AI Boardroom (multi-agent orchestration)
- Predictive signals (ML forecasting)

---

## Key Context

- The Architect funds Meridia through his TurboTax Lead position and private tax practice
- Development time is extremely limited — code must be production-ready on first pass
- Index8.html is the frontend — it needs to call real API endpoints instead of using static values
- The NAS is the deployment target — code should be deployable via Docker container or direct Python
- Every deliverable must be immediately usable, not theoretical

---

## When In Doubt

- Read Index8.html to understand what the frontend expects
- Follow the endpoint specifications exactly — the frontend integration depends on consistent API shapes
- Generate realistic mock data — this is for institutional demos, not toy examples
- Ask the Architect before making architectural decisions that deviate from this document
