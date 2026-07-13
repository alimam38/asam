# Skills Scout — 2026-07-13 (catch-up run)

Note: this is a **catch-up run after a 22-day gap** — the job last ran 2026-06-21, so this
digest covers roughly 2026-06-22 → 2026-07-13 in one pass. A window this wide means more
churn than a daily run; I kept the bar high and pushed borderline finds to the skip list.
Deduped against seen-index. Freshness caveat still applies — web search can't pin exact
publish dates, so "fresh" means current-period unless a date is stated; one item (Candid)
is older but promoted because it directly serves an otherwise-unserved focus lane.

## Items

### 1. Claude Code `/dataviz` skill (new official skill)
- **What:** A new built-in Claude Code skill for chart and dashboard design — form heuristics,
  a color formula with a runnable palette validator, mark specs, and interaction rules, in a
  brand-neutral system you can re-skin.
- **Why relevant:** Plumbline **is** an executive dashboard (active build #1, embedded
  analytics). This gives every dashboard/chart session a consistent design system instead of
  ad-hoc chart styling — directly usable for Plumbline UI work now.
- **Source:** https://code.claude.com/docs/en/changelog (current-period; also covered at
  releasebot.io/updates/anthropic/claude-code)
- **Trust:** Tier 1 — Anthropic-verified, ships with Claude Code.

### 2. Claude Design overhaul — design-system imports + code round-trips
- **What:** Major July update: import design systems from a GitHub repo/design files, Claude
  builds with those components and auto-corrects against the system; code round-trips with
  Claude Code; usage limits now shared with chat/Cowork/Code (fixes the separate
  token-pool problem).
- **Why relevant:** Claude Design is an explicit focus (open item #5 — when to use it, UI
  mockups/prototypes). Importing a Plumbline design system and round-tripping mockups into
  code is exactly the mockup→build bridge flagged in the 06-21 digest, now much stronger.
- **Source:** https://venturebeat.com/technology/anthropic-ships-major-claude-design-overhaul-with-design-system-imports-code-round-trips-and-a-fix-for-its-token-burning-problem
  (July 2026; corroborated by https://support.claude.com/en/articles/12138966-release-notes)
- **Trust:** Tier 1 — Anthropic-verified feature; VentureBeat is secondary coverage.

### 3. `mcp-server-dev` plugin — official successor to mcp-builder
- **What:** The old `mcp-builder` skill is **deprecated**; its replacement is the
  `mcp-server-dev` plugin in anthropics/claude-plugins-official — three composing skills
  (`build-mcp-server`, `build-mcp-app`, `build-mcpb`) that interrogate your use case, pick a
  deployment model (remote Streamable HTTP, MCP apps, MCPB bundles, local stdio), and
  scaffold. Install: `/plugin marketplace add anthropics/claude-plugins-official` →
  `/plugin install mcp-server-dev`. Now the recommended path on modelcontextprotocol.io.
- **Why relevant:** MCP-server building is a named focus (e.g., a future Populi/Plumbline MCP
  server). If any local work still references mcp-builder, migrate. Watch item: the final MCP
  spec ships 2026-07-28 and drops the session model — build against these updated skills, not
  older tutorials.
- **Source:** https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev ·
  https://modelcontextprotocol.io/docs/develop/build-with-agent-skills (verified by fetch)
- **Trust:** Tier 1 — Anthropic official plugin repo + MCP official docs.

### 4. Claude Code `/doctor` — context-cost audit of skills, MCP servers, plugins
- **What:** `/doctor` now diagnoses installation health and **finds unused skills, MCP servers,
  and plugins versus their context cost**, dedupes local CLAUDE.md against checked-in ones,
  proposes trimming derivable CLAUDE.md content, and flags slow hooks.
- **Why relevant:** This is the skill/plugin **curation** focus turned into a tool — with this
  session's long connector list and a growing skill set, a periodic `/doctor` run is the
  cheapest way to keep context spend honest. Pairs with this scout: scout adds, doctor prunes.
- **Source:** https://code.claude.com/docs/en/changelog (current-period; also at
  releasebot.io/updates/anthropic/claude-code)
- **Trust:** Tier 1 — Anthropic-verified, built into Claude Code.

### 5. Candid MCP connector + Claude for Nonprofits
- **What:** Candid (the nonprofit-data authority: 990s, funders, grants) has an official MCP
  connector in Claude's Connectors Directory — search orgs/funders by cause or region, free
  tier included; part of "Claude for Nonprofits," which also includes **discounted Claude
  subscriptions for eligible organizations**.
- **Why relevant:** Hits the grants & nonprofit/education pricing focus twice: funder
  prospecting for Turner/Hypomone work, and the discount program may apply to Turner's own
  Claude spend — worth checking eligibility.
- **Source:** https://candid.org/blogs/claude-for-nonprofits-candid-mcp-connector-access-nonprofit-data-ai-assistant/
  (verified by fetch — published 2025-12-02, so **not new**; promoted as foundational because
  nothing in this lane has been surfaced before)
- **Trust:** Tier 1/2 — official Candid + Anthropic partnership, connector in the official directory.

## Skipped (logged to skipped-log.md)
- Claude Sonnet 5 now default in Claude Code (1M context) — model release, not a skill/plugin.
- Final MCP spec ships 2026-07-28 (sessions dropped; Tasks first-class) — spec, not installable;
  noted as watch item under item 3.
- Claude Managed Agents scheduled deployments + vault env vars (beta) — scheduled-tasks adjacent
  but a platform product outside the current stack.
- Nonprofit Grant Intelligence MCP (Apify) — Tier 4, pay-per-call; grants lane covered by Candid.
- Claude Cowork on web + mobile — platform expansion, not an installable skill/plugin.
- tonsofskills.com marketplace (425 plugins / 2,810 skills, jeremylongshore) — bulk directory
  churn, low per-item signal.
