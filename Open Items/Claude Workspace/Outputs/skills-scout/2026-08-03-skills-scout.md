# Skills Scout — 2026-08-03 (Monday)

Window: Sat Aug 1 – Mon Aug 3 morning. A quiet weekend at Tier 1 — the signal this run is in community GitHub drops and two vendor items. SerpAPI used (3 calls: 24h GitHub sweep, Google News sweep, week-scoped edu/fintech/governance sweep). Venture context from current-focus.md v3 (2026-08-02), which embeds each venture's STATUS summary.

## Official / Tier 1

Nothing new to surface this window:

- **anthropics/claude-plugins-official** — only automated version bumps since Jul 27 (exa, neon, postman, gitkraken, carta-cap-table, wix, firecrawl, databricks, etc.); no new plugin additions.
- **anthropics/skills** — no commits since the Jul 27 claude-api refresh (surfaced 07-27).
- **Claude Code "What's new"** — no weekly digest published past Week 29 (Jul 13–17) yet; releasebot shows nothing after v2.1.219/2.1.220 (Jul 24, surfaced 07-26).
- **MCP 2026-07-28 rollout** continues across Claude products (950+ connectors, MCP Apps UIs in conversations) — spec surfaced 07-28, Claude-side rollout blog logged 07-30; no new increment.

## Agentic tooling, plugin & skill curation

1. **claude-octopus (nyldn)** — Claude Code plugin that orchestrates up to 8 AI providers (Codex, Gemini, Copilot, Qwen, Ollama, Perplexity, OpenRouter, Claude) for multi-model consensus; 48+ commands across a Discover/Define/Develop/Deliver flow, 52 skills, 32 personas, an optional MCP server for other clients, and `/octo:usage` per-provider/per-skill/per-MCP token attribution with context-compression hooks. Why: multi-agent orchestration + usage-attribution lanes; the heavyweight alternative to oh-my-claudecode (07-24). Trust: Tier 3 — established (~3.4k★, MIT, 1,100+ commits, active in the last 24h), but a big surface area — review before enabling. github.com/nyldn/claude-octopus
2. **Agent Skills discovered from MCP servers (Microsoft Agent Framework, .NET)** — Microsoft's agent framework now discovers Agent Skills directly *from* an MCP server, i.e. an MCP server can advertise skills, not just tools. Why: spec-level convergence of the two distribution channels this scout tracks; a pattern worth copying if populi-mcp-style servers or Hypomone infra should ship skills alongside tools. Trust: Tier 2 — official Microsoft dev blog (Jul 28). devblogs.microsoft.com/agent-framework/discover-agent-skills-from-mcp-servers-in-net
3. **do-it-skill (nraford7)** — single-shot autonomous build pipeline (spec → plan → build → review → commit) with tiered review and a "diminishing-returns judge" that stops iterating when gains flatten. Why: verification-loop + build-methodology lane (pairs with Finn-loop 07-23 and Anthropic's verification-loops post 07-23); the judge idea is the novel bit. Trust: Tier 4 — day-one repo, ~2★, unvetted. github.com/nraford7/do-it-skill
4. **learn-from-session (notacp)** — turns your last AI coding session into a credibility-checked, quiz-placed reading path. Why: session-mining for *learning* rather than memory/handoff — a fresh angle on the distillation wave, and education-adjacent. Trust: Tier 4 — day-one, ~15★. github.com/notacp/learn-from-session
5. **artifact-to-pdf (yheshamx)** — Claude artifact (or any HTML) → one continuous pixel-perfect PDF, no page breaks; CLI + Claude skill. Why: live-artifacts lane — a clean way to hand a Cowork artifact to a board/committee as a single PDF. Trust: Tier 4 — day-one, ~3★, small scope so low risk. github.com/yheshamx/artifact-to-pdf

## Education / Recess (K-12)

6. **lecture-to-notes (drpwchen)** — lecture recordings → structured grounded notes plus a synced HTML viewer (video, timestamped transcript, curated summary on one page); local-GPU pipeline (Whisper ASR, slide extraction, OCR, VLM). Why: teacher-facing content tooling for the Recess lane, and local-first processing is the FERPA-friendlier posture. Trust: Tier 4 — created yesterday; 44★/12 forks day-one is unusually fast for an unknown author, so verify the pipeline before running it on real classroom media. github.com/drpwchen/lecture-to-notes

Otherwise quiet; freshest education-connector item remains ASSISTments' free Claude connector for teachers (logged 08-02).

## Fintech & lending data / Meridia–Hypomone

7. **geo-mcp-servers (willcadell)** — curated catalog of 55 geospatial MCP servers (geocoding/place search, PostGIS spatial databases, remote sensing/earth observation incl. NASA & Copernicus, weather/climate, QGIS/ArcGIS) maintained as a `servers.yaml` source of truth, plus an installable Claude skill that discovers and tracks new geo MCPs. Why: Meridia's FRED/FDIC/HMDA/census platform will need geographic joins sooner or later, and the PostGIS entries fit the NAS/Postgres stack; the catalog-plus-discovery-skill shape also mirrors this scout. Trust: Tier 3 — author founded Sparkgeo (credible geospatial firm); individual catalog entries unvetted. github.com/willcadell/geo-mcp-servers
8. **SAS Viya MCP Server + Claude Cowork credit-risk workflow** — SAS demo of an end-to-end credit-risk modeling agentic workflow: Cowork driving the Viya MCP server to build and validate a credit model. Why: Hypomone lending lane — a vendor-blessed reference architecture for agentic credit modeling; worth skimming for workflow shape even though SAS itself is off-stack. Trust: Tier 2 — official SAS channel (video, last week). youtube.com/watch?v=DqTXug8YJy4

## Governance & audit / Aegis

Searched (MCP governance, audit trails, approval patterns): nothing new and installable this window — only enterprise-gateway marketing content (e.g. MintMCP's "governance for MCP servers" listicle). One-line lane check: covered.

## Populi / Postgres / NAS

Nothing new this window — Neon/Supabase/pg lanes quiet after last week's official vendor-skills wave (07-29/07-31); plugin marketplace showed only version bumps.

---

*Method: Tier 1 checked via code.claude.com what's-new, releasebot (Claude + Claude Code), claude-plugins-official + anthropics/skills commit logs. Community via GitHub repo search (created ≥ 08-01), SerpAPI 24h site:github.com sweep, Google News, HN Algolia (0 hits last 3 days). Dedup against seen-index through 2026-08-02. Skipped/increments logged separately.*
