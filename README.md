# ASAM

ASAM (Hebrew: storehouse — divine provision and blessing) is the umbrella product repository for six sub-systems built by Aliman Neal:

| Sub-system | What it is |
|---|---|
| Plumbline | Executive institutional-effectiveness dashboard for small accredited institutions: enrollment, student success, and strategic-goal KPIs from SIS data (Populi at Turner), refreshed bi-weekly, with accreditation evidence. Spec: `specs/plumbline/spec-v1.md`. **Lead sub-system.** |
| Eden Crown | Not yet defined in this repo. Defining question: what does Eden Crown do, for whom, in one sentence? |
| Meridia | Financial-data intelligence work; an ingestion/wiring prototype (`integra-wiring`, Python/FastAPI) exists. Defining question: what is Meridia's deliverable product, beyond the prototype? |
| Waypoint | Not yet defined in this repo. Defining question: what does Waypoint do, for whom, in one sentence? |
| Aegis | Not yet defined in this repo. Defining question: what does Aegis do, for whom, in one sentence? |
| Recess | Not yet defined in this repo. Defining question: what does Recess do, for whom, in one sentence? |
| Kingdom Soundworks (KSW) | Not yet defined in this repo. Defining question: what does KSW do, for whom, in one sentence? |

## Current status

Nothing in this repository runs yet. The repository currently holds migrated specs, decision records, reports, and collateral from prior working sessions, plus prototype source under `src/`.

The first gate is **Gate 1 — SPEC** (see GATES.md). Plumbline is the lead sub-system: `specs/plumbline/spec-v1.md` was drafted 2026-06-11 from the Turner dashboard planning deck; the gate closes when the spec's open-items table is resolved or signed off with defaults.

## How to run it

Not yet defined. There is no runnable system at the repo root. The Meridia `integra-wiring` prototype under `src/meridia/` has its own README and requirements; it has not been verified to run from this repo.

## Repository layout

- `docs/` — decision records and reports, by sub-system
- `specs/` — requirements and schemas, by sub-system
- `src/` — code, by sub-system
- `tests/` — automated tests
- `infra/` — Docker and deployment notes (target: Synology NAS, Docker, PostgreSQL)
- `assets/` — collateral (pitch material, audio, design)
- `GATES.md` — the production line and exit criteria
- `CHANGELOG.md` — notable changes
- `MIGRATION-LOG.md` — every artifact migrated into this repo, and what was left behind

## Working convention

An artifact becomes an asset when it is versioned, named consistently, and consumed by the next stage of work. Every working session reads from and writes to this repo. Nothing here is decorative.
