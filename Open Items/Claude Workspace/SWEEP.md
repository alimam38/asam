# SWEEP — Weekly Repo Librarian

Scheduled job. Runs weekly, same pattern as skills-scout / grants-scout: read context, do the pass, write dated output, update the seen-index. **This job keeps the repo honest; it does not do project work.**

## What to read
1. `/INVENTORY.md` (root) — the master index
2. Every `STATUS.md` in the repo:
   - `docs/plumbline/STATUS.md`
   - `docs/clients/turner/STATUS.md`
   - `docs/meridia/STATUS.md`
   - `docs/asam/hypomone/STATUS.md`
   - `docs/waypoint/STATUS.md`
   - `docs/recess/STATUS.md`
   - `docs/aegis/STATUS.md`
   - `docs/eden-crown/STATUS.md`
   - `docs/ksw/STATUS.md`
   - `docs/agency/STATUS.md`
   - `infra/STATUS.md`
3. `git log --since="8 days ago" --name-only` — what actually changed this week

## What to do
1. **Reconcile.** For each initiative, compare its STATUS.md against files actually added/changed this week. If new artifacts landed but STATUS wasn't updated, update the "Current state" and "Last reviewed" lines and note it in the sweep report.
2. **Flag STALE.** Any STATUS.md with "Last reviewed" older than **21 days** AND status 🟢 or 🔴 gets flagged. (🟡 parked items with a stated reason — e.g., WayPoint's patent gate — are exempt.)
3. **Flag contradictions.** INVENTORY.md says one thing, STATUS.md says another → list both, don't guess which is right.
4. **Surface open decisions.** Collect every "Open decisions" item across all STATUS files into one ranked list (rank by what unblocks the most).
5. **Update INVENTORY.md** status emojis only when a STATUS.md clearly supports the change.

## Hard rules
- **Never invent progress.** If nothing changed, the report says nothing changed.
- **Never resolve an open decision.** Decisions belong to Ali; the sweep only surfaces them.
- **Never delete or archive anything.** Recommend, don't act.

## Output
Write to `Open Items/Claude Workspace/Outputs/sweep/YYYY-MM-DD-sweep.md`:

```
# Sweep — YYYY-MM-DD
## Changed this week (from git log)
## STATUS files updated by this sweep
## STALE flags
## Contradictions
## Open decisions, ranked
## One suggested focus for the coming week (single line, based only on the above)
```

Append one line per run to `Open Items/Claude Workspace/Outputs/sweep/seen-index.md`.
