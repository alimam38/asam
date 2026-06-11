# Meridia WayPoint — Demo Sprint Plan
## From Prototype to Working Product

**Goal:** Wire Index8.html to a live FastAPI backend so the demo breathes real data.  
**Timeline:** 4 weeks (evenings + weekends alongside Intuit/Turner)  
**Success criteria:** Walk into any room, open the app, and it responds with live governed outputs.

---

## Week 1: Foundation
**Theme: Stand it up**

### Day 1–2: Entity & Environment
- [ ] File Meridia Holdings LLC (Georgia Secretary of State — $100, online, same-day)
- [ ] Apply for EIN (IRS online — instant)
- [ ] Sign operating agreement (fill in date + initial contribution)
- [ ] Open business bank account (Relay or Mercury)
- [ ] Install Claude Code (`npm install -g @anthropic-ai/claude-code`)
- [ ] Place CLAUDE.md in project root
- [ ] Initialize `integra-core/` repo with git

### Day 3–4: FastAPI Skeleton
- [ ] Create project structure:
  ```
  integra-core/
  ├── app/
  │   ├── main.py          # FastAPI app + CORS
  │   ├── models.py         # Pydantic schemas
  │   ├── mock_data.py      # Seeded realistic data
  │   ├── routers/
  │   │   ├── position.py   # /api/v1/position
  │   │   ├── entities.py   # /api/v1/entities
  │   │   ├── signals.py    # /api/v1/signals
  │   │   ├── governance.py # /api/v1/governance/*
  │   │   ├── scenario.py   # /api/v1/scenario
  │   │   └── reports.py    # /api/v1/reports/{audience}
  │   └── services/
  │       ├── trust_index.py
  │       ├── report_generator.py
  │       └── scenario_engine.py
  ├── requirements.txt
  └── README.md
  ```
- [ ] Define all Pydantic models (Position, Entity, Signal, TrustIndex, Report)
- [ ] Implement `/api/v1/position` with mock data returning financial grid
- [ ] Implement `/api/v1/entities` and `/api/v1/entities/{id}`
- [ ] Run locally, confirm JSON responses at `localhost:8000/docs`

### Day 5: Mock Data Layer
- [ ] Build `mock_data.py` with seeded, realistic data (not random)
- [ ] Create demo persona: "Greater Hope AME Church" as pilot institution
- [ ] Include 12 months of financial position data
- [ ] Include 5 entities (church, foundation, building fund, scholarship, pastor's discretionary)
- [ ] Include 8–10 governance signals (mix of alerts, approvals, notifications)

**Week 1 checkpoint:** FastAPI running locally, returning structured JSON for position, entities, and signals.

---

## Week 2: Intelligence Layer
**Theme: Make it think**

### Day 1–2: Trust Index & Governance
- [ ] Implement Trust Index calculation (four dimensions):
  - Financial Health (liquidity, solvency, cash flow)
  - Governance Compliance (filing status, audit currency, policy adherence)
  - Operational Efficiency (expense ratios, revenue diversification)
  - Mission Alignment (program spending %, scholarship deployment)
- [ ] Implement `/api/v1/trust-index` endpoint
- [ ] Implement `/api/v1/governance/alerts` — returns pending items
- [ ] Implement `/api/v1/governance/approve` — POST to approve/deny

### Day 3–4: Report Generator
- [ ] Build report generation service
- [ ] Implement `/api/v1/reports/{audience}` with four output modes:
  - `board` — strategic summary, 3 key risks, 3 recommendations, trust score
  - `technical` — data sources, calculation methodology, API health status
  - `regulator` — compliance checklist, audit trail, policy status
  - `family` — plain-language summary, 3 action items, Aletheia guidance note
- [ ] Each report returns structured JSON (title, sections, metadata)
- [ ] Test: same underlying data, four distinct outputs

### Day 5: Scenario Engine
- [ ] Implement `/api/v1/scenario` POST endpoint
- [ ] Accept scenario parameters (revenue change %, expense adjustment, new entity, grant received)
- [ ] Return projected position, updated trust index, risk flags
- [ ] Support 3 pre-built scenarios for demo:
  - "What if enrollment drops 15%?"
  - "What if we receive a $200K grant?"
  - "What if we add a community outreach program?"

**Week 2 checkpoint:** All endpoints live. Report generator producing four differentiated outputs from same data. Scenario engine returning projections.

---

## Week 3: Frontend Integration
**Theme: Wire it up**

### Day 1–2: Connect Index8 to API
- [ ] Copy Index8.html to working version (Index9.html or similar)
- [ ] Replace all static financial position values with `fetch('/api/v1/position')`
- [ ] Replace entity list with `fetch('/api/v1/entities')`
- [ ] Replace signal feed with `fetch('/api/v1/signals')`
- [ ] Wire Trust Index display to `/api/v1/trust-index`
- [ ] Add loading states for each panel

### Day 3: Aletheia Panel Integration
- [ ] Wire Aletheia panel to pull governance alerts
- [ ] Add report generation buttons (Board | Operations | Compliance | Family)
- [ ] Each button calls `/api/v1/reports/{audience}` and renders in panel
- [ ] Style report output within existing Aletheia aesthetic

### Day 4: Scenario Sliders
- [ ] Wire scenario sliders to POST to `/api/v1/scenario`
- [ ] Show projected changes inline (before/after position grid)
- [ ] Highlight risk flags from scenario response
- [ ] Pre-load three demo scenarios as quick-select buttons

### Day 5: Polish & Error Handling
- [ ] Add error states (API unavailable, timeout)
- [ ] Add graceful fallback for offline mode
- [ ] Ensure CORS headers configured for local development
- [ ] Test full flow: load → data populates → interact → reports generate → scenarios calculate

**Week 3 checkpoint:** Index8 frontend fully wired. No static values. Every panel pulls from API. Reports generate on click. Scenarios calculate in real time.

---

## Week 4: Demo Ready
**Theme: Dress it for the room**

### Day 1–2: Demo Script & Data Tuning
- [ ] Write 5-minute demo script (problem → solution → live walkthrough → ask)
- [ ] Tune mock data for narrative coherence:
  - Greater Hope AME shows real financial patterns (seasonal giving, fixed costs, restricted funds)
  - Trust Index tells a story (high mission alignment, moderate governance, improvement trajectory)
  - Signals include mix of urgent (insurance renewal), informational (quarterly close), celebratory (scholarship fully funded)
- [ ] Create "Andre demo" path: emphasize report differentiation
- [ ] Create "Keith demo" path: emphasize technical architecture
- [ ] Create "Pinnacle demo" path: emphasize market opportunity + founder-market fit

### Day 3: Deploy to NAS
- [ ] Containerize FastAPI app (Docker or direct on NAS)
- [ ] Deploy to Meridia NAS alongside PostgreSQL
- [ ] Configure Nginx reverse proxy for clean URLs
- [ ] Test from laptop connecting to NAS over local network
- [ ] Bonus: configure Tailscale or Cloudflare tunnel for remote demo access

### Day 4: Stress Test
- [ ] Run through full demo 3 times without interruption
- [ ] Have Keith review technical architecture (informal call)
- [ ] Test on phone browser (responsive check)
- [ ] Test on slow connection (loading states work?)
- [ ] Identify and fix any data inconsistencies

### Day 5: Package
- [ ] Final one-pager with live demo URL added
- [ ] Final pitch deck with screenshots of working product added
- [ ] Prepare Pinnacle application draft (if applications open)
- [ ] Draft intro email to Keena Pierre at gener8tor
- [ ] Backup everything: NAS snapshot, git push, local copy

**Week 4 checkpoint:** Demo-ready product. Can open browser, show live financial intelligence platform with governed outputs, differentiated reports, and scenario modeling. Pitch deck updated with real screenshots. Ready for Keith, Andre, or Pinnacle.

---

## Post-Sprint: First Revenue
**After demo is working, before next feature:**

- [ ] Run WayPoint on Turner's actual QuickBooks data (first real pilot)
- [ ] Generate Turner board report using the system
- [ ] Document before/after (manual process vs. WayPoint output)
- [ ] Identify 3 institutions in AME network for beta outreach
- [ ] Price and propose: $500/quarter or $2,000/year per institution
- [ ] First invoice = Meridia Holdings LLC has revenue

---

## Rules for the Sprint

1. **No architecture expansion.** Build what's scoped. Crown's Eye, Manus, and multi-tenant can wait.
2. **No perfectionism.** Mock data is fine. Real Plaid integration is Phase 3.
3. **No new prototypes.** Index8 is the frontend. Wire it, don't redesign it.
4. **Ship > polish.** Working demo with rough edges beats beautiful static prototype.
5. **Every session ends with a commit.** No lost work. Git push after every session.
6. **If blocked, flag it.** Use the Guardrail Protocol — state constraint, explain why, propose paths, ask for direction.

---

*Sprint starts when the LLC is filed.*  
*Sprint ends when the demo breathes.*
