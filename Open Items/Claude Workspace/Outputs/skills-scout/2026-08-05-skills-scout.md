# Skills Scout — 2026-08-05

_Scan window: Aug 4–5 (last ~24–48h). SerpAPI recency layer used (3/3 calls: last-24h GitHub sweep, Google News, focus-lane sweep). Sources per skills-scout-sources.md; deduped against seen-index.md._

## Official / Tier 1
Quiet window. No new Anthropic announcements Aug 4–5; Claude Code v2.1.221 (Aug 4) was already surfaced 08-04. `anthropics/skills` has no commits since Aug 1. `anthropics/claude-plugins-official` saw version bumps only in the window (carta ×3, looker, neon, sentry, spotify-ads-api, data-agent-kit-starter-pack, wix, deepeval, aws-core, auth0, expo, …) — no new vendors.

## Skill & agent infrastructure (curation + supply-chain security — cross-venture, Aegis-adjacent)
1. **Trail of Bits Claude Code skills** — github.com/trailofbits/skills. Official skills collection from Trail of Bits for security research, vulnerability detection, and audit workflows (6.4k★, pushed today; includes an iterative skill-improver; installable via plugin marketplace). Not launched this week — created Jan 2026 — but newly caught by the scout and too good to leave unlogged. Why: the highest-credibility security shop publishing skills in this ecosystem; directly useful for the install-with-caution vetting posture and as reference architecture for Aegis-style audit workflows. Trust: Tier 2 — official vendor repo from a top security firm; still review individual skills before install.
2. **tech-leads-club/agent-skills** — github.com/tech-leads-club/agent-skills. "Secure, validated skill registry for professional AI coding agents" (~5.0k★, active in window) with a companion MCP server (`@tech-leads-club/agent-skills-mcp`) exposing the catalog via progressive disclosure — search first, fetch only what's needed. Works across Claude Code / Cursor / Copilot / Antigravity. Why: skill-curation lane; a validated registry answers the supply-chain worry, and the progressive-disclosure MCP pattern keeps context cost tiny (pairs with the /doctor context audit, surfaced 07-13). Trust: Tier 3 — established community org with real traction; validation claims are theirs — spot-check.
3. **Google tightens oversight of its Agent Skills repository** — itbrief.asia, Aug 4. Google adding stricter review/controls to its official Agent Skills repo. Why: ecosystem-governance signal — major vendors are formalizing skill supply-chain review, the exact pattern Aegis cares about (and that this scout's trust-tiering mirrors). Trust: Tier 2 press, single outlet — directional until Google documents it.

## Plumbline — Populi / Postgres / embedded analytics
4. **Apache Superset MCP server (official docs)** — superset.apache.org/admin-docs/configuration/mcp-server. Superset now documents a first-class MCP server: list dashboards, query datasets, execute SQL, create charts from any MCP client, with run/secure/deploy guidance. Why: self-hostable OSS BI that fits the NAS/Docker/Postgres stack — a governed agent-to-BI path for small-institution dashboards, as an alternative or complement to the Cube semantic layer (surfaced 06-24). Trust: Tier 2 — official Apache project documentation.

## Aegis — governance / audit patterns
5. **Gentkey governed Stripe MCP proxy** — gentkey.com/connectors/stripe. Vendor service that fronts the official Stripe MCP server behind one OAuth-protected URL: scoped writes, per-call gating, audit trail — the agent never holds a raw restricted key. Why: a live commercial implementation of governed-access-to-MCP, the governance-not-guardrails shape Aegis is about; useful as a pattern reference even if never bought, and payments-adjacent for Hypomone's later gates. Trust: Tier 4 — vendor promo, unverified; do not point it at real Stripe keys without vetting.

## Lanes searched, nothing new
- **Recess / K-12 education**: nothing new in window (ASSISTments connector already logged 08-02; Claude for Teachers wave is July news).
- **Meridia / Hypomone fintech-lending data**: nothing new (Blend Autopilot MCP backfilled 08-04; no new Plaid/CRA/CDFI tooling in window).
- **Grants / nonprofit**: nothing new in window.
