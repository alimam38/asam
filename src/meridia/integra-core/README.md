# Integra Core — WayPoint Financial Intelligence API

**Meridia Holdings LLC**

The backend that makes the prototype breathe.

## Quick Start

```bash
cd integra-core
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000/docs` for interactive API documentation.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/position` | Financial position grid (23 line items) |
| GET | `/api/v1/trust-index` | Trust Index — 4 dimensions, composite score |
| GET | `/api/v1/entities` | All tracked entities |
| GET | `/api/v1/entities/{id}` | Entity detail with monthly activity |
| GET | `/api/v1/signals` | Signal feed (filterable by severity, category, action_required) |
| GET | `/api/v1/governance/alerts` | Governance alerts requiring attention |
| POST | `/api/v1/governance/approve` | Process approval, denial, or escalation |
| POST | `/api/v1/scenario` | Run financial scenario projection |
| GET | `/api/v1/reports/{audience}` | Generate report — `board`, `technical`, `regulator`, or `family` |

## Report Audiences

Same data, four outputs:

- **board** — Strategic summary, risk indicators, recommendations
- **technical** — Data lineage, calculation methodology, system status
- **regulator** — Compliance status, audit trail, policy adherence
- **family** — Plain-language position, action items, guided next steps

## Scenario Engine

POST to `/api/v1/scenario` with:

```json
{
  "name": "Enrollment drops 15%",
  "enrollment_change_pct": -15,
  "revenue_change_pct": 0,
  "expense_change_pct": 0,
  "grant_amount": 0,
  "new_program_cost": 0
}
```

Returns projected revenue, expenses, cash position, trust score, risk flags, and opportunities.

## Demo Institution

**Greater Hope AME Church** — fictional institution with realistic financial patterns:
- $3.5M total assets, $2.96M net assets
- $753K revenue, $762K expenses (seasonal deficit)
- 5 entities (general fund, foundation, building fund, scholarship, discretionary)
- Trust Index: 75.5/100 (B grade)

## Stack

- Python 3.11+
- FastAPI
- Pydantic v2
- uvicorn

## Next Steps

1. Wire Index8.html frontend to these endpoints
2. Deploy to Meridia NAS alongside PostgreSQL
3. Replace mock data with real QuickBooks integration
