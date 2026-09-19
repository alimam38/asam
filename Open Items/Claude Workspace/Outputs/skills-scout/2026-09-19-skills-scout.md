# Skills Scout — 2026-09-19

Window: since the 09-17 run (Sep 17–19). Sources per skills-scout-sources.md; SerpAPI used (3/3 calls, qdr:d2 + Google News). Seen-index checked (468 lines).

## Official / Tier 1

- **Claude Code Projects relaunch (beta, cloud)** — Projects rebuilt as "always-on" workspaces that remember context and coordinate multiple parallel agent threads (chief-of-staff pattern); cloud-first, local/CLI parity "must wait." Why: this is Anthropic productizing exactly what the asam scheduled-task fleet + Cowork lanes do by hand — worth a deliberate look at whether any lane moves into a Project thread. Caution from press: parallel threads can burn plan usage fast (The New Stack). Trust: Tier 1 origin via press wave (VentureBeat/Verge/ZDNet/SD Times/Register, 09-17/18). — theverge.com/ai-artificial-intelligence/997134 · venturebeat.com/orchestration/anthropic-launches-claude-code-projects
- **AGENTS.md support lands in Claude Code (v2.1.277, 09-18)** — in a project with no CLAUDE.md, Claude Code now reads AGENTS.md; Anthropic formally adopting OpenAI's cross-agent instruction spec. Also v2.1.276: proxy/gateway 400 hotfix. Why: affects repo-memory conventions across asam and every venture repo (keep CLAUDE.md canonical; AGENTS.md now a viable cross-tool fallback if Codex/other agents ever touch the repos). Ignore "Claude Code fully open-source" framing circulating on 36Kr — only the AGENTS.md adoption is confirmed by Tier 1/2 sources. Trust: Tier 1 (changelog via releasebot; The Register). — theregister.com/ai-and-ml/2026/09/18/anthropic-decides-to-support-openais-markdown-instructions-spec · releasebot.io/updates/anthropic/claude-code
- **Official plugin directory adds: Wingspan + incident.io (09-18)** — Wingspan (contractor payroll/benefits ops; fintech-adjacent) and incident.io (incident response/on-call ops). Plus partner-metadata touch-ups (Qodo, Airwallex). Why: directory watch; Wingspan is a light Hypomone-lane signal (contractor-finance workflows as plugins), incident.io is an ops/audit-trail pattern. Trust: Tier 1 (anthropics/claude-plugins-official #6258/#6252). — github.com/anthropics/claude-plugins-official

## Security (cross-lane — act on this one)

- **"Plugin4Shell" — plugin-install RCE class across Claude Code / Codex / Copilot / Gemini CLI** — AIR Security disclosed a flaw letting a repository owner swap pinned plugin code (bypasses SHA pinning), i.e. a plugin you vetted can be silently replaced upstream; billed as the first cross-agent AI supply-chain vuln. Claude Code and Codex are patched; Copilot/Gemini CLI reportedly still exposed at disclosure. Why: Ali installs Tier 3/4 plugins weekly off this digest — update Claude Code to current (≥2.1.276/277) before the next install, and treat "pinned" third-party plugins as re-vettable. Trust: Tier 2 (thehackernews.com + vendor writeup; multiple carriers). — thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html · air.security/blog-posts/plugin4shell

## Claude / Cowork / skill-authoring lane

- **scs0209/skilldiff** — behavioral regression testing for agent skills: runs the skill in a real agent harness and diffs behavior on every PR. Why: pairs with skill-forge + `claude plugin eval` for the growing asam skill fleet — regression-diff is the missing piece after authoring. Trust: Tier 4 (★4, d1 — unknown author, read before use). — github.com/scs0209/skilldiff
- **Mine-FNL/skillmd-lint** — SKILL.md linter/validator against the open spec: 22 rules + JSON Schema, CI-friendly, offline, no API key. Why: cheap CI gate for asam's .claude/skills and delivered SKILL.md files. Trust: Tier 4 (new, unknown author; offline/no-key lowers risk). — github.com/Mine-FNL/skillmd-lint

## Fintech / lending — Meridia & Hypomone lane

- **AI Consulting Network: open-source library expanded to 90 agent skills for CRE underwriting/lending** (09-18 PR) — commercial real estate underwriting, lease abstraction, loan workflows as agent skills. Why: closest public analog yet to Hypomone/Meridia-style lending workflow skills — worth mining for underwriting-skill structure even if CRE ≠ community lending. Trust: Tier 4 (GlobeNewswire press release, unverified library — inspect before any use). — streetinsider.com (Globe Newswire, 09-18)
- **Carlosdalv669/formify-skills** — skills for e-signature contracts, form fills, and identity verification (BankID-flavored). Why: The Charter as structured intake + membership onboarding will need exactly this shape (sign/verify/track); pattern reference more than install candidate. Trust: Tier 4 (unknown author, touches identity — do not connect real credentials). — github.com/Carlosdalv669/formify-skills

## Governance / audit — Aegis lane

- **Credal governed MCP platform** — centralized MCP gateway pitching consolidated audit logs across Claude/ChatGPT/Cursor plus templated, governed MCP servers; actively pushed this week. Why: another proof point for Aegis's governance-not-guardrails thesis (audit-trail-first agent access); vocabulary worth borrowing for the JPMC-style positioning. Trust: Tier 2 (established vendor, marketing page). — credal.ai/products/mcp-platform
- **Tenable CyberAgents Exchange listing GRC skills for Claude** — Tenable's exchange now carries governance/risk/compliance agent skills (e.g. ComplyAgent, FedRAMP-flavored) targeted at Claude Code/Desktop. Why: a major security vendor becoming a skills distribution channel for compliance work — Aegis-relevant pattern (and a place to watch for audit-pattern prior art). Trust: Tier 2 (Tenable-operated directory; individual skills vary — vet per item). — exchange.tenable.com/browse

## Education — Recess lane

- **Claude Secure launches at WashU (09-18)** — Washington University rolls out "Claude Secure," a locked-down workspace tier alongside Claude Edu for faculty/staff with sensitive data. Why: the FERPA-conscious deployment shape (secure workspace tiers per data sensitivity) is the pattern Recess/Shadow Rock will be asked about; higher-ed today, district-level tomorrow. Trust: Tier 2 (official university IT announcement of a Tier 1 program). — it.washu.edu/2026/09/18/claude-secure-launches-at-washu
- **Claude Academy: "Collaborating with AI" collection + Education Report on discernment** — new Academy collection including survey work on how people check Claude's output. Why: directly usable framing for Recess teacher-facing AI (educator discernment/verification is the adoption blocker); K-12 lane otherwise quiet this window. Trust: Tier 1. — academy.claude.com/collections/collaborating-with-ai

## Lanes searched, nothing new

- **Populi / SIS / Postgres-NAS**: nothing new this window (pgEdge GA was logged 09-17 as an increment).
- **anthropics/skills**: no commits since 09-16. **KSW (grants/music-ed)**: nothing.
