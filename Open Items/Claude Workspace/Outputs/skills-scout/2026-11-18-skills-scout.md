# Skills Scout — 2026-11-18

_Window: Nov 16–18 2026. Sources: Tier 1 repos (anthropics/claude-code, claude-plugins-official, skills, knowledge-work-plugins), Anthropic news/release notes, Releasebot, Cowork changelog, GitHub repo search (created ≥ Nov 16), web search across focus lanes, SerpAPI (3 × 24h queries; the site:github.com query returned 0 results). Deduped against seen-index.md._

## Official / Tier 1

### 1. Claude Code 2.1.327 (published to CHANGELOG Nov 17)
- **What:** Adds `claude mcp add-json <name> -`, which reads a server's JSON from stdin so tokens stay off the command line and out of shell history. `/status` now lists broken agent, skill, command and output-style files, ignored permission settings, and hook matchers that never match. Fixes: `claude mcp add/remove` with project scope no longer deletes other keys in `.mcp.json`; remote MCP servers are retried in the background for about a day after an outage such as a VPN drop; a new artifact that was approved is no longer refused in a **cloud scheduled task's session** (orgs that require per-artifact approval); Remote Control worktree mode no longer deletes a running session's git-ignored files such as `.env`; `--agents` and plugin agents now survive a reload or resume.
- **Why it matters:** Standing Claude Code / MCP / scheduled-tasks lane. `add-json` from stdin suits the single `.env` credential hub, and `/status` flags skill and hook problems you would otherwise have to hunt for. The scheduled-task artifact fix and the remote-MCP retry apply directly to routines like this one, and to NAS-hosted MCP servers reached over VPN (Meridia/Hypomone).
- **Trust:** Anthropic-verified (github.com/anthropics/claude-code CHANGELOG.md).

## Recess / K-12

### 2. Anthropic adopts AFT/UFT contract protections for Claude for Teachers (Nov 10) [backfill]
- **What:** Districts can now sign contractually enforceable safety and data-privacy terms for Claude for Teachers. The contract language was developed for the AFT-linked National Academy for AI Instruction (NYC). Terms: student, educator and customer data is not used for training, apart from specific research and safety data; Anthropic must alert customers about breaches and mitigate them, even after a contract ends; higher-risk tools (biometrics, memory, profiling, tracking) get extra review; districts must make sure humans review AI-informed grading, discipline and placement decisions. The terms cover Claude for Teachers only, not third-party tools built on Claude. Existing district contracts are covered; districts must opt in for future licences.
- **Why it matters:** Recess / Shadow Rock: concrete DPA language and a human-review requirement that line up with the pilot's FERPA discipline and governance correction ledger. Worth citing in the 2026–27 pilot plan, and a template for Recess's own vendor stance.
- **Trust:** Tier 2 (EdWeek reporting on an Anthropic announcement): edweek.org/technology/anthropic-agrees-to-protections-for-teachers-who-use-claude/2026/11

### 3. fluki3-06s/songngan-mcp: self-hosted Google Classroom MCP (created Nov 16)
- **What:** stdio MCP server (Node 20+, MIT) that lets Claude read classes, assignments, due dates, attachments, announcements and grades through your own Google Cloud OAuth client. Token is kept in the OS keychain; no server in between.
- **Why it matters:** Recess: a pattern for read-only LMS access with no third-party data path. It is built for students; a teacher/admin-scoped fork would need different OAuth scopes and FERPA review. Relevant only if Shadow Rock uses Google Classroom (not confirmed).
- **Trust:** Tier 4 (new repo, 7★): install with caution; review the scopes before any use with real student accounts. github.com/fluki3-06s/songngan-mcp

## Plumbline / Talbot / Hypomone (sensitive-data handling)

### 4. min-1225/veil-skill: mask PII before Claude sees it, unmask after (created Nov 17)
- **What:** Claude Code skill (MIT, zero-dep Node core, optional local NER) that replaces names, organisations, phone numbers, IDs, account numbers and API keys with tokens like `[PERSON_1]`, lets Claude work on the masked text, then restores the originals locally. Includes a leak check.
- **Why it matters:** A FERPA-aware pattern for Plumbline and Talbot Hall work (student rosters, balances) and for Hypomone member intake (Charter responses). Useful as a design reference for a governance-gate step even if the skill itself isn't adopted. Language coverage leans KO/EN/JA/ZH; test English edge cases (SSNs, Populi IDs).
- **Trust:** Tier 4 (new, 9★, has CI tests): install with caution; read the masking script before trusting it with real records. github.com/min-1225/veil-skill

## Aegis / governance patterns

### 5. tusharsrivastava/shark-skills: operator pattern plugin, audited merges (created Nov 16)
- **What:** Claude Code plugin where the main session never writes code. It acts as an "operator" that briefs subagent lanes building in parallel against one shared contract. Every merge is audited and every bug gets a root cause before a fix. Ships a debugger MCP server; can be enabled for a whole team through `.claude/settings.json`.
- **Why it matters:** Aegis (approval and audit patterns for agents) and how you run lanes in general: it codifies "audited merge" and "root cause before fix" as rules. Worth mining for rules rather than installing whole.
- **Trust:** Tier 4 (12★): install with caution; it pulls an npx MCP server. github.com/tusharsrivastava/shark-skills

## Lanes searched, nothing new in window
- **Fintech/lending (Meridia/Hypomone):** no new in-window MCPs beyond ones already seen (Blend, Lendscape, Grasshopper/Narmi, Plaid, Finom, Schwab, Omni-53).
- **Populi / SIS, Postgres/NAS, grants/KSW, Claude Design, Cowork changelog:** nothing dated Nov 16–18. The newest Cowork changelog entry is Oct 22.
- **anthropics/skills, knowledge-work-plugins:** no new commits beyond what's already logged. **claude-plugins-official:** only security-guidance fixes and a Discord tool (see skipped log).

## Ask
Pick any to adopt or trial: (1) start using `claude mcp add-json` from stdin for NAS MCP servers, (2) put the AFT terms into the Recess pilot plan, (4) trial veil on a de-identified Talbot sample, (5) mine shark's rules into the lane OS files.
