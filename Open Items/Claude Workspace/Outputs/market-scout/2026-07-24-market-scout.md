# Market scout — 2026-07-24 (Fri)

_Lookback: since the 2026-07-23 run (short window — an off-schedule run happened yesterday). Layers: GitHub topic/created searches + release radar (Composio), HN Algolia, Anthropic news, X via SerpAPI, Google News via SerpAPI (4/6 SerpAPI calls used)._

## Ranked picks

### 1. OneCLI — OSS credential gateway that keeps secrets out of AI agents ⭐ worth a session this week
[github.com/onecli/onecli](https://github.com/onecli/onecli) · [onecli.sh](https://onecli.sh/) · [HN (101 pts)](https://news.ycombinator.com/item?id=49023427)
A network gateway that sits between agents and the services they call: the agent only ever holds a placeholder; OneCLI matches request host/path, checks the agent's authorization, swaps in the real credential, and forwards. Secrets never enter the agent's context or logs.
**Why it matters to Ali:** your scheduled agents currently do .env-shuffling gymnastics (Dropbox key fetch → shell var → never print) — this kills that entire risk class at the network layer, it's self-hostable (NAS/Docker-friendly), and it's the OSS counterpart to the 1Password zero-exposure item surfaced 07-17. Session shape: run it in Docker, put the SerpAPI + one low-stakes key behind it, point a Claude Code session at it. Caveat: day-old repo — sandbox first.

### 2. Claude Cookbook — official Anthropic recipe hub
[platform.claude.com/cookbook](https://platform.claude.com/cookbook/) · [HN (98 pts)](https://news.ycombinator.com/item?id=49031409)
Anthropic consolidated its build-with-Claude recipes into a first-party cookbook on the platform site — agent patterns, tool use, memory, RAG, evals.
**Why it matters to Ali:** cheapest way to pressure-test whether the patterns in your scheduled jobs (memory files, tool loops, orchestration) match Anthropic's current recommended shapes before you build more on top of them.

### 3. Echo — open-weight model pool claiming Fable-level results at 1/3 cost
[echo.tracerml.ai](https://echo.tracerml.ai/) · [Show HN (397 pts, 49 comments)](https://news.ycombinator.com/item?id=49026810)
Routes/combines a pool of open-weight models (GLM-5.2, Kimi K2.7, others) per-task instead of picking one model; claims the ensemble beats any single member and approaches frontier quality at a third of the price.
**Why it matters to Ali:** third data point in two weeks (Kimi K3 on 07-23, Cursor's "agent swarms and the new model economics" on 07-23) that open-weight routing is compressing frontier pricing — relevant to what Plumbline's eventual per-seat AI costs look like. Skeptic flag: self-reported evals, Show HN post, no independent benchmark yet.

### 4. Fake GitHub repos are luring AI agents into malware
[techzine.eu (Jul 22)](https://www.techzine.eu/news/devops/143078/fake-github-projects-lure-ai-agents-into-malware/)
Documented campaign of GitHub projects crafted so that agentic coding tools (not just humans) clone and execute malicious code — star-farming plus README instructions aimed at the agent.
**Why it matters to Ali:** your scouts surface young, unvetted repos weekly (including this digest). Adopt a standing rule: new repos get cloned and run only in a throwaway sandbox/worktree, never on the NAS, and never with real credentials — which is also pick #1's argument.

### 5. finna/Finn-loop — a 3-skill "software factory" for Claude Code
[github.com/finna/Finn-loop](https://github.com/finna/Finn-loop) — 174★/27 forks within ~48h of creation (07-22)
Spec → build → review as three chained Claude Code skills; humans only merge. The most concrete public artifact yet of the "factory loop" pattern.
**Why it matters to Ali:** it's roughly the pipeline you run by hand across sessions — worth skimming the skill files for structure to steal, even if you don't adopt it. Star-velocity caution applies (see pick #4).

## Watchlist (one-liners)
- **MCP 2026-07-28 goes stable next Tuesday** — [The Register on the stateless break (Jul 23)](https://www.theregister.com/devops/2026/07/23/model_context_protocol_prepares_to_break/); RC was surfaced 07-17 — expect connector churn the week after.
- [Screenpipe (YC S26)](https://news.ycombinator.com/item?id=49024620) — records how you work and turns it into agents (Launch HN, 79 pts).
- [surya-koritala/sigbound](https://github.com/surya-koritala/sigbound) — parallel coding agents on one repo; only changes that build+pass tests auto-merge.
- [VinvAI/VinvAI](https://github.com/VinvAI/VinvAI) — "your agent says it's done, Vinv says prove it" — closed-loop verification served over MCP.
- [hyungchulc/memory-forest](https://github.com/hyungchulc/memory-forest) — verifiable local memory architecture for long-running agents.
- X signal (via SerpAPI): [@claudeai "New in Claude Cowork"](https://x.com/claudeai/status/2079595988998554047) and [lawrencecchen's "Superrepos" worktree piece](https://x.com/lawrencecchen/article/2080441004881215520) are the two highest-signal posts of the window.
- Anthropic news this week was economics-research focused ([Economic Futures research agenda, Economic Index connector](https://www.anthropic.com/news)) — no product capability change.
- **Plumbline/higher-ed layer: nothing new this window** (Google News sweep returned only items from earlier months).

## Method notes
SerpAPI available and used (X via SerpAPI worked — no login-wall fallback needed). Claude Code release radar: latest is still v2.1.218 (Jul 22), already covered in the 07-23 run. vercel-labs/skills still at v1.5.20 (seen).
