# Plumbline — Specification v1

Date: 2026-06-11. Source material: `2026-06-11-turner-dashboard-populi-meeting-deck.pptx` (in this folder) and the Turner engagement artifacts under `docs/clients/turner/`. Status: draft for Gate 1; open items listed at the bottom with defaults so implementation can start.

## What Plumbline is

Plumbline is an executive institutional-effectiveness dashboard for small accredited institutions. It turns student-information-system (SIS) data into one at-a-glance executive view — enrollment, student success, and strategic-goal progress — refreshed on a bi-weekly rhythm, and preserves the finding → action → follow-up chain as accreditation evidence.

Proving-ground client: Turner Theological Seminary. SIS: Populi. Accreditor: SACSCOC.

## Users

| Role | Who (at Turner) | What they do in Plumbline |
|---|---|---|
| Executive | President / leadership | View dashboard: KPI tiles, trends, goal scores; drill down; record decisions |
| Operator | IE / registrar staff | Run the bi-weekly refresh: export Populi saved reports, load into Plumbline, validate numbers |
| Evidence consumer | SACSCOC liaison / accreditor | Retrieve the evidence packet: baseline, finding, action, follow-up, improvement |

## Architecture decision

Hybrid, per the planning deck's framing: **Populi is the source data engine; Plumbline is the dashboard home.**

- Phase 1: a standard set of saved Populi reports (Data Slicer + Analytics presets) exported as XLS/CSV on a bi-weekly cadence, loaded into Plumbline.
- Phase 2: Populi API/webhook automation, only if the saved-report routine proves insufficient.

Runtime: Docker on the Synology NAS, PostgreSQL for storage, web UI reachable on the local network (Gate 4 extends reach beyond it). This matches the Gate 2 environment in GATES.md.

## Core workflow (bi-weekly cycle)

1. Operator runs the saved report set in Populi and exports each as XLS/CSV.
2. Operator drops the exports into the Plumbline ingest folder (or uploads via the UI).
3. Plumbline validates each file against its ingestion contract (expected columns, row counts vs. prior run, definition checks) and reports anomalies before loading.
4. Plumbline computes the KPI snapshot for the period and refreshes the dashboard.
5. Executive reviews the dashboard; findings and decided actions are recorded against strategic goals.
6. Plumbline archives the period's evidence packet: source exports, KPI snapshot, findings, actions, follow-ups.

## Dashboard requirements

- Filters: term, program, modality.
- KPI tiles with target and status (on/off track) where targets are defined.
- Trend charts: term series for each KPI.
- Drill-down from any tile to the underlying records (permission-gated).
- Strategic-goal panel: average survey score by goal, response rate, trend, linked evidence.
- One-page executive summary view, exportable as PDF for board/accreditation use.

## KPI set (v1)

| KPI | Formula | Source report | Definition status |
|---|---|---|---|
| Headcount | count of active enrolled students in term | enrollment export | Pending official definition of "active" |
| FTE | per institution's credit-hour divisor | enrollment export | Not yet defined — what is Turner's FTE divisor? |
| Funnel: applicants → admits → enrolled | stage counts per term | admissions export | Defined by funnel stage field |
| Yield / conversion | enrolled ÷ admits; admits ÷ applicants | admissions export | Defined |
| Enrollment status mix | counts by status | enrollment export | Pending source-of-truth status definitions |
| Retention / persistence | cohort enrolled at t+1 ÷ cohort at t | cohort export | Not yet defined — cohort construction rules in Populi |
| Graduation / completion | completers ÷ cohort | cohort export | Not yet defined — same |
| Credits / GPA / course bottlenecks | per course outcomes where available | academic export | Phase 1 optional |
| Avg survey score by goal | mean of mapped question scores | survey export | Pending survey-question → goal mapping |
| Survey response rate | responses ÷ invited | survey export | Defined |

## Data model (PostgreSQL)

Core entities: `student` (SIS id, demographics, status), `term`, `program`, `enrollment` (student × term × program, status, credits), `cohort` (definition + membership), `application` (funnel stage per term), `survey`, `survey_question`, `goal_mapping` (question → strategic goal), `strategic_goal` (target, owner), `kpi_snapshot` (kpi × term × filter-slice × value, computed per refresh), `finding`, `action` (finding-linked, with follow-up date and status), `ingest_run` (file, hash, row counts, validation results — the audit trail).

Identity: students keyed by Populi person ID. Snapshots are immutable; recomputation creates a new `ingest_run`.

## Governance and permissions

- Executive role sees aggregates only; record-level drill-down restricted to Operator.
- Source-of-truth definitions for active, enrolled, retained, withdrawn, graduated live in one reference table in the repo (`specs/plumbline/definitions.md`, to be created) and in the app — Populi field mappings point at them.
- Every number on the dashboard must be traceable to an `ingest_run` and source file.

## Evidence requirements (SACSCOC)

Each period's packet preserves: baseline, finding, action, follow-up, improvement. Packets are retrievable by term and goal. Storage: Plumbline database + exported packet archived under the Turner engagement folder.

## Acceptance behavior (binary)

1. Operator can complete a full bi-weekly refresh from Populi exports to updated dashboard in under 30 minutes without developer help.
2. Every KPI tile matches a hand-computed value from the same source exports.
3. Validation rejects a malformed or stale export with a human-readable reason.
4. Executive summary exports to a one-page PDF.
5. A finding can be recorded, linked to a goal, given an action and follow-up date, and retrieved in the evidence packet.
6. Executive role cannot reach student-record detail.

## Open items

| # | Item | Question that closes it | Owner | Default until closed |
|---|---|---|---|---|
| 1 | Populi meeting outcomes | What did the SACSCOC liaison recommend (dashboard home, report set, definitions)? | Aliman | Hybrid architecture as specified |
| 2 | Official status definitions | Definitions of active, enrolled, retained, withdrawn, graduated? | Turner registrar + liaison | Populi default statuses |
| 3 | FTE divisor | What credit-hour divisor does Turner use for FTE? | Turner registrar | 12 (typical graduate FT load) — flag on dashboard until confirmed |
| 4 | Cohort rules | How are cohorts and retention windows structured in Populi? | Liaison | Fall-entry annual cohorts |
| 5 | Survey → goal mapping | Which survey questions map to which strategic goals? | Aliman + Turner IE | Unmapped questions excluded from goal scores |
| 6 | Saved report set | Exact Populi saved reports, fields, tags, filters | Aliman (post-meeting) | Ingestion contract columns named in code as placeholders |
