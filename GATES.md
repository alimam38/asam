# ASAM — Production Gates

The production line. Each gate has a binary exit criterion: it is either met or it is not. Gates are evaluated per sub-system (Eden Crown, Meridia, Waypoint, Aegis, Recess, KSW); ASAM 1.0 is defined at the bottom.

## Gate 1 — SPEC

A buildable specification exists: someone could start implementing without asking Aliman clarifying questions.

**Exit criterion:** a spec document in `specs/<sub-system>/` that names the user, the core workflow, the data model, and the acceptance behavior. Met / not met.

## Gate 2 — BUILD

Core functionality runs end-to-end in the local Docker environment (Synology NAS: Docker + PostgreSQL).

**Exit criterion:** one documented command sequence brings the system up and the core workflow completes. Met / not met.

## Gate 3 — TEST

Automated tests cover the critical paths and pass.

**Exit criterion:** `tests/` contains tests for every critical path named in the spec, and the suite passes clean. Met / not met.

## Gate 4 — DEPLOY

The system runs on target infrastructure, reachable by someone other than Aliman.

**Exit criterion:** a second person reaches and uses the running system without Aliman's machine involved. Met / not met.

## Gate 5 — DEMO

A scripted walkthrough exists that a stakeholder can follow.

**Exit criterion:** a walkthrough document in `docs/` that a stakeholder has actually followed start-to-finish. Met / not met.

## Gate 6 — FIRST DOLLAR

A real external party uses it under real terms.

**Exit criterion:** signed terms and at least one real transaction or paid use. Met / not met.

## Definition of 1.0

Someone outside Aliman's ecosystem can use this without him in the room.

## Current state

| Sub-system | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Gate 5 | Gate 6 |
|---|---|---|---|---|---|---|
| Plumbline | in progress | — | — | — | — | — |
| Eden Crown | open | — | — | — | — | — |
| Meridia | open | — | — | — | — | — |
| Waypoint | open | — | — | — | — | — |
| Aegis | open | — | — | — | — | — |
| Recess | open | — | — | — | — | — |
| KSW | open | — | — | — | — | — |

No gate has been passed. First open gate: **Gate 1 — SPEC** for **Plumbline** (lead sub-system). `specs/plumbline/spec-v1.md` exists (drafted 2026-06-11); the gate closes when its open-items table — KPI definitions, cohort rules, FTE divisor, survey-to-goal mapping, saved Populi report set — is resolved or signed off with the stated defaults.
