# Skills Scout — 2026-09-10

Scan window: last ~48h (Sep 8–10). SerpAPI used (3/3 last-24h precision queries) + built-in search + GitHub API sweep via Composio. Lanes searched: official/Tier 1, skills ecosystem/dev tooling, Meridia/Hypomone fintech, Aegis governance, Recess K-12, Populi/SIS/Postgres, KSW/grants.

## Official / Tier 1

1. **Claude Code v2.1.265–267 (Sep 9)** — 267 adds effort-level controls + system-prompt rendering options; 265 brings safer plugin loading, improved telemetry/gateway handling, faster session resume, workflow + slash-command UX, and fixes across remote control, VS Code, MCP, Windows permissions; 266 fixes a `CLAUDE_CODE_USE_GATEWAY` regression. Also prompt-cache, artifact-publishing, and sandbox workflow improvements. Why: core harness for every lane; effort-level controls are directly useful for cost-tiering the task fleet. Trust: Anthropic changelog via releasebot mirror (Tier 1).
2. **security-guidance plugin 2.0.7→2.0.8** (claude-plugins-official, Sep 9) — Anthropic hardened its official security-guidance plugin: repository now resolved from the command and edited paths, hardened git invocation, adjusted SubagentStop handling. Why: this is the official session guard-rail plugin; the fixes close repo-resolution gaps. Distinct from the claude-security scanner plugin (surfaced 07-23). Marketplace otherwise quiet: ~20 routine version bumps Sep 8 (qodo/greptile/box repoints — increments of known items). Trust: Tier 1 (official marketplace commits).
3. **WATCH (unverified)** — an aggregator reports Anthropic disclosed four unauthorized-access incidents on Sep 9 with METR engaged for independent audits — would follow the Aug 31 alignment/security post-mortem (surfaced 09-01). Not found on anthropic.com in this scan. Trust: Tier 4 aggregator (aiweekly.co) — verify before repeating or acting.

## Skills ecosystem & agent tooling

4. **NVIDIA-Verified Agent Skills** — github.com/NVIDIA/skills [backfilled, May 2026; trending this week] — official NVIDIA skills catalog where every skill is cataloged, scanned, cryptographically signed, and ships a "skill card" (capabilities, origin, security validation, authenticity). Why: the cleanest vendor implementation yet of skill supply-chain governance — a concrete reference for Aegis governance-not-guardrails thinking, and the vendor-skills wave continues. Trust: Tier 2 (official NVIDIA; verified via developer.nvidia.com blog).
5. **y0f/fable-orchestration-5.1** (Sep 9, ★7) — Claude Code skill: Fable 5.1 decides, Opus 5 / Sonnet 5 / Haiku 4.5 execute; five wiring patterns (advisor, architect+delegate, agent teams, workflows…). Why: directly on-model for fleet orchestration + model cost-tiering, and pairs with the new effort-level controls above. Trust: Tier 4 — unknown author, day-one; read before install.
6. **asm0dey/precedent** (Sep 10, day-one) — Claude Code skill that remembers architectural/business decisions across every project and surfaces them as precedent when a comparable choice comes up. Why: same shape as the OS-file/lane-memory pattern — a candidate to mine for the os-architect lane. Trust: Tier 3/4 — known OSS developer-advocate author, but brand new.
7. **yuna78/html-to-pptx** (Sep 10, day-one) — HTML slide decks → truly editable PPTX (native DrawingML shapes, not screenshots); Claude skill or plain CLI. Why: bridges the HTML-first document pipeline to Turner/board decks; third entrant in this niche (ConnorRX56 08-26, ppt-master 09-07) but the cleanest framing. Trust: Tier 4 — unverified, day-one.

## Meridia / Hypomone — fintech & lending

8. **Sumsub compliance MCP server + open-source agent-skills suite** (fresh blog, last 24h) — KYC/AML vendor ships an MCP server plus agent skills for one workflow: hand the agent a compliance policy and it runs checks against Sumsub data. Why: policy-driven compliance agents are exactly the Charter-intake / membership-verification shape for Hypomone, and a reference for how a regulated vendor packages MCP + skills together. Trust: Tier 2 vendor blog — verify scope/pricing before touching.
9. **SECURITY: CVE-2026-87911 — postgres-mcp-server read-only bypass** (AWS security bulletin, last 24h) — OS command injection in the read path of the Python postgres-mcp-server package defeats its read-only enforcement. Why: the stack leans on "read-only Postgres MCP" as a safety boundary (NAS Postgres; mcp-warehouse/db-mcp patterns logged 09-01) — this shows read-only labels can be bypassed; audit any Postgres MCP in use and pin patched versions. Trust: Tier 1/2 (official AWS bulletin).

## Aegis — governance & audit
Nothing new beyond the NVIDIA skill-governance item (#4); governed-DB and agentic-SOC vendor pieces went to the skipped log.

## Recess — K-12 education
Searched (Claude for Teachers wake, edtech outlets, GitHub) — nothing new in-window; Sep 8 Beneficial Deployments item was surfaced yesterday.

## Populi / SIS + Postgres ops
Nothing new in-window beyond CVE-2026-87911 (#9).

## KSW — grants & music education
Nothing new; a patent-search MCP skill was logged to the skipped log for the Meridia patent lane.

---
_SerpAPI: available, 3/3 budget used (site:github.com qdr:d, official-outlets qdr:d, lane-keywords qdr:d). Seen-index dedupe applied; 13 borderline items logged to skipped-log._
