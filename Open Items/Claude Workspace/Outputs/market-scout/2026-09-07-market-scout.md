# Market scout — 2026-09-07

_Lookback: 2026-08-25 → 2026-09-07 (13 days — the Sep 1 and Sep 4 runs did not land, so this digest covers the full gap). Sources: GitHub (Composio, authenticated), HN Algolia, anthropics/claude-code CHANGELOG, SerpAPI (4 of 6 calls: 2 Google News, 2 X via site:x.com). Readwise Reader: still only onboarding docs — skipped. Deduped against seen-index._

## Ranked picks

### 1. Claude Fable 5.1 + Mythos 5.1 — and Fable 5.1 is now the Claude Code default
[anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1) · [HN 1,415 pts](https://news.ycombinator.com/item?id=49525378)
Announced Sep 1. Claude Code v2.1.257 makes `claude-fable-5-1` the default Fable model: 1M context, $10/$50 per Mtok, $0.25/Mtok cache reads. Same week, Anthropic shipped [a Claude-formalized proof of Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) and [autonomous lab-equipment control](https://singularityhub.com/2026/09/04/anthropics-claude-can-now-autonomously-run-science-experiments-with-lab-equipment/) as capability demos.
**Why it matters to Ali:** your entire task fleet runs on Fable. The default likely already moved under you — 1M context changes what a single scheduled session can hold (whole OS files + transcripts), and the cache-read price changes fleet economics. Worth checking which model your routines actually resolved to this week.

### 2. Agent security had a very bad two weeks — auto mode, Postgres MCP, and a real AI breakout
[Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) ([HN 399 pts](https://news.ycombinator.com/item?id=49506819)) · [Postgres MCP Pro restricted-mode bypass](https://forkast.news/postgres-mcp-pro-restricted-mode-bypass-exposes-the-gap-in-ai-database-security/) · [Anthropic admits security failures behind Claude hacking incidents](https://decrypt.co/377232/anthropic-security-claude-ai-hacks) · [OpenAI agents hijacked German website](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/)
Rehberger's embracethered post demonstrates prompt-injection paths that get Claude Code auto mode to approve exfiltration; Anthropic's response was the new auto-mode "Containment Escape" rule in v2.1.257. Separately, a Postgres MCP server's restricted mode was bypassed, and Reuters reports a previously undisclosed incident of OpenAI agents defacing a live site.
**Why it matters to Ali:** you run unattended auto-mode-adjacent agents with credentials to Postgres (Meridia), QuickBooks, and Dropbox. The Postgres MCP bypass is your exact architecture. A quick pass over which of your routines hold write credentials — and whether restricted/read-only modes are load-bearing — is cheap insurance.

### 3. Claude Code v2.1.246–263 release radar: /skill-doctor, managedMcpServers, model-switch hooks
[CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
Densest run of ops-relevant releases in months: `/skill-doctor` (shows which loaded skills go unused and their context cost), `/diff` side panel, `managedMcpServers`, `--restricted` mode, `--permission-prompts none` for unattended hosts, `PreModelSwitch`/`PostModelSwitch` hooks, prompt-cache miss diagnostics in `/cost`, per-agent `cacheTtl`, and the Fable 5.1 default (v2.1.257).
**Why it matters to Ali:** your sessions load a very large skill/plugin roster; `/skill-doctor` was practically built for you. `PreModelSwitch` hooks also give you a guardrail for the silent default-model change in pick 1.

### 4. GLM-5.3 goes open-weight; GLM-5.3-Flash tops the small-model tier
[GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) ([HN 1,132 pts](https://news.ycombinator.com/item?id=49449507)) · [GLM-5.3 weights on HF](https://huggingface.co/zai-org/GLM-5.3) ([HN 805 pts](https://news.ycombinator.com/item?id=49479878))
Z.ai released GLM-5.3 weights and a Flash variant that HN consensus treats as the strongest openly runnable agentic model of the cycle; Cloudflare was already running GLM at scale (seen 08-04). Related: [Nvidia agreed to acquire Hugging Face (~$13B)](https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html) — the neutral home of open weights now belongs to the GPU vendor.
**Why it matters to Ali:** first open-weight tier that plausibly handles real agent work on owned hardware — relevant to your Docker/NAS lane as a fallback when Anthropic has weeks like Sep 3's [multi-provider outage](https://news.ycombinator.com/item?id=49551096). The HF acquisition is worth watching for what it does to open-weight distribution.

### 5. lemmalog — a Datalog engine as agent memory, exposed over MCP
[github.com/JordyZomer/lemmalog](https://github.com/JordyZomer/lemmalog) (288★, created 08-27)
Stratified rules, provenance-tracked facts, incremental derivation — a real reasoning substrate rather than another notes-file. Credible author (Google security researcher). This is the most substantive entry yet in the agent-memory thread you've been tracking (kaas, memory-forest, cost-of-remembering, stalebrain).
**Why it matters to Ali:** your OS-file pattern is exactly "facts + provenance that survive resets." A Datalog layer that agents query over MCP is a plausible next form of MASTER.md-style state — worth a look even if only to steal the provenance model.

## Worth a session this week
**Fleet ops pass on the new Claude Code tooling (picks 1–3 together):** one session to (a) confirm which model each scheduled routine now resolves to post-Fable-5.1-default, (b) run `/skill-doctor` and prune the skill roster your sessions carry, and (c) audit unattended routines' credentials against the auto-mode/Postgres-MCP findings — flip anything that can be read-only to read-only. One sitting, three compounding payoffs.

## Also noted
- [Spotify's Portal cut Claude Code token usage 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90) ([HN 270](https://news.ycombinator.com/item?id=49571465)) — tool-proxy pattern you could copy for Composio-heavy sessions.
- [cbrock84/headcount](https://github.com/cbrock84/headcount) (1.3k★) — "agent org as a company" for Claude Code, 125+ skills; overlaps skills-scout beat but marketplace-level.
- [2akouwu/reverify](https://github.com/2akouwu/reverify) (1k★ in a week — star-velocity caution) and [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) (660★) — verification and continual-learning infra; unvetted.
- [Continuum-AI-Corp/OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) — record/replay/fork agent runs; [useagenthq/useagent](https://github.com/useagenthq/useagent) — open-source Cowork competitor.
- [Armature: 17k runs measuring which tools coding agents install](https://armature.tech/blog/which-tools-coding-agents-install) ([HN 296](https://news.ycombinator.com/item?id=49557206)).
- [claude.com/check-content](https://claude.com/check-content) — public checker for Claude-watermarked files ([CNET on the catch](https://www.cnet.com/tech/services-and-software/anthropics-content-checker-tool-is-here-with-one-big-catch/)); follow-on to the Aug watermarking story.
- [DocuSign opens its MCP server to every AI agent](https://finance.yahoo.com/technology/ai/articles/docusign-docu-opens-mcp-server-021223276.html) and [Snowflake's enterprise MCP-gateway guide](https://www.snowflake.com/en/blog/engineering/enterprise-mcp-gateway-ai-agent-governance/) — MCP consolidating as the enterprise integration surface (Google News via SerpAPI).
- [Anthropic opens real Claude usage data to outside researchers](https://www.edtechinnovationhub.com/news/anthropic-opens-real-claude-usage-data-to-outside-researchers-for-fir) (via SerpAPI).
- X via SerpAPI: [@nutlope's design MCP server for coding agents](https://x.com/nutlope/status/2095890193957962077) · [Baseten's remote MCP + skill launch](https://x.com/saimaddali/article/2095497965230010863) · [testingcatalog: Claude Hub → Early Access, Managed Projects coming to Claude Code](https://x.com/testingcatalog/status/2094441489124200826).
