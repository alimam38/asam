# Skills Scout — 2026-08-23

_Scan window: last ~36h (Aug 22–23, Sat–Sun). Weekend lull on official channels; the 24h GitHub index carried the signal. SerpAPI used (3/3 calls: 24h GitHub-scoped, Google News, 24h Reddit/HN). Official Anthropic repos checked directly via commit log._

## Official / Tier 1

- **Claude Code v2.1.239** (Aug 22) — cost estimates for data-residency workspaces, fullscreen renderer support on Bedrock/Vertex, Python SDK 0.x→1.x migration tooling surfaced in the release, plus proxy/terminal/cross-session-messaging fixes. Why: standing Claude Code lane; the data-residency cost estimates matter if Managed Agents ever host Plumbline tenant work, and the SDK migration tooling pairs with the claude-api skill upgrade surfaced 08-22. Trust: Tier 1 (code.claude.com changelog via releasebot.io).
- Official repos quiet: `anthropics/skills`, `claude-plugins-official`, `claude-plugins-community` verified by commit log — nothing new since the 08-22 digest (claude-api SDK guide #1623, Security v0.10.2, eli5 merge — all already surfaced/logged).

## Agentic context, memory & MCP (standing Claude/Cowork lane)

- **volcengine/OpenViking** — ~32.3k★. "Self-evolving Context Database for AI Agents" from ByteDance's Volcengine: unifies agent memory, knowledge RAG, and skills in one store. Why: squarely on the agentic-context + corpus/RAG axis — worth reading for Meridia corpus architecture even if never adopted. Trust: Tier 2 — major-vendor OSS with real traction, but a China-hosted vendor's stack; review data flow before pointing any tenant/FERPA/financial data at it.
- **yvgude/lean-ctx** — ~3.6k★. LeanCTX: a single local Rust binary as a "context intelligence layer" — decides what the agent reads, remembers what it learns, guards what it touches. Why: context engineering with a governance flavor (controlling what the agent may see) that rhymes with Aegis; local-first fits the NAS posture. Trust: Tier 3 — real traction, community author; audit before trusting the guard claims.
- **mozilla/firefox-devtools-mcp** — 371★, active this week (pushed Aug 21, trending in the 24h index). Official Mozilla MCP server that lets agents inspect and control Firefox via the Remote Debugging Protocol. Why: MCP lane; a vendor-official second-browser debugging path for Plumbline dashboard/frontend work. Trust: Tier 2 — Mozilla org repo.
- **oxbshw/watch-skill** — 308★. Video understanding + self-verification: turns videos, streams, and agent screen recordings into searchable timestamped evidence, then runs "THE LOOP" (inspect → fix → verify). Why: extends the verification-loops lane (surfaced 07-23) to the visual channel; conceptual pair to Cowork's "Record a skill" (07-22). Trust: Tier 3/4 — community, decent stars; verify the evidence-extraction claims before relying on them.

## Aegis — governance & audit patterns

- **mizcausevic-dev/evidence-labeling-protocol** (+ companion **deterministic-core-llm-surface-pattern**) — two day-one skills: (1) a no-fabrication evidence taxonomy — every agent claim about tests/deployments/systems labeled Observed / Executed / Verified / Predicted / Blocked; (2) a "95/5" pattern keeping AI features mostly deterministic code with the LLM confined to the thin surface that needs judgment. Why: both read like Aegis doctrine (audit-trail honesty, governed core engine) — cheap to mine for patterns even without installing. Trust: Tier 4 — 0★ day-one, install-with-caution; same author as mcp-kinetic-gain (surfaced 07-21).

## Meridia / Hypomone — fintech & lending

- **Agentic Banking Directory (Open Banking Tracker)** — a standing directory of banks/platforms shipping first-party MCP servers, plus the surrounding agentic-banking landscape (consent flows, transfer limits, audit trails): Griffin, Grasshopper, Coinbase, Nymbus core-banking MCP (19 tools), Meow's "agentic banking platform," etc. Why: a scan-ready map of exactly Hypomone's infra/competitive terrain (membership-lending for misbanked operators); worth bookmarking as a recurring source. Trust: Tier 2 — known tracker; entries date to Mar–Apr 2026 but the directory itself was never surfaced here. https://www.openbankingtracker.com/agentic-banking-and-mcp

## Recess — K-12 education

- Searched (news + GitHub 24h index + education-MCP queries): nothing new in this window — only recycles of Claude for Teachers coverage (lane current as of the 08-09 k12-teacher-skills item).

## Populi / SIS-LMS + Postgres

- Nothing new in this window (GitHub 24h index + registry queries checked).
