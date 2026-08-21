# Skills Scout — 2026-08-21

Window: Aug 20 → Aug 21 (last run 2026-08-20). Method: repo context + SerpAPI recency layer (3 calls, qdr:d) + built-in web search + GitHub API sweeps (anthropics repos, new-repo searches). Deduped against seen-index.

## Official / Tier 1

1. **Claude Platform: Agent Skills + Files API GA for Managed Agents (+ web access controls)** (Aug 19)
   - What: The Claude Developer Platform made Files API and Agent Skills support generally available, with new web access controls for Managed Agents. This is the platform-side GA of the skills stack — Managed Agents can now load skills and files as supported primitives rather than beta features.
   - Why it matters: Direct fit for the agentic-context-setup lane; if Plumbline or Hypomone ever run Managed Agents (scheduled cron runs surfaced 07-03, August wave 08-09), skills + files + web-access gating are now the stable substrate. The web access controls are also an Aegis-relevant governance primitive.
   - Trust: Tier 1 (Anthropic release notes, via releasebot.io/updates/anthropic). Note: the 08-20 run logged only the Admin API half of this release; the skills/files GA half is the part that matters for you.

2. **Claude Code v2.1.236–237** (Aug 19–20)
   - What: `ANTHROPIC_DEFAULT_MODEL` env var (sets the model new sessions *start* with, without locking like ANTHROPIC_MODEL); `notify_when_idle` cross-session idle notifications (one session pings another on the same machine when it goes idle — extends the SendMessage story from 08-08/08-17); built-in **Concise** output style (results first, no preamble); prompt-caching fix for LLM gateways/custom base URLs (cost + speed); auto-mode hardening (Monitor allow-rules disabled in auto mode); macOS sandbox read-deny rules now win even inside allowed areas.
   - Why it matters: Daily-driver release. The gateway caching fix is real money if you ever route via a gateway; notify_when_idle is a building block for your fleet-of-sessions/scheduled-task patterns; Concise style suits scheduled runs.
   - Trust: Tier 1 (code.claude.com changelog; detail via dev.classmethod.jp write-up, Tier 3 carrier).

## Claude / Cowork / skills ecosystem (registries & tooling)

3. **mcpmarket.com Agent Skills marketplace** — cross-platform skills directory + marketplace
   - What: MCP Market (an established MCP directory) now runs an Agent Skills marketplace — discover, install, and *sell* skills targeting Claude.ai, Claude Code, Codex, and ChatGPT. Actively indexed (fresh pages in last-24h search).
   - Why it matters: Candidate Tier 2 addition to skills-scout-sources.md (the sources file philosophy is patching directories together); the paid-skills angle is also a data point for your skill/plugin-curation lane and any future skill-monetization thinking.
   - Trust: Tier 2/4 — known directory operator, but listings are unvetted; verify each item before install.

4. **panaversity/learn-stateless-mcp** — twin-SDK tutorial for the stateless MCP spec
   - What: Teaching repo (created Aug 20) that builds the 2026-07-28 stateless MCP revision twice — Python SDK v2 and TypeScript SDK v2, five lessons mirroring each other file-for-file (no-session server/client, where tool JSON Schema comes from, multi-round-trip requests).
   - Why it matters: MCP-building lane. You've tracked the stateless spec since 07-03/07-28; this is the first clean hands-on migration reference in the index — useful if/when populi-mcp-style or Meridia/Aegis servers get built or updated to the new spec.
   - Trust: Tier 3 — Panaversity is a large known edu org, but the repo is day-one (4★); treat as reference material, not production code.

## Aegis (governance / audit patterns)

5. **JFrog MCP Registry (GA) + AI Catalog MCP/skills governance**
   - What: JFrog is shipping a universal MCP Registry as a "secure system of record" for MCP servers, inside its AI Catalog — shadow-AI/MCP detection, curation/blocking policy, and governance over models, agent skills, and MCP servers as supply-chain artifacts. Fresh Aug 20 blog ("Don't Break the Agent") shows the working stack; companion pieces cover the registry GA and shadow-MCP detection.
   - Why it matters: Aegis lane — this is the enterprise articulation of governance-not-guardrails applied to agent tooling: registry-as-system-of-record + policy gates + audit visibility. Pairs with Cloudflare's shadow-MCP detection (surfaced 08-19) as evidence the governed-agent-supply-chain category is consolidating fast — relevant prior art context for the governance patent claim.
   - Trust: Tier 2 (vendor blog/press). The Aug 20 blog is verified fresh; exact GA dates for the registry come from vendor materials and were not independently dated this pass.

## Lanes searched, nothing new

- **Education / K-12 (Recess):** only Claude for Teachers press recycle (stacker syndication) — increment of items logged 08-09/08-19.
- **Fintech / lending (Meridia, Hypomone):** only Plaid × Claude press recycle of the 08-17 MCP early-access item; no new lending/CRA/Plaid tooling.
- **Populi / SIS + Postgres:** guide/blog recycling only (pgEdge, Postgres MCP setup guides); no new servers or skills.
- **Official repos:** anthropics/skills quiet since 08-18; claude-plugins-community quiet; claude-plugins-official was 27 version bumps, no new vendors (see skipped log).

---
*SerpAPI: used (3/3 calls, qdr:d). Seen-index and skipped-log updated this run.*
