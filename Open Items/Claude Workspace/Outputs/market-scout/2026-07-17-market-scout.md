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
