# Plugin audit — 2026-06-21

## How to read this

- **Basis:** the installed-plugin manifest from this session, what we've actually used together, and your known project surface (Talbot Hall / Turner operations & finance, the ASAM monorepo build, the grant scout, Hypomone / Prep Capital).
- **Limit:** I can't see per-plugin usage counts across all your sessions, so "used / unused" is scoped to our work plus obvious relevance. Treat Tiers 2–3 as judgment, not verdicts.
- **Everything here is reversible** in **Settings → Capabilities**. Disabling a plugin keeps it installed; you can flip it back anytime.

## The headline

You have **~67 plugins** enabled. That's why **hundreds of tools load every session** and why you see MCP servers connecting/disconnecting in the background each turn — each one is startup cost, context bloat, and occasional instability (and, in CockroachDB's case, a hook firing on every edit). The goal isn't minimalism; it's **keeping what earns its place and cutting what only adds weight**.

Three signals I used to judge "side effects":
1. **Ships a hook** — runs code on your edits (CockroachDB's SQL checker — the thing that's been erroring).
2. **Bundles an MCP server that (re)loads each session** — observed this session: cockroachdb (toolbox + cloud), prisma, tooluniverse, twilio-docs, zoom (3 servers), desktop-commander, pdf-viewer, ip-legal/Descrybe.
3. **Outside any domain you actually work in** — telephony, CDNs, 3D, enterprise security, etc.

---

## Tier 1 — Disable now (high confidence: side effects and/or clearly outside your work)

| Plugin | Why disable | Note |
|---|---|---|
| **cockroachdb** | The SQL-edit hook that's been erroring + 2 MCP servers + 3 agents. You don't run CockroachDB. | **Disabling this is the hook fix.** |
| **prisma** | Prisma-Local MCP loads each session; no Prisma/Postgres app in play. | |
| **tooluniverse** | MCP loads each session; niche research toolkit. | |
| **twilio-developer-kit** | ~70 telephony skills + a docs MCP; only useful if you're building SMS/voice. | |
| **zoom-plugin** | Three MCP servers load each session; only for Zoom app development. | |
| **desktop-commander** | Heavy terminal/process-control MCP; overlaps the shell + file access you already have here. | |
| **zscaler** | Enterprise security-appliance management — hundreds of tools, zero overlap. | Biggest single tool-count offender. |
| **blender** | 3D modeling. | |
| **fastly-agent-toolkit** | CDN / VCL edge config. | Keep only if an ASAM service runs on Fastly. |
| **claude-for-msft-365-install** | Deploys a Microsoft 365 add-in; not applicable. | |

That's ~10 plugins, and it kills the hook, the worst of the MCP churn, and the largest irrelevant tool surfaces.

---

## Tier 2 — Keep (central to your actual work)

| Plugin | Why it earns its place |
|---|---|
| **small-business** | QuickBooks / PayPal / Square / Stripe / Gmail / Calendar / HubSpot / Canva — the core of Talbot Hall + Turner finance & ops. Your QBO connector lives in this lane. |
| **finance** | Journal entries, reconciliation, financial statements, variance — directly supports your manual Populi↔QBO reconciliation and month-end. |
| **data** | SQL, analysis, dashboards, visualization — the Plumbline data layer. |
| **engineering** | Code review, debugging, architecture, testing — the ASAM build. |
| **figma** | Plumbline UI and the Claude Design → code path. |
| **productivity** | Task + memory management — the "running system / partner" theme you've been building toward. |
| **product-management** | Specs, brainstorming — Hypomone and ASAM spec work. |
| **cowork-plugin-management** | You build Cowork plugins; this is the toolkit for it. |
| **operations** | Process docs, runbooks, status reports — operationalizing the systems you're standing up. |
| **(grant/funder connectors)** | Whichever connectors do funder / open-grant / 990 / federal-grant search — these power open item #2 (the grant scout). Keep them; confirm which plugin owns them in Settings. |

---

## Tier 3 — Review (could matter to a known project; decide per cluster)

Clusters, with a one-line heuristic each. Default leaning in **bold**.

- **Deep finance / capital-markets verticals** — daloopa, bigdata-com, sp-global, equity-research, market-researcher, pitch-agent, model-builder, valuation-reviewer, statement-auditor, kyc-screener, fund-admin, gl-reconciler, month-end-closer, earnings-reviewer, investment-banking, private-equity, financial-analysis, meeting-prep-agent, wealth-management. → You don't run a fund or a bank. **Keep at most one market-research tool (bigdata-com *or* sp-global) for Hypomone/Prep Capital reads; disable the rest.** `financial-analysis` is a maybe if you want modeling templates. The Turner-finance overlap (`gl-reconciler`, `month-end-closer`) is largely redundant with `finance` + what we built — **likely disable**.
- **Legal verticals** — legal, commercial-legal, ip-legal, employment-legal, litigation-legal, privacy-legal, product-legal, regulatory-legal, ai-governance-legal, legal-builder-hub. → You're not a law firm, but Turner *does* sign vendor / Spelman / CORT agreements and Hypomone has real compliance ahead. **Keep one general contract reviewer (commercial-legal); disable the litigation / IP / employment / privacy / product / regulatory specialists** until a specific need.
- **Sales / CRM** — apollo, common-room, zoominfo, vpai, sales, adspirer-ads-agent. → No sales org. **Disable the lot.**
- **Marketing / outreach** — marketing, brand-voice, postiz. → Possibly useful for Turner recruiting/comms. **Keep one if you do outreach; otherwise disable.**
- **Web research / scraping** — nimble, brightdata-plugin. → Genuinely useful for the curation scouts and grant research. **Keep one (nimble *or* brightdata); disable the other.**
- **Misc tools** — base44, cloudinary, airtable, zapier, langfuse, enterprise-search, product-tracking-skills, ai-firstify, adobe-for-creativity, customer-support, human-resources, pdf-viewer, design. → **Keep only what you actually touch:** likely `human-resources` (Turner staff/hiring), `zapier`/`airtable` if you use them, `pdf-viewer` if you read PDFs here (note: its MCP churns), `langfuse` later if you instrument ASAM agents. `adobe-for-creativity` and `design` overlap `figma`/Canva → probably disable. The rest → disable unless one is a known part of your stack.

---

## Suggested action order (the 15-minute pass)

1. **Disable CockroachDB first** and make one trivial edit — the hook noise should stop. That confirms the diagnosis before you touch anything else.
2. Disable the rest of **Tier 1**.
3. Walk **Tier 3 cluster by cluster**, keeping the bolded default unless you know you use a specific one.
4. Leave **Tier 2** alone.

Net effect: from ~67 plugins to roughly **12–15**, a big drop in tools-per-session, no more edit-time hook, and far less background MCP churn — without losing anything you actually use.

> Re-evaluate quarterly, or whenever you install a few new ones to try. Installing-to-evaluate is fine; this audit is just the periodic prune that keeps it from accumulating.
