# Skills Scout — 2026-08-01

_Scan window Jul 30 – Aug 1. Official Anthropic channels quiet since the Jul 28 MCP-spec rollout (already logged); today's signal is community + vendor side. SerpAPI recency layer used (3/3 budget)._

## 1. ratchet — measured rule-compliance for coding agents
- **What:** PostToolUse hook + CLI that measures every Edit/Write your agent makes against minimalism rules (new deps, duplicate helpers, hand-rolled stdlib, wrapper/YAGNI), grades findings certain/likely/heuristic, reports back into the live session, and keeps a per-repo complexity ledger with an accepted "mark". advise/guard/strict budget modes; existing debt grandfathered via baseline.
- **Why you:** the missing enforcement half of your CLAUDE.md / agentic-context-setup lane — injected rules are open-loop; this closes the loop with numbers, not prompts. Pairs with karpathy-coder and the verification-loops doctrine (07-23).
- **Trust:** Tier 4 (unknown author, created Jul 31) but ~400★/43 forks in day one, 115 tests, honest limits section. Hooks execute code on every edit — read the hook source before installing. — github.com/0xwilliamortiz/ratchet

## 2. better-skill-creator — a skill-creator rewrite that refuses to guess
- **What:** unaffiliated Apache-2.0 derivative of Anthropic's skill-creator focused on trustworthy measurement: evals that fail loudly instead of reporting "Delta +0.00" from zero runs, target-aware frontmatter validation (Claude Code's 31 keys vs agentskills.io's 6 vs claude.ai caps), spend caps on the description optimizer, probe isolation, Windows-safe I/O.
- **Why you:** you author and curate skills daily (skill-forge; skill-creator evals surfaced 06-20) — its reproduced-bug list doubles as a checklist of silent failure modes in your own skill-testing loops.
- **Trust:** Tier 4, day-one (Jul 31), few stars — but a detailed reproduction-backed README; cheap to read, vet before adopting. — github.com/OpenCnid/better-skill-creator

## 3. QuickBooks deepens its Claude integration — payroll + lending join invoicing
- **What:** Intuit announced (Jul 28) expanded QuickBooks capabilities inside Claude and ChatGPT: sales, invoicing, payroll, and lending features — building on the QuickBooks Connector (surfaced 07-03) and the dev MCP server (06-23).
- **Why you:** squarely the Talbot/Turner month-end + Plumbline stack; payroll actions in-Claude would touch your QBO+Gusto lane.
- **Trust:** Tier 2 (vendor-official blog); verify which features reach your QBO plan/region before relying on it. — intuit.com/blog/news-social/quickbooks-expands-into-claude-and-chatgpt-with-new-sales-invoicing-payroll-and-lending-features/

## 4. architecture-drawer — text → editable PowerPoint architecture diagrams
- **What:** Claude Code/Codex skill that turns a text description of a system into an editable .pptx architecture diagram made of native shapes (not a rendered image), so you can hand-tune instead of regenerate.
- **Why you:** fits Plumbline spec/GTM deck work alongside your pptx + slide-deck-builder skills.
- **Trust:** Tier 4, created Jul 31, 15★ day one; small scope, low blast radius. — github.com/Andy1314Chen/architecture-drawer

## 5. The "content → skill" distillation wave keeps building
- **What:** two more day-one repos converting books/PDFs/courses into structured local Agent Skills — 47thtechcorner/RayCodes_BookToSkill ("turn any PDF into a local AI skill") and ilia-pluzhnikov/book-distill (adds triple-verification; RU localization of cangjie-skill) — following video-to-skill (seen 07-31).
- **Why you:** your skill-distiller pattern going ecosystem-wide; watch for a winner to standardize on rather than adopting either yet.
- **Trust:** Tier 4, both day-one, low stars; treat as trend signal, not tools. — github.com/47thtechcorner/RayCodes_BookToSkill
