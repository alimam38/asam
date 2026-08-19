# Skills Scout — 2026-08-19

_Scan window: Aug 17–19 (delta since 08-18 run). SerpAPI recency layer used (3/3 budget). Quiet day in Tier 1; the signal is in MCP governance._

## Official / Tier 1

- **Claude Code v2.1.235** (Aug 18) — Optional spellcheck in prompts, better terminal list rendering, session/permission/dialog/slash-command fixes, and faster background cloud sessions. Routine but worth knowing before your next `claude` update; the cloud-session perf touches scheduled/Cowork-style runs like this one. _Trust: Tier 1 (official changelog via releasebot)._
- **claude-plugins-community adds a deterministic static pin check for auto-exec MCP launchers** (CI, Aug 19) — The community marketplace's scanner now statically verifies that plugins auto-launching MCP servers pin their sources. Small commit, real signal: Anthropic keeps hardening the skill/plugin supply chain — a pattern worth copying in any Aegis-governed skill registry. _Trust: Tier 1 infra (anthropics/claude-plugins-community)._
- Otherwise quiet: official plugin marketplace showed version bumps only Aug 18–19 (no new vendors), and anthropics/skills only renamed claude-academy-guide → academy-guide (increment of the 08-18 item).

## Governance / audit patterns (Aegis)

- **Cloudflare Gateway MCP protocol detection + AI Security dashboard** — Cloudflare One's Gateway now detects MCP traffic on the wire, makes "shadow MCP" (servers employees wire up without approval) visible, and can block MCP calls that bypass approved portals; ships with an AI Security dashboard and an enterprise MCP reference architecture. This is the strongest network-layer answer yet to MCP sprawl — directly relevant to Aegis's governance-not-guardrails framing, and to any future NAS/tenant deployment. Changelog is Aug 12; press wave ran through Aug 17. _Trust: Tier 2 (official Cloudflare changelog/blog; verify fit before relying on claims)._ https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/
- **promptfoo Agent Skills plugin (evals + red teaming)** (updated Aug 18) — Four skills (promptfoo-evals, provider-setup, redteam-setup, redteam-run) that make Claude Code write correct promptfoo eval suites and security-test configs, installable via `/plugin install promptfoo@promptfoo` from the Claude Code marketplace. Fits two lanes: Aegis (red-team/audit workflow for agentic systems) and your skill-curation practice (eval suites for skills you author). _Trust: Tier 2 (promptfoo is an established eval vendor; official docs)._ https://www.promptfoo.dev/docs/integrations/agent-skill/
- **caura-ai/caura** (433★; formerly MemClaw) — Governed shared memory for AI agent fleets: multi-agent, multi-tenant, MCP-native, with trust tiers on what agents may read/write. The memory lane is saturated (claude-mem, memsearch), but this is the first entrant leading with governance and tenancy rather than recall — the Aegis-shaped take on agent memory, and a pattern reference for Hypomone's multi-tenant thinking. _Trust: Tier 3 (community repo with traction; audit before use)._ https://github.com/caura-ai/caura

## Product / GTM

- **Yuzzyuk/marketing-os** (119★ within ~48h of launch, Aug 17) — "An entire marketing department as one Claude skill": 14 modules covering audits scored 0–100, an 18-tactic hook engine, copy grading, ad diagnosis, GEO, email, launches, and pricing; works in Claude Code and Cowork. Fast day-one traction for the GTM lane (Plumbline/MIG go-to-market). _Trust: Tier 4 (new author, unaudited — read the SKILL.md before install; prompt-only skills are low-risk but verify no exec hooks)._ https://github.com/Yuzzyuk/marketing-os

## Dev tooling / vendor skills wave

- **elevenlabs/skills** (official ElevenLabs, 419★, active Aug 18) — Official skills for building with ElevenLabs (TTS/voice agents). The vendor-skills wave continues; flagged mainly for the KSW lane (music/audio-education tooling) and any future Recess voice/read-aloud features. _Trust: Tier 2 (official vendor repo)._ https://github.com/elevenlabs/skills

## Lanes searched, nothing new

- **Education / K-12 (Recess):** only press recycle of Claude for Teachers (Aug 11–14 stacker syndication) — already covered via k12-teacher-skills (08-09).
- **Fintech / lending (Meridia/Hypomone):** no new Plaid/lending MCP or skill items beyond the Aug-17 Plaid MCP early-access already surfaced.
- **Populi / SIS + Postgres:** no new items in the last 48h.

---
_Skipped-log additions this run: 12 (churn roll-up, increments, off-stack)._
