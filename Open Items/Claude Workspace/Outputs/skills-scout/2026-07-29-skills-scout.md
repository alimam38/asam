# Skills Scout — 2026-07-29

_Method: SerpAPI 3/3 (last-24h GitHub scope, Google News, last-24h web) + built-in search + GitHub API (repo search created/pushed >07-27; plugins-official commit audit). All 30 commits to anthropics/claude-plugins-official since 07-28 are version bumps — no new official plugins after the Jul 27 wave already surfaced._

## 1. posit-dev/skills — Posit's official Claude Skills collection
- **What:** Data-science Claude Skills from Posit (the RStudio company) — R/Python/Quarto/Shiny workflows. 446★, pushed Jul 28.
- **Why it matters:** Vendor-authored SKILL.md patterns for analytics and reporting work — directly reusable craft for Plumbline's embedded-analytics/reporting layer and your SKILL.md authoring practice.
- **Trust:** Tier 2 — official vendor org; verify individual skills before install.
- github.com/posit-dev/skills

## 2. neondatabase/agent-skills — official Neon serverless-Postgres agent skills
- **What:** Neon's own Agent Skills for working with serverless Postgres (81★; pushed Jul 27, freshly indexed in the last 24h).
- **Why it matters:** A database vendor's official take on teaching agents safe Postgres workflows — patterns port to your NAS/Docker Postgres and the Plumbline data layer even if you never use Neon itself.
- **Trust:** Tier 2 — official vendor org.
- github.com/neondatabase/agent-skills

## 3. simonw/mcp-explorer + datasette/datasette-mcp — day-one MCP tooling from Simon Willison
- **What:** Shipped Jul 28: `mcp-explorer`, a CLI for exploring/debugging any MCP server, and `datasette-mcp`, which mounts a `/-/mcp` MCP endpoint on any Datasette instance; plus a companion TIL on adding custom MCP servers to Claude (til.simonwillison.net/llms/mcp-in-claude-and-chatgpt).
- **Why it matters:** Practical test/debug tooling landing the same day as the MCP 2026-07-28 stateless spec (surfaced yesterday) — useful for poking at populi-mcp or any MCP server you build for Plumbline.
- **Trust:** Tier 2/3 — highly reputable OSS author, but day-one repos (7★); expect churn.
- github.com/simonw/mcp-explorer · github.com/datasette/datasette-mcp

## 4. Manufact — "MCP Cloud" for Claude connectors (YC launch, last 24h)
- **What:** Deploy and host MCP servers as Claude connectors with build/runtime logs and per-tool usage observability — no infra to stand up. Note: a Manufact MCP connector already shows up as available in this Cowork workspace.
- **Why it matters:** Shortest path to shipping a hosted Plumbline/Populi MCP server without running your own gateway (complements MCPJungle 06-27 / MCP Tunnels 06-28 for the self-hosted route).
- **Trust:** Tier 3/4 — brand-new YC-launch startup; install-with-caution, don't route FERPA data through it yet.
- ycombinator.com/launches/RxG-manufact-mcp-cloud-for-your-claude-connector-chatgpt-plugin

## 5. Anthropic Economic Index connector
- **What:** Official Anthropic connector (Jul 22 — missed by earlier passes) exposing the Anthropic Economic Index dataset (AI usage/adoption data) inside Claude.
- **Why it matters:** Lower direct fit than the rest, but Tier 1 on the connector beat: a clean reference implementation of an Anthropic-built data-source connector, and usable AI-adoption evidence for MIG GTM material.
- **Trust:** Tier 1 — Anthropic-verified.
- anthropic.com/news/anthropic-economic-index-connector

_Near-misses logged to skipped-log: genpark MCP schema-validator skill, substack-api-mcp, CesiumGS/cesiumjs-skills, Amex GBT Egencia connector, kenn-io/agentsview, Marktechpost financial-analysis-agents tutorial._
