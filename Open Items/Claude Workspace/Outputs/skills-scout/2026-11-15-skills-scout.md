# Skills Scout — 2026-11-15

_Window: Nov 14–15 (Sunday, so a quiet window). Sources: Tier 1 changelog/news, releasebot, Google News, GitHub repo search (created ≥ Nov 13), and web search across the lanes. SerpAPI was used for 3 calls: `site:github.com` qdr:w, Google News, and a cross-lane MCP qdr:w query. Everything already in the seen index was dropped; most of this week's Anthropic news (Manufacturing plugin, Meetings, Sheets/Whiteboards/Data, Fable 5.2, self-hosted Managed Agents, CC 2.1.321–325) was surfaced earlier this week._

## Official / Tier 1
- **Nothing new Nov 13–15.** The newest entry on the Claude Code docs changelog page is still 2.1.312 (Oct 27); the GitHub CHANGELOG already reached 2.1.325, and that was surfaced on 11-14. Releasebot (last updated Nov 13) shows only Nov 12 items, all already seen.

## Aegis — governance / approval / audit
- **codersanjay3/mcp-leash**: a one-command scan that finds the dangerous (write/delete/exec) tools across your configured MCP servers and locks them down in Claude Code's permission rules. *Why it matters:* this is the "deny-by-default for agent tools" pattern that Aegis's governance-alert approvals describe, applied to the MCP layer. It pairs with mcp-attest (11-14), which tests authorization while this tool enforces it. It could also tighten the many connectors in Ali's own Cowork setup. *Trust:* Tier 4. Created today, 2★, MIT. Read the code before running it, because it edits your permission settings. [repo](https://github.com/codersanjay3/mcp-leash)

## NAS / Docker / self-hosted ops (Meridia infra, Hypomone Postgres-on-NAS)
- **simbaTmotsi/simba-skills**: agent skills for running self-hosted production safely, covering feedback loops that are safe in production, safe deploys, server maintenance, and setup hygiene for Claude Code. *Why it matters:* the Synology/Docker/Postgres stack behind integra-core and the planned Hypomone ledger is exactly this kind of self-hosted production box. These are guardrail patterns worth comparing against how agents touch the NAS. *Trust:* Tier 4. Created Nov 13, 2★, MIT. Mine it for patterns rather than installing it wholesale. [repo](https://github.com/simbaTmotsi/simba-skills)

## Lanes searched, nothing new
- **Recess / K-12:** only older or recycled items. The Teachfloor MCP is corporate-LMS and undated. The claude-education-skills listings mirror GarethManning (seen 06-25). Both are in the skipped log.
- **Meridia / Hypomone fintech & lending:** the lending-MCP launches that turned up (Blend Autopilot, Carrington, Bud, Nymbus, Narmi) are all already in the seen index.
- **Populi / SIS, Postgres MCP, Claude Design, KSW grants/music:** nothing new in the window.

## Ask
Pick any to adopt. The likeliest pick is **mcp-leash**, as a one-time audit of your own connector sprawl, after reading its code.
