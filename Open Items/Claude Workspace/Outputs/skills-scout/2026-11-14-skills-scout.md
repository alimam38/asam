# Skills Scout — 2026-11-14

_Window: last ~24–48h (Nov 12–14). Sources per skills-scout-sources.md. SerpAPI used 3/3 (qdr:d GitHub/Anthropic queries returned near-nothing again; Google News query mostly older governance-MCP launches → logged to skipped). Composio GitHub search covered last-48h repos. Seen index checked by name + URL; the Nov 12 Anthropic batch (Meetings, self-hosted Managed Agents, Claude for Manufacturing) was already surfaced/logged and is not repeated._

## Official / Tier 1

1. **Claude Code 2.1.325 (Nov 13) — permission changes that can stall scheduled runs**
   - What: Scheduled tasks and `/loop` now **ask before running a skill that declares `allowed-tools` or hooks**; you add `Skill(name)` to `permissions.allow` to let it run unattended. Sandboxed Bash now goes through the normal permission flow by default (`sandbox.autoAllowBashIfSandboxed: true` restores the old no-prompt behavior). "Always allow" in Desktop/IDE/SDK hosts is offered only when the saved rule would really allow that command again, so a scheduled task that relied on one may now **wait for you**. Also: the sandbox now refuses writes to `.claude` settings, skills, agents and hooks in added directories; sandbox helper programs no longer get sign-in tokens or API keys in their environment; `claude plugin validate` reports unsafe paths and links; Cowork cloud sessions and cloud scheduled tasks start even with `sandbox.failIfUnavailable`.
   - Why it matters: This hits your **scheduled-task fleet** (skills scout, ledger sweeps, Talbot reports) and your SKILL.md authoring (skill-forge). Any routine skill whose frontmatter has `allowed-tools`/hooks may now stop and wait for an approval that nobody gives. It mainly affects Claude Code CLI/Desktop hosts. Cloud Cowork runs are touched only by the sandbox line, but that is unconfirmed.
   - Action: list which of your routine skills declare `allowed-tools` or hooks, and add `Skill(name)` allow rules where you want them to run unattended.
   - Trust: Anthropic-verified (code.claude.com/docs/en/changelog). Note: no separate 2.1.324 entry was found.

## Aegis — governance / audit patterns

2. **Balanov/mcp-attest** — github.com/Balanov/mcp-attest
   - What: A harness that checks whether an MCP server's permissions behave the way your policy says. It calls a live server as each identity, builds the identity×tool permission grid automatically, gives the same results on every run (so it can gate CI), and saves request/response logs an auditor can verify. Also runs OAuth checks and OWASP-based checks. Python 3.10+, standard library only. It tests; it does not enforce or block.
   - Why it matters: This is the "evidence an auditor can verify" half of Aegis's governance-alert approvals. It's also a way to show Plumbline's FERPA role boundaries actually hold before tenant #1 relies on them. It pairs with the AGP/SidClaw enforcement-side items from 11-13.
   - Trust: unknown/community → install-with-caution (Tier 4; 5★, created Nov 13). Read the code before pointing it at anything holding real data.

## Meridia / Hypomone — fintech & lending

3. **Charles Schwab's own MCP servers, moving from read-only to agentic (Nov 13)**
   - What: Press reports say Schwab launched first-party MCP servers for retail brokerage clients that go beyond reading data to taking actions (trades, portfolio tasks), with support for multiple LLMs. RIAs are excluded for now.
   - Why it matters: A large regulated financial institution is putting *write-capable* MCP in front of members. That's a reference pattern for Hypomone's later lending steps, which needs a consent, scoping and approval design. Compare with Finom's strictly read-only design from 11-13.
   - Trust: known press (Tier 2: riabiz.com 2026-11-13, fxnewsgroup.com). Scope and safeguard details unverified, and the headline's claim about Schwab's Anthropic exclusivity is commentary. Treat it as a pattern signal, not a spec.

## Lanes searched with nothing new

- **Recess / K-12:** nothing new since the McGraw Hill × Claude for Teachers backfill (11-13).
- **Populi / SIS / FERPA:** no new MCP servers or skills.
- **Postgres / NAS / Docker:** only older pgEdge items (Starfleet, ~late Sep) → skipped log.
- **KSW (grants / music education):** nothing.
- **Claude Design / Cowork:** nothing beyond the 11-12 batch already seen.
- **GitHub last 48h:** mostly off-focus churn (video, game, job-search skills). Another wave of near-identical Blender "AI copilot" repos showed up, each with ~230★ on day one — looks like star-farming, don't trust the star counts.

---
**Your call:** decide whether to (a) add `Skill(name)` allow rules for routine skills that declare `allowed-tools`/hooks (2.1.325), (b) trial mcp-attest against an Aegis mock or a Plumbline dev MCP, (c) file the Schwab pattern into Hypomone lending-step notes.
