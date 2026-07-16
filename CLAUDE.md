# ASAM — repo instructions for Claude

ASAM is Aliman Neal's umbrella product repository (six sub-systems; see `README.md` and `GATES.md`). Working convention: nothing here is decorative — every session reads from and writes to this repo, and an artifact becomes an asset only when it is consumed by the next stage of work.

## Recess governance is OPERATIVE — read before Recess work

Recess for AI's governance spine lives at `src/recess/governance/`. It is a **running system, not reference material.** A ledger that isn't loaded and applied is the exact failure Recess exists to fix ("storage without action is not memory"). Loading it *is* the point.

1. **Before any Recess (or Recess-adjacent) work**, read `src/recess/governance/correction-ledger.md` and `src/recess/governance/architectural-state-graph.md`. Treat every `HELD` / `ACTIVE` entry as a **binding constraint**. In particular:
   - Recess is a **Bilateral Governed Learning Framework** (governs a human learner *and* the AI), **not** a playground/recess-operations tool and not a generic K-12 ed-tech app.
   - **Crown's Eye ⊂ Recess** — Crown's Eye is the K-12 *deployment*; the enterprise AI-governance half ("Recess for AI") is core.
2. **When the human corrects an AI behavior, or the AI catches its own drift**, append a Correction Ledger entry (what, when, trigger, condition, resolution/source, operative rule, status).
3. **When an architectural decision is made** that would otherwise be re-litigated or forgotten later, append an Architectural State Graph node; mark anything it supersedes (never delete).
4. Corrections and decisions cross-link by ID — that circularity is the framework working.

## Orientation
- `docs/asam/session-preflight.md` — environment/capabilities manifest (plugins, connectors, skills, secrets); read at session start to activate what's needed.
- `docs/asam/session-handoff.md` — living work state + open threads; read at session start to resume.
- `GATES.md` — the production line; gates are per sub-system and binary (met / not met).
- `specs/recess/2026-05-24-recess-framework-package-2026.docx` — the authoritative definition of Recess.
- Guardrails: Meridia / Recess is sensitive IP and Turner client data is confidential — never expose either externally. Draft-then-approve external outputs; never execute payments, only prepare them.
