# Skills Scout — 2026-09-14

_Window: 2026-09-13 → 09-14 (last scan 09-13). Method: SerpAPI qdr:d ×3 (GitHub 24h, Google News, lane keywords) + GitHub API (topic searches, official-repo commits, Claude Code changelog) + built-in web search. Note: WebFetch to anthropic.com/releasebot was permission-blocked this run; official items verified via GitHub API + search snippets instead._

## Official / Tier 1

- **BlackRock Advisor Center plugin added to the official directory** (claude-plugins-official #6094, Sep 13). Skills-only plugin from `blackrock/advisor-center-agent-skills` (Apache-2.0): six SKILL.md workflows plus rendering/design assets for advisor work. Why it matters: the clearest Tier-1 signal yet that regulated-finance institutions are shipping official skills through Anthropic's pipeline — a direct pattern reference for how Meridia/Hypomone could package institutional-finance skills (and worth skimming their SKILL.md structure). Trust: Anthropic-verified directory; content authored by BlackRock. https://github.com/anthropics/claude-plugins-official/pull/6094
- **Quiet lanes:** No new Claude Code release (changelog still tops at v2.1.270, surfaced 09-13). `anthropics/skills` has no commits since 09-12. The plugin directory otherwise saw only routine version bumps (~30 on Sep 13).

## Governance / agent audit (Aegis)

- **Salt "Claude Connect"** — Salt Security product giving continuous MCP-server visibility/inventory for Claude Enterprise orgs (Security Boulevard, Sep 9 — just outside window, caught via news sweep). Why: MCP-estate observability is exactly the governance surface Aegis cares about; also relevant if Plumbline tenants ever run Claude Enterprise. Trust: Tier 2 vendor press — capability claims unverified. https://securityboulevard.com/2026/09/introducing-the-salt-claude-connect-continuous-mcp-server-visibility-for-claude-enterprise/
- **chenqg618/compliance-skills** (Sep 13, ★0, EN/ZH) — mechanical-check agent skills for contracts, invoices, tender documents and ad copy where *every finding is recomputable evidence*, fully offline, no model calls. Why: the evidence-not-vibes checking pattern maps onto Aegis audit-trail thinking and Turner finance/covenant checking. Trust: Tier 4, day-one, unvetted — read before use. https://github.com/chenqg618/compliance-skills
- **pliablepixels/gap-trap** (Sep 13, ★22 in ~1 day — real early traction) — installs rules and gates in a repo so AI-written code stays correct without human review of every line. Why: governed-agent-coding gates for Plumbline/Hypomone repos; overlaps your proposal-review/print-preflight "gate" philosophy applied to code. Trust: Tier 4 community. https://github.com/pliablepixels/gap-trap
- **SSRN preprint: skill "operational identity" can exceed a signed directory** — argues Agent Skills combine instructions + files + packages + tools + services, so signing the directory alone under-scopes what you're trusting; proposes versioned transitive dependency-closure binding (Sep 13-ish). Why: the academic backbone for the skill-supply-chain thread you've been tracking (cisco skill-scanner, NVIDIA-Verified Skills, ibl.ai shadow agents). Trust: Tier 3 preprint, not peer-reviewed. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7456458
- **allierays/agentic-architecture-review** (Sep 14, ★0) — skill that reviews/redesigns agentic architectures on the principle "be no more agentic than the problem requires"; classifies every component before allowing agency. Why: useful stance for Aegis's governed-core engine and for keeping Plumbline's automation surface small. Trust: Tier 4, day-one. https://github.com/allierays/agentic-architecture-review

## Skill curation & Claude Code ops

- **nktznl/skillwise** (Sep 14, ★0) — `npx skillwise`: scans a project, finds the Agent Skills it's *missing*, and audits candidate skills before you trust them. Why: install-side counterpart to this scout — discovery + pre-trust audit in one CLI; worth a test drive on the asam repo. Trust: Tier 4, day-one, run in a sandbox first. https://github.com/nktznl/skillwise
- **HarveyJhuang1010/unhobble** (Sep 14, ★0) — slims CLAUDE.md, rules, skills and harness config for newer models: measure first, re-verify every fact, propose cuts once. Why: directly the "agentic context setup" lane — post-Fable-5.1 context diets are exactly the maintenance your MASTER.md/lane-registry setup will need. Trust: Tier 4, day-one. https://github.com/HarveyJhuang1010/unhobble
- **bjcoombs/ai-native-toolkit** (★30, active again Sep 14) [backfilled, Jan 2026] — Claude Code plugin bundling codebase-readiness scoring (/assess), Six-Thinking-Hats deliberation (/huddle), AI-slop removal (/deslop) and *its own* /skill-forge skill-hardening command. Why: overlaps three of your installed skills (skill-forge by name, proposal-review, slop-check) — worth a comparative skim, and note the /skill-forge name collision before installing. Trust: Tier 3/4, modest traction. https://github.com/bjcoombs/ai-native-toolkit
- **Kerneta/daidocs** (Sep 13, ★10 d1) — open plain-text `.dai` file format for AI long-term memory on disk, readable by Claude/GPT/Gemini/grep, with an MCP server. Why: the agent-memory lane is crowded (agent-memory, okf, baron…), but this is the first *open-format* pitch — closest to your Dropbox/GitHub file-as-memory pattern. Trust: Tier 4; watch rather than adopt. https://github.com/Kerneta/daidocs

## Design / UX (Plumbline, Claude Design lane)

- **DrSmile444/ux-crux** (Sep 13, ★0) — evidence-driven UX review skills for coding agents: usability, psychology, accessibility, product and trust, each finding graded by evidence strength. Why: a review gate for Plumbline's dashboard UI that matches your evidence-graded-review taste (verified-roster, slop-check). Trust: Tier 4, day-one. https://github.com/DrSmile444/ux-crux

## Fintech / lending data (Meridia · Hypomone)

- Lane searched (SerpAPI lane query + Google News). Nothing new inside the window beyond the BlackRock item above (filed under Tier 1). Aave's official DeFi-lending MCP (Sep 9) and Futurum's institutional-intelligence MCP (Sep 11) went to the skipped log — fintech-adjacent but DeFi/market-intel, not community lending.

## Education / K-12 (Recess)

- Lane searched. No new tools in the window — only sentiment press (a Penn student op-ed against the university's Claude partnership, Sep 13; logged). Claude for Teachers coverage in results is the July launch, already surfaced.

---
_Skipped log updated with 7 entries (quota-reset increment, genpark flood increment, SEO-repo caution trio, off-lane sweep). Seen index +11._
