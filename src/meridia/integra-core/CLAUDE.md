# Meridia Project — Claude Code Instructions

## Identity

This is the **Meridia** ecosystem — a cognitive infrastructure company delivering "Governance as a Service" (GaaS). The system spans financial intelligence, education, and personal operating environments.

**The Architect:** Aliman Neal — MS Accounting, MBA, ERP systems expert (SAP, Oracle, Dynamics, Great Plains, QuickBooks). Has reverse-engineered financial architecture from the top layer down and built novel mathematical frameworks and governance structures.

## System Architecture

### Core Components

**Integra** — The orchestrator. Technical spine. Governance-not-guardrails. Bilateral integration. Routes queries, enforces permission cascades, manages memory corpus.

**Aletheia** — The intelligence interface. What users interact with. Truth-seeking, dignity-first steward guide. Appears in financial (WayPoint), education (Crown's Eye), and personal contexts.

**Manus** — Future wearable/token layer. Smart glasses, tokenized access, council-in-your-ear. Phase 2-3 for build, Phase 1 for narrative.

### Product Lines

| Product | Tier | Audience |
|---------|------|----------|
| WayPoint Core | Everyday | Individuals/households building financial stability |
| WayPoint Renaissance | Re-entry | People excluded from traditional banking |
| WayPoint Edge | Vertical-specific | Industries in permanent penalty boxes |
| WayPoint Crown | UHNW/Family Office | Multi-generational governance, entity mapping, Trust Index |
| Crown's Eye | Education | K-12 adaptive learning platform aligned to state standards |

## Current Priority: Phase 1 — Integra Core Services

### Technology Stack

- Python 3.11+
- FastAPI
- Pydantic v2
- PostgreSQL 16 (running on Synology DS925+ NAS)
- Optional: Redis for session caching

### Database Connection

```
Host: [NAS_LOCAL_IP — set in .env file]
Port: 5432
Database: meridia_core
User: meridia
Password: [set in .env file]
```

The `meridia_edu` database contains 17 tables, 2 views, and 6,030 Georgia K-12 education standards already loaded.

### FastAPI Endpoints to Build

```
GET  /api/v1/position          — Financial position grid
GET  /api/v1/trust-index       — Trust Index (four dimensions)
GET  /api/v1/entities          — Entity listing with status
GET  /api/v1/entities/{id}     — Entity detail
GET  /api/v1/signals           — Signal feed (alerts, notifications)
GET  /api/v1/governance/alerts — Governance alerts requiring approval
POST /api/v1/governance/approve — Approval endpoint
POST /api/v1/scenario          — Scenario modeling
GET  /api/v1/reports/{audience} — Differentiated report generation
```

### Report Generator

The `/api/v1/reports/{audience}` endpoint produces different outputs from the same underlying data:

- `board` — Strategic summary, risk indicators, recommendations
- `technical` — Data lineage, calculation methodology, API health
- `regulator` — Compliance status, audit trail, policy adherence
- `family` — Plain-language position, action items, Aletheia guidance

### Project Structure

```
integra-core/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/v1/
│   │   ├── position.py
│   │   ├── trust_index.py
│   │   ├── entities.py
│   │   ├── signals.py
│   │   ├── governance.py
│   │   ├── scenario.py
│   │   └── reports.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── mock_data.py
│   │   ├── calculations.py
│   │   └── report_gen.py
│   └── db/
│       ├── session.py
│       └── models.py
├── .env
├── requirements.txt
└── main.py
```

### Mock Data

Use Faker with seed=42 for demo consistency. Generate realistic financial data including multiple entity types (LLC, Trust, Foundation, SPV), varied positions, Trust Index scores across four dimensions (Structural, Behavioral, Temporal, Relational), signal events with severity levels, and governance alerts pending approval.

## Existing Prototype

`Index8.html` is the working frontend (WayPoint Crown FPS console with Aletheia panel). The backend must serve JSON that this frontend consumes. Match Pydantic schemas to what the frontend expects.

## Coding Standards

- Type hints on all function signatures
- Pydantic v2 models for all request/response schemas
- Docstrings on all public functions
- async endpoints where appropriate
- Environment variables for configuration (never hardcode secrets)
- Files: snake_case / Classes: PascalCase / Routes: kebab-case URLs
- Structured error responses with appropriate HTTP status codes

## Guiding Principles

1. Governance over guardrails — route through review, don't block
2. Dignity over charity — sophistication, not condescension
3. Transparency over opacity — every score explained
4. Stewardship over extraction — multi-generational wellbeing
5. Human oversight always — AI proposes, humans approve

## Guardrail Protocol

When hitting constraints: state it, explain why, propose 2-3 paths forward, request direction. Never halt. Always propose forward momentum.

## Deprecated Terms

- "Aegis" → Use "Meridia"
- "Sentiarch" → Subsumed into Meridia architecture
