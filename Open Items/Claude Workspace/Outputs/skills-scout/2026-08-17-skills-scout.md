# Skills Scout — 2026-08-17

_Window: 2026-08-11 → 2026-08-17 (last digest 2026-08-10). Sources per `skills-scout-sources.md`; SerpAPI recency layer used (3/3 calls, week-scoped)._

## Official / Tier 1

- **Claude Cowork in the Chrome side panel** (Aug 12) — full Cowork sessions now run in a Chrome sidebar; sessions save to history and carry across desktop, web, and mobile. Why: Cowork lane — changes where sessions live, and puts Cowork next to browser-side Populi/QBO work. Trust: Tier 1 origin (Anthropic release; Engadget/9to5Mac/TechRadar coverage).
- **Claude Code v2.1.232–.233** (Aug 14–15) — subagent forking on by default (subagents inherit the full conversation), cross-session SendMessage messaging, `claude plugin validate` now checks `.claude/skills` directories, GitLab support (marketplace URLs + `--worktree` MR), MCP v2 connection fixes. Why: agentic-context setup + skill/plugin curation lanes; extends the fleet-of-sessions pattern (seen 08-08) into default tooling. Trust: Tier 1 (official changelog via releasebot).
- **Compliance API extended to Cowork and Claude Code sessions** (Aug 11, Enterprise beta) — agentic session data now flows into the official Compliance API. Why: Aegis lane — a first-party audit-trail surface for agentic sessions; reference for governance-not-guardrails patterns. Trust: Tier 1.
- **Official plugin marketplace: first observed removal + fast-widening vendor set** — `aws-dev-toolkit` removed Aug 14; active vendor plugins now include dash0, aikido, wix, sumup, render, amd-skills, buildkite, expo, forge-skills, hyperframes, and a three-plugin Carta suite (investors / cap-table / crm). Why: curation signal both ways — the directory now prunes, and vertical-SaaS-ships-a-plugin (Carta, seen 07-30) is accelerating; the GTM pattern Plumbline would follow. Trust: Tier 1 (repo commit log).
- **Claude now watermarks all outputs — invisible SynthID-Text in text, C2PA metadata in files** (models deployed since Aug 2; press wave Aug 11–13) — imperceptible statistical watermark in generated text across every surface (web, API, Claude Code, Cowork, Tag); signed C2PA provenance on .svg/.png/.jpg. **No opt-out on any tier**; a detection API is coming. Why: cross-cutting — every deliverable you ship (Plumbline docs, grant applications, The Charter instruments, client-facing reports) now carries provenance signal; worth knowing before anyone runs a detector on your output. Note: a detected mark is provenance, not proof of AI authorship, and C2PA strips on re-save. Trust: Tier 1 origin (Anthropic-confirmed technique), broad Tier 2 press (Forbes/PCMag/CNET/Gizmodo). *(added by evening delta run)*
- **skill-doctor plugin (anthropics/claude-plugins-community)** — QA plugin for Agent Skills: validate, test, and score skills (spec conformance, script testing, quality grades, security posture). Why: SKILL.md authoring/curation lane; natural companion to skill-forge. Trust: Tier 1 infra / community-authored — install from the anthropics marketplace; same-named lookalike repos are already appearing (see skipped log).

## Skills & plugin ecosystem (dev tooling / curation)

- **Vendor official-skills wave, continued** — new this window: `hashicorp/agent-skills` (installable Claude plugin bundles per product), `microsoft/skills` (skills + MCP servers + custom agents for Foundry/Azure), `awslabs/agent-plugins` (skills+MCP bundles for AWS), `elastic/elastic-docs-skills`. Why: "official vendor skills repo" is now table stakes — the model for a future Plumbline/Populi skills repo, and HashiCorp/AWS bundles are directly useful for infra/Docker work. Trust: Tier 2 (official vendor repos; still verify contents before install).
- **JetBrains: Agent Skills in IntelliJ IDEA** (blog, Aug 12) — IDE-native support for the Agent Skills standard. Why: skills-standard adoption beyond Claude — your SKILL.md investment stays portable. Trust: Tier 2 (official JetBrains blog).
- **Leutenegger/book-to-skill** (Aug 13; ~1.2k★ in 4 days) — turn any technical book PDF into a Claude Code skill. Why: breakout entrant in the book→skill distillation wave (seen 08-01); same pattern applies to distilling the Meridia corpus into loadable skills. Trust: Tier 3/4 — big traction, new author; review before feeding it proprietary PDFs.
- **rolecraft-sh/rolecraft** (~75★) — "package manager for AI agents": install/test/publish skills & MCP servers across 86+ agents; zero-dependency CLI. Why: curation lane; competes with `npx skills` (07-01) and `gh skill` (07-06). Trust: Tier 3/4.
- **nduc99911/repo-context-mcp** (Aug 12; ~104★) — MCP server for repo maps, code search, and token-aware context packs. Why: agentic-context setup for a monorepo like asam. Trust: Tier 4 — unknown author, install-with-caution.
- **fellowgeek/mcp-memory** (Aug 13; ~179★) — persistent long-term memory MCP backed by SQLite FTS5. Why: the persistent-memory wave continues (claude-mem 07-13, memsearch 07-25) in a simple self-hostable form. Trust: Tier 4.

## Meridia / Hypomone (fintech & lending)

- **Plaid ships MCP support (early access)** (Aug 14) — data partners can connect AI agents (Claude, Cursor, Codex named) to resolve integration issues; same release adds Consumer Report webhook diagnostics (error / repairable_items / failed_products) for credit underwriting. Why: Plaid is named in the Hypomone stack — an official first-party Plaid MCP path, even integration-support-scoped, is the beachhead to watch. Trust: Tier 2 (Plaid release via The Paypers).
- **Plain-language skills wave (ISO 24495)** — `danyuchn/iso-24495-skill` (~107★), `GaZmagik/iso-24495` (skill + plugin), plus `surendranb/writing-skills` (plain language, GOV.UK, business-writing frameworks). Why: The Charter is a compliance-safe intake instrument — plain-language rewriting rules as skills are directly usable for drafting §4 intake questions. Trust: Tier 4 — new repos; review the rules before adopting.
- **OpenLabs-so/openanalytics** (Aug 11; ~224★) — open-source, privacy-first, cookieless web analytics with revenue attribution and an MCP server. Why: self-hosted (NAS/Docker posture) analytics for Plumbline/Hypomone web surfaces without a privacy fight. Trust: Tier 3/4 — young repo, fast traction.

- **FiscalNote PolicyNote MCP in the Claude Connectors Directory** (Aug 13) — official connector bringing FiscalNote's legislative/regulatory policy intelligence into Claude. Why: Meridia lane — CRA/community-lending policy monitoring via a governed connector rather than ad-hoc scraping; also touches grants/regulatory watch. Trust: Tier 2 (vendor press release, Businesswire; connector is in the official directory). *(added by evening delta run)*

## Recess / K-12

- **vasanthsreeram/Alvarmethod** (Aug 16; ~25★) — one-to-one AI teaching skills ("Alvar method"), portable across Claude Code and other agents. Why: 1:1 tutoring method packaged as skills — worth a read for the Recess pedagogy layer. Trust: Tier 4 — unknown author, install-with-caution.
- Otherwise quiet: nothing new this window beyond the already-surfaced anthropics/k12-teacher-skills ecosystem (directories are now re-listing it).

## Aegis (governance / audit)

- **bar181/bar-observatory** (Aug 12; ~17★) — deterministic, local-only audit reports for Claude Code agent sessions (Rust + SQLite, zero network calls, exposed as an MCP server). Why: the audit-trail-for-agentic-systems pattern in minimal local form — a useful reference next to Aegis's governance-alert approvals. Trust: Tier 4 — tiny/new; treat as a pattern reference, not a dependency.
- Cross-ref: the Compliance API expansion (Tier 1 above) is the official-platform expression of the same concern.

## Populi / Postgres / NAS · KSW

- Quiet this window. No new Populi/SIS, Postgres, or NAS-specific skills/MCPs beyond already-seen items; nothing on grants or music/education tooling for KSW.

---
_Skipped-log additions this run: increments + non-fits incl. auto-mode default rollout (increment of 08-08 PSA), the Aug 15–16 Anthropic outage, and the DeepSeek Harness ecosystem — see `skipped-log.md`._

_Evening delta run (same day): merged 2 additional items (Claude output watermarking; FiscalNote PolicyNote MCP) missed by the morning pass; 7 further delta finds were increments/non-fits and went to the skipped log. SerpAPI used (3/3 day-scoped calls)._

---

## Addendum — second pass, ~17:30 UTC scheduled run (increment over the morning digest)

### Official / Tier 1
- **Claude now watermarks outputs — invisible, text + images, no opt-out** (rolled out Aug 11–13) — EU-AI-Act-driven provenance marking (C2PA-adjacent), applied globally to Claude outputs. Why: Cowork lane — touches every deliverable produced through Claude (client docs, grant drafts, content); detection/removal behavior is still being characterized. Trust: Tier 1 origin (Anthropic change) via heavy press (Forbes, Fortune, Euronews); official docs detail still thin — don't assume any output is watermark-free.

### Skills & plugin ecosystem (dev tooling / curation)
- **Untrivial-ai/agent-orchestrator** (~9.6k★, very active) — "agent IDE" for managing fleets of coding agents: an orchestrator plans tasks, spawns agents, and auto-handles CI fixes, merge conflicts, and code review. Why: the fleet-of-sessions pattern (SendMessage 08-08, peer-sessions 08-09) as a full product; established repo never previously surfaced. Trust: Tier 3 — popular non-vendor project; evaluate before adopting.
- **backnotprop/plannotator** (~7.9k★) — visually annotate and review agent plans and code diffs, share with a team, send feedback back to the agent in one click. Why: human-in-the-loop review layer for agentic work (pairs with facet, seen 08-04); author already known (effective-html). Trust: Tier 3.
- **bozhouDev/anthropic-mind** (Aug 17, day-one) — a Claude skill distilled from 428 primary Anthropic sources, shipped with the full corpus and the distillation pipeline. Why: read it for the corpus→skill distillation pattern (maps directly to the Meridia corpus work) more than for the skill itself. Trust: Tier 4 — unknown author, install-with-caution.

### Other lanes
- Recess/K-12, Meridia/Hypomone fintech, Aegis governance, Populi/Postgres/NAS, KSW: nothing genuinely new in this increment beyond the morning digest; fresh-repo churn logged to the skipped log.

_Addendum method: SerpAPI last-24h layer (3/3 calls) + GitHub `created:>2026-08-15` sweep + news verification, deduped against seen index and morning skipped-log entries._
