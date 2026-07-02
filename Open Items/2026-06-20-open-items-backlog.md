# Open Items — captured backlog (2026-06-20)

Triage of everything in `Open Items/` plus Aliman's "Other Open Items" list. Capture only —
nothing here is being built. Each item has: state · type · next gate · next action · deps.
Run them later, one at a time, each in its own clean flow. Gates per `GATES.md`
(SPEC → BUILD → TEST → DEPLOY → DEMO → FIRST DOLLAR).

## 0. Already in flight (not "open")
- **Plumbline** (the `/48` "first MIG GTM SaaS build" in `Cowork HQ Recap.md`). Live Phase-0 President's View built this session (Populi + QBO). State: Gate 1→2. This is the worked example for items 9–11 below.

## A. Switch-on-now (scheduled tasks — low friction)
1. **Daily Curation / skills scout** (`Claude Workspace/Daily Curation.md`). Fully specified 7:30 AM digest of new skills/plugins. State: ready. Next: create the scheduled task + scaffold the two files it reads/writes (`Context/current-focus.md`, `Outputs/skills-scout/seen-index.md`). Type: BUILD (minutes).
2. **Nonprofit/education pricing curation** (list #2). A scheduled task that finds free/reduced pricing on products, services, and hardware for nonprofits/education (TechSoup, Google/Microsoft nonprofit, edu/hardware grant programs). State: net-new, fully a scheduled-task pattern. Next: define focus + cadence, then create task.
3. **Grants/opportunities curation** (list #1, second half). Scheduled scan for relevant grants. Feasible — grant-search connectors are available. Depends on item B1 (the grant "system") for what to match against.

## B. Build / stand-up
1. **Finalize the grant system** (list #1, first half). State: partially built in a prior thread. Next: SPEC what "the grant system" is (intake, fit criteria, tracker, the curation task above), then BUILD. Deps: a focus/criteria file.
2. **Cowork HQ workspace** (`Cowork HQ (Original).md`). Full blueprint for a clean Cowork+Obsidian workspace (Context / Projects / Outputs / Templates + connector standup + a custom skill). State: vault seeded, empty. Next: BUILD from the prompt. Becomes the home for the curation tasks' context files.
3. **NAS cleanup & reinstatement** (list #3). The Synology NAS (spec-v2 calls it dev/staging). State: needs cleanup + reinstatement. Next: scope on your machine — mostly outside Cowork (your hardware); I can produce the runbook. Deps: NAS access.

## C. Ventures needing a SPEC
1. **Hypomone venture** (`Hypomone/`). Misbanked-operator membership-lending institution; Atlanta launch; founding cohort. Strategy is well-developed (Market Read v1 + GA/Atlanta addendum v2, Naming & Architecture, The Charter v2, Founding Member Survey). Corporate stack maps to repo sub-systems:
   - **Eden Intelligence Group** (Delaware C-Corp, holds AIA methodology) → repo **Eden Crown** (currently "Not yet defined").
   - **Meridia LLC** (GA, commercialization) → repo **Meridia** (`integra-core` is its prototype).
   - **Hypomone** (the institution / "The Reserve") → new sub-system.
   - **The Charter** + **The Solera Principle** → founding instrument + cohort architecture.
   State: strategy done, nothing stood up. Next: SPEC Eden Crown / Hypomone in the repo; decide what "stand up" means (entity/brand, the Charter as a live first-party-data instrument, a landing surface). FLAG: a lending/membership institution carries real regulatory weight (lending/licensing, fair-lending, possible securities in "stake/charter") — legal/regulatory scoping is a Gate-0 dependency before build.

## D. Learning / enablement (deliver as briefings)
- **#4 Differences between current AI models** — short, current briefing.
- **#5 True understanding of Claude Design** — what it is, when to use it, worked example.
- **#6 Curation of capabilities** — a living map of your skills/connectors/tools (overlaps A1).
- **#7 LLM capabilities & how to maximize them** — practical playbook (context setup > prompt polishing — the Code-vs-Cowork lesson).
- **#8 Understanding GitHub & using it properly** — and a fix for the real problem we hit: the repo's `.git` lives on a Dropbox mount, which blocks git locks. Recommend a proper local clone / GitHub remote (see Recommendations).
Source thread: `Code vs Cowork.md` already started #5–#8.

## E. Product method — the core thread (list #9, #10, #11)
Reframe: these are not three tasks to "do" — they're a capability the repo already encodes. `GATES.md` *is* the production path from idea → sellable product; Plumbline is the live worked example.
- **#9 True product development & buildout** — run a product through all six gates once, end to end (Plumbline is the candidate).
- **#10 True spec buildout & production path on current products** — write real specs for the undefined sub-systems (Eden Crown, Hypomone, Waypoint, Aegis, Recess, KSW) before building.
- **#11 Scope real products vs one-off workflows** — the test: a product survives without you in the room (GATES "1.0" definition). Apply that test to each idea.

## F. Recommendations (list #12 — things not yet named)
1. **Set a WIP limit.** There are ~8 sub-systems, most undefined. Pick **1–2** to push through gates (Plumbline + one other) and explicitly park the rest. Sprawl is the main risk.
2. **Productize Plumbline deliberately.** It's "the first MIG GTM SaaS." Capture the Turner build as a repeatable multi-tenant template (tenant onboarding + mapping wizard), not a one-off — that's the literal answer to #11.
3. **Move the repo off the Dropbox `.git`.** Git can't manage lock files on the Dropbox mount (it blocked every commit this session). Put the working repo on a local disk with a GitHub remote; sync deliverables, not `.git`. Solves #8 in practice.
4. **Stand up a secrets store now.** Populi + QBO + Gusto keys are accumulating; spec-v2 already requires it. Do it before any multi-tenant work.
5. **Create `Context/current-focus.md` first.** Multiple curation tasks (skills, grants, nonprofit pricing) all read it. It's the cheap spine that makes the rest compound.
6. **Hypomone: legal/regulatory scoping before build** (see C1) — flag, not advice.

## Suggested first moves (when you're ready, separately)
1. Switch on **Daily Curation** (A1) — fastest visible win.
2. Create **`current-focus.md`** (F5) — unlocks the curation tasks.
3. Write the **Eden Crown / Hypomone SPEC** (C1) — converts your best strategy work into a buildable path.
