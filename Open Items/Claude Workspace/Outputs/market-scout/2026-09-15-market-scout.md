# Market scout — 2026-09-15 (Tue run; lookback Sep 8–15)

_Sources: GitHub topic searches + release radar (Composio connector), HN Algolia, Google News + X via SerpAPI (4 of 6 calls used). Readwise: no saves since Sep 8 — skipped. Focus file honored; skills-scout beat (skills/plugin/MCP directories) excluded._

## Ranked picks

### 1. Anthropic ships "Claude for Financial Advisors" — as an open Cowork plugin
- Repo: [anthropics/claude-for-financial-advisors](https://github.com/anthropics/claude-for-financial-advisors) (created Sep 14) — "a Claude Cowork plugin with ready-to-run workflows for financial advisors." Coverage: [Barron's (Schwab partnership)](https://www.barrons.com/articles/anthropic-charles-schwab-claude-for-financial-advisors-630ea9a9), [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-deploys-claude-automate-financial-adviser-prep-work/).
- **Why it matters to Ali:** This is Anthropic's template for vertical AI products: a domain plugin (workflows + skills + connectors) on top of Cowork, not a new app. It's the closest public analog yet to what Plumbline would be for small-college ops (SIS overlays, Populi/QuickBooks workflows) — and the repo is public, so the packaging pattern is inspectable end to end.

### 2. Skills over MCP — SEP-2640 v1 spec text lands in an official working group
- [modelcontextprotocol/ext-skills](https://github.com/modelcontextprotocol/ext-skills) (558★) is now the Skills Over MCP WG incubator; [SEP-2640](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2640) is the source-of-truth v1 spec for skills discovery/distribution through MCP primitives. Active pushes through Sep 14.
- **Why it matters to Ali:** If skills become an MCP-native primitive, every skill in his fleet (and any Plumbline skill pack) gains a standard distribution channel — the same shift MCP itself caused for tools. Marketplace-level mover; per-item vetting stays with the skills scout.

### 3. Agent audit/governance layer hardens — open-source and enterprise at once
- New repos this week: [Shalimov04/mcp-airlock](https://github.com/Shalimov04/mcp-airlock) (stateless governance proxy targeting the 2026-07-28 MCP spec: policy, dry-run, human confirmation, audit), [FankChen/tracecrate](https://github.com/FankChen/tracecrate) (local-first trace workbench for Claude Code/Codex/OTLP logs), [Matthew0822/ToolReplay](https://github.com/Matthew0822/ToolReplay) (hash-chain-sealed tool-call transcripts + deterministic replay; 168★ in a day — star-velocity caution). Enterprise side, same week: [Oracle Integration MCP Gateway](https://blogs.oracle.com/integration/introducing-oracle-integration-mcp-gateway-governed-access-for-enterprise-ai-agents), [Harness report: agent confidence isn't backed by controls](https://www.prnewswire.com/news-releases/new-harness-report-reveals-enterprise-confidence-in-ai-agents-isnt-backed-by-real-control), [Cymphony $30M](https://www.newswire.com/news/cymphony-launches-with-30-million-to-secure-ai-agents-access-to-22857048).
- **Why it matters to Ali:** The market is converging on "agents need an audit trail and a policy gate," which is exactly the weak spot of a multi-lane task fleet like his. tracecrate (local-first, no backend) is the one worth a look for inspecting his own Claude Code/Cowork session logs.

### 4. Claude Code v2.1.265–272: plugin eval suites, fast mode in cloud sessions
- [Releases](https://github.com/anthropics/claude-code/releases), Sep 8–15: `claude plugin eval` (scored, reproducible eval suites for plugins, JSON+HTML reports, v2.1.269), fast mode in Remote/cloud sessions via `/fast` (v2.1.271), `maxEffortLevel` setting (v2.1.267), Bash edit diffs in tool results, and a fix for **Cowork scheduled tasks in the cloud failing at startup under sandboxing-required managed settings** (v2.1.267).
- **Why it matters to Ali:** Plugin eval is the missing QA harness for his skill/plugin factory — regression-test a skill the way code gets tested. The scheduled-task fix and fast mode land directly on the fleet this scout runs in.

### 5. Agent-misuse drumbeat gets louder (context for policy + client conversations)
- [Anthropic threat intelligence report, Sept 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) (Houthi missile-guidance attempt, bioweapons/cyber-espionage disruptions; [HN](https://news.ycombinator.com/item?id=49684266)) · [OpenAI agents' undisclosed "attack" on RubyGems](https://www.rubyhack.ai/) ([HN 964](https://news.ycombinator.com/item?id=49666735)) · [Bengio: "Why are AI agents lying, cheating and coordinating?"](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating) ([HN 649](https://news.ycombinator.com/item?id=49678969)).
- **Why it matters to Ali:** No adoption action, but this is the backdrop for item 3 — misuse reports are what turn audit/governance tooling from nice-to-have into procurement requirement, including for higher-ed IT committees.

## Worth a session this week
**Clone and dissect [anthropics/claude-for-financial-advisors](https://github.com/anthropics/claude-for-financial-advisors).** Map its plugin structure (workflows, skills, connector assumptions) and sketch the Plumbline/Turner equivalent — "Claude for Small-College Operations" — reusing the exact packaging. One session: read the repo, list what transfers 1:1, note what higher-ed needs that finance didn't.

## Also noted (no action)
- [Siri code shows Claude/ChatGPT swappable as backend](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/) ([HN](https://news.ycombinator.com/item?id=49695409)) — consumer distribution signal.
- [Google opens Claude to all engineers](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) — adoption signal, no artifact.
- [Kerneta/daidocs](https://github.com/Kerneta/daidocs) — open plain-text `.dai` format for portable AI memory; continues the OKF-style portable-memory wave. Small, watch.
- [vercel-labs/skills v1.5.25–26](https://github.com/vercel-labs/skills/releases) — maintenance (JSON output flag, agent coverage fixes).
- [Dario Amodei, "We Must Pace the Frontier"](https://darioamodei.com/post/we-must-pace-the-frontier) — policy essay, discussion only.
- HasData published ~10 near-identical scraper MCP servers in one week (Yelp/Walmart/Redfin/etc.) — coordinated marketing flood, not picked.
- XDA re-covered Anthropic's [400k Claude Code sessions study](https://www.anthropic.com/research/claude-code-expertise) — study itself is from June; not new.
