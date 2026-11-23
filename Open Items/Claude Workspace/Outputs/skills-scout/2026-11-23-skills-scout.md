# Skills Scout — 2026-11-23

_Window: Nov 22–23, 2026. Deduped against the seen index and skipped log. SerpAPI was degraded: call 1 (`qdr:d` site:github skills query) returned "couldn't get valid results", call 2 hung and timed out, and call 3 was not sent. Built-in web search and Composio GitHub search (repos created on or after Nov 22, plus official-repo commit checks) covered the rest._

**Light day.** No new Claude Code release and no Anthropic product news. The most useful finds are an MCP Registry safety change and a self-hosted corpus server from Bluesky that fits the Meridia/Hypomone Postgres spine.

## Official / Tier 1
1. **MCP Registry now checks packages against OSV malware records (on publish and daily)**. The registry shipped v1.8.12 → v1.8.15 to production on Nov 22. It now checks every listed package against the OSV malware database when the package is published, runs a daily sweep, and reports entries whose package has disappeared. *Why it matters:* you install many third-party MCP connectors. A registry listing now carries a real supply-chain signal, so prefer servers listed on registry.modelcontextprotocol.io when vetting a new connector (MCP connectors lane). It does not replace reading the code. *Trust:* official MCP project (registry is a Tier 2 source in the sources file; commits by registry maintainers). — github.com/modelcontextprotocol/registry (PRs #1889–#1904)
- Other official repos: Claude Code is still on **2.1.330** (surfaced 11-21). `anthropics/skills`, `claude-plugins-official` and `knowledge-work-plugins` had no commits since Nov 22. `claude-plugins-community` had one increment: "Plugin checks: hardening" (#3124, Anthropic staff, Nov 23), logged as skipped. A Claude for iOS visual refresh (Nov 20) is not a skill/plugin, so it is logged as skipped.

## Meridia / Hypomone (corpus, Postgres, NAS)
2. **bluesky-social/diderot**: a self-hosted "ask your organization's knowledge" server. It ingests Slack, Discord, Notion, Linear, Zendesk, Claude Code/Codex sessions and folders of Markdown into **one Postgres event log**, embeds the content into Qdrant, and answers with citations in Slack and **as an MCP server**. Every event carries a permission scope, and every search is filtered to the caller's scopes (Apache-2.0, Go, ★48, created Nov 20). *Why it matters:* it is close to the Meridia corpus/RAG design (event log as the spine, Postgres on NAS/Docker). It is a working reference for scoped retrieval, which matters for FERPA-aware Plumbline data and Hypomone member data. It could also index the asam repo docs and session transcripts behind one MCP endpoint. *Trust:* Tier 3/4. The repo is new, but it comes from a known organization (Bluesky). Retrieval is vector-only (no reranker, no keyword index), so judge answer quality before relying on it. — github.com/bluesky-social/diderot · diderot.dev

## Claude Code / skills / MCP-building lane
3. **mq-yuan/project-docs**: an agent skill that keeps project facts as a few "converged" repo docs that are rewritten in place instead of appended to, plus a zero-dependency structural linter (MIT, ★17, created Nov 22). *Why it matters:* this is the same pattern as your `docs/<venture>/STATUS.md` files and lane OS files (os-architect). The linter could catch the truncation and drift problems STATUS files have had, such as the KSW tail restore on 07-13. *Trust:* Tier 4, new. Read it before adopting. — github.com/mq-yuan/project-docs
4. **fazxes/questionnaire**: a skill that asks the coding agent about its task first, then tells it which skills to load and which rules to follow (MIT, ★31 in about a day, created Nov 22). *Why it matters:* it is a skill-routing front door, close to your ask-card skill. It is worth comparing if your skill library keeps growing and the wrong skill triggers. *Trust:* Tier 4. — github.com/fazxes/questionnaire
5. **soodhere/saktum-check**: a one-command test for an MCP server. It checks the OWASP MCP Top 10, OAuth sign-in, protocol conformance, agent experience and context cost, and returns a grade with fixes (Apache-2.0, npm `saktum`, ★2, created Nov 22). *Why it matters:* it is a pre-flight check for any MCP server you build (a Populi/Plumbline MCP, Meridia data endpoints) before a connector goes live. *Trust:* Tier 4, brand new, single author. Run it only against your own servers. — github.com/soodhere/saktum-check

## Lanes searched, nothing new in window
- **Education / K-12 (Recess):** no new K-12 MCP or skill releases. Search results were older roundups (McGraw Hill / Claude for Teachers and canvas-mcp are already in the index).
- **Fintech/lending (Hypomone/Meridia):** no new lender or bank MCPs since Lendflow and Built (11-20). An older Wolters Kluwer commercial-lending MCP piece (Oct 6) is logged as skipped.
- **Governance/audit (Aegis):** only gated-workflow plugins with 1★ each (IdeaToProd, herd-sdlc), logged as skipped.
- **Populi / Postgres:** no Populi tooling. A small safe-migrations skill pack is logged as skipped.
- **Grants / KSW:** nothing.

## Ask
Pick any to adopt or trial: **diderot** (Meridia corpus / org-knowledge MCP on the NAS), **project-docs** (STATUS-file linter), **saktum-check** (MCP pre-flight for anything you build). No action is needed on the registry malware check. It only changes how much weight a registry listing gets when vetting connectors.
