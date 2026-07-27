# STATUS — Aegis (governed core engine)

**State:** 🟡 Architecture documented; superseded-or-absorbed question open
**Last reviewed:** 2026-07-27 (sweep)

## Where things live in this repo
- Specs: `specs/aegis/` (complete global architecture, demo use-case packages)
- Docs: `docs/aegis/` (roadmap, system assessment, strategy)
- Code: `src/aegis/aegis-backend/` (FastAPI), `src/aegis/prototypes/` (Index series)
- Partnership asset: `assets/aegis/2026-01-26-aegis-jpmc-partnership-deck.md`

## Current state
- Jan 2026 architecture work; Index8 lineage continued into `src/meridia/integra-core/`.
- 2026-07-21: PR #8 merged — governance-alert approval recording implemented in the mock backend (`src/aegis/aegis-backend/api_v1.py`, `data_generator.py`, +33/−10). First Aegis code change since the disposition question was queued 2026-07-02. (sweep-reconciled 2026-07-27)

## Open decisions
- Reviewed with Ali 2026-07-02: the live-vs-absorbed question **needs a dedicated working session** — not answerable in one line; the outcome must be worked through and recorded. (reconstructed)

## Next action
- Schedule the disposition working session (queued 2026-07-02; see INVENTORY open decision #5). Note: development effort is now accruing on Aegis (PR #8) while its disposition is open — one more reason to hold the session soon.

<!-- Tail restored 2026-07-13: the 2026-07-02 v0.3 commit truncated this file mid-sentence. Unchanged sections recovered verbatim from commit 31bbb6b4 (v1); sentences v0.3 had rewritten were completed from the v0.3 body itself and are marked (reconstructed). -->
