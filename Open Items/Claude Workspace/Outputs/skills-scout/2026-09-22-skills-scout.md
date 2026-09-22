# Skills Scout — 2026-09-22

_Scan window: since the 2026-09-21 digest (~last 24-48h). SerpAPI available and used (3-call budget: 2 productive qdr:d queries, 1 returned empty). Sources per skills-scout-sources.md; GitHub recency sweep via Composio._

## Official / Tier 1
- **Quiet lane — no new Anthropic motion since yesterday's digest.** Claude Code latest remains v2.1.278 (Sep 19, already surfaced); `anthropics/claude-plugins-official` last commit is Sep 18 (#6257 Qodo/Airwallex metadata, #6258 Wingspan — surfaced 09-19); `anthropics/skills` last commit Sep 10 (#1750, surfaced 09-12). Weekend press (ExtremeTech 09-21 etc.) is recycled coverage of the Sep 16 Cowork→Claude merge. Trust: Anthropic-verified (checked repos + releasebot + changelog directly).

## Skills & plugin ecosystem (Cowork / Claude Code / curation lanes)
- **microsoft/azure-skills** — official Microsoft plugin repo of Agent Skills + MCP server configurations for Azure scenarios (e.g. microsoft-foundry skill). Distinct from `microsoft/skills` (surfaced 08-17). Matters: the vendor-skills wave now has per-cloud official repos; relevant if any venture lands on Azure services, and as the reference shape for vendor skill+MCP pairing. Trust: Tier 2 (official Microsoft org).
- **K-Dense-AI/claude-skills-mcp** — MCP server that vector-searches and serves their 38k★ Scientific Agent Skills library on demand. Matters: cleanest working example yet of "skills discovery/distribution over MCP" — the exact direction of the `modelcontextprotocol/ext-skills` WG (surfaced 09-05); pattern applies to serving Ali's own skill fleet without context bloat. Trust: Tier 2/3 (known org behind the library surfaced 08-30).
- **Snow7-G/SkillSeam** — simulates how an agent picks among installed skills and shows which skill "steals" whose tasks before users hit it; works with any SKILL.md runtime. Matters: skill-triggering overlap is a real failure mode in a ~50-skill fleet like Ali's (e.g. three prompt-optimizer variants live now). Day-one repo. Trust: Tier 4 — unknown author, inspect before running.
- **wasd96040501/taskcut** — Claude Code plugin that compacts the conversation at sub-task boundaries instead of at the context limit. Matters: complements the Messages API on-demand compaction beta (surfaced 09-16) with an in-session discipline; cheap to trial on long Cowork sessions. Trust: Tier 4, new repo.
- **tomsen02/oss-audit** — agent skill that evaluates a GitHub project from an outside contributor's perspective, with a read-only collector and evidence-based methodology. Matters: near-direct overlap with the template-vetting workflow (keep/mine/discard); worth mining its evidence rubric even if not adopted. Trust: Tier 4.
- **iliasabk/claude-plugins-radar** — "live, hand-curated, machine-readable directory of Claude Code plugins, skills and agents," actively pushed. Matters: candidate Tier 2/3 addition to skills-scout-sources.md if it proves durable; low stars so far. Trust: Tier 4 until track record.
- **Caution — subscription-piggyback wave**: `NousResearch/hermes-plugin-claude-subscription-directsdk` (drive Claude Pro/Max subscription from Hermes Agent via the official CC CLI, "experimental") and `gabyic/agentdock-mcp-harness` (use ChatGPT/Claude web quota for remote coding). Matters as an ecosystem signal: third-party agents tunneling through consumer subscriptions is ToS-gray and a likely enforcement target — don't build on it. NousResearch is a known org, which makes the normalization notable. Trust: Tier 3 org / Tier 4 pattern — avoid.
- **Caution — SEO-farm "awesome-list" flood**: a batch of same-shaped gh-pages repos bulk-created 09-21 across fresh orgs (`token-counter/awesome-claude-code-github`, `heygen-mcp/awesome-blader-humanizer`, `grok-cli/claude-code-github-examples`, `x-api-dev`, `taplio-dev`, `blotato-dev`…), each ~10★ overnight. Same shape as the genpark flood (flagged 09-03). Treat unfamiliar "awesome claude" lists from young orgs as marketing surface, not curation. Trust: Tier 4 signal.

## Dev / agent tooling — decision-model ecosystem
- **Laya — open-source decision-model wave** (`wdobry/laya-playground` ~97★ d1: site, games, benchmark + agent skill; `neko233-com/laya-go`: Go server + agent CLI/MCP "replacing Jev"; `wsargent/laya-mcp`: local MLX inference on Apple Silicon). Matters: the answer wave to TypeSafe's commercial Jev (surfaced 09-20) arrived within a week — open, local, "horizontal System 1" typed-decision models. If typed sub-second decisions ever enter Aegis/Hypomone gating logic, the open local option changes the build calculus vs a paid API. Trust: Tier 3/4 — young repos, real momentum; the Jev repo flood itself continues (increments logged, not repeated here).

## Aegis — governance, audit, approval patterns
- **Patsakas/mcp-governance-layer** — a policy-enforcement MCP layer that sits between agents and the systems they can damage: suspends risky tool calls and routes them to a human verdict. Matters: this is the Aegis governance-alert/approval pattern implemented at the MCP boundary — worth reading the policy model even at ★2. Trust: Tier 4, day-old.
- **NextEpochs/opifer** — agents run "like an organisation": org chart, budgets reserved before every call, one database, one interface, governed learning. Matters: budget-reservation-before-action is a governance primitive Aegis's approval flow doesn't have yet. Trust: Tier 4.
- **elementalsouls/Claude-BugHunter** — plain Agent Skills for bug-hunting workflows with optional Burp Suite MCP wiring (`--burp-mcp`). Matters: offensive-security skill packs keep maturing (Trail of Bits lineage, surfaced 08-05); relevant to how Aegis-side security review gets tooled. Trust: Tier 4 — security tooling, sandbox and inspect first.

## Meridia / Hypomone — fintech & lending data
- Lane quiet this window: nothing new at Tier 1/2. The pgEdge "MCP Server GA" press resurfacing in search is dated April 2026 (pgEdge surfaced 06-21). One Hypomone-adjacent increment (Argentine bank-statement→CSV plugin with balance reconciliation) logged to the skipped log against bank-statement-to-table (09-09).

## Recess — K-12 education
- Lane quiet this window: no new education skills/MCP items beyond yesterday's bb-mcp (LMS-MCP pattern, 09-21). Education press in search is July-era Claude for Teachers coverage, all previously surfaced.

## Populi / Postgres / NAS ops
- Lane quiet this window: no new Postgres/SIS MCP motion; searched directly (Glama/PulseMCP roundups list only previously-surfaced servers).
