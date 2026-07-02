[Ran scheduled task

](https://claude.ai/scheduled-task/daily-skills-scout)

Thought process

Thought process

I'll start by reading the context files that drive this scan.

Searched the web, used 5 tools, read 4 files

Searched the web, used 5 tools, read 4 files

Found a strong set. Marking search tasks done and writing the digest.

Used 4 tools, created a file, ran a command

Used 4 tools, created a file, ran a command

A digest for today already exists from an earlier run — let me read it before deciding whether to overwrite or extend.

Read a file

Read a file

The earlier run was a legitimate first pass (heavy on platform changelog items). My picks are all distinct installable skills/MCP servers/plugins and none repeat the seen-index — so I'll append a clearly-labeled second pass rather than clobber it.

Edited a file

Edited a file

The edit succeeded; that hook error is a misconfigured external SQL-check hook (unresolved `${CLAUDE_PLUGIN_ROOT}`), unrelated to this Markdown file. Now updating the logs.

Edited 2 files, used a tool

Edited 2 files, used a tool

Done — today's scan is logged. An earlier run today had already written a 2026-06-20 digest (platform changelog items + one Postgres MCP), so I appended a **second pass** to the same dated file rather than clobber it, with 5 distinct, installable picks (none repeating the seen-index):

1. **anthropics/knowledge-work-plugins** (Tier 1) — open-source Cowork plugin repo + `create-cowork-plugin` skill
2. **Claude Design / Anthropic Labs** (Tier 1) — your open item #5; re-surfaced as a real pick since the first pass dismissed it as tangential
3. **Postgres MCP Pro / crystaldba** (Tier 2/3) — index-tuning + health, distinct from the call518 ops server already seen
4. **dbt Semantic Layer MCP server** (Tier 2) — governed metrics over MCP for your semantic-layer domain
5. **skill-creator evals/benchmarking update** (Tier 1) — rigor layer for your SKILL.md authoring

Most lean foundational over bleeding-edge — the right call while the seen-index is still small. Seen-index got the 5 new entries; 3 borderline items (Claude Code dynamic workflows, pgEdge Postgres MCP, OSI v1.0 spec) went to skipped-log.

Two notes for your review: (a) the earlier run's seen-index/skipped handling was inconsistent (it listed skipped items inline in the digest but never wrote them to skipped-log) — mine follows the task spec; (b) a misconfigured `check-sql-files.py` PostToolUse hook is firing on every Edit with an unresolved `${CLAUDE_PLUGIN_ROOT}` — harmless to these Markdown writes, but worth fixing so it stops erroring.

Files updated:

* `Outputs\skills-scout\2026-06-20-skills-scout.md` (second-pass section appended)
* `Outputs\skills-scout\seen-index.md` (+5)
* `Outputs\skills-scout\skipped-log.md` (+3)

Sources: [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · [Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs) · [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) · [dbt MCP](https://www.getdbt.com/blog/dbt-mcp-server-conversational-analytics) · [skill-creator update](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)
