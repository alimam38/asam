# Architectural State Graph — Recess for AI (Component 02)

Every architectural decision in the build environment: what was decided, the rationale, the dependencies, and current validity. Prevents the **rebuild loop** by making prior decisions accessible and their dependencies traceable. Functions as persistent project memory.

**Status legend:** `ACTIVE` = current · `SUPERSEDED` = replaced (points to successor) · `PROPOSED` = decided but not yet effected.

| ID | Date | Decision (short) | Status |
|---|---|---|---|
| ASG-2026-06-30-001 | 2026-06-30 | Innovation Radar = config-driven modular pipeline system | ACTIVE |
| ASG-2026-06-30-002 | 2026-06-30 | Recess build order = Option A: operative spine before the experiment | ACTIVE |
| ASG-2026-06-30-003 | 2026-06-30 | Spine lives at `src/recess/governance/`, Markdown-first, wired via `asam/CLAUDE.md` | ACTIVE |
| ASG-2026-06-30-004 | 2026-06-30 | Re-scope the `edtech-recess` radar pipeline (was mis-scoped) | PROPOSED |

---

### ASG-2026-06-30-001
- **Decision:** The Innovation Radar is a config-driven, modular pipeline system — a registry (`config/pipelines.yaml`) of separable pipelines over a shared engine, file-based storage, in `Cowork-Master/Innovation Radar/`.
- **Rationale:** Ali wants deep dives now on a system where pipelines can be added/updated independently ("separated pipelines").
- **Dependencies:** none.
- **Status:** ACTIVE.

### ASG-2026-06-30-002
- **Decision:** Recess build sequence = **Option A** — stand up the operative governance spine (Correction Ledger + Architectural State Graph) first, dogfooded on this collaboration, **before** the four-month Python research experiment.
- **Rationale:** Recess's own thesis (storage ≠ action; the rebuild loop) means the framework must be *operative* before its validation experiment is credible. The spine is a hard prerequisite for the experiment (which requires a live ledger, developmental protocol, and self-assessment layer).
- **Dependencies:** none. **Blocks:** the research-experiment build.
- **Status:** ACTIVE.

### ASG-2026-06-30-003
- **Decision:** The operative spine lives at `src/recess/governance/`, **Markdown-first** (human-reviewable), with loading + append discipline wired via a repo-root `asam/CLAUDE.md`.
- **Rationale:** Markdown is the substrate the work happens in and that human governance can review (the Human Adjudication Memorandum requires human authority over the AI's memory). Loading via `CLAUDE.md` is what converts "stored" → "operative." YAML/DB can mirror this later if machine consumption is needed.
- **Dependencies:** `ASG-2026-06-30-002`.
- **Status:** ACTIVE.

### ASG-2026-06-30-004
- **Decision:** Re-scope / split the `edtech-recess` Innovation Radar pipeline into two correctly-aimed pipelines: **(a) adaptive-learning / prerequisite-mapping edtech** (Crown's Eye, human side) and **(b) AI governance / evaluation / observability** (Recess-for-AI, enterprise side).
- **Rationale:** The original pipeline scoped Recess as playground operations — a direct consequence of the misframe corrected in the ledger.
- **Supersedes:** the original `edtech-recess` pipeline scope (initial 2026-06-30 radar config).
- **Links:** driven by `CL-2026-06-30-001`, `CL-2026-06-30-002`.
- **Status:** PROPOSED (config change + re-run pending Ali's go).

---
*Append a node whenever an architectural decision is made. When a decision replaces an earlier one, set the old node to `SUPERSEDED` and point it here — never delete it (the record of what changed and why is the anti-rebuild-loop value).*
