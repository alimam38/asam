# Skills Scout — 2026-08-10

Window: Aug 8–10 (weekend sweep; last digest 2026-08-09). Method: SerpAPI recency layer (3/3 calls: 24h GitHub sweep, Google News, lane-scoped 24h) + built-in web search + Composio GitHub search (repos created/pushed ≥ Aug 8, anthropics org commit logs). Deduped against seen index.

## Official / Tier 1

- **`ant` — the official Claude Platform CLI (anthropics/anthropic-cli)** — Anthropic's official CLI for the Claude API: send messages, manage Managed Agents/sessions/files, script against every API endpoint; jq-style `--transform` output, relaxed JSON/YAML flags, `@path` file syntax; Homebrew or Go install; active (pushed Aug 9, 610★). Why it matters: the missing scripting piece for the Managed Agents wave surfaced 08-09 — schedule/steer agents and sessions from the NAS, cron, or CI without hand-rolled REST calls (Claude/Cowork lane; Aegis ops adjacent). Newly noticed rather than newly shipped — it wasn't in the index. Trust: Anthropic-verified (Tier 1). https://github.com/anthropics/anthropic-cli
- **anthropics/claude-plugins-community — the community plugin marketplace repo** — Anthropic-run read-only mirror of community plugin submissions (via clau.de/plugin-directory-submission) for Claude Cowork and Claude Code; 341★, very active (dozens of automated version-bump PRs daily; plugins span zapier, whodb, web-vitals-auditor, workshop-mode, etc.). Why it matters: it's the third leg of the official plugin infrastructure alongside claude-plugins-official and knowledge-work-plugins, and the best single place to watch community-plugin flow for the curation lane. Newly noticed (created Mar 2026), not newly shipped. Trust: Tier 1 infrastructure, but the plugins inside are community-authored — vet each before install. https://github.com/anthropics/claude-plugins-community
- **Official marketplaces quiet this window** — claude-plugins-official, knowledge-work-plugins, and claude-plugins-community had version bumps only Aug 8–10 (hyperframes/deepeval/nimble/qodo/wix/lumen/remember/carta/auth0 etc.) — no new vendors; anthropics/skills had no commits. Claude Code shipped only v2.1.226 (Aug 8; SendMessage cross-machine origin + auth fixes) — logged as an increment.

## Claude / Cowork / scheduled-task ecosystem

- **cth9191/morning-intel** — self-installing Claude Code skill pack billed as "the morning brief on steroids": AI news, X, HN, YouTube, GitHub trending, Gmail triage in one scheduled run. Why it matters: it's a packaged, open version of exactly the scheduled-scout pattern this job runs — worth a skim for technique (self-installation, source fan-out), not necessarily for adoption. Trust: Tier 4 — day-one repo (~2★, created Aug 9), unvetted; read before running, especially anything touching Gmail. https://github.com/cth9191/morning-intel

## Recess / K-12 education

- **rudini/claude-edu-plugins — Moodle + Kahoot skills for Claude Code** — open-source (MIT) education toolkit: a Moodle skill covering course/section management, GIFT quiz imports, assignment grading + gradebook commands, an AI essay-grading pipeline, and course round-trip (download → edit locally → re-upload); plus a Kahoot quiz-generation skill with preview/validation; other agents connect via a bundled MCP server. Why it matters: first LMS-operations skill pack seen in the K-12 lane — directly relevant to Recess/Shadow Rock admin-ops piloting even if the school isn't on Moodle (the grading-pipeline and round-trip patterns transfer). Newly found (last updated ~June 2026), not newly shipped. Trust: Tier 3/4 — single known author, real repo, MIT; test on a sandbox Moodle before any live gradebook writes. https://github.com/rudini/claude-edu-plugins
- Otherwise quiet: no new K-12/teacher-facing skills, connectors, or MCP servers in the window (last-24h and news sweeps both ran).

## Aegis / governance & audit

- **superdesigndev/tools-registry — shared skill & secret vault for teams and agents** — a registry that lets a team share skills and the secrets they need "without leaking keys" (64★, created mid-July, pushed daily). Why it matters: skill distribution with credential hygiene is the Aegis-lane gap — most skill managers ignore secrets entirely; the design is worth reading even if the tool isn't adopted. Trust: Tier 4 — community project from the superdesign.dev crowd, Discord-driven, unaudited; don't put real keys in it yet. https://github.com/superdesigndev/tools-registry
- Otherwise quiet: governance/audit-trail results in the window were vendor thought-pieces (MintMCP, Preloop, obot.ai supply-chain post), not installables.

## Meridia / Hypomone — fintech & lending data

- Quiet this window. Nothing new on Plaid (Effects recap and the official Plaid MCP server predate the window; Plaid × Sierra was surfaced 08-08); the only new fintech-ish MCPs were a trading platform (pyon-mcp) and a web3 pay-per-call server — both off the lending/CRA focus (logged).

## Populi / Postgres / NAS

- Quiet this window. New memory-layer MCPs (memorry, Anchor) are churn in a saturated lane; nothing Populi- or SIS-specific surfaced.

## KSW (grants / music-education)

- Quiet this window — no new grant-tooling or music-education skills found.
