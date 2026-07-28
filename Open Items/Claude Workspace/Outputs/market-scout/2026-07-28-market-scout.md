# Market scout — 2026-07-28 (Tue run, covering Sat 07-25 → Mon 07-27)

_Sources: GitHub via Composio connector (topic + release radar), HN Algolia, SerpAPI (news + X via site:x.com). Deduped against seen-index. SerpAPI: 4/6 calls used._

## Ranked picks

### 1. Claude Opus 5 — new default Opus, 1M context, fast mode
Anthropic shipped Opus 5 on Jul 24 (post-cutoff of the last run): new state-of-the-art on coding/knowledge-work evals, 1M-token context, fast mode at $10/$50 per Mtok, same price as Opus 4.8, default on Max, and defaults to **high effort** in Claude Code (v2.1.219 makes it the default Opus there). Anthropic followed up with ["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) (458 pts on HN) — concrete guidance on how prompting/context habits should change for the 5-gen models.
- Announcement: https://www.anthropic.com/news/claude-opus-5 · [HN thread, 1777 pts / 1323 comments](https://news.ycombinator.com/item?id=49038433)
- Claude Code v2.1.219 notes (Opus 5 default, `sandbox.network.strictAllowlist`, `DirectoryAdded` hook): https://github.com/anthropics/claude-code/releases/tag/v2.1.219
- Caveat: three "elevated errors on Opus 5" incidents Jul 26–27 ([1](https://status.claude.com/incidents/zftg3gqkmv18), [2](https://status.claude.com/incidents/lhqp09kxq7pb), [3](https://status.claude.com/incidents/mfdtrknpxghq)) — launch-week capacity wobble; don't judge it by this week's latency.
- Independent read: [TheZvi's system-card review](https://x.com/TheZvi/article/2081021049475391730) (X via SerpAPI) — biggest gains in agentic coding, computer use, long-horizon tasks; [Arena placement](https://x.com/arena/status/2081831019377004727): #1 Frontend Arena at max reasoning.

**Why it matters to Ali:** this is the model family under your Cowork/Code sessions. 1M context + a cheap fast mode changes what's practical for Populi/Plumbline data work — whole-schema or whole-repo context without RAG plumbing — and the context-engineering post is the vendor telling you which prompting habits to drop.

### 2. MCP 2026-07-28 spec goes stable **today** — sessions removed
The stable release of the 2026-07-28 MCP revision lands today; press is framing it as "MCP's largest spec change since launch" (stateless core / sessions dropped). The RC was covered in prior digests — what's new is the adoption clock starting: SDKs and hosted servers will begin migrating, and TechTarget's piece argues all agentic data access/orchestration now hinges on MCP + A2A.
- https://www.techtimes.com/articles/321671/20260727/ai-tool-protocol-drops-sessions-tomorrow-mcps-largest-spec-change-sin (via SerpAPI)
- https://www.techtarget.com/searchcustomerexperience/news/366646258/All-agentic-AI-data-access-orchestration-hinges-on-th (via SerpAPI)
- Release tag (RC → watch for stable tag today): https://github.com/modelcontextprotocol/modelcontextprotocol/releases

**Why it matters to Ali:** any MCP servers you run or build (NAS/Docker, Postgres, QuickBooks bridges) will see SDK churn over the next weeks; stateless core also makes serverless/cheap hosting of your own servers simpler.

### 3. Azure DevOps MCP flaw: hidden PR comments hijack AI review agents
The Hacker News (Jul 22, unsurfaced in prior runs): a flaw in Microsoft's Azure DevOps MCP server let hidden PR comments steer AI code-review agents — a working exploit of the "agent reads attacker-controlled text through a trusted tool" class, following last week's fake-GitHub-repos-lure-agents item. The agent-security beat is now producing real CVE-grade artifacts, not thought pieces.
- https://thehackernews.com/2026/07/microsoft-azure-devops-mcp-flaw-lets.html (via SerpAPI)
- Related market signal: NVIDIA formed a 37-member Open Secure AI Alliance and open-sourced its NOOA agent-security framework (Jul 27) — with major frontier labs sitting out: https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html · https://www.techrepublic.com/article/news-nvidia-open-secure-ai-alliance/

**Why it matters to Ali:** you run review/coding agents against GitHub with write access — untrusted-content injection via PR comments/issues is exactly the vector to sandbox (Claude Code's new `strictAllowlist` setting in v2.1.219 is a direct mitigation lever).

### 4. deerwork-ai/deer-workflow — graph runtime that keeps orchestration in code, agents replaceable
New repo (Jul 26) at ~308★/23 forks in two days: an open-source "graph engineering runtime" where orchestration stays in deterministic TypeScript and semantic work is delegated to swappable agent runtimes (Claude Code, Codex, etc.). Same thesis as Cowork's Workflow tool — deterministic control flow, model-driven leaves — but as a standalone OSS runtime. Star-velocity caution applies (two days old), but the artifact is real.
- https://github.com/deerwork-ai/deer-workflow

**Why it matters to Ali:** it's the pattern you'd want for repeatable Populi/QuickBooks pipelines — deterministic graph, replaceable agent per node — worth skimming the design even if you never adopt it.

## Worth a session this week
**Switch a real task to Opus 5 in Claude Code (`/model claude-opus-5`) and read the context-engineering-for-Claude-5 post first.** One session, two payoffs: you find out what high-effort-by-default + 1M context does to a Plumbline-sized job, and you recalibrate prompting habits against the vendor's own guidance while the model is new.

## Also noted (below the line)
- Salesforce launched MCP servers to turn Slack into an AI workspace (Jul 24) — enterprise MCP adoption datapoint: https://cloudwars.com/cloud-wars-minute/salesforce-launches-mcp-servers-to-turn-slack-into-an-ai-workspace/
- Claude Code v2.1.220 (Jul 25): bug fixes only — https://github.com/anthropics/claude-code/releases/tag/v2.1.220
- `0xwilliamortiz/openclaude-improved` hit 577★ in a day with a no-content description — pattern-matches star-farming/lure repos (see Jul 24 malware item); deliberately not picked.
- X layer labeled "X via SerpAPI" throughout; HN via Algolia API; no Plumbline/higher-ed-SaaS signal this window.
