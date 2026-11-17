# Skills Scout — 2026-11-17

_Window: Nov 15–17, 2026. Sources: Claude Code changelog, Releasebot (Developer Platform), anthropics/skills + claude-plugins-official commit logs (GitHub API), web search, SerpAPI (3 calls, last-24h)._

## Official / Tier 1
1. **Claude Code 2.1.326 (Nov 16)** — biggest permissions/sandbox pass in weeks: sessions with no mode set now start in **auto mode** (not Manual) when org policy hasn't loaded; auto is default for the Claude Code + Cowork HIPAA config; file tools refuse writes to sign-in files (`.credentials.json`); more `cp`/`mv`, PowerShell and long-value commands now ask — or are **refused in unattended runs**; hook `"decision": "block"` holds in more cases; plugins with a malformed `plugin.json` display field now load (with hooks + MCP servers); plugin uninstall removes `.mcpb`/`.dxt` bundle files; Code Mode now works with agent teams; `/claude-api` skill builds on **Managed Agents** by default.
   _Why it matters:_ scheduled tasks (this scout, sweeps) may hit new refusals; worth a glance if a routine starts failing. Plugin authoring (skill-forge). _Trust:_ Tier 1 — code.claude.com/docs/en/changelog
2. **Self-hosted Managed Agents (Developer Platform, Nov 12)** — run the full Managed Agents service and store agents, sessions and history on your own infrastructure; model calls go to a chosen provider (default Anthropic).
   _Why it matters:_ Hypomone/Meridia — agent data on the Synology NAS instead of Anthropic's cloud; Aegis governance/audit pattern (you own the session ledger). Pairs with item 1's `/claude-api` → Managed Agents default. _Trust:_ Tier 1 origin, seen via Releasebot mirror (Tier 2) — verify on platform.claude.com release notes before planning on it. releasebot.io/updates/anthropic/claude-developer-platform

## Skills & MCP infrastructure (skill curation / skill-forge)
3. **FastMCP 4.2 — skills over MCP (Nov 13)** — a FastMCP server can serve a folder of SKILL.md skills (or Python-defined skills) next to its tools via the MCP Skills extension; `ResourcesAsTools` fallback for clients that can't read skills yet; client extension copies a server's skills locally.
   _Why it matters:_ one canonical skill library (e.g., your Turner/Talbot skills) served from one server to Cowork, Code and other agents — fixes drift between copies. Concrete implementation of the Skills-over-MCP WG (seen 09-05). _Trust:_ Tier 2 (Prefect, FastMCP maintainer) — prefect.io/blog/fastmcp-4-2-skills-over-mcp
4. **NVIDIA SkillEvaluator v0.9.0 (Nov 13)** — checks agent skills and measures their effect on task results (with/without comparison).
   _Why it matters:_ evals for skills you write with skill-forge — evidence a skill actually helps before you keep it. _Trust:_ Tier 2/3 (NVIDIA org repo; verify maturity) — github.com/NVIDIA/SkillEvaluator

## Governance / audit — Aegis lane
5. **Sushegaad/Claude-Skills-Governance-Risk-and-Compliance** — MIT, ★1,083, updated Nov 15 (monthly cadence): GRC skills for ISO 27001, SOC 2, NIST CSF, **EU AI Act, ISO 42001, NIST AI RMF**, GDPR, HIPAA, CCPA, PCI DSS and more; claims 92% vs 53% benchmark with/without skills.
   _Why it matters:_ Aegis governance framing and the "governance-not-guardrails" patent prep (AI-risk framework mapping); Plumbline security questionnaires. No FERPA/GLBA module — gap to note. _Trust:_ Tier 3/4 community (high stars; benchmark self-reported) — github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance

## Fintech / lending data — Meridia / Hypomone lane
6. **Omni-53 (Coeus Institute) MCP for credit-union intelligence** — exposes 4,500+ federally insured credit unions: key ratios (6 yrs quarterly), peer percentiles, rankings by asset size/state/charter, specific **NCUA call report line items**, and **annual HMDA mortgage summaries**; public data only (no core/member connection); beta for Pro/Elite subscribers. [backfill, ~Oct 2026]
   _Why it matters:_ closest commercial analog to integra-core's FDIC/HMDA layer and the Trust Index — competitive read for Meridia, and a peer-benchmark data source for Hypomone's membership-lending model. _Trust:_ Tier 2 press release (paid product; verify access/terms) — ffnews.com/news/omni-53-opens-credit-union-intelligence-to-chatgpt-claude-and-copilot-through-mc-1d5c9035

## Dev tooling — Plumbline build
7. **petrkindlmann/qa-skills** — 50 QA/test-automation skills (Agent Skills standard), MIT, ★282, pushed Nov 16.
   _Why it matters:_ Plumbline test coverage before the tenant-#1 rollout; mine a few (API contract tests, regression) rather than install all 50. _Trust:_ Tier 4 community — install with caution — github.com/petrkindlmann/qa-skills

## Lanes searched, nothing new
- K-12 / Recess: nothing new in window (clickedu teacher MCP already seen).
- Populi / SIS, NAS/Docker/Postgres, grants/KSW: nothing new.

## Ask (pick to adopt)
- [ ] Self-hosted Managed Agents → spec a NAS pilot for Hypomone? (verify first)
- [ ] FastMCP 4.2 → serve your skill library from one server?
- [ ] SkillEvaluator → add to skill-forge eval step?
- [ ] GRC skills → mine AI-risk mappings for Aegis / patent prep?
- [ ] Omni-53 → competitive note in docs/meridia/research?
