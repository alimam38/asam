# Skills Scout — 2026-11-27

_Window: last 24–48h (Nov 25–27) plus verified backfills. Sources: Tier 1 changelogs (code.claude.com, releasebot mirror of Anthropic notes), Cloudflare docs changelog, press, registries. SerpAPI used (3 calls: 1 site:github SKILL.md last-24h, 1 Anthropic news last-24h, 1 vertical-MCP last-24h → no results). Quiet day after the Nov 23–25 launch cluster (Claude Ship, Skills over MCP, Artifacts-as-apps — all already surfaced); most last-24h GitHub hits were repeats._

**Decision for Ali:** pick any of the below to adopt/trial. Top picks today: **#1 plugin optionalDependencies** (skill/plugin curation) and **#3 Claude for Teachers free through July 2028** (Recess pricing runway).

## Official / Tier 1

1. **Claude Code 2.1.331 — plugin `optionalDependencies` + Code Mode on Bedrock/Vertex/Foundry (Nov 23)**
   - What: plugin manifests can now list optional dependencies that install with the parent plugin but can be disabled/uninstalled independently. Code Mode now works in terminal sessions on Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry and Claude Platform on AWS.
   - Why it matters: lets you package a "core + optional add-ons" plugin (e.g., a Plumbline/Populi core skill with optional QBO or Gusto add-ons) without forcing every install to carry everything — directly relevant to skill-forge / plugin curation. (2.1.332's MCP-skills + `PreSkillShellCommand` hook already surfaced 11-25.)
   - Trust: Tier 1 — Anthropic-verified (code.claude.com/docs/en/changelog).

2. **Anthropic engineering: "Migrating our Messages API to Rust" (Nov 25)**
   - What: Anthropic ported the Messages API from Python to Rust, using production-traffic shadowing and Claude agents to verify behavioural parity while the service kept shipping.
   - Why it matters: a worked pattern for "agents verify parity during a rewrite" — reusable for Aegis (governed migrations, audit evidence) and for any Plumbline/integra-core refactor. Read for method, not tooling. Third-party CPU-savings claims (40–50%) are unverified.
   - Trust: Tier 1 — Anthropic-verified (anthropic.com/engineering; mirrored at releasebot.io/updates/anthropic). Verification note: explainx.ai/blog/anthropic-messages-api-rust-rewrite-claude-wrote-code-cpu-40-50-percent-claimed-vs-verified-2026 (Tier 4).

3. **Claude for Teachers free access extended to July 30, 2028 [backfill, Nov 18]**
   - What: verified U.S. K-12 educators, qualifying schools and districts on centrally managed accounts keep premium Claude, teaching tools and the Learning Commons standards-mapped curriculum connection free through July 30, 2028 (follows the AFT/UFT privacy agreement already logged 11-18).
   - Why it matters (Recess / Shadow Rock): removes the pricing cliff for the pilot — your wife's school can standardize on Claude for Teachers for two school years without budget approval, and Recess can design around a free teacher-facing baseline. The Learning Commons connector is already available in this workspace.
   - Trust: Tier 1 fact via Tier 2 press (edtechinnovationhub.com/news/anthropic-extends-free-claude-for-teachers-access-for-us-k-12-educators-to-july-2028); confirm on anthropic.com/news/claude-for-teachers before relying on the date in a contract.

## Recess / K-12

4. **parentsquare-mcp (unofficial ParentSquare MCP; MIT; v0.4.0 Aug 26)**
   - What: Python MCP server giving Claude ParentSquare feeds, calendar, messages, directories and (opt-in) admin roster writes for students/guardians.
   - Why it matters: ParentSquare is a common K-12 parent-comms platform — if Shadow Rock uses it, this is the fastest path to admin-ops automation (calendar digests, message drafts).
   - Trust: Tier 4 — **install-with-caution.** Not affiliated with ParentSquare; logs in with a username/password (session cookies, MFA handling), likely against ParentSquare ToS, and touches student/guardian PII (FERPA). Read-only use on a staff account at most; never enable roster writes without district sign-off. (pypi.org/project/parentsquare-mcp)

5. **ckz/edu_data_mcp_server — Urban Institute Education Data API MCP (MIT)**
   - What: MCP wrapper over the Urban Institute Education Data Portal (CCD, CRDC, IPEDS, etc.) by school, district and college; enrollment, directory, finance topics.
   - Why it matters: public district/school context for Recess market sizing and Shadow Rock benchmarking, and a K-12/higher-ed data feed beside Meridia's FRED/FDIC/HMDA/census stack. Public data only — no FERPA exposure. Overlaps partly with the EduInsights connector (IPEDS-side) already in this workspace; this adds K-12 (CCD/CRDC).
   - Trust: Tier 3 — known directory (mcpservers.org/servers/ckz/edu_data_mcp_server ; github.com/ckz/edu_data_mcp_server); last-update date not shown — check repo activity before relying on it.

## Platform / agent discoverability (Plumbline, ventures' public sites)

6. **Cloudflare "Search for Agents" (Nov 25)**
   - What: a dashboard toggle that stands up an AI Search instance and exposes a discoverable `/.well-known/search?q=` endpoint returning Markdown, advertised to agents via `agent:*` meta tags — no custom search integration needed.
   - Why it matters: you already have the Cloudflare connector. Any public venture site (Meridia, Recess, Plumbline marketing/docs) becomes agent-searchable in one switch — cheap GTM surface for "agents read your docs". Already live on developers.cloudflare.com and mcpservers.org.
   - Trust: Tier 2 — vendor-official docs (developers.cloudflare.com/changelog/product/ai-search ; developers.cloudflare.com/ai-search/how-to/search-for-agents/).

## Watch (unreleased)

7. **Claude Google Drive file browser (in development)** — TestingCatalog reports Anthropic building an in-Claude browser to search/manage Docs, Sheets, Slides, possibly inside Projects. Not shipped; relevant to Cowork context setup if it lands. Trust: Tier 4 — leak/unconfirmed (testingcatalog.com/anthropic-prepares-google-drive-file-browser-for-claude/).

## Lanes searched with nothing new
- Meridia / Hypomone (fintech/lending MCP): only repeats (Blend, Nymbus, Carrington, Bud, FDIC BankFind) or non-fits — see skipped log.
- Aegis (governance/audit): no new approval/audit tooling; one supply-chain incident logged to skipped (context only).
- Populi / SIS, Postgres/NAS, KSW (grants/music): nothing new.
- Tier 3 GitHub (last 24h SKILL.md repos): all repeats or off-focus churn.
