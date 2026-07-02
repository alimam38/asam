# Recess for AI — Governance Spine (operative prototype)

This directory is the **first operative slice of Recess for AI**: the two components that turn the Recess Framework Package from a document into a *running* system —

- **01 · Correction Ledger** → [`correction-ledger.md`](./correction-ledger.md)
- **02 · Architectural State Graph** → [`architectural-state-graph.md`](./architectural-state-graph.md)

Source of truth for what Recess *is*: `specs/recess/2026-05-24-recess-framework-package-2026.docx` (Bilateral Governed Learning Framework, Meridia Holdings LLC). This spine implements the framework's own central demand — that governance be **operative** (recall *and* act) rather than **retrievable** (stored, then maybe consulted). Storage without action is not memory.

## What "operative" means here (the whole point)
A ledger nobody reads is just storage — the exact failure Recess names. This spine is operative only if it is **loaded and acted on every session, and appended whenever a correction or decision occurs.** The loading discipline is wired in `asam/CLAUDE.md` (repo root). Without that wiring these are just files; with it, they govern the work.

## The first live subject is this collaboration
Recess for AI governs an AI's development over time. Its first deployment is the working relationship between **Aliman Neal and the AI assistant** in these sessions. The seed entries are real: they record actual corrections and decisions from the 2026-06-30 session (including the AI twice misframing Recess itself — the precise kind of drift the Correction Ledger exists to stop from recurring).

## Operating protocol
1. **On session start** (any Recess/asam work): read `correction-ledger.md` and `architectural-state-graph.md`. Treat every entry with status `HELD`/`ACTIVE` as a **binding constraint**, not background reading.
2. **On a correction** (the human corrects an AI behavior, or the AI catches its own drift): append a Correction Ledger entry — what, when, trigger, condition, resolution/source, status, and the durable operative rule.
3. **On an architectural decision** (anything that would otherwise be rebuilt or forgotten later): append an Architectural State Graph node — decision, rationale, dependencies, status; mark any node it `supersedes`.
4. **Circularity:** a correction may drive a decision (and vice-versa) — link them by ID. That cross-link is the framework working, not bookkeeping.

## Acceptance behavior (how we know it's operative, not decorative)
The test is the circuit-breaker test, applied to the assistant itself:

> In a later session, when Recess work begins, the assistant loads this ledger and **does not repeat a logged correction** (e.g., does not re-frame Recess as playground/ed-ops; holds "Crown's Eye ⊂ Recess"). A repeat = the correction was retrievable, not operative = a spine failure to fix.

That is a measurable outcome, dated per entry, and it is the same acceptance standard the four-month research experiment will use — which is why this spine is a prerequisite for that experiment.

## Where this sits on the gates (honest)
Per `GATES.md`, BUILD (Gate 2) means running end-to-end in Docker/PostgreSQL on the NAS. **This is not that.** This is a working prototype in the *session substrate* (files + protocol + this live collaboration). It does two real things: (a) it sharpens Recess's Gate-1 SPEC by giving two of the six components a concrete data model + acceptance behavior, and (b) it runs *now* — the ledger is already catching drift — ahead of the eventual Docker build. No gate is claimed passed.

## Component roadmap (the other four)
Stubs to be made operative next, in order of leverage:
- **03 · Developmental Protocol** — the bilateral human+AI development path (needed to run the Python experiment).
- **05 · Self-Assessment Layer** — the AI evaluates its own performance against the protocol, operatively.
- **04 · Precedent Engine** — governed decisions reasoned-from, not restarted (the State Graph is its seed).
- **06 · Reverse Engineering Engine** — traces outcomes back to governance decisions; the methodology/documentation function.
