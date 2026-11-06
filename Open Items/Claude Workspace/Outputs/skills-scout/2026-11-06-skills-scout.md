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

- **Populi / SIS-LMS / FERPA:** nothing.
- **KSW (grants / music-ed):** nothing.
- **NAS / Docker / Postgres:** only `Balanov/shim` (★466, a tiny local-first harness with MCP and skills), logged as skipped.
- **Recess teacher-facing AI:** coverage is still the July Claude for Teachers launch (already seen).

---
**Ask (for Ali):** Which do you want to adopt? Suggested:
- (a) **Set the Console IP allowlist** for the hub API key, and check scripts for `speed:"fast"` before Nov 30.
- (b) Read the **inference-hooks** allow/deny contract into the Aegis spec, plus argus's "signed execution grant" model.
- (c) Try **fdic-mcp-server + cu_MCP** in a Meridia session for the NCUA gap.
- (d) Point the Shadow Rock analysis at **mcp-education-data**.
- (e) Decide whether **Personal Finance in Claude** changes the Hypomone member-experience pitch.
