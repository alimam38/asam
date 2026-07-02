# ASAM

ASAM (Hebrew: storehouse — divine provision and blessing) is the umbrella product repository for six sub-systems built by Aliman Neal:

| Sub-system | What it is |
|---|---|
| Plumbline | Hosted executive intelligence layer for small accredited institutions on Populi — Admissions, Academics, Financials, Scholarships, and strategic-goal/accreditation evidence in one always-current President's view. Populi doesn't build dashboards; that gap is the product. Spec: `specs/plumbline/spec-v2.md`. **Lead sub-system.** |
| Eden Crown | Not yet defined in this repo. Defining question: what does Eden Crown do, for whom, in one sentence? |
| Meridia | Financial-data intelligence work; an ingestion/wiring prototype (`integra-wiring`, Python/FastAPI) exists. Defining question: what is Meridia's deliverable product, beyond the prototype? |
| Waypoint | Not yet defined in this repo. Defining question: what does Waypoint do, for whom, in one sentence? |
| Aegis | Not yet defined in this repo. Defining question: what does Aegis do, for whom, in one sentence? |
| Recess | **Bilateral Governed Learning Framework** (Meridia Holdings LLC) — a governance architecture that develops a human learner *and* the AI system simultaneously, both assessed, corrected, and documented. Human side deploys to K-12 as Crown's Eye; the enterprise AI-governance side ("Recess for AI") is the licensable product. Spec: `specs/recess/2026-05-24-recess-framework-package-2026.docx`. Operative governance spine (Correction Ledger + Architectural State Graph) running at `src/recess/governance/`. |
| Kingdom Soundworks (KSW) | Not yet defined in this repo. Defining question: what does KSW do, for whom, in one sentence? |

## Current status

Nothing in this repository runs yet. The repository currently holds migrated specs, decision records, reports, and collateral from prior working sessions, plus prototype source under `src/`.

The first gate is **Gate 1 — SPEC** (see GATES.md). Plumbline is the lead sub-system: `specs/plumbline/spec-v2.md` (full build, 2026-06-11) defines the product; v1 remains as the Turner planning baseline. The gate closes when v2's open-items table is resolved or signed off with defaults — most items close at the 2026-06-12 Turner meeting.

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
