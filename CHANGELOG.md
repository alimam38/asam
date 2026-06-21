# Changelog

## 2026-06-20

- Plumbline: live Phase-0 President's View prototype (`src/plumbline/prototypes/2026-06-20-president-view-live.html`) — pulls Admissions funnel, Academics census (YoY + program mix), and Talbot Hall housing occupancy/auxiliary revenue live from Populi API2 via the MCP connector; Financials/Scholarships/Strategy shown as defined-but-pending. Also published as a Cowork artifact. Aggregates only, no student PII.
- Plumbline: verified additional API2 routes (campuslife/rooms, campuslife/students, applications lifecycle) appended to `specs/plumbline/populi-api2-findings.md`.
- docs/plumbline/2026-06-20-phase0-president-view.md — build note + gate progress.
- Plumbline: live Financials panel in the President's View — cash, A/R, working capital and current ratio pulled live from QuickBooks Online (Turner Theological Seminary, Inc); R-14 composite (1.67→0.63) and CFI (1.39→−5.42) shown as an annual trend from audited financials.
- Plumbline: QBO chart-of-accounts → KPI mapping and reconciliation findings in docs/plumbline/2026-06-20-qbo-financials-mapping.md — flags A/R aging not reconciling to GL, a ~93% naive tuition discount needing validation, no budget-vs-actuals via the connector, and a housing GL crosswalk (Populi 40005-01 vs QBO 41064-01).

## 2026-06-11

- Repository created: scaffold, gates, and initial artifact migration from Dropbox, Desktop, Downloads, Documents, and the local meridia working folder.
- Turner client engagement work products migrated to docs/clients/turner (86 files); institutional records intentionally left in Dropbox.
- Plumbline added as lead sub-system; specs/plumbline/spec-v1.md drafted from the Turner dashboard planning deck.
- Plumbline spec-v2 (full build): five domain modules (Admissions, Academics, Financials, Scholarships, Strategy/Evidence), Populi + QBO API ingestion, hosted SaaS end state; v1 retained as Turner planning baseline.
