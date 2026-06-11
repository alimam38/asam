# WayPoint Demo Sprint Plan

**Objective:** Connect Index8.html frontend to a live FastAPI backend producing differentiated reports from real data.

**Success criteria:** Walk into any room, open the app, interact with live data, generate reports for different audiences from the same source.

**Duration:** 4 weeks (March 2026)
**Architect:** Aliman Neal
**Build environment:** Claude Code + NAS PostgreSQL

---

## Pre-Sprint (This Weekend — March 1-2)

- [ ] File Meridia Holdings LLC — Georgia Secretary of State online portal ($100)
- [ ] Apply for EIN — IRS online (instant, same session)
- [ ] Sign operating agreement — fill in effective date and initial capital contribution
- [ ] Open business bank account — Relay or Mercury
- [ ] Connect Google Drive in Claude settings
- [ ] Place CLAUDE.md in project directory
- [ ] Set up Claude Code for integra-core development

---

## Week 1: Foundation (March 3-9)

**Goal:** FastAPI skeleton running, mock data layer producing realistic output, first endpoint returning data.

### Day 1-2: Project Scaffold
- [ ] Initialize `integra-core/` with FastAPI project structure
- [ ] Create Pydantic models for all data structures:
  - `FinancialPosition` (assets, liabilities, net worth, cash flow)
  - `TrustIndex` (four dimensions: financial health, governance, compliance, stewardship)
  - `Entity` (name, type, status, linked accounts, jurisdiction)
  - `Signal` (type, severity, message, timestamp, requires_action)
  - `GovernanceAlert` (type, entity, action_required, locked_until_approved)
  - `ScenarioInput` / `ScenarioResult`
  - `Report` (audience, sections, generated_at)

### Day 3-4: Mock Data Engine
- [ ] Build `mock_data.py` with seeded random generation
  - Consistent seed for demo reproducibility
  - 3 entity profiles: church, seminary, household
  - 12 months of financial history per entity
  - Realistic Georgia nonprofit financials (based on Turner actuals)
- [ ] Verify mock data produces varied, believable output

### Day 5: First Endpoints Live
- [ ] `/api/v1/position` — returns financial position grid
- [ ] `/api/v1/trust-index` — returns Trust Index with four dimensions
- [ ] `/api/v1/entities` — returns entity listing
- [ ] `/api/v1/entities/{id}` — returns entity detail
- [ ] Run locally, confirm JSON responses in browser

### Week 1 Checkpoint
**Test:** Hit each endpoint in browser, get clean JSON. Mock data looks real. No static values — everything generated from the data layer.

---

## Week 2: Intelligence Layer (March 10-16)

**Goal:** Signal feed, governance alerts, scenario engine, and the report generator working.

### Day 1-2: Signals & Governance
- [ ] `/api/v1/signals` — signal feed (alerts, notifications, insights)
  - Cash flow warnings
  - Compliance deadlines
  - Budget variance alerts
  - Entity status changes
- [ ] `/api/v1/governance/alerts` — items requiring human approval
- [ ] `/api/v1/governance/approve` — POST to approve/reject with audit trail

### Day 3-4: Scenario Engine
- [ ] `/api/v1/scenario` — POST endpoint
  - Accepts slider values (revenue change %, expense change %, new entity, policy change)
  - Returns projected position, trust index delta, risk assessment
  - Shows before/after comparison

### Day 5: Report Generator (Core Deliverable)
- [ ] `/api/v1/reports/{audience}` — the differentiation engine
  - `board` — Strategic summary: net position trend, risk indicators, 3 recommendations, plain-language narrative
  - `technical` — Data lineage: calculation methodology, data freshness, API health metrics, processing log
  - `regulator` — Compliance pack: policy adherence checklist, audit trail, governance decision log, exception report
  - `family` — Plain-language guide: "here's where you stand," action items, next steps, Aletheia-style guidance
- [ ] Same underlying data, four completely different outputs
- [ ] Each report includes `generated_at`, `data_source`, `confidence_score`

### Week 2 Checkpoint
**Test:** POST a scenario, see projected changes. Request reports for all four audiences from same entity — verify they contain the same data presented completely differently. This is the slide Keith and Andre need to see.

---

## Week 3: Frontend Integration (March 17-23)

**Goal:** Index8.html calls real endpoints. No more static values.

### Day 1-2: API Connection Layer
- [ ] Add fetch calls to Index8.html replacing all static data
  - Financial position grid pulls from `/api/v1/position`
  - Trust Index pulls from `/api/v1/trust-index`
  - Entity list pulls from `/api/v1/entities`
  - Signal feed pulls from `/api/v1/signals`
- [ ] Loading states for each panel
- [ ] Error handling (graceful degradation if backend unreachable)

### Day 3: Scenario Integration
- [ ] Wire scenario sliders to POST `/api/v1/scenario`
- [ ] Display projected results in real-time as sliders move
- [ ] Before/after visual comparison in the UI

### Day 4: Report Generation UI
- [ ] "Generate Report" button in Aletheia panel
- [ ] Audience selector (Board / Technical / Compliance / Family)
- [ ] Report renders in a styled panel or downloads as formatted output
- [ ] Demonstrate: click Board, see strategic summary. Click Family, see plain-language guidance. Same data.

### Day 5: Aletheia Panel Live
- [ ] Aletheia responds to entity interactions with contextual insights
- [ ] "What should I know about this entity?" → pulls signals, position, governance status
- [ ] Guided tour works with live data instead of scripted responses

### Week 3 Checkpoint
**Test:** Full walkthrough. Open Index8 → see live financial position → click entity → see detail → adjust scenario sliders → see projected impact → generate board report → generate family report → see difference. All from one data source. All live.

---

## Week 4: Polish & Demo Prep (March 24-30)

**Goal:** Demo-ready. No rough edges. Ready for Keith, Andre, and Pinnacle.

### Day 1-2: Edge Cases & Polish
- [ ] Handle empty states (no signals, no alerts, new entity with no history)
- [ ] Responsive behavior (works on laptop screen during live demo)
- [ ] Loading performance (under 2 seconds for any view)
- [ ] Consistent data across all views (no contradictions between panels)

### Day 3: Demo Script
- [ ] Write 5-minute walkthrough script
  - 60 seconds: Arrive at WayPoint, see financial position at a glance
  - 60 seconds: Drill into entity, see governance status and signals
  - 60 seconds: Run scenario — "what if enrollment drops 15%?"
  - 60 seconds: Generate reports — show board vs. family output from same data
  - 60 seconds: Aletheia interaction — contextual intelligence, not chatbot
- [ ] Practice twice. Time it. Cut anything over 5 minutes.

### Day 4: Deployment
- [ ] Backend running on NAS (accessible on local network)
- [ ] Frontend served from NAS or local machine
- [ ] Confirm demo works without internet dependency
- [ ] Backup: static fallback if backend connection fails during live demo

### Day 5: Documentation
- [ ] Update one-pager with "live demo available" language
- [ ] Screenshot deck: 5 key screens for email attachments
- [ ] Prep Pinnacle application draft (entity filed, demo working, pitch ready)

### Week 4 Checkpoint
**Test:** Hand laptop to someone who has never seen WayPoint. Can they understand what they're looking at in 30 seconds? Can you walk them through the full demo in 5 minutes without apologizing for anything?

---

## Post-Sprint: Ready State

After 4 weeks, you have:

1. **Filed entity** — Meridia Holdings LLC with EIN and bank account
2. **Working product** — Frontend connected to live backend with real data flow
3. **Differentiated reports** — Same data, four governed outputs (the Andre requirement)
4. **Live demo** — 5-minute walkthrough proving the system breathes (the Keith requirement)
5. **Pitch materials** — One-pager, pitch deck, demo screenshots
6. **Application readiness** — Everything Pinnacle needs to see

---

## Technical Stack

| Component | Tool | Status |
|-----------|------|--------|
| Backend | FastAPI + Python 3.11 | To build |
| Data models | Pydantic v2 | To build |
| Database | PostgreSQL 16 on NAS | Running |
| Frontend | Index8.html | Complete |
| Development | Claude Code | Ready |
| Hosting | Synology NAS | Online |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Tax season time crunch | Week 1-2 are backend-only (can build in evening sessions). Week 3-4 need focused blocks. |
| NAS connectivity issues | Backend also runs on laptop locally. No hard dependency on NAS for demo. |
| Scope creep | Every feature not on this list waits. No education platform, no Crown tier, no Manus layer until this sprint is done. |
| Perfectionism | Demo-ready means it works and looks intentional. It does not mean production-ready. Ship the sprint, iterate after. |

---

*This plan gets you from "beautiful prototype" to "working product" in 4 weeks.*
*Everything else is roadmap. This is the road.*
