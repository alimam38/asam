# Skills Scout — 2026-11-12

Window: Nov 11–12, 2026 (last ~24–36h). Sources: SerpAPI (3 calls, past-24h: GitHub site query returned no results; Google News + Anthropic-domain queries useful), built-in web search, GitHub API (new repos created ≥ Nov 11; commits to anthropics/skills, claude-plugins-official, knowledge-work-plugins, claude-code). Every item below was checked against the seen index.

**Bottom line:** A quiet day for official releases. anthropics/skills had no new commits; claude-plugins-official added an off-focus manufacturing plugin and more security-guidance fixes (logged as skipped). What matters today is **security posture** (two Claude Code credential-exposure stories) and one **Meridia-relevant find** (a local MCP that prepares a provisional patent packet).

---

## Official / Tier 1

1. **"Per-message effort" — Claude Platform docs** — The API now documents changing the effort level partway through a conversation with a `system` message, without losing the prompt cache. *Why it matters:* lets Plumbline and Hypomone API flows run cheap, low-effort turns by default and switch to high effort only for hard steps (reconciliation, underwriting logic) without paying again to re-cache context. *Trust:* Tier 1 (platform.claude.com/docs/…/build-with-claude/effort-per-message). Google indexed the page within the last 24h; the exact launch date is unverified. Check the English page before building on it.

2. **Lydia Hallie (Anthropic) at AI Engineer: "Rethinking Claude Code best practices"** — In her talk, humans caught only about 14% of the dangerous commands they were asked to approve, while auto mode blocked about 89%. Her advice: stop approving every command by hand. *Why it matters:* this is evidence on approval fatigue for the **Aegis** lane (governance-alert approvals). Human-in-the-loop only works when approvals are rare and meaningful, so let a classifier gate routine actions and route only real exceptions to a human. *Trust:* Tier 1 origin; seen only through a Tier 4 recap (finance.biggo.com/podcast/38f9e32eae85e487). Confirm the figures against the talk recording before quoting them.

## Security posture (Claude Code / Cowork — all lanes)

3. **Claude Code "Yes, and don't ask again" writes secrets into `.claude/settings.local.json`** (GitGuardian, Nov 9; updated Nov 11) — When you pick "don't ask again", Claude Code saves the full shell command as an allow rule, including any secrets in it. GitGuardian found 31,088 secrets across 23,276 public GitHub repos (5,343 still valid) and 613 more in Docker Hub images. `settings.json`, `CLAUDE.md` and `.credentials.json` can be affected too. Boris Cherny (Claude Code lead) says a fix is being looked at; auto mode and built-in secret scanning are being prototyped. *Why it matters:* the asam repo and every NAS/Docker build (Meridia, Hypomone) are exposed to this pattern. **Action:** check `.claude/` across your repos for secret-bearing allow rules, add `.claude/` to `.gitignore` and `.dockerignore`, and rotate anything found. *Trust:* Tier 2 vendor research (blog.gitguardian.com/claude-code-settings-local-json-secrets-docker-hub), widely reported (Ars Technica, CSO, iTnews).

4. **Darktrace: stolen Claude API keys can turn Claude Code into a remote-controlled implant** (Help Net Security, Nov 12) — Darktrace showed this in a lab. With stolen keys, an attacker used Console **memory stores** as a job queue and the **Files API** to exfiltrate a 1 GB file, running Claude Code with permission prompts disabled. It isn't a platform vulnerability, has not been seen in the wild, and no fix is coming because nothing is broken. *Why it matters:* every scheduled routine here pulls keys from the hub `.env`. Prefer OAuth or identity federation, and keep API keys short-lived, narrowly scoped, and out of dotfiles and shell history. Relevant to the Aegis audit-trail pattern: alert on unusual memory-store or Files API volume. *Trust:* Tier 2 press reporting Tier 2 vendor research (helpnetsecurity.com/2026/11/12/stolen-claude-api-keys-remote-controlled-implant).

## Meridia / EIG (IP & patents)

5. **ckaico/patty v0.6.0 — local MCP server for software inventions** (created Nov 11; ★4; Apache-2.0; TypeScript) — Runs with Claude Code. It maps the mechanisms in a repo with `file:line` evidence, searches prior art (patents, papers, repos), and builds a per-element prior-art chart. It then drafts a **US provisional patent application** (specification, figures, cover-sheet worksheet, docket), and a check step fails the packet on uncited claims or limiting language. It also does patent clearance and trademark knockout checks. It never signs, pays or files, and it is not legal advice. *Why it matters:* Meridia's 3 planned provisionals (FPS, Trust Index, governance-not-guardrails) are unfiled and block all external motion. This could produce a structured first draft and prior-art chart for counsel to review, which saves money and time. *Trust:* Tier 4 (new author, day-1 repo) — install with caution. Run it only on a sandbox copy of the code, review what its prior-art fetches send out, and have a patent attorney review any packet.

## Aegis (governance / agent safety)

6. **PrashnaLabs/agent-blast-radius — agent skill** (created Nov 11) — Reads an agent's codebase and writes `BLAST_RADIUS.md`. It answers two questions: what crosses the boundary (hosted model calls, telemetry, start-time `npx`/`pip` fetches, SaaS connectors), and what a poisoned document or compromised host could do inside. Findings come with `file:line` evidence, OWASP agentic (ASI) IDs, and the smallest fix for each. *Why it matters:* a ready-made pre-deployment audit for Aegis, and for anything bound for the Synology NAS (Meridia/Hypomone on Docker). It matches the "governance-not-guardrails" thesis. *Trust:* Tier 4 — read the skill before running it; it is read-only analysis.

## Skills curation / MCP

7. **pamelafox/skills-mcp-server** (created Nov 11) — A small local FastMCP server that serves every `SKILL.md` folder under `./skills` over MCP. It re-reads skills on each request, so edits apply without a restart, and it runs over stdio or HTTP. It works with VS Code's `chat.agentHost.mcpSkills.enabled`. *Why it matters:* a simple, inspectable way to serve one skill library to several agents (Claude Code, VS Code, other hosts) from the asam repo or the NAS, instead of copying skills into each tool. *Trust:* Tier 3 (known author: Pamela Fox, Microsoft Python advocate); tiny codebase, no license yet.

---

**Lanes searched with nothing new:** K-12/Recess (only a Chinese personal-study classroom agent → skipped), fintech/lending MCP (no newly dated launches; Bud/Nymbus/Carrington already seen), Populi/SIS, Postgres MCP, KSW/grants.

*Ask:* Pick what to adopt. Suggested now: **#3 (repo secret sweep, today)**, **#5 (trial Patty on a sandbox copy before counsel engagement)**, **#6 (run on Aegis)**.
