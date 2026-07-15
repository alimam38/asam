# STATUS — Plumbline (Populi + QuickBooks analytics for Turner)

**State:** 🟢 Active — immediate build priority
**Last reviewed:** 2026-07-02

## Where things live in this repo
- Specs: `specs/plumbline/spec-v1.md`, `spec-v2.md`, `populi-api2-findings.md`
- Meeting deck: `specs/plumbline/2026-06-11-turner-dashboard-populi-meeting-deck.pptx`
- Docs: `docs/plumbline/2026-06-20-phase0-president-view.md`, `2026-06-20-qbo-financials-mapping.md`
- Code: `src/plumbline/probe/` (Populi API probes), `src/plumbline/prototypes/` (exec demo, president-view live)
- Related tool: `tools/populi-billing-extract/`

## Current state
- OAuth 2.0 credentials secured; five-layer architecture locked (Integration / Normalization / Metrics / Presentation / Auth), TypeScript/Next.js.
- Phase 0 president-view prototype exists (`2026-06-20-president-view-live.html`).
- Target: one source of truth before **August** for SACSCOC/TRACS/ATS.

## Open decisions
- How much of the president-view prototype carries into the real Next.js build vs. rebuild clean — **decide at the first build session** (deferred 2026-07-02).

## Next action
- Confirmed 2026-07-02: **no TypeScript build code exists** beyond the probes/prototypes; next step is the first build session against `specs/plumbline/spec-v2.md`, where the president-view carry-over question is decided. (reconstructed)

<!-- Tail restored 2026-07-13: the 2026-07-02 v0.3 commit truncated this file mid-sentence. Unchanged sections recovered verbatim from commit 31bbb6b4 (v1); sentences v0.3 had rewritten were completed from the v0.3 body itself and are marked (reconstructed). -->
