# Skills Scout — 2026-11-06

_Window: Nov 3 – Nov 6 (everything since the 11-02 digest), plus a few never-logged items marked [backfill]. SerpAPI: 3/3 calls used (Google News qdr:d for Anthropic, `site:` Anthropic/Claude qdr:w, fintech/K-12 "MCP server" qdr:w). GitHub via Composio (commits since 11-02 on the official repos; repo search created ≥ 10-30). **Repair note:** the 11-02 run wrote its digest but never appended to `seen-index.md`. Its 11 items are backfilled into the seen index in this commit so they are not repeated._

## Official / Tier 1

1. **Personal Finance in Claude (beta, Nov 5)**. You link bank, credit-card, loan and investment accounts through **Plaid**. Access is read-only. Claude shows balances and spending on one page and answers questions about your own money. It is available on Pro, Max and Ultra plans, in the US only, and it does not give investment advice. **Why it matters (Hypomone / Meridia):** Anthropic now ships a consumer "your accounts, explained" surface using the same Plaid trust layer Hypomone plans for members. That is a direct comparable for the member-ledger experience, and it raises the baseline for what a misbanked operator will expect. It also confirms Plaid read-only as the accepted pattern, so the Hypomone pitch should not lean on "AI reads your bank data" as a differentiator. **Trust:** Tier 1 (support.claude.com release notes, Nov 5), with details from Tier 2 press (Reuters, TechCrunch, The Verge). — https://support.claude.com/en/articles/12138966-release-notes · https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance · https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/
2. **Claude Enterprise security bundle (Nov 5): security center, inference hooks, centralized management, more access controls (several in beta)**. An inference hook sends every governed request by HTTPS to a server the organization runs. The server answers `{"action":"allow"}` or `{"action":"deny"}` before the model runs. Hooks cover claude.ai web, desktop, Claude Code and **Cowork**. If the server is unreachable the request goes through by default (fail-open), and this can be switched to fail-closed. Zscaler, Cisco AI Defense, Check Point and Reco already integrate. **Why it matters (Aegis):** this is Anthropic's own version of the Aegis governance-alert/approval gate, built as a pre-inference policy checkpoint. The allow/deny contract and the fail-open-or-closed choice are worth copying into the Aegis backend spec. It is Enterprise-only, so it applies to Turner only if seats move to Enterprise. **Trust:** Tier 1 (release notes). The protocol detail comes from Mint Security's review (Tier 2/3 vendor blog). — https://support.claude.com/en/articles/12138966-release-notes · https://www.mint.security/blog/claude-enterprise-inference-hooks-a-protocol-review
3. **Claude Code 2.1.314 → 2.1.318 (Nov 3–4): agent-safety and headless-run controls**
   - `permissions.blockWritesOutsideWorkingDirectories` makes Write and Edit refuse paths outside the working directories, in every mode.
   - Agent SDK hook callbacks get `onFailure: "block"`: if the callback fails, the action is blocked instead of going through.
   - `/schedule` now warns when a new cloud scheduled task picks up connectors you did not ask for.
   - Claude Code now asks before a web or shell call sends your account email to the network.
   - `claude auth status` and `claude -p` JSON now report when a stored sign-in expires (`loginExpiresAt` / `credential_expires_at`). `claude -p` prints a stderr warning starting 10 days before expiry.
   - Fixed: skills synced from claude.ai being lost or re-downloaded every 10 minutes.

   **Why it matters:** the scheduled-routine fleet (this scout, readai-ledger-sweep, the morning brief) runs headless. Sign-in expiry warnings and connector-scope warnings cover both of the ways those runs fail without anyone noticing. `onFailure: "block"` is the fail-closed choice Aegis approvals need. **Trust:** Tier 1 (anthropics/claude-code CHANGELOG). — https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
4. **Claude Platform API changes (Oct 28 – Nov 5)**
   - **Message threads** beta (`message-threads-2026-08-12`, Nov 2): conversations stay server-side and each request sends less, for long agent loops.
   - **Console IP allowlist** (beta, Nov 5), so a leaked API key cannot be used from anywhere. The Admin API can also now sign a member out everywhere.
   - **Usage and Cost Analytics API** beta (Oct 29). The older usage endpoints are now legacy.
   - Maximum request size raised from 32 MB to 128 MB (Oct 28).
   - Opus 4.8 fast mode is deprecated (Oct 30) and will be removed **Nov 30**.

   **Why it matters:** two of these apply now. Set the IP allowlist for the hub API key. Use the cost API for per-tenant cost lines in Plumbline. Check any script that sends `speed:"fast"` before Nov 30. **Trust:** Tier 1 (platform release notes). — https://platform.claude.com/docs/en/release-notes/overview
5. **Provable inference: FlashProve, open-sourced (Nov 2–3)**. Anthropic released a zkSNARK prototype under Apache-2.0. It includes a prover, a C++ verifier, a verifier written and proved correct in the Lean proof language, and a protocol spec. It proves that a committed model produced specific output tokens without revealing the weights; the demo model is Llama 4 Maverick. This is a research prototype, not an API. **Why it matters (Aegis / Meridia):** "prove which model produced this output" is the far end of a tamper-evident audit trail. It is a reference for the Trust Index and governance-not-guardrails patent framing, not something to build on yet. **Trust:** Tier 1. — https://www.anthropic.com/research/provable-inference
6. Official repos were quiet in our lanes. `anthropics/skills` had no commits since 11-02. In `claude-plugins-official`, most activity was `security-guidance` hardening (an increment of 09-10) plus new champion-kit and Xcode plugins, outside every lane. `knowledge-work-plugins` had version bumps only. All of these went to the skipped log.

## Meridia / Hypomone (fintech, lending data)

7. **jflamb/fdic-mcp-server (MIT, pushed 09-18)** [backfill]. An MCP server that exposes the FDIC BankFind Suite APIs (institutions, financials, failures) as structured tools. It is also listed on Glama. **Why it matters:** this is a ready MCP front-end over the same FDIC data integra-core already loads. Use it as a reference or a quick tool for Meridia analysis sessions instead of hand-writing a new server. **Trust:** Tier 4 (★0, single author). Read before running. — https://github.com/jflamb/fdic-mcp-server
8. **kylelegare/cu_MCP** [backfill]. NCUA 5300 call-report data loaded into a database and served over MCP. **Why it matters:** this is credit-union peer data (assets, members, loans, net worth), the closest public comparison set for a membership-lending institution like Hypomone. It is also a source integra-core does not cover yet; it has FDIC/HMDA but not NCUA. **Trust:** Tier 4 (★0, no license). Read only. — https://github.com/kylelegare/cu_MCP
9. **Izzy-Gottz/aggregate-finance (AGPL-3.0, created Nov 1)**. A read-only finance MCP that connects banks, cards, payments, books, payroll and cap table across several companies, so you can ask questions across all of them. **Why it matters:** this is a multi-entity "books + payroll + bank" aggregation shape. It overlaps Plumbline (QBO + Gusto) and the Meridia Holdings multi-entity books. Use it as a pattern only, because AGPL means any hosted derivative must publish its source. **Trust:** Tier 4 (★2, day-5). — https://github.com/Izzy-Gottz/aggregate-finance
10. **seanlnge/fin**. Local Plaid bank data for agents, packaged as a JSON CLI, a FastMCP server and a Claude skill. **Why it matters:** a small local-first Plaid pipeline that fits the NAS/Docker posture for Hypomone prototyping in Plaid Sandbox. **Trust:** Tier 4 (★0, no clear license). — https://github.com/seanlnge/fin

## Recess / K-12 and campus data (Talbot Hall)

11. **pipeworx-io/mcp-education-data (MIT, pushed Nov 1)**. An MCP server for US K-12 schools, districts, funding and child-poverty data. The same organization publishes `mcp-college-scorecard` and `mcp-education-feeds`. **Why it matters (Recess):** it gives district and funding context for the Shadow Rock pilot (Title I and poverty context for the math-gap analysis) without building a data pull. **Trust:** Tier 4. Pipeworx publishes many generated MCP wrappers, so check its data sources before relying on it. — https://github.com/pipeworx-io/mcp-education-data
12. **Bedcount: student-housing data MCP (`loans.studenthousing`)**. Three tools: IPEDS enrollment, college housing beds and bed gap at 693 US campuses, and a loan sizer. AptLynx lists it as checked on Nov 6. **Why it matters (Talbot Hall / Plumbline):** this is housing supply-and-demand benchmarking, close to the Talbot Hall occupancy and pricing review. It is worth checking whether Turner or its peer seminaries are in its 693 campuses. **Trust:** Tier 4 (directory listing only, unknown publisher). — https://aptlynx.net/servers/loans.studenthousing/studenthousing-loans

## Aegis (governance, approvals, audit)

13. **Self-hosted agent governance control planes (both created Nov 3)**. `DanielRoenko69/argus` (AGPL) covers identity, SSO/RBAC, approvals, **signed execution grants** and a tamper-evident audit log. `euron-sde-team/euron-open-agent-guard` (MIT) covers identity, policy, approvals, secrets, threat detection and a tamper-evident audit log. **Why it matters:** "signed execution grant" is a clean name for an Aegis approval record. Read both data models next to the inference-hooks contract (#2). **Trust:** Tier 4 (★0, day-3). Pattern reference only. — https://github.com/DanielRoenko69/argus · https://github.com/euron-sde-team/euron-open-agent-guard

## Plumbline (exec dashboard / semantic layer)

14. **gogoymh/auto-ontology-mcp (Apache-2.0, created Nov 6)**. An MCP server over NVIDIA Auto Ontology's semantic layer plus a personal knowledge base. It needs no LLM API key. **Why it matters:** this belongs to the semantic-layer lane (one shared metric vocabulary over Populi + QBO + Gusto). Read it to see how an ontology is exposed to agents. **Trust:** Tier 4 (★11, day-0). — https://github.com/gogoymh/auto-ontology-mcp
15. **Rollstack/skills (MIT, Nov 5)**. Vendor agent skills that build decks from company data, refresh them, and schedule and send reports through Rollstack's MCP server. **Why it matters:** a working "data → scheduled board deck" skill set, the same shape as the monthly B&F report and board packages. It is a reference for how Plumbline could expose a "send the monthly pack" action. **Trust:** Tier 2/3 (vendor organization). — https://github.com/Rollstack/skills

## Cowork / skill authoring (skill-forge lane)

16. **KKKKhazix/agent-autoloop (★3.6k in 3 days, MIT)**. It lets a command-line agent pick up work in the background and follow it through to the end. It stays quiet and sends a decision card only when it is unsure (README in Chinese). **Why it matters:** it is the same design as this routine fleet plus the ask-card skill: autonomous by default, with a single point where you decide. Compare its escalation rules with `ask-card` and the routine notification rules. **Trust:** Tier 3 (fast-rising, single author). Review it before installing. — https://github.com/KKKKhazix/agent-autoloop
17. **iDiagoValeta/mouseketool (MIT)**. An MCP server and skill that searches GitHub for projects that already cover your idea, reads their code and returns a verdict before you build. **Why it matters:** it automates the "does this exist?" gate in skill-forge and template-vetting, and the prior-art step before new venture tooling. **Trust:** Tier 4 (★8). — https://github.com/iDiagoValeta/mouseketool
18. **ai-agent-manager/agent-lint (Apache-2.0)**. Validates Agent Skills (SKILL.md) and other agent files. **Why it matters:** a CI-style check for the roughly 60-skill fleet before you publish edits. **Trust:** Tier 4 (★1, day-2). — https://github.com/ai-agent-manager/agent-lint
19. **⚠️ Star-farm cluster, Nov 5**. At least 9 skill and MCP repos were created the same day, each with 36–41 stars, under throwaway account names: `AcrossTopazcache8602`, `WolfZorace44832`, `Vespermagnet`, `NightUnderAurora41899`, `AgainstStoneGold`, `RainedFeral`, `gravityellestone`, `Galehashoid`, `BehindProxySolar` (names often include "rpocket", "resocket" or "resp"). `globalmpc/backendskills` (★39, same day) carries the same star signature, so treat it with the same caution. **Why it matters:** this matches the 09-22 SEO-farm wave and the 10-29 extension-trojan pattern. Do not install anything from this batch. **Trust:** Tier 4 caution signal. — github.com search, created:2026-11-05

## Lanes searched, nothing new in window

- **Populi / SIS-LMS / FERPA:** nothing in the first run; the same-day re-run found #30 (patterns only, no Populi-specific tool).
- **KSW (grants / music-ed):** nothing.
- **NAS / Docker / Postgres:** only `Balanov/shim` (★466, a tiny local-first harness with MCP and skills), logged as skipped.
- **Recess teacher-facing AI:** coverage is still the July Claude for Teachers launch (already seen).

## Late-October backfill (Oct 18 – 26), recovered from the paused 10-27 run

_The scheduled 10-27 run did its research but paused before committing; it resumed today. The 11-02 digest flagged a 09-23 → 11-01 gap and did not backfill these. Each item below was checked against the seen index (none present) and against the 11-02 and 11-06 digests. SerpAPI on 10-27: 3/3 calls (two `site:github.com` qdr:d queries returned nothing; the Google News query found the leads)._

### Official / Tier 1 [backfill]

20. **Claude for Nonprofits plugin (Oct 26, free)**. It installs automatically for verified nonprofits on Team and Enterprise plans. Skills cover four areas:
    - **Set-up:** a records map (where donor data, grant files, finances and policies live) and a check of staff questions against your AI-use policy.
    - **Funding:** funder and grant research with cited sources, RFP eligibility breakdowns, proposal and report drafting, and donor stewardship (call briefs, thank-you notes).
    - **People:** job posts, interview guides and 90-day onboarding.
    - **Board:** skills-gap analysis, candidate outreach, onboarding packets and meeting decks.

    It builds on the Blackbaud, Candid and Benevity connectors (seen 07-05). Webinars: **Nov 10** (admins: data handling and AI-use policy) and **Nov 12** (staff, day one). **Why it matters (Turner, KSW grants):** if Turner's Claude seats are on a Team plan under a verified nonprofit, this arrives without any setup. The board-support and grant skills overlap the monthly report, the Phase III / Elevation materials and the KSW PG-2 grant work. Check Turner's nonprofit verification status before building more grant tooling yourself. **Trust:** Tier 1 (claude.com article, Oct 26). — https://claude.com/resources/articles/expanding-claude-for-nonprofits
21. **Agent Skills standard donated to the Agentic AI Foundation (Linux Foundation), Oct 22**. MCP already sits under the same foundation. Anthropic says the standard stays "open, community-driven, and vendor-neutral". No change to the SKILL.md format was announced. **Why it matters (skill-forge lane):** your roughly 60-skill fleet is now written to a vendor-neutral standard, which makes the skills more portable to Codex and other agents and lowers the risk of relying on them for Plumbline and venture IP. Watch the AAIF repo for spec changes rather than Anthropic's docs alone. **Trust:** Tier 1 (Anthropic announcement, via Simon Willison and the Linux Foundation press release). — https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation · https://simonwillison.net/2026/Oct/22/donating-agent-skills/
22. **"When to fold subagents into your main agent loop" guidance, plus `anthropics/single-agent-loop-kit` (Apache-2.0, ★525)**. Anthropic says split-up subagent designs (routers, org-chart-style domain agents) often add delay and lose context. It recommends one loop with skills and progressive tool disclosure, and warns that tool-selection accuracy can drop past about **30–50 tools**. Keep subagents for real context bloat, parallel fresh-context work, verification, or separating privileges. The migration method: build about 10 golden test cases, fold tightly coupled agents first, turn the rest into tools, and keep any subagent whose removal makes results worse. It comes with `/claude-api` migration skills (build-eval, prompt-audit, hillclimb, cost-optimize) and `/skill-doctor`. The kit is an unmaintained reference repo. **Why it matters:** this directly informs the council and multi-agent skills and the routine fleet. Runs like this one load Composio, Dropbox and GitHub tools at once, which puts them in the range where selection accuracy drops. The 10-golden-case method is also a cheap eval harness for the receivables and monthly-report skills. **Trust:** Tier 1 (claude.com article and the anthropics org repo). The summary of specifics comes from SmartScope (Tier 3). — https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop · https://github.com/anthropics/single-agent-loop-kit
23. **Claude Duet, research preview (Oct 21)**. A proactive agent that runs on its own cloud machine and browser, across email, calendar and payments. It sends a morning briefing and checks connected accounts every few hours. Safety tiers:
    - **Approval needed** for payments, signing documents and deleting.
    - **Always blocked**, even with approval: moving money and acting in someone else's account.
    - **Credentials** stay isolated; Duet never sees passwords or tokens.
    - **Outbound messages** pass a classifier that looks for sensitive data.

    Access: Pro and Max plans, US only, from a waitlist. Not available on Team or Enterprise yet. **Why it matters:** (a) for **Aegis**, the three tiers (approve / never allowed even with approval / credential isolation) are a clean reference structure for governance alerts. (b) It overlaps the morning-brief and routine fleet, so compare it before building more "watch my accounts" routines. **Trust:** Tier 1 (release notes via releasebot) plus Tier 2 press. — https://www.vktr.com/ai-platforms/claude-duet-anthropic-previews-an-ai-agent-that-messages-you-first/ · https://releasebot.io/updates/anthropic
24. **Cowork / desktop October changes (Oct 1 – 22) that affect your skills and routines**:
    - **Skill descriptions longer than 1,024 characters are now refused (Oct 6).** Audit the fleet, since several long descriptions may be near the cap.
    - Skill uploads now keep every file in the archive, not only `SKILL.md` (Oct 5).
    - Cowork scheduled tasks default to "Automatically approve" where the organization allows it (Oct 1). Tasks under an "ask" policy now stop and wait (Oct 8).
    - `/schedule` was removed from the Cowork slash menu (Oct 22).
    - Skills, local MCP servers and plugins can be imported from third-party Claude (Oct 8, Oct 15).
    - Chart.js, Grid.js and Mermaid ship with the app, so artifacts render them offline (Oct 13).

    **Why it matters:** the 1,024-character cap can silently block a skill-forge or skill-creator output, and the approval-default change decides whether routines like this one run unattended. **Trust:** Tier 1 (Claude desktop changelog). — https://claude.com/docs/cowork/changelog
25. **Claude Code 2.1.307 → 2.1.311 (Oct 21 – 26)**:
    - New `claude_code.safety_event` OpenTelemetry event for every tool call that a permission rule, auto mode, hook or sandbox stopped, prompted or sent back.
    - HTTP MCP tool calls are retried **only if the tool is read-only or idempotent** (fixes calls being sent twice).
    - Sandbox hardening: shell startup files no longer run outside the sandbox, and `--mcp-config` can't be edited by sandboxed commands.
    - Enterprise custom roles control access to cloud sessions and Remote Control.
    - Subagents can now use MCP servers that connect after the subagent starts.
    - Claude Tag gets a skills-analytics view.

    **Why it matters:** `safety_event` is a ready-made audit feed for the Aegis approvals model. The idempotent-only retry rule is the same discipline the Hypomone ledger needs (never post twice). This complements 2.1.314–318 (item 3). **Trust:** Tier 1 (Claude Code changelog). — https://code.claude.com/docs/en/changelog
26. **Claude Models on Google Cloud, Anthropic-managed, GA (Oct 22)**. You reach the Claude API through your own Google Cloud project, with Google Cloud IAM, and the spend counts toward existing Google Cloud commitments. Opus 5.5 fast mode is priced at $8 / $40 per million input / output tokens. **Why it matters:** low today. It becomes relevant if Meridia or Hypomone hosting moves to GCP, since Hypomone's model policy is Claude first and Gemini second and both could then sit on one bill. Note the fast-mode price alongside the Nov 30 removal of Opus 4.8 fast mode (item 4). **Trust:** Tier 1 (platform release notes via releasebot). — https://releasebot.io/updates/anthropic

### Recess / K-12 [backfill]

27. **xiaoyang111222/cn-math-taxonomy (★6.9k, created Oct 18, custom license)**. An open K-12 knowledge graph covering math (elementary through high school), English and middle-school physics. It has 1,644 knowledge points, **2,403 prerequisite edges** and 6,723 practice items, aligned to the curriculum standard, with **adaptive prerequisite diagnosis** and a live demo. **Why it matters (Recess):** this is close to the Shadow Rock 5th-grade prerequisite-routing and math-gap work, as a data model and diagnostic flow. The curriculum is Chinese, so use it as a schema and algorithm reference and pair it with the connected Learning Commons Knowledge Graph for US standards. **Trust:** Tier 3 (fast-rising, active today). The license is non-standard ("Other"), so read its terms before reusing any data. — https://github.com/xiaoyang111222/cn-math-taxonomy

**Added asks:**
- (f) Confirm whether Turner's seats get the **Nonprofits plugin**, and put the Nov 10 admin webinar on the calendar.
- (g) Audit the skill fleet for **descriptions over 1,024 characters**.
- (h) Use the **single-agent-loop** golden-case method on one routine.
- (i) Point the Recess prerequisite-routing work at **cn-math-taxonomy**'s schema.

---
**Ask (for Ali):** Which do you want to adopt? Suggested:
- (a) **Set the Console IP allowlist** for the hub API key, and check scripts for `speed:"fast"` before Nov 30.
- (b) Read the **inference-hooks** allow/deny contract into the Aegis spec, plus argus's "signed execution grant" model.
- (c) Try **fdic-mcp-server + cu_MCP** in a Meridia session for the NCUA gap.
- (d) Point the Shadow Rock analysis at **mcp-education-data**.
- (e) Decide whether **Personal Finance in Claude** changes the Hypomone member-experience pitch.

## Same-day re-run (Nov 6, 16:05 UTC): last-24h additions

_A second scheduled pass today. SerpAPI 3/3 more calls (Google News qdr:d "Anthropic Claude", `site:github.com` skill/MCP qdr:d, a fintech/K-12/governance "MCP server" qdr:d query that returned nothing), GitHub repo search for repos created Nov 5–6, and commit checks on the official repos since the first run. Official repos had only increments since the first run (claude-code "privacy mod", MCP reference servers v2.3.0); both went to the skipped log. Everything below was checked against the seen index and this file._

### Aegis (governance, approvals, audit)

28. **Ravi041/mcp-policy-library (Apache-2.0, v0.1, created Nov 5)**. Tested OPA/Rego policy packs that decide whether an agent may make a given MCP tool call, for the filesystem, GitHub and Postgres servers. Default is deny, and every refusal says why. It is policy content only: you load it into OPA behind whatever gateway sits between agents and MCP servers (only agentgateway is tested live). The README says plainly that the Postgres pack inspects SQL as text and cannot catch everything, so least-privilege database roles stay underneath. **Why it matters (Aegis):** this is the "the decision lives in reviewed policy, not in the model" layer, and it pairs directly with the inference-hooks allow/deny contract (#2). The Postgres pack is a ready starting point for governing agent access to integra-core. **Trust:** Tier 4 (★0, single author), but tested and candid about its limits. — https://github.com/Ravi041/mcp-policy-library
29. **Prashant-thakur77/Shadow-Run (MIT, created Nov 5)**. Before an agent touches production, it rehearses the risky plan on a clone inside a no-network microVM, measures the effect in Postgres, and applies the plan only if the result matches. The person who requests a change cannot approve it (separate `judge` and `reviewer` identities). Its own test: on 23 held-out risky tasks, harm on prod fell from 10.67 to 2.67 even when every plan was approved unread. **Why it matters (Aegis):** "rehearse, compare, then apply" plus requester-is-not-approver is a stronger approval model than a plain yes/no gate, and its numbers are a benchmark the Aegis spec can cite. It runs on Vultr microVMs, so treat it as a pattern, not something to deploy. **Trust:** Tier 4 (★0, hackathon-style live demo). — https://github.com/Prashant-thakur77/Shadow-Run

### Populi / SIS-LMS (FERPA patterns)

30. **Two school-system MCP servers with student-data guardrails (both MIT, created Nov 5)**. `elehmanndev/clickedu-mcp` lets a teacher run a school-management system (schedule, rosters, attendance, messages) from Claude. It runs locally only, keeps the session cookie on the teacher's disk, and allows writes only as single actions the teacher confirms in the moment: no bulk mode, no loop over a class, no scheduled runs, and student impersonation refused outright. `fabioov/moodle-mcp` is a read-only LMS server (courses, assignments, deadlines, grades, forums) with CI. **Why it matters (Plumbline / Populi / Recess):** neither is Populi, but together they spell out a clean policy for an MCP over student records: read-only by default, one confirmed write at a time, never autonomous. A Populi MCP for Plumbline should take the same stance, and the clickedu "Ethics and scope" section is worth copying into the FERPA notes. **Trust:** Tier 4 (★0 each, single authors). — https://github.com/elehmanndev/clickedu-mcp · https://github.com/fabioov/moodle-mcp

### Recess / K-12

31. **VIABLE-Learning-Lab/viable (code MIT, data CC BY 4.0, created Nov 5)**. An open kit for "AI that teaches the way a teacher wants." The Harness wraps any agent so that, before answering a learner, it reads the teacher's limit for today, picks a teaching move and the one misconception that fits, and asks how the learner got there instead of handing over the answer. It installs as a skill (`npx skills add VIABLE-Learning-Lab/viable --skill teaching-with-viable`); a separate Engine runs classes on your own server, and a hosted platform sits outside the repo. **Why it matters (Recess):** this is the teacher-controlled, misconception-first behavior the Shadow Rock math-gap and prerequisite-routing work needs, as a reusable skill rather than a product to buy. It pairs with cn-math-taxonomy (#27): that gives the prerequisite graph, this gives the teaching move. Check its misconception data against the 5th-grade gap report before relying on it. **Trust:** Tier 4 (organization account, ★0, day-1, CI tests). — https://github.com/VIABLE-Learning-Lab/viable

### Meridia (corpus / RAG)

32. **mauriciosutton/rag-ingestion-pipeline ("dropbox-rag", MIT, created Nov 5)**. Indexes chosen Dropbox folders for search. Docling OCR and a local llama.cpp summary per document run in Docker on your own host; chunks then go to Postgres (pgvector, full-text and trigram search), and an MCP server answers questions with citations to document and page. It needs a Voyage AI key (the free tier works) and assumes Supabase, though the schema is plain Postgres. **Why it matters (Meridia corpus):** this is close to the AIA corpus pipeline that has stalled, and it reads straight from Dropbox, where the hub lives. The main change is swapping Supabase for the NAS Postgres; the prompts are tuned for real-estate deal documents and need re-pointing. **Trust:** Tier 4 (★0, single author, day-1). Read the code before giving it a Dropbox token, and use a read-only app scope as its README says. — https://github.com/mauriciosutton/rag-ingestion-pipeline

**Re-run asks:**
- (j) Load **mcp-policy-library**'s Postgres pack as the first Aegis policy-as-code layer, and add Shadow Run's requester-is-not-approver rule to the spec.
- (k) Try the **VIABLE** teaching skill, with cn-math-taxonomy, against the Shadow Rock 5th-grade gap report.
- (l) Decide whether **dropbox-rag** (re-pointed at NAS Postgres) unblocks the Meridia corpus ingestion.
