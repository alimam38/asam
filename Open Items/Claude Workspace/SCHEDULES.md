# SCHEDULES — the recurring jobs (LIVE as of 2026-07-13)

Why this file exists: all four scheduled jobs below were specified by 2026-07-02, but for
weeks nothing reliably scheduled them — they only ran when a session happened to run them.
A spec without a trigger is storage without action. As of 2026-07-13 all four are live
Routines (scheduled triggers); the live trigger IDs and actual schedules are recorded per
job below. This file is the source of truth for WHAT each job does; the Routine prompts
implement it.

All Routines fire as **fresh cloud sessions**. The repo (`Open Items/Claude Workspace/`)
is the **single memory** for these jobs: each run reads its Context/ files and seen-index
from the repo and ends by committing and pushing its outputs. The parallel Dropbox
`/Claude Workspace` store used by the first-generation Routines was retired 2026-07-13
(see status log).

Times below are cron in UTC (7:30 AM ET = 11:30 UTC during daylight time).

---

## 1. skills-scout — DAILY (cron `30 11 * * *`) — Routine `trig_01MdyXPhrcQdTTK37iB2xCWG` "Daily skills scout"
Per "Open Items/Claude Workspace/Daily Curation.md": read Context/current-focus.md and
Context/skills-scout-sources.md, research skills/plugins/MCP servers from the last 1–2 days,
dedupe against Outputs/skills-scout/seen-index.md, write a dated digest (max 5 items, trust
notes per source tier) to Outputs/skills-scout/, append to seen-index.md and skipped-log.md,
commit and push.

## 2. SWEEP — WEEKLY, Monday (cron `0 12 * * 1`) — Routine `trig_016akV8Et7bpn9cMjKBnUBSw` "asam weekly sweep"
Run the weekly repo sweep exactly per "Open Items/Claude Workspace/SWEEP.md" (read
INVENTORY.md, all 11 STATUS.md files, and the last 8 days of commits; reconcile, flag STALE
>21 days, flag contradictions, rank open decisions; never invent progress, never resolve
decisions, never delete). Write Outputs/sweep/YYYY-MM-DD-sweep.md, append one line to
Outputs/sweep/seen-index.md, commit and push. NOTE: this Routine (created from Cowork
2026-07-13) works against the GitHub remote via API rather than a local clone, and includes
a staleness gate: if the repo's last push is >8 days old it goes report-only and flags it.

## 3. grants-scout — WEEKLY, Monday (cron `45 11 * * 1`) — Routine `trig_018pizgAbZCGKv7VASAwCSUb` "Weekly grants scout"
Read Context/grants-focus.md and Context/grants-sources.md, search for live grant
opportunities fitting Turner Theological Seminary (Granted/Kindora connectors when available,
plus web search), always flag eligibility, dedupe against Outputs/grants-scout/seen-index.md,
write a dated digest to Outputs/grants-scout/, append to seen-index.md, commit and push.

## 4. nonprofit-pricing — MONTHLY, 1st (cron `0 12 1 * *`) — Routine `trig_01Rz71jFwuiYhwrKEhDuTVXD` "Monthly nonprofit pricing scout"
Read Context/nonprofit-pricing-focus.md and Context/nonprofit-pricing-sources.md, verify
current free/discounted programs (note the validation each requires), dedupe against
Outputs/nonprofit-pricing/seen-index.md, write a dated digest to Outputs/nonprofit-pricing/,
append to seen-index.md, commit and push.

## 5. market-scout — TUE + FRI (cron `30 11 * * 2,5`) — Routine `trig_01JJuEhYRTgwMnEJpVpYYi3Z` "Market scout"
Broader software/AI marketplace scan (added from Cowork 2026-07-13, outside the original
four; migrated to repo-based later the same day). Read Context/market-scout-focus.md (signal
vs skip vs output stance) and Context/market-scout-sources.md (GitHub queries, HN Algolia,
X-with-fallback), lookback since the previous run, dedupe against
Outputs/market-scout/seen-index.md (created on first run), skip the daily skills scout's
beat, write a ranked 3–5-pick digest with exactly one "worth a session this week"
recommendation to Outputs/market-scout/, append to seen-index.md, commit and push.

---

Status log:
- 2026-07-13 — All four defined here after the catch-up session ran each job manually.
  Routine creation attempted from the catch-up session and blocked (non-interactive approval).
- 2026-07-13 (later) — Discovered that a Cowork interactive session had ALREADY created
  Routines for all four jobs (plus market-scout) earlier the same day, but the three scouts
  read/wrote a parallel **Dropbox** /Claude Workspace store — splitting memory from the repo
  and diverging from the catch-up run's repo seen-indexes. Resolution (Ali's call):
  repo is the single memory. Dropbox seen-index + skipped-log entries (2026-06-20..07-13)
  were merged into the repo copies, the three Dropbox-based scout Routines were deleted
  (old IDs trig_01MBrPipmAVn8EaAZK67VY47, trig_01WgDHsMngeNVHreB6fopELa,
  trig_01SwxMQDodx63N44VGNS3gBJ), and repo-based replacements were created with the same
  names and schedules (IDs above). Sweep Routine kept as-is (already repo-targeting);
  market-scout kept as-is pending migration of its Context files.
- 2026-07-13 (later still) — market-scout migrated too: its focus/sources files copied from
  Dropbox into repo Context/, the Dropbox-based Routine deleted (old ID
  trig_01C7oLgeqFhnzrTju4Aj8kH1) and recreated repo-based (ID above). No Dropbox
  seen-index existed yet (the first-generation Routine never fired). The Dropbox
  /Claude Workspace store is now retired for ALL jobs: do not write scout outputs there.
- ALL FIVE JOBS LIVE. Next fires: skills-scout daily 11:30 UTC; market-scout Tue/Fri
  11:30 UTC; grants-scout Mon 11:45 UTC; sweep Mon 12:00 UTC; nonprofit-pricing 1st 12:00 UTC.
