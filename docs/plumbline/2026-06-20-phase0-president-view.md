# Plumbline — Phase 0 President's View (live prototype)

Date: 2026-06-20.

## What landed
A live, responsive President's-view dashboard that pulls real Turner data from Populi API2
**on open** (no baked snapshot). File: `src/plumbline/prototypes/2026-06-20-president-view-live.html`.
Also published as a Cowork artifact (`plumbline-president-view`). Successor to the
2026-06-11 exec demo, which embedded a static aggregate pull; this build is connector-driven.

## Live modules (spec-v2 §3, Phase 0)
- **Admissions funnel** — applications by lifecycle stage for the incoming term (§3.1).
- **Academics census** — term headcount with year-over-year vs. same season last year,
  plus program mix (§3.2).
- **Housing & auxiliary** — Talbot Hall occupancy and auxiliary-enterprise revenue
  (GL 40005-01); the live slice of Financials already flowing through Populi (§3.3, partial).

## Shown as defined-but-pending (honest scope)
- Financial position (QuickBooks Online + Gusto) — Phase 1.
- Scholarships / aid (fund ledger) — Phase 1.
- Strategy & accreditation (survey feed) — Phase 1.
- Executive Brief PDF export — Phase 1.

## Data layer
Populi API2 via the MCP connector at `Talbot Hall Management/populi-connector/`
(`populi_mcp.py`). Routes used: `academicterms`, `campuslife/students`, `campuslife/rooms`,
`applications`. Newly verified routes recorded in `specs/plumbline/populi-api2-findings.md`
(2026-06-20 section).

## Governance
Aggregates only — no student-level records rendered. SSN / alien-registration /
social-insurance fields are never requested, displayed, or stored (spec-v2 §5 PII rule).
"Headcount" computes under the Populi default roster definition, visibly flagged pending
Registrar sign-off (open item #3).

## Gate progress (GATES.md)
- **Gate 1 — SPEC:** spec-v2 in place; open item #1 (Populi API access) is now operationalized
  by a working, verified MCP connector plus live reads against the four KPI routes above.
- **Gate 2 — BUILD:** first live end-to-end view of real institutional data for the Populi
  half of Phase 0. This is a connector-driven prototype that proves the data and the
  President's view; it is **not yet** the Dockerized FastAPI + PostgreSQL build spec-v2 §5–6
  defines as the Gate-2 product. That backend remains the next build.

## Not done / next
- QBO + Gusto wiring for Financial position and Scholarships (Phase 1).
- Inquiry → lead top-of-funnel, term-scoped, for Admissions.
- Backend: FastAPI + PostgreSQL landing → conformed → KPI snapshot marts (spec §5–6).
