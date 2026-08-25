# Market scout — 2026-08-25 (Tue run; window Sat 08-22 → Tue 08-25 morning, deduped against the 08-24 run)

_Sources this run: Composio GitHub search + release radar, HN Algolia, SerpAPI (4/6 calls: 2 news, 2 X). Readwise was added as a source layer per Ali's mid-run request — the account is brand-new (only onboarding docs), so no reading signal yet; it will feed future runs once articles are saved._

## Top picks

**1. Claude Code v2.1.243–245 — prompt-cache TTL controls, /usage Loops breakdown, curated model picker**
[CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) · Since the .241 covered last run: `promptCacheTtl`/`subagentPromptCacheTtl` settings (1-hour cache on the main loop, 5-min for subagents), a per-loop token breakdown in `/usage` so runaway `/loop` tasks are visible, `modelPicker` curation, keyless Console sign-in, and a 75 MB (was 340 MB) zstd binary with big memory reductions. Also: Sonnet 5's $2/$10 per Mtok is now standard list price, not a promo.
*Why it matters to Ali:* the Loops breakdown and cache-TTL knobs are directly about the cost profile of scheduled/looping agent jobs like this one; Sonnet 5 at $2/$10 standard changes the cheap-lane math for Plumbline batch work.

**2. sodiumsun/agenttrail — local observability map for AI coding agents**
[github.com/sodiumsun/agenttrail](https://github.com/sodiumsun/agenttrail) · ~190 stars since 08-21. Watches Claude Code, Codex, and Cursor sessions locally — plans, tool calls, file changes, progress — in one real-time map. Real artifact, runs against tools he already uses.
*Why it matters to Ali:* he runs multiple scheduled Claude sessions against one repo; a local pane showing what each agent actually did (files touched, tools called) is the missing audit layer, and it's inspectable before trusting it.

**3. Supabase MCP server: enterprise-managed auth GA, built with Anthropic and Okta**
[@supabase announcement](https://x.com/supabase/status/2091979342419001685) (X via SerpAPI) · Admin-authorized, org-managed MCP auth is now GA on a mainstream developer platform — the first big consumer of the EMA extension pattern flagged in earlier runs, and a concrete step on the MCP Roadmap's "agent auth" focus area.
*Why it matters to Ali:* Postgres-backed app platform + managed MCP auth is exactly the shape a Plumbline-style SIS overlay would need to let institutions connect agents to their data without hand-managed tokens.

**4. Headlong — a "microharness" for persistent agents (Laude)**
[laude.org write-up](https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents) · [HN](https://news.ycombinator.com/item?id=49428882) (77 pts) · A minimal harness pattern for agents that persist across sessions rather than restarting cold — small enough to read in one sitting, and a counterpoint to heavyweight frameworks.
*Why it matters to Ali:* his scout/OS-file pattern (stateless workers + durable memory files) is a hand-rolled version of this; worth comparing notes before building more lanes.

**5. "My agent.md to improve LLM-assisted code quality" — Fabien Sanglard**
[fabiensanglard.net/agent.md](https://fabiensanglard.net/agent.md/index.html) · [HN](https://news.ycombinator.com/item?id=49410932) (404 pts, 174 comments) · A respected low-level engineer's concrete, opinionated agent instructions file, with a large HN thread arguing over what actually moves code quality.
*Why it matters to Ali:* directly harvestable ideas for CLAUDE.md/agent instruction files across his repos; the comment thread is a compressed survey of what practitioners are converging on.

## Worth a session this week

**agenttrail** — install it locally against a Claude Code session and see whether its plan/tool-call/file-change map is good enough to become the standing audit view for the scheduled agents. One session tells you if it's real; if it is, it slots straight into the NAS/Docker setup.

## Also noted (briefly)

- **Anthropic expands Mythos 5 access to defenders + $35M open-source security fund** — [SecurityWeek](https://www.securityweek.com/anthropic-expands-mythos-5-access-to-more-defenders-unveils-35m-open-source-fund/): security-model access widening; watch for artifacts funded out of the $35M.
- **duty1g/x64dbg-mcp-server** — [GitHub](https://github.com/duty1g/x64dbg-mcp-server): 1.3K stars in ~3 days; full debugger control over MCP. Niche for Ali but a marker of MCP eating specialist tooling.
- **"LLMs could control their host machines by exploiting inference engines"** — [essay](https://boydkane.com/essays/llms-could-control-their-host-machines-by-exploiting-inference-engines) / [HN](https://news.ycombinator.com/item?id=49424387) (160 pts): threat-model reading for anyone self-hosting models.
- **Enterprise cooling on Opus-tier pricing** — [FT](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) / [CIO](https://www.cio.com/article/4213299/companies-not-as-enthusiastic-about-anthropics-best-ai-model.html): buyers routing volume work to cheaper models; consistent with the Sonnet 5 price normalization above. Anthropic IPO reporting ([NYT](https://www.nytimes.com/2026/08/21/technology/anthropic-ipo-100-billion.html)) is market context only — no product change.
- **Claude multi-model outage Aug 24 (resolved)** — [status](https://status.claude.com/incidents/vgz5psbjmt1h) / [HN](https://news.ycombinator.com/item?id=49415907): second elevated-error incident this month; argues for retry/fallback in scheduled jobs.
- **TrueFoundry open-source agent harness** — [InfoWorld](https://www.infoworld.com/article/4211969/truefoundry-debuts-open-source-ai-agent-harness-claiming-up-to-75-lower-costs.html): "75% lower cost" claim unverified; harness-space entrant to track, not adopt.
- **kgoedecke/doop** — [GitHub](https://github.com/kgoedecke/doop): open-source multiplayer design canvas with MCP built in (340 stars since 08-22).
- **Codex `mcp-server` command deprecated** — [@CodexReleases](https://x.com/CodexReleases/status/2091929016194289782) (X via SerpAPI): OpenAI consolidating on its app server for MCP.
- Skipped as star-velocity caution: ApodexAI/FrontierAgent (418 stars in 3 days, vague provenance). Skipped as skills-scout beat: Kindle-highlights Claude skill, agent-skill-languages survey.
