# Market scout — 2026-07-17

_First run of this scout — no prior seen-index existed, so this uses a 7-day lookback (2026-07-10 → 2026-07-17)
instead of the usual Tue/Fri cadence window. GitHub API search is repo-scoped to this session (asam only) and
returned `"sessions are bound to their configured repositories"` for any other repo/topic query — GitHub findings
below are via WebSearch, not the authenticated API, per the sources file's documented fallback. X API returned
401 on one probe (no credits, as the sources file already notes) — X item below is "X via fallback" (WebSearch).
Composio MCP (suggested mid-run) is connected at the org level but not enabled in this chat, so its tools weren't
reachable this session — worth turning on for a future run to get authenticated GitHub search back._

## Ranked picks

### 1. AWS Labs ships an MCP-native multi-agent CLI orchestrator — [awslabs/cli-agent-orchestrator](https://github.com/awslabs/cli-agent-orchestrator)
Hierarchical supervisor/worker orchestration for CLI coding agents — Claude Code is one of 9 supported providers (also Codex, Copilot, Cursor, OpenCode, etc.). Each agent runs in an isolated tmux session; a supervisor delegates via **handoff** (sync), **assign** (async), and **send_message** (inbox) primitives over a local MCP server. v2.3.0 shipped July 12; 902 stars, 263 commits, 13 releases — real AWS-backed infra, not a demo (bundled web UI, REST API, Slack/Discord event plugins, DNS-rebinding protections).
**Why it matters to Ali:** This is the actual missing piece for running Claude Code across the six ASAM sub-systems concurrently instead of one session at a time — a supervisor could fan work out to Recess, Plumbline, and Crown's Eye sessions and collect results, which is close to what this very scout job needs (a coordinator dispatching sub-tasks). Worth a real trial, not just a read.

### 2. MCP spec's biggest rewrite goes stateless — final ships 2026-07-28 — [MCP 2026-07-28 release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
Removes the `initialize` handshake and `Mcp-Session-Id` entirely — client info now travels via `_meta` per-request, so any server instance can handle any request (no sticky sessions, plain round-robin load balancing). New extensions framework ships **MCP Apps** (sandboxed server-rendered UI) and **Tasks** (graduated from experimental; `tasks/get`/`update`/`cancel`). Auth tightens toward OAuth2/OIDC (mandatory `iss` validation per RFC 9207). Roots, Sampling, and Logging are formally deprecated (12-month sunset) in favor of tool params, direct LLM calls, and OpenTelemetry.
**Why it matters to Ali:** Direct infrastructure change to anything he runs behind an MCP gateway — the stateless requirement removes the session-affinity problem that's usually the annoying part of scaling a self-hosted MCP server (relevant to any Postgres/Docker-NAS-hosted server). 11 days until final; worth reading the migration notes before it ships, especially the Roots/Sampling/Logging deprecations if any current server leans on them.

### 3. 1Password for Claude — zero-exposure credential injection for browser agents — [1password.com/blog/1password-for-claude](https://1password.com/blog/1password-for-claude)
Claude can complete logins/OTP flows in-browser without the credential, vault item, or OTP ever entering the model's context, memory, or Anthropic's systems — 1Password injects directly into the page after biometric approval, scoped per-task, and post-fill checks confirm nothing leaked back into the page/DOM. Mac only, ships now across individual/family/business plans.
**Why it matters to Ali:** Directly reduces the "how much do I trust the agent with this login" tax for any Cowork automation that touches QuickBooks, Gusto, or Populi through a browser rather than an API — this is the shape of credential handling that should eventually extend to those workflows.

### 4. Ratel — progressive tool/skill disclosure so agents don't pay for context they don't use — [ratel-ai/ratel](https://github.com/ratel-ai/ratel)
BM25-indexed catalogs of tools and skills; the agent searches and gets back only what's relevant per turn instead of loading everything up front — claims ~80% fewer tokens per call with no external vector DB required. Modest but real: 207 stars, 43 releases, SDKs in TS/Python/Rust, integrations for Vercel AI SDK and Pydantic AI.
**Why it matters to Ali:** This is the same problem ToolSearch/deferred-tools solves inside Claude Code itself — worth a look as a reference implementation if he ever builds a custom agent harness (Recess governance tooling, e.g.) that needs the same trick outside Claude Code's own runtime.

### 5. Herdr — an agent-aware terminal multiplexer for running multiple coding agents at once — [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)
tmux-alike, single Rust binary, but panes know agent state (blocked/working/done) instead of just being a shell. Detach and reattach (incl. over SSH) while agents keep running; agents themselves can drive it through a socket API to spawn panes and wait on each other. Real traction: 17.3k stars, 1.1k forks, 1,141 commits, v0.7.4 on July 15 — active, not star-farmed.
**Why it matters to Ali:** Overlaps conceptually with pick #1 (CAO) but at the terminal-UX layer rather than the orchestration-API layer — useful if the AWS tool's web UI isn't the workflow and he'd rather stay in a terminal while running several Claude Code sessions in parallel.

## Also noted, not ranked
- **X ships a hosted MCP server** ([TechCrunch](https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/), X via fallback) — launched June 30, still generating developer discussion into July; read-only (no write API), so an agent can search/read X's live corpus but not post. Slightly outside the 7-day window but flagged since it's a "major server" per the focus file's MCP-ecosystem criterion.
- HN discussion layer this week skewed toward general AI/Claude coverage (LM Studio's new agent launch, a Show HN prompt-injection gate) rather than anything new and artifact-backed beyond what's captured above — no additional items met the bar.

## Worth a session this week
**AWS Labs' `cli-agent-orchestrator`** (pick #1). It's installable today, directly targets the "run several Claude Code sessions and coordinate them" problem Ali's ASAM workflow already has, and is backed by an org (AWS) likely to keep maintaining it — higher payoff than reading about the MCP spec rewrite (real, but nothing to build with until July 28) or the terminal-multiplexer option (same idea, less structural leverage).
# Market Scout — 2026-07-17

_First run of this scout — no seen-index existed yet, so this covers a 7-day lookback (2026-07-10 → 2026-07-17). Going forward: Tue run covers Sat–Mon, Fri run covers Tue–Thu._

**Environment note:** GitHub's API is proxy-scoped to this repo only in this session (`GitHub access to this repository is not enabled for this session`) — direct authenticated GitHub search (topic:ai-agents, topic:mcp-server, etc.) was not available. Fell back to web search for repo/release discovery per the sources file's fallback instruction. HN via the Algolia API worked directly. Worth fixing for next run if a GitHub connector becomes available — see `session-preflight.md`.

## Top picks (ranked)

**1. MCP spec heading into its biggest revision yet — Release Candidate for 2026-07-28**
[blog.modelcontextprotocol.io — 2026-07-28 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) · final spec ships **July 28, 2026** (11 days out)
Drops the `initialize` handshake and session IDs for a stateless core (servers can now sit behind a plain round-robin load balancer), formalizes an Extensions framework (MCP Apps, Tasks), hardens OAuth/OIDC authorization, and sets a formal deprecation policy — **Roots, Sampling, and Logging are deprecated**, 12-month minimum removal window. Paired with this: the **Enterprise-Managed Authorization (EMA) extension** already went stable and is adopted by Anthropic (Claude, Claude Code, Cowork), Microsoft, VS Code, and Okta as identity provider — see [InfoQ, 2026-07-06](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/).
**Why it matters to Ali:** any MCP server you've built or plan to build for Plumbline integrations should be checked against the stateless-core change and the Roots/Sampling/Logging deprecations before the spec locks. EMA is also the shape a future "single sign-on across client MCP integrations" would take if Plumbline ever needs it.

**2. Claude Code shipped a real setup-checkup tool + in-app browser (v2.1.202–206, Week 28)**
[code.claude.com — What's new, Week 28](https://code.claude.com/docs/en/whats-new/2026-w28) · 2026-07-06–10
`/doctor` (alias `/checkup`) is no longer read-only — it now diagnoses unused skills/MCP servers/plugins by context cost, dedupes `CLAUDE.md` against checked-in versions, and flags slow hooks, asking for confirmation before changing anything. Desktop also got a sandboxed in-app browser, and auto mode now blocks tampering with session transcripts.
**Why it matters to Ali:** `/doctor` is directly useful for trimming the asam repo's own accumulating `CLAUDE.md`/skill/MCP footprint — worth running once as a checkup on this repo.

**3. Microsoft ships an Agent Framework for Go (public preview) — with Anthropic as a first-class model provider**
[devblogs.microsoft.com — Microsoft Agent Framework for Go, public preview](https://devblogs.microsoft.com/go/microsoft-agent-framework-for-go-public-preview/) · 2026-07-10
Multi-agent workflows, tool/MCP support, routing, checkpoints, and OpenTelemetry tracing, in Go — supporting Microsoft Foundry, Azure OpenAI, **Anthropic**, Gemini, and A2A as providers.
**Why it matters to Ali:** signals language diversification in the agent-framework space beyond Python/TS — worth knowing if any future Plumbline backend service that talks to Claude gets built in Go.

**4. Anthropic enters K-12 education directly — free Claude for Teachers + curriculum-standards integration**
[anthropic.com/news — Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers) · 2026-07-14
Free through June 2027 for verified US K-12 teachers: lesson planning aligned to all-50-state academic standards ("Learning Commons"), class-data analysis via Claude Code, and an **open-source repo of teaching skills** for other ed-tech builders. Excludes students; piloting with Detroit Public Schools.
**Why it matters to Ali:** this is Anthropic building education-specific data models (standards alignment, teacher workflows) directly — a useful competitive read for how Plumbline should think about its own higher-ed-specific data layer, even though this launch targets K-12 not small colleges.

**5. LM Studio ships a self-hosted, privacy-first agent app — LM Studio Bionic**
[lmstudio.ai — Introducing LM Studio Bionic](https://lmstudio.ai/blog/introducing-lm-studio-bionic) · 2026-07-16
A separate app from LM Studio proper: agentic coding help, document/spreadsheet work, and voice dictation, running fully local or via "LM Studio Secure Cloud" open models, with a zero-data-retention commitment.
**Why it matters to Ali:** a concrete example of a fully local, privacy-first agent app — relevant given your Docker/NAS self-hosting habits, and a pattern worth studying if Plumbline ever needs agent features that can't touch FERPA-covered student data over the network.

## Worth a session this week

**#1 — the MCP 2026-07-28 Release Candidate.** It's the most consequential item here: it ships in 11 days, deprecates protocol features (Roots/Sampling/Logging) outright, and changes the transport model (stateless core). If any current or planned Plumbline integration touches MCP, this is the one to actually sit down and read before it locks.

## Also on the radar (not ranked — outside strict window or thinner signal)

- **Claude Cowork expands to mobile/web** for Max subscribers — [TechCrunch, 2026-07-07](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/) — 3 days before this run's window, flagging for continuity since it directly touches your stack. Anthropic noted software dev is only 8.7% of Cowork usage — it's being pushed as a general knowledge-work agent, not a coding tool.
- **X ships a hosted MCP server** (`api.x.com/mcp`, 200+ endpoints: search, trends, post/bookmark management) — [X Developers announcement](https://x.com/XDevelopers/status/2071752389183647758) — June 30, outside window, mentioned as background since it's a concrete example of a major platform standing up MCP infrastructure.
- **X discussion (via fallback — no live API credit, web-search only):** the X MCP server launch got positive developer reception (2.8M views in its first day per TechCrunch coverage); Cowork's mobile expansion is generating comparison-piece coverage but not much organic X discussion yet.
- HN this week was heavy on low-signal "Show HN" agent-tooling posts (agent memory CLIs, agent orchestration wrappers, security-monitoring launches) mostly sitting under 10 points — treated as noise/star-farming risk rather than picks; none had enough independent traction to include.
