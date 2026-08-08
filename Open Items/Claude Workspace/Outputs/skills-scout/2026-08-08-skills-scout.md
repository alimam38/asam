# Skills Scout — 2026-08-08

_Scan window: Aug 5–8 (last committed run was 08-05; this run covers the 3-day gap). SerpAPI recency layer used (3/3 calls). All four context files + venture STATUS files read._

## Official / Tier 1

1. **Claude Code cross-session messaging (`SendMessage`, v2.1.224, Aug 7)** — sessions on macOS/Linux can now message each other (`crossSessionInbound` / `dialogExpiry` settings); the Aug 7–8 press wave framed it as the multi-agent-collaboration step. Why it matters: real context handoff between concurrent Cowork/Code sessions — useful for the Plumbline-vs-Hypomone parallel-build pattern and for scheduled-task orchestration. Trust: Anthropic-verified (changelog); coverage 9to5Mac/MacRumors.
2. **Self-hosted Claude Code environments (Aug 6–7)** — `claude self-hosted-runner` (v2.1.224) + platform-side "self-hosted environments": run Claude Code sessions on your own infrastructure with internal-network access and compliance controls. Why it matters: cleanest path yet to running agent sessions against the Synology NAS/Postgres stack without tunneling data out — FERPA (Plumbline/Recess) and Meridia data-control fit; complements MCP Tunnels (seen 06-28). Trust: Anthropic-verified.
3. **Skill & plugin security scanning (Enterprise beta, Aug 6)** — Anthropic now auto-scans third-party skill/plugin uploads for malicious content. Why it matters: first-party answer to the supply-chain wave (malskanner 07-22, SkillSpector 07-28, assay 08-04); governance signal for the Aegis lane and validation of the install-with-caution posture. Enterprise-gated for now. Trust: Anthropic-verified.
4. **PSA: Auto mode becomes Claude Code default "next week" (Aug 7)** — auto mode (fewer permission prompts) flips to default. Why it matters: ops heads-up — review permission settings/managed policies before it lands, especially where scheduled jobs touch repos. Trust: Tier 1 origin via press (9to5Mac, The New Stack).
5. **Claude Code v2.1.222–224 bundle (Aug 5–7)** — 200-subagent spawn cap removed; `/teleport` (move cloud sessions local); marketplace owner-wildcard controls; workflow scripts banned from dynamic `import()`; worktree isolation hardened against destructive git; Bash permission-bypass fixed. Trust: Anthropic-verified (changelog).

## Security alert (cross-lane)

6. **Claude Code + Gemini CLI prompt-injection flaws reach CI secrets (Aug 7)** — reported chain: a crafted GitHub Issue read by the agent can exfiltrate CI workflow secrets. Why it matters: touches the GitHub-workflow lane this job runs on; treat issue-reading automations as untrusted input and keep Claude Code current (the 2.1.223 permission-prompt neutralization fixes land in the same window). Trust: Tier 4 press (The Hacker News, credible outlet) — verify patch status before acting.

## Meridia / Hypomone (fintech & lending)

7. **Plaid × Sierra — Plaid Link inside AI agents (Aug 3–4)** — official partnership putting secure bank-account connection and actions inside Sierra agent conversations. Why it matters: first mainstream template for "agent conversation → authorized bank action" — the interaction pattern Hypomone lending (Gate 2/3) will need; read Plaid's post for the consent/authorization flow. Not a Claude tool. Trust: Tier 2 (official Plaid announcement; CNBC/PYMNTS coverage). https://plaid.com/blog/plaid-link-inside-sierra-ai-agents/
8. **mintlify/index — retrieval engine + MCP server (Aug 5)** — Mintlify's new `npx mint index` retrieval engine, MCP-exposed. Why it matters: docs-corpus RAG infrastructure from a known docs vendor — candidate pattern (or tool) for the Meridia corpus / AIA cataloger pipeline. Early (31★, 3 days old). Trust: Tier 2 (known vendor; verify before use). https://github.com/mintlify/index

## Aegis (governance & audit)

9. **AWS: Agent Skills for Automated Reasoning policies in Bedrock (Aug 6)** — skills that let agents author/apply formal Automated Reasoning policies (provable guardrails). Why it matters: off-stack, but the closest industrial artifact yet to the "governance-not-guardrails" thesis — formal policy verification wrapped as agent skills; read for Aegis approval-gate design and the Meridia patent-3 prior-art file. Trust: Tier 2 (official AWS blog). https://aws.amazon.com/blogs/machine-learning/agent-skills-for-automated-reasoning-policies-in-amazon-bedrock/

## Design / UI (open item #5) + comms

10. **jakubkrehel/skills (~3.2k★)** — interface-craft agent skills: animation, UI polish, accessibility, product writing. Why it matters: strongest community design-skill pack since emilkowalski/skills (07-28); serves the Claude Design / UI-mockup open item for Plumbline dashboards and Hypomone's phone-first Charter UI. Trust: Tier 3 (community, heavy traction; created Jul 10, pushed this week). https://github.com/jakubkrehel/skills
11. **resend/resend-skills (official Resend, refreshed Aug 7)** — Agent Skills for sending/receiving email via Resend. Why it matters: transactional-email capability for agent workflows — Hypomone membership/Charter follow-ups, Plumbline notifications. Trust: Tier 2 (official vendor repo). https://github.com/resend/resend-skills

## Lanes searched, nothing new
- **Education / K-12 (Recess):** no new skills/plugins/MCPs in window — Claude for Teachers ecosystem quiet since the ASSISTments item (logged 08-02).
- **Populi / SIS + Postgres:** vendor-content churn only (Supabase / Tiger Data / pgEdge pieces, all previously surfaced); no new tools.
- **Grants / nonprofit (KSW-adjacent):** nothing new in window.

---
_Method: SerpAPI 3/3 (github qdr:d3, google_news, lane-scoped qdr:w) + built-in web search + Composio GitHub search. Deduped against seen-index through 2026-08-05._
