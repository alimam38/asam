# SCHEDULES — the recurring jobs and how to switch them on

Why this file exists: all four scheduled jobs below were specified by 2026-07-02, but nothing
actually scheduled them — they only ran when a session happened to run them (skills-scout
stopped 2026-06-21; SWEEP, grants-scout, and nonprofit-pricing never ran until the 2026-07-13
catch-up session). A spec without a trigger is storage without action.

Creating a Routine (scheduled trigger) requires an approval that only an **interactive**
Claude session can grant. From any interactive session, say: *"Create the Routines defined in
Open Items/Claude Workspace/SCHEDULES.md"* — each entry below is a complete definition.

All Routines should fire as **fresh sessions** (each run starts clean and reads its context
files from the repo), and every run ends by committing and pushing its outputs.

---

## 1. skills-scout — DAILY, 7:30 AM (cron `30 7 * * *`)
Prompt: Run the daily skills-scout job for the asam repo per
"Open Items/Claude Workspace/Daily Curation.md": read Context/current-focus.md and
Context/skills-scout-sources.md, research skills/plugins/MCP servers from the last 1–2 days,
dedupe against Outputs/skills-scout/seen-index.md, write a dated digest (max 5 items, trust
notes per source tier) to Outputs/skills-scout/, append to seen-index.md and skipped-log.md,
commit and push.

## 2. SWEEP — WEEKLY, Monday 8:00 AM (cron `0 8 * * 1`)
Prompt: Run the weekly repo sweep for the asam repo exactly per
"Open Items/Claude Workspace/SWEEP.md" (read INVENTORY.md, all 11 STATUS.md files, and
git log --since="8 days ago"; reconcile, flag STALE >21 days, flag contradictions, rank open
decisions; never invent progress, never resolve decisions, never delete). Write
Outputs/sweep/YYYY-MM-DD-sweep.md, append one line to Outputs/sweep/seen-index.md, commit
and push.

## 3. grants-scout — WEEKLY, Tuesday 7:30 AM (cron `30 7 * * 2`)
Prompt: Run the grants-scout job for the asam repo: read
"Open Items/Claude Workspace/Context/grants-focus.md" and Context/grants-sources.md, search
for live grant opportunities fitting Turner Theological Seminary (use the Granted connector
plus web search), always flag eligibility, dedupe against
Outputs/grants-scout/seen-index.md, write a dated digest to Outputs/grants-scout/, append to
seen-index.md, commit and push.

## 4. nonprofit-pricing — MONTHLY, 1st at 7:30 AM (cron `30 7 1 * *`)
Prompt: Run the nonprofit/education pricing scout for the asam repo: read
"Open Items/Claude Workspace/Context/nonprofit-pricing-focus.md" and
Context/nonprofit-pricing-sources.md, verify current free/discounted programs (note the
validation each requires), dedupe against Outputs/nonprofit-pricing/seen-index.md, write a
dated digest to Outputs/nonprofit-pricing/, append to seen-index.md, commit and push.

---

Status log:
- 2026-07-13 — All four defined here after the catch-up session ran each job manually.
  Routine creation attempted from the catch-up session and blocked (non-interactive approval).
  NOT YET SCHEDULED — switch on from an interactive session, then update this line.
