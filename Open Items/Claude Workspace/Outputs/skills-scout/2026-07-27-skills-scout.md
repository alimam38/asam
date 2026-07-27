# Skills Scout — 2026-07-27

Weekend-quiet window (Jul 26–27): no new Anthropic releases since Claude Code 2.1.219 / Opus 5 (Jul 24).
Reminder (not a repeat item): the stateless MCP spec finalizes tomorrow, Mon Jul 28 — re-check any MCP server
builds after it lands. SerpAPI used (3/3 calls: two qdr:d GitHub sweeps + one news sweep).

## 1. MengTo/Skills — agent skills for designers & builders
- **What:** ~3.6k★ skill library by Meng To (Design+Code) for Claude Code / Codex / Cursor — design-quality site
  building, audit-verify-explain-grade loops, daily-inspiration site generators; actively updated through Jul 25–27.
- **Why it matters:** the strongest designer-authored skill set yet for UI mockups / interactive prototypes — a
  direct feed for the Claude Design question (open item #5) and for SKILL.md curation taste.
- **Trust:** Tier 3 — well-known author with a long design-education track record; still review before install.
- github.com/MengTo/Skills

## 2. browser-use/browser-harness — the agent writes its own skills
- **What:** 16.3k★ "self-healing harness" from the browser-use org: when the agent figures out a non-obvious flow
  it files the SKILL.md itself — the README explicitly says don't hand-author skill files.
- **Why it matters:** first large project to invert skill authoring (agent-generated, self-healing). The pattern —
  not the browser use case — is the takeaway for your skill-forge / agentic-context practice.
- **Trust:** Tier 2/3 — major known org; young pattern, watch more than adopt.
- github.com/browser-use/browser-harness

## 3. Official claude-api skill refreshed — Opus 5 + Managed Agents July wave
- **What:** anthropics/skills updated the claude-api skill Jul 22–24: Claude Opus 5 as the default model across SDK
  examples/pricing tables, plus the Managed Agents July launch wave (cron runs, partner pricing, tool-runner fixes).
- **Why it matters:** if Plumbline agent work touches the Claude API, re-pull this skill so generated code targets
  current models and Managed Agents features instead of stale examples.
- **Trust:** Tier 1 — Anthropic-verified.
- github.com/anthropics/skills (claude-api skill)

## 4. realchendahuang/pi-config — a complete agent setup as one installable
- **What:** one repo = 17 plugins + 18 global skills + 2 MCP servers with a one-line installer and tutorial README;
  ~95★ in its first two days (created Jul 25).
- **Why it matters:** your "agentic context setup, not one-shot prompts" thesis packaged as a reproducible artifact —
  a working template for a MIG/Plumbline standard-setup repo.
- **Trust:** Tier 4 — unknown author, fast traction; read the installer before running it.
- github.com/realchendahuang/pi-config

## 5. whisperx-transcribe — meetings → speaker-labeled Markdown
- **What:** new Claude Code skill/plugin (Jul 26) that runs WhisperX locally to turn audio/video into clean,
  speaker-labeled Markdown an LLM can read without touching raw audio.
- **Why it matters:** cheap ops win for Talbot/Turner — board meetings, committee calls, and chapel recordings become
  searchable minutes without cloud transcription fees or FERPA-awkward third-party uploads.
- **Trust:** Tier 4 — day-one repo, unknown author; local-run, so risk is mostly install hygiene.
- github.com/abubakarsiddik31/whisperx-transcribe
