# Skills Scout — 2026-11-21 (Sat)

Window: Nov 20–21. SerpAPI: 3/3 calls used (google qdr:d ×2, google_news qdr:d ×1). Sources: Claude Code CHANGELOG, Claude help-center release notes, claude-plugins-official / skills / knowledge-work-plugins commits (via Composio), GitHub repo search (created ≥ Nov 19), web search for the K-12 and fintech lanes.

**Ask:** pick anything below to adopt. The two items most worth a decision: **#3 skill-distill** (compare it with your existing skill-distiller) and **#4 skillaudit** (a check you could run before installing any Tier 4 skill).

---

## Official / Tier 1

1. **Claude Code 2.1.330** — Adds sign-in to orgs managed in the new Enterprise Admin Console (Claude Code then applies the org's settings and gateway). Adds **easel**, a built-in mod that draws charts on request and under MCP metric results (turn off in `/config`). Self-hosted runner gets `--start-dir` and plugin-marketplace refusal notices. Fixes: claude.ai connectors that share a server URL were being dropped; MCP resources from claude.ai connectors and plugin servers weren't attached when @-mentioned; an MCP server declared by subagents shut down while others still used it; turns failed with "JSON schema is invalid" when many MCP tools had bad schemas; settings and task updates were lost under concurrent saves.
   *Why it matters:* the connector fixes touch your many-connector stack (Composio, Dropbox, QBO). Easel gives Plumbline-style metric pulls a quick chart without building one. *Trust:* Anthropic-verified — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).
2. **Computer use (beta) for Team and Enterprise plans (Nov 20)** — Claude can see a user's screen and work in the desktop apps they allow. Works in Claude Desktop, and from web and mobile where Computer access is on. Rolling out to orgs gradually. Separately, on **Nov 17 Claude Desktop added release channels**: Stable (default) or Latest (about one new version a day).
   *Why it matters:* if Turner is on a Team plan, this is how Claude can drive screens that have no API or connector (Populi screens the API doesn't cover, Authorize.Net). It needs an admin to turn it on, so it's a governance decision (Aegis lane). *Trust:* Anthropic-verified — [release notes](https://support.claude.com/en/articles/12138966-release-notes).

## Skill / plugin curation (Cowork, Claude Code, skill authoring)

3. **sybil-solutions/skill-distill** (MIT, ★98, created Nov 21) — Turns a good Claude Code or Codex session into a skill that an open-weight model can follow to repeat the task.
   *Why it matters:* this does almost the same job as your own `skill-distiller` skill (capture a stronger model's method for a weaker executor). Compare the two and take the best ideas from it rather than installing it. *Trust:* unknown/community — install with caution; it's one day old. [repo](https://github.com/sybil-solutions/skill-distill)
4. **DebugDyanmo/skillaudit** (MIT, ★11, created Nov 19) — Like "npm audit" for agent skills: scans SKILL.md folders for prompt injection, hidden instructions and data exfiltration.
   *Why it matters:* it could be a check you run before installing anything from this digest's Tier 4 items, and it fits the Aegis governance lane. Test it on a known-clean skill before trusting what it reports. *Trust:* unknown/community — install with caution. [repo](https://github.com/DebugDyanmo/skillaudit)

## Governance / audit patterns (Aegis)

5. **AlterAIDev/alter-mcp-servers** (MIT, ★5, created Nov 19) — Gmail and LinkedIn MCP servers where the agent never holds the token: sends and posts wait for human approval, and every call is audited.
   *Why it matters:* the token-custody idea (the agent never sees the credential) goes a step past the approval gateways surfaced earlier (Bastion, SidClaw). It's a reference pattern for Aegis's approval flow; don't use it in production. *Trust:* unknown/community — install with caution. [repo](https://github.com/AlterAIDev/alter-mcp-servers)

## Lanes searched with nothing new

- **K-12 / Recess:** no new Claude-for-Teachers or K-12 MCP news in the window. Latest items (McGraw Hill, AFT/UFT terms) were already surfaced.
- **Fintech / lending (Meridia/Hypomone):** no new lending, credit-union or CDFI MCP launches dated Nov 20–21. Older launches found again (Allocore Jun 2026, LoanPro Oct 2025) are logged in the skipped log.
- **Postgres / NAS / Docker:** only recordari-labs/postgres-mcp (read-only, YAML policies, Docker; ★3), which is weaker than pgharbor (surfaced 11-19), so it's logged in the skipped log.
- **Populi / SIS, grants:** nothing new.

---
_Also checked: anthropics/skills and knowledge-work-plugins had no commits since Nov 20; claude-plugins-official had only increments (logged in the skipped log)._
