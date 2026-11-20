# Market scout — 2026-11-20 (Fri)

_Lookback: Tue 2026-11-17 → Thu 2026-11-19, plus early Fri. Sources: GitHub search (Composio), HN Algolia, Claude Code CHANGELOG, Google News + X via SerpAPI (5 of 6 calls used), Readwise Reader (nothing new saved). Items already in the seen index were dropped, and so was anything on the skills scout's beat._

**Theme of the week:** the agent supply chain and MCP keep turning out to be the weak points. A compromised Microsoft agent package, MCP servers running outside the coding-agent sandbox, and an MCP server that can now write to Azure with the user's full permissions all landed in the same three days. Vendors also started shipping "agent coordination boards" as products.

---

## Top picks (ranked)

### 1. Microsoft's `agent-framework` PyPI package was compromised with a credential stealer (Nov 17)
- Versions **1.26.1 and 1.26.2** were published with `.pth` startup hooks. (A `.pth` file is a small Python path file that runs code every time Python starts, even if you never import the package.) The hooks collected credential environment variables, config and credential files, other processes' environments, and cloud and CI identity tokens (Azure managed identity, GitHub Actions OIDC, Azure DevOps), then sent them to a `webhook.site` endpoint. Socket's advice: don't install either version, and if you did, remove it and rotate credentials. — [Socket](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer) · [The Register](https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858) · [HN](https://news.ycombinator.com/item?id=50542084)
- X via SerpAPI: Rami McCarthy [says](https://x.com/ramimacisabird) the attacker got in through compromised credentials for Microsoft's release pipeline and used an AI agent toolchain to run the attack. Treat that as **unverified** until Microsoft publishes a post-mortem.
- **Why it matters to Ali:** this is the second week in a row of supply-chain risk in the agent tooling layer. Last week Corelight found that "pinned" uvx MCP servers still pull fresh dependencies. The hub runs Python scripts (for example `sosmon/dbx.py`) and Python MCP servers on the same machines that hold the single `.env` credentials file. A `.pth` hook needs nothing more than `pip install` to run, so pinning exact versions and using a lockfile is the defense.

### 2. Claude Code 2.1.327–2.1.329: one change can silently stop scheduled tasks, plus MCP and hook hardening
- **Scheduled tasks:** *"in new signed-in sessions, most [scheduled tasks] saved by earlier versions need scheduling again."* This applies to Claude Code's own local scheduled tasks and `/loop`. It does **not** obviously apply to Cowork cloud scheduled tasks like this scout, but any Claude Code `/loop` or local schedules Ali set up should be checked.
- **MCP file fix:** PDFs, images, `.docx`, `.xlsx` and `.pptx` files that MCP servers send as `application/octet-stream` were being saved as `.bin`, so Claude couldn't read them. That's fixed, which matters for Dropbox, Drive and Populi document pulls.
- **Hooks:** the trust dialog now says where a folder's hooks are declared, and `mcp_tool` hooks gain `"onFailure": "block"` (a failing hook blocks the action instead of letting it through). `/code-review` now reports only bugs and CLAUDE.md violations, each tagged Important / Pre-existing / Nit; cleanup suggestions moved to `/simplify`.
- Source: [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **Why it matters to Ali:** the scheduled-task change is the kind that fails silently: a job simply stops running and nothing tells you. The octet-stream fix may explain past cases where a connector returned a document Claude "couldn't read."

### 3. MCP is the side door: servers sit outside sandboxes and allowlists, and now get write access
- A six-document comparison found that **Claude Code puts local MCP servers outside its shell sandbox, and Codex leaves MCP connections out of its command proxy.** So an approved MCP server can reach destinations that the agent's network allowlist was meant to block. Suggested fix: outbound network controls at a lower layer, plus managed settings that require the sandbox and a strict allowlist. — [Superpower Daily](https://superpowerdaily.com/posts/codex-and-claude-code-leave-separately-launched-tool-servers-outside-command-network-limits)
- Microsoft announced at Ignite that the **Azure Resource Manager MCP server now has write tools, and agents inherit the user's full permissions.** — [Tech Times](https://www.techtimes.com/articles/331140/20261119/azure-resource-manager-mcp-server-adds-write-tools-ignite-agents-inherit-users-full-permissions.htm). For contrast, SonarQube's hosted MCP server [added OAuth](https://securityboulevard.com/2026/11/oauth-comes-to-the-sonarqube-cloud-hosted-mcp-server/), the scoped-access pattern to look for.
- **Why it matters to Ali:** Ali's setup leans heavily on MCP (Composio, Dropbox, QuickBooks, Gusto, Populi scripts). The sandbox only protects shell commands, not the MCP servers. For financial and SIS systems, prefer read-only or OAuth-scoped connectors, and treat any write-capable MCP server as running with full access.

### 4. Agent coordination is becoming a product: Vercel Board and Mastra Factory
- **Vercel Board** (experimental, all plans, free for now) is a "headless Slack": a shared message board where agents claim tasks, post findings and track progress. Claude Code, Codex, Mastra, LangChain and others can use it through the Vercel CLI or JS SDK, and it syncs with Slack and GitHub. The article doesn't mention MCP or an open-source release. — [The New Stack](https://thenewstack.io/vercel-board-agent-swarms/)
- **Mastra Factory** (open source) is the "software factory" Mastra uses to maintain its own TypeScript agent framework. It's an agent kanban board you can @-tag in Slack, with durable agents, conversational memory, markdown wikis, signals from PR comments, and a cloud sandbox. HN critics argued it's ordinary development with agents doing the work, and that the board could get absorbed into Claude itself. — [Show HN](https://news.ycombinator.com/item?id=50548660) · [repo: mastra-ai/template-factory](https://github.com/mastra-ai/template-factory)
- **Why it matters to Ali:** this is the same pattern as Ali's MASTER.md lane registry and task fleet: a shared board that stateless workers read from and write back to. Mastra Factory is a working open-source reference to compare against (wiki memory plus a kanban plus Slack intake). The sensible move is to borrow ideas, not migrate. A Vercel dependency doesn't fit a NAS/Docker stack.

### 5. Higher-ed adjacent (Plumbline watch): agentic AI moves into student lifecycle platforms
- **Element451** joined the "Connected Campus" ecosystem, bringing agentic AI engagement across the student lifecycle. — [PR Newswire](https://www.prnewswire.com/news-releases/element451-joins-the-connected-campus-ecosystem-extending-agentic-ai-engagement-across-the-student-lifecycle-302939419.html) (Nov 16, just before the window; not in the seen index)
- **McGraw Hill**'s first investor day since its IPO pitched an agentic AI strategy with 5–8% annual growth targets through 2030. — [MLQ.ai](https://mlq.ai/news/mcgraw-hill-targets-5-to-8-annual-revenue-growth-through-2030-and-pitches-an-agentic-ai-strategy-at-its-investor-day/)
- **Why it matters to Ali:** large vendors are packaging "agents across the student lifecycle" for big institutions. Small schools on Populi-class SIS systems are still left out, which is the gap Plumbline aims at. These are positioning signals, not artifacts, so rank them low.

---

## Worth a session this week
**Supply-chain and MCP side-door audit of the hub (picks 1 and 3).** In about one focused session:
1. List every Python package, uvx/npx MCP server and script that runs on Ali's machines and NAS.
2. Pin exact versions with a lockfile, and confirm nothing pulls `agent-framework` 1.26.1/1.26.2.
3. Flag each MCP connector as read-only or write-capable, and as OAuth-scoped or full-permission.
4. Decide which machines are allowed to hold the hub `.env` file.

Deliverable: a one-page "connector trust register" in the asam repo that future scouts and the os-architect skill can check against. If Ali also runs Claude Code `/loop` or local schedules, re-check them during the same session (pick 2).

---

## Also noted (not ranked)
- **Anthropic's Nasdaq debut and IPO pricing:** big headline, but no change to what Ali can build. — [Reuters](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) · [Anthropic](https://www.anthropic.com/news/anthropic-prices-initial-public-offering) · counterpoint: [coalition challenge to Anthropic's safety branding](https://www.businesswire.com/news/home/20261118974464/en/Anthropic-is-Not-a-Safe-AI-Company---Broad-Coalition-of-Scientists-Legal-Scholars-and-Tech-Leaders-Challenge-Anthropics-Safety-Branding-Ahead-of-IPO)
- **Capability:** Anthropic reports Claude [solved two open problems in black-hole physics](https://www.anthropic.com/research/claude-black-hole-physics) (509 pts on HN).
- **Pricing pressure:** Gemini 4 Neon is [documented](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-neon); a comparison puts it at [$3/$15 vs Fable 5.2's $8/$40](https://shattered.io/gemini-cli-vs-claude-code-neon-3-15-vs-fable-8-40-tokens/) per million tokens. Relevant if a bulk or batch job ever needs a cheaper model.
- **Studies:** [Harvard finds coding agents moved the bottleneck to code review](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/) (325 pts); [AI agents asked better questions than KPMG accountants in an audit trial](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/) (490 pts; relevant to Ali's finance and audit-prep work, but I only read the headline).
- **Harness engineering:** [HubSpot's Aviator agent harness](https://hubspot.engineering/blog/aviator-hubspots-agent-harness/); [ADE Index](https://adeindex.com), a sourced ranking of 975 agentic coding tools; X via SerpAPI: Philipp Schmid argues [harnesses should expose themselves as MCP servers](https://x.com/_philschmid/status/2123028985990754329) instead of building in multi-agent features.
- **Launches:** [StarSling (YC)](https://news.ycombinator.com/item?id=50536468), self-improving CI for agent-volume repos; [Maritime (YC F26)](https://news.ycombinator.com/item?id=50549188), managed cloud for production agents; [Onlook](https://github.com/onlook-dev/onlook/), open-source design tool; [hackclub/orchard](https://github.com/hackclub/orchard), self-hosted git-to-server deploy (possible NAS fit).
- **MCP adoption:** [Esri ArcGIS Monitor 2026.1 adds MCP](https://www.esri.com/arcgis-blog/products/monitor/administration/arcgis-monitor-2026-1-support-for-ai-with-model-context-protocol-mcp); [Snap Lens Studio works with Claude Code and Cursor](https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/); Deque's Axe accessibility MCP server added a free plan ([X via SerpAPI](https://x.com/dequesystems)), useful for checking Plumbline's accessibility.

## Skipped: likely star-farming
- `bookwjitchieni1986/blender-ai-mcp-addon`: 1,014★ within a day of creation, same pattern as earlier Blender MCP farm repos.
- `ai--manus2.0` clone farm is still going: 9+ copies at exactly 56★ each (eluyonga, AntikvarX, Sorsax, …).
- `setyamickala/airdrop-agent` (crypto airdrop automation); `kenzz-devv/open-webui-talora-ai-workspace`.

---
_Ask: pick the items you want to discuss or adopt. The recommended starting point is the connector trust register audit._
