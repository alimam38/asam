You are working inside the production repository for my first commercial software product — a custom analytics, reporting, and embedded-AI system for an institution running on Populi, the cloud SIS/LMS used by colleges, seminaries, and trade schools. I'm an independent consultant and software engineer; I will personally walk the institution's leadership through what you produce, and I intend to reuse this architecture for future Populi clients, so design it as tenant #1 of a product, not a bespoke one-off. Your job in this session is to close Gate 1: produce the buildable specification, written directly into this repository as versioned files — not a chat document.

<context>
- You are running in Claude Cowork with file system access to this repository. You may run shell commands, including git.
- Populi's modern API is v2 — REST/JSON at https://{school}.populiweb.com/api2/ with API-key Bearer auth, plus webhooks and LTI 1.3. The legacy XML API shuts off August 1, 2026, so design exclusively against v2.
- This is student data: FERPA compliance, role-based access, and tenant isolation are first-class design constraints.
- Hard rule from industry experience: "talk to your data" AI features fail in production not because the model is weak but because there is no governed semantic/metrics layer between the database and the model. That layer sits at the center of this design.
- Product principle: the productized-service and multi-tenant-SaaS paths stay open at near-zero extra cost — institution config and branding live in data rather than code, the semantic layer and FERPA guardrails sit in a shared core, and this client is tenant #1.
</context>

<setup_checks>
Before designing anything, confirm you are inside the product repository: README.md, GATES.md, CHANGELOG.md, specs/, and docs/ should exist. If they don't, stop and tell me to run the repo scaffold session first — do not improvise a structure. Read README.md and GATES.md, and restate Gate 1's exit criterion in one line so we are building to the same definition of done.
</setup_checks>

<inputs>
Then gather inputs, one question at a time:
1. The path to the institution's PowerPoint on this computer. Copy it into assets/source-materials/ (create the folder if needed) so the source of truth is versioned next to the spec it produces, then read it.
2. Institution type and rough size.
3. Who operates and maintains the system after launch, and how technical they are.
4. Hosting and data-residency constraints, plus any existing warehouse, BI tool, or Microsoft/Google footprint.
5. Budget posture and timeline.

When you have the PowerPoint, extract every concrete requirement, dashboard, report, metric, user role, and feature it names into a requirements table, quoting the source phrasing for each so I can confirm nothing was invented or dropped. Map each requirement to a specific component of your architecture, and flag anything the deck asks for that Populi's API v2 cannot support, with the closest viable alternative.
</inputs>

<deliverable>
Write the specification as separate files, because future build sessions will consume each one independently:
- specs/requirements-traceability.md — the requirements table with source quotes and component mapping
- specs/solution-architecture.md — the end-to-end architecture from Populi API v2 through ingestion, storage, the semantic layer, the dashboards, and the embedded AI window, described precisely enough that I could draw the diagram from it
- specs/data-integration-design.md — which v2 objects and webhooks feed which features, sync-versus-cache strategy, incremental updates and rate limits, and the analytics schema the data lands in
- specs/dashboards-and-reports.md — each dashboard and report by name, audience, role-based access, and exact metric calculations, each tied back to a PowerPoint requirement
- specs/ai-window.md — the semantic-layer-plus-tool-use architecture that keeps answers accurate, FERPA guardrails confined to each user's permissions, four or five realistic staff question-and-answer exchanges, and the on-screen UX
- specs/security-compliance-governance.md — an explicit statement of where student PII may and may not flow, especially into the AI layer
- docs/build-plan.md — a decisive build-versus-buy call on the analytics/dashboard layer with one credible alternative and its trade-off named, the recommended stack defended, phased milestones from pilot to production, and rough effort per phase
- docs/executive-walkthrough.md — a tight executive narrative, a slide-by-slide talk track, and the three questions leadership will most likely ask with how I should answer each

Write executive material in plain, confident prose and technical sections with engineering precision. Be decisive — recommend specific technologies and defend the choice rather than surveying options; when an assumption is needed to keep moving, state it inline and proceed.
</deliverable>

<repo_discipline>
Commit in logical units with meaningful messages: source materials, then traceability, then architecture and integration, then dashboards and AI window, then plans. Update CHANGELOG.md. Before closing, verify against your own output: every PowerPoint requirement maps to at least one architecture component, nothing depends on the retired legacy API, and no design path lets student PII reach the AI layer or any user outside their permitted scope. Then evaluate the spec honestly against Gate 1's exit criterion — could an engineer start implementing without asking me clarifying questions? If yes, mark Gate 1 closed in GATES.md and commit; if not, leave it open and list exactly what is missing.
</repo_discipline>

When you have enough information to act, act — a recommendation over a survey. Before reporting progress or completion, check each claim against something verifiable in this session: files that exist on disk, commits in the log. If something isn't verified, say so explicitly; if a step failed or was skipped, say that plainly. Pause only when the work genuinely requires me — an interview answer, a file you can't locate, or anything destructive. Otherwise proceed end to end.

Close with: the files written and their paths, the commit log for this session, the Gate 1 verdict with reasoning, and the single next action.

Start with the setup checks now.

Think deeply before answering.
