# Plumbline — Specification v2 (Full Build)

Date: 2026-06-11. Supersedes spec-v1 in scope; v1 remains as the record of the Turner planning baseline. v2 is the product Plumbline is actually building toward. Context that drove the expansion: Populi does not build dashboards for its customers — that gap is the product. The system is not destined for a NAS; it is a hosted product. The President's view must be available at any time, from any device, and must span Admissions, Academics, Financials, and Scholarships — not a handful of enrollment tiles.

## 1. Product definition

Plumbline is a hosted executive intelligence layer for small accredited institutions running on Populi. It continuously syncs SIS and finance data into one governed model and gives the President a complete, always-current view of the institution — admissions pipeline, academic health, financial position, scholarship economics, and strategic-goal progress — with drill-down, alerts, board-ready briefs, and an accreditation evidence chain.

Positioning in one sentence: Populi runs the institution's records; Plumbline tells the President what they mean.

Proving-ground tenant: Turner Theological Seminary (Populi + QuickBooks + Gusto). Design constraint from day one: nothing Turner-specific in the core — Turner is tenant #1, not the product.

Builder's standing at the tenant: Aliman served two years as Turner's Controller and now leads Operations, Facilities, and Student Support — full Populi API and QBO access are already authorized through that role. Data governance for the pilot rests on that standing; the multi-tenant product must replace it with the tenant-onboarding authorization flow (Phase 2).

## 2. Users and roles

| Role | Example at Turner | Access |
|---|---|---|
| President | Dr. Davis | Full executive view, all domains, aggregates + drill-down to governed detail, anytime/any device |
| Cabinet / VP | Academic Dean, CFO/Business Office, Admissions Director, Advancement | Domain view(s) matching portfolio; aggregates + their domain's detail |
| Operator | Registrar, finance staff, admissions staff | Data administration: sync status, mapping, validation queues, definition table |
| Board | Trustees | Published board packet view: one-page brief + trend pack, read-only, no drill-down |
| Evidence consumer | SACSCOC liaison | Evidence packets: baseline → finding → action → follow-up → improvement, by goal and term |

All record-level access is role-gated and logged (FERPA discipline throughout).

## 3. Domain modules

### 3.1 Admissions

Funnel: inquiry → applicant → admit → deposit → enrolled, by term, program, modality, and source. KPIs: stage counts and conversion rates; yield; melt (deposit → no-show); application velocity (days inquiry→app, app→decision); pipeline vs. same point last cycle; projected entering class vs. target.

### 3.2 Academics (enrollment + student success)

Census: headcount, FTE, status mix, credit load distribution, program/modality trends, term-over-term and year-over-year. Success: retention/persistence by cohort, completion/graduation rates, time-to-degree, course outcomes (grade distribution, DFW rates, bottleneck courses), academic standing counts, advising flags (students below credit pace or GPA threshold).

### 3.3 Financials

Position: cash position and trend, AR aging (student accounts), tuition billed vs. collected, net tuition revenue and institutional discount rate, budget vs. actuals by department, payroll cost snapshot, auxiliary/other revenue. Health: composite financial index (CFI) and its four ratios — already computed manually for Turner (R-14 work) — produced continuously instead of annually. Sources: Populi financial module (student accounts, billing) + QuickBooks Online (GL, budget vs. actuals) + payroll summary (Gusto export or API).

### 3.4 Scholarships / financial aid

Aid awarded vs. aid budget by term and fund; scholarship utilization by fund (awarded vs. available, donor-funded vs. institutional); average award and net price by program; discount rate contribution; disbursement status; stacking and over-award flags; donor-fund reporting view (what each fund supported — feeds Advancement conversations).

Scope ruling (2026-06-11): Turner's aid is institutional scholarships only — no DOE/Title IV participation. FAFSA/ISIR intake, R2T4, and SAP compliance machinery are out of scope for the pilot and remain a Phase 2+ product question for Title IV tenants.

### 3.5 Strategic goals and accreditation (carried from v1)

Survey-score-by-goal, response rates, trends, targets and status; findings and actions linked to goals; evidence packets preserved per period with full source traceability. This module is what makes the dashboard SACSCOC evidence rather than just a screen.

## 4. Cross-cutting capabilities

- One-page Executive Brief: auto-generated, exportable PDF, the "walk into the board meeting" artifact.
- Alerts: threshold rules per KPI (e.g., cash days < X, melt > Y%, retention cohort drops) delivered in-app and by email.
- Period intelligence: any KPI comparable to prior term, same term last year, and target.
- Annotations: leadership can pin a narrative note to any KPI/period (the "why" travels with the number).
- Drill-down: every aggregate traces to governed detail, permission-gated, and every number traces to a sync run and source record.
- Definitions registry: official definitions (active, enrolled, retained, withdrawn, graduated, FTE divisor, cohort rules) live in one versioned table; every KPI cites the definition version it was computed under.

## 5. Architecture

**End state: multi-tenant SaaS.** Pilot: single-tenant cloud instance for Turner. The Synology NAS is a development/staging environment only — it is explicitly not the product's home.

- **Ingestion:** three first-class API sources, all authorized and verified live (2026-06-11) — **Populi API2 only** (bearer auth against turnerseminary.populiweb.com; Populi has deprecated the legacy XML API, so API2 is the sole integration path — verified route inventory in `populi-api2-findings.md`), QuickBooks Online API (GL, budget vs. actuals), and Gusto API (payroll cost, comp categories incl. housing allowance). Scheduled sync: nightly full reconciliation + intraday incremental, plus on-demand refresh. CSV/XLS import lane remains for API-less sources (survey exports) and as fallback. **PII rule from probe findings: Populi's people object exposes SSN/alien-registration/social-insurance fields — Plumbline never requests, syncs, or stores them.**
- **Storage:** PostgreSQL. Raw landing tables (immutable, per sync run) → conformed model → KPI snapshot marts. Snapshots immutable; recomputation = new run.
- **Backend:** Python/FastAPI (consistent with integra-core patterns in src/meridia), background workers for sync and KPI computation.
- **Frontend:** responsive web app (works on the President's phone/tablet without a native app); PDF export service for briefs and packets.
- **Deployment:** containerized (Docker), single cloud VM or container platform for pilot; tenancy isolation by schema per tenant when multi-tenant.
- **Security:** SSO-capable auth with MFA, role-based authorization, TLS everywhere, encryption at rest, per-tenant isolation, full audit log of access to student-level data, API credentials in a secrets store (never in the repo).

## 6. Data model (conformed core, PostgreSQL)

Tenancy: `tenant`, `app_user`, `role_grant`, `audit_log`.
People/academic: `person`, `student`, `program`, `term`, `cohort` (versioned rules + membership), `application` + `application_event` (funnel transitions with timestamps), `enrollment` (student × term × program: status, credits), `course`, `section`, `grade_record`.
Financial: `gl_account_map`, `ledger_snapshot`, `budget_line`, `student_account_txn`, `ar_aging_snapshot`, `payroll_snapshot`, `cfi_ratio_snapshot`.
Aid: `fund` (donor/institutional, restrictions), `award` (student × fund × term: offered/accepted/disbursed amounts), `aid_budget`.
Strategy/evidence: `strategic_goal`, `survey`, `survey_question`, `goal_mapping`, `survey_response_agg`, `finding`, `action`, `evidence_packet`.
Pipeline: `sync_run` (source, scope, hashes, row deltas, validation results), `kpi_definition` (versioned), `kpi_snapshot` (kpi × period × slice × value × definition-version × sync_run).

## 7. KPI catalog (v2 initial set)

| Domain | KPIs |
|---|---|
| Admissions | inquiries, applicants, admits, deposits, enrolled; conversion per stage; yield; melt; days-to-decision; pipeline vs. last cycle; projected class vs. target |
| Academics | headcount; FTE; status mix; credit load; retention/persistence; graduation/completion; time-to-degree; DFW rate; bottleneck courses; standing/advising flags |
| Financials | cash position + days cash; AR aging buckets; billed vs. collected; net tuition revenue; discount rate; budget vs. actuals variance; payroll cost; CFI + four ratios |
| Scholarships | aid awarded vs. budget; utilization by fund; average award; net price by program; disbursement status; over-award flags |
| Strategy | avg survey score by goal; response rate; goal status vs. target; open findings; overdue follow-ups |

Each KPI ships with: formula, source mapping, definition-version reference, owner, refresh cadence, and target/threshold slots. Definitions pending institutional sign-off compute under stated defaults and are visibly flagged until confirmed.

## 8. Phasing (mapped to GATES.md)

- **Phase 0 — Pilot core (drives Gate 2):** Populi API sync + QBO read-only sync; Academics + Admissions + Financial-position KPIs; President's view + Executive Brief PDF; definitions registry; runs end-to-end in the dev Docker environment.
- **Phase 1 — Full domains (drives Gates 3–4):** Scholarships module, CFI engine, strategy/evidence module, alerts, annotations, board view; automated tests on every KPI formula; deployed to the pilot cloud instance, reachable by Turner leadership (Gate 4's "someone other than me").
- **Phase 2 — Product (drives Gates 5–6):** multi-tenant hardening, tenant onboarding flow (Populi credentials + mapping wizard), pricing and terms; scripted demo (Gate 5); first paying institution (Gate 6).

## 9. Acceptance behavior (binary, v2)

1. The President can open Plumbline on a phone at any time and see all five domains with data no older than the last completed sync, with sync age displayed.
2. A full nightly sync from Populi and QBO completes unattended, and a failed sync alerts the Operator with a human-readable cause.
3. Every KPI value matches a hand-computed value from raw landing data for the same period (verified per KPI in the test suite).
4. Every displayed number traces to sync run + source records + definition version via the UI.
5. Funnel, retention, discount rate, and CFI each reproduce Turner's existing manually-computed figures within defined tolerance for the baseline term.
6. Role gates hold: Board and President-aggregate views expose no student-level records; access to student-level detail is logged.
7. Executive Brief exports as a one-page PDF; the evidence packet for a closed period is retrievable complete.
8. A second tenant can be provisioned without code changes (Phase 2 gate).

## 10. Open items

| # | Item | Question that closes it | Owner | Default until closed |
|---|---|---|---|---|
| 1 | Populi API access | **CLOSED 2026-06-11** — full-access API key already in hand. Key lives in the secrets store / deployment .env only, never in this repo. | Aliman | — |
| 2 | QBO access | **CLOSED 2026-06-11** — QBO access in hand; live connector verified against "Turner Theological Seminary, Inc" (NAICS 611310). Credentials follow the same secrets-store rule as Populi. | Aliman | — |
| 3 | Official definitions | active / enrolled / retained / withdrawn / graduated / FTE divisor. **Cohort rules CLOSED 2026-06-11:** cohorts are keyed to entry term under Turner's standalone status — Cohort 1 = Fall 2024 entrants; pre-standalone history is outside cohort scope. | Registrar + liaison (remaining: statuses, FTE divisor) | Populi defaults; FTE divisor 12 — flagged |
| 4 | Aid data location | **CLOSED 2026-06-11** — aid is institutional scholarships only; no DOE/Title IV. Scholarships module scope set accordingly (§3.4). | Aliman | — |
| 5 | Survey tooling | Where do surveys live (Populi? Google Forms?) and can responses export with question IDs? | Turner IE | CSV import with question→goal mapping table |
| 6 | Payroll feed | **CLOSED 2026-06-11** — Gusto API; live connector verified against "Turner Theological Seminary" (Gusto Plus, non-profit, single pay schedule). Comp types include Minister Housing Allowance — the payroll model must carry it as its own category (seminary-relevant for the product, not just Turner). | Aliman | — |
| 7 | Pilot hosting | Cloud target and budget for the pilot instance? | Aliman | Single small cloud VM, Docker Compose |
| 8 | Turner-facing scope cut | **CLOSED 2026-06-11** — Turner-facing view: Admissions, Academics, Strategy/Evidence. Financials and Scholarships are not for that audience; they may be alluded to as future modules. Financials remains President-only in role design. | Aliman | — |

## 11. What changed from v1

NAS demoted to dev/staging; bi-weekly manual export demoted to fallback lane; scope expanded from 3 KPI groups to 5 domain modules (Admissions, Academics, Financials, Scholarships, Strategy/Evidence); QuickBooks and payroll brought into the model; CFI made continuous; multi-tenant SaaS named as the end state; President-anytime access made an acceptance criterion.
