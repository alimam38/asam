# Populi API2 — Verified Findings (Turner tenant)

Probed 2026-06-11 against `turnerseminary.populiweb.com` with the production token (read-only; structures and counts recorded, values never). Probe scripts: `src/plumbline/probe/`.

## Verdict

- The **legacy XML API is deprecated by Populi** — every legacy task returns a deprecation error. API2 (`/api2/`, bearer token) is the only integration path. The spec is API2-only.
- Bearer auth with the production token works.

## Verified routes

| Route | HTTP | Records | KPI-relevant fields observed |
|---|---|---|---|
| `academicterms` | 200 | 14 terms | id, academic_year_id, name, start/end dates, grades_date, add/drop, enrollment window |
| `academicyears` | 200 | 4 years | start_year, end_year, num_academic_terms — consistent with the standalone era (Cohort 1 = Fall 2024) |
| `programs` | 200 | 8 | id, name, units, graduate_level |
| `degrees` | 200 | 17 | id, program_id, department_id, name, abbrv, status, cip_code, degree_level_id |
| `departments` | 200 | 18 | id, name, status |
| `campuses` | 200 | 2 | id, name, city/state, primary, timezone |
| `inquiries` | 200 | 125 | person_id, lead_id, program/degree/term ids, status, closed_at, lead_source_id |
| `leads` | 200 | 659 | person_id, status, active, program/degree/term ids, lead_source_id, declined_reason, counselor_id |
| `applications` | 200 | 200 | person_id, lead_id, template_id, program/degree/term/campus ids, started_on, submitted_at, pending_decision_on, lead_source_id |
| `applicationtemplates` | 200 | 14 | id, name, type, published, fee |
| `people` | 200 | 672 | id, names, status, demographics — **also exposes social_security_number, alien_registration_number, social_insurance_number** |
| `enrollments` | 200 | 2,282 | person-shaped payload at top level; enrollment detail shape to confirm at build |
| `tags` | 200 | 27 | id, name |

The full admissions funnel — inquiry → lead → application → enrollment — is reachable end-to-end, which is everything the Admissions and Academics modules need.

## Routes that are NOT these names (404 invalid_route)

`terms`, `persons`, `students`, `courses`, `admissions/applications`, `admissions/leads`, `customfields`, `customfields/person`, `aid/awards`, `financialaid/awards`.

## Parameterized routes (exist, need arguments)

`courseofferings` and `events` return `missing_parameter` (likely require `academic_term_id`) — to probe at build time.

## Standing rules adopted from these findings

1. **PII field exclusion at sync:** `social_security_number`, `alien_registration_number`, `social_insurance_number` are never requested, synced, or stored by Plumbline. The conformed model carries Populi person_id as the identity key.
2. Financial-aid route names remain undiscovered — Scholarships module route discovery is a build-time task (Turner's aid is institutional-only, so the funds ledger may live partly outside Populi anyway).

## Open probe items

- Enrollment record shape (status/credits per term) — confirm whether `enrollments` expands per-term detail or requires parameters.
- `courseofferings` with `academic_term_id` (course outcomes / DFW KPIs).
- Custom fields route name (taxonomies for survey/goal tagging).
- Aid/awards route name.
