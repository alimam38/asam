You are standing up the production repository for my first commercial software product. I'm a solo founder. For months I've produced high-quality specs, reports, and architecture documents through AI conversations — and none of it accumulates, because it all lives as loose documents. Today we convert from artifacts to assets: one versioned repository that every future working session reads from and writes to. This repo is the single source of truth from now on.

<context>
- You are running in Claude Cowork on my desktop with file system access. You may run shell commands, including git.
- My infrastructure: Synology NAS running Docker and PostgreSQL, Dropbox for file sync, and a GitHub account. A developer collaborator may need access later.
- Operating principle: an artifact becomes an asset when it is versioned, named consistently, and consumed by the next stage of work. Nothing in this repo is decorative.
</context>

<setup_checks>
Before asking me anything, check what exists: is git installed and configured with a user identity? Is the GitHub CLI (gh) installed and authenticated? Report what you find. If git is missing, stop and give me the exact install steps for my OS before continuing. If gh is missing or unauthenticated, proceed local-only and include push-to-GitHub steps in the close-out report instead.
</setup_checks>

<interview>
Then ask me these, one at a time, adapting to my answers:
1. The product name for this repository (propose a kebab-case repo name from my answer).
2. Where the repo should live locally — propose a default of a top-level "Products" folder containing one folder per product, and confirm or adjust.
3. The locations of my existing artifacts: folder paths, Dropbox directories, anything downloaded from past sessions. I'll give you a rough list; you inventory the actual contents.
4. Whether to create the GitHub remote now as a private repo (only if gh is authenticated).
</interview>

<build>
1. Initialize the repository with this structure:
   - README.md — what the product is, current status, and how to run it. If nothing runs yet, say exactly that and state the first gate instead. No aspirational language; describe only what is true today.
   - GATES.md — the production line with binary exit criteria. Write it with this content, adapted to the product name:
     Gate 1 SPEC: a buildable specification exists — someone could start implementing without asking me clarifying questions. Gate 2 BUILD: core functionality runs end-to-end in the local Docker environment. Gate 3 TEST: automated tests cover the critical paths and pass. Gate 4 DEPLOY: the system runs on target infrastructure, reachable by someone other than me. Gate 5 DEMO: a scripted walkthrough exists that a stakeholder can follow. Gate 6 FIRST DOLLAR: a real external party uses it under real terms. Definition of 1.0: someone outside my ecosystem can use this without me in the room.
   - docs/ for decision records and reports, specs/ for requirements and schemas, src/ for code, tests/, infra/ for Docker and deployment notes, assets/ for collateral. Use .gitkeep in empty folders.
   - CHANGELOG.md and MIGRATION-LOG.md (created in step 2).
   - A .gitignore appropriate for this stack, excluding OS cruft, secrets, and .obsidian.
2. Migrate the artifacts: inventory every file in the locations I gave you. Classify each as spec, decision record, report, collateral, or not-worth-migrating. Copy (never move, never delete) each keeper into the right folder with kebab-case names prefixed by date where the original date is known. Write MIGRATION-LOG.md listing every file: source path, destination, classification — and for anything left behind, one line on why. If a file's classification is genuinely ambiguous, ask me; otherwise decide and note your reasoning in the log.
3. Commit in logical units with meaningful messages (scaffold, then migration, then gates). Push if a remote was created.
</build>

<close_out>
Finish with: the repository tree as it actually exists on disk, the commit log, a count of migrated vs. left-behind artifacts, and the first open gate with the single next action that closes it. Report only what exists on disk — if something failed or was skipped, say so plainly.
</close_out>

Conventions throughout: plain Markdown, kebab-case filenames, no boilerplate text in any committed document — if something is unknown, write "Not yet defined" plus the question that would define it. Pause only when a decision genuinely needs me; never delete or overwrite my original files.

Start with the setup checks now.

Think deeply before answering.


