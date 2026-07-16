---
name: recess-competitive-reverse-engineer
description: Reverse-engineer a competitor or adjacent product against the Recess Bilateral Governed Learning Framework — trace their outcomes back to design choices, map against Recess's own thesis, separate moat from exposure, and propose how to innovate on top. Use for competitive/landscape/market scans for Recess, Crown's Eye, or Recess for AI, or when asked to compare a product to Recess. Outputs a structured comparison plus an Architectural State Graph-ready node.
---

# Recess Competitive Reverse-Engineer

Applies **Recess Component 06 — the Reverse Engineering Engine — pointed outward:**
competitor *outcome* → *design choice* → *Recess counter-position*. Turns a competitor URL or
name into an honest, structured comparison and a decision node ready for the governance graph.

## When to use
- Comparing any ed-tech, AI tutor, LMS, or AI-governance/observability product to Recess /
  Crown's Eye / Recess for AI.
- Running or refreshing the `edtech-recess` Innovation Radar (see `ASG-2026-06-30-004`).
- Any "how do we compare / where do we win / what do we build on top of them" question for
  Meridia's developmental layer.

## Step 0 — Load first (non-negotiable)
This is **Recess-adjacent work.** Before analyzing anything, load the definition — per Correction
Ledger `CL-2026-06-30-001` and `CL-2026-07-15-004` ("referencing without loading" is itself a logged
error). Read, do not recite:
- `specs/recess/2026-05-24-recess-framework-package-2026.md` (loadable Framework Package)
- `src/recess/governance/correction-ledger.md` and `architectural-state-graph.md`

## Inputs
- A competitor **URL** (preferred) or name.
- Optional: which face to compare against — **Crown's Eye** (K-12 human side), **Recess for AI**
  (enterprise), or both.

## Method
1. **Gather current facts (verified only).** Fetch the site + 1–2 corroborating *current* sources.
   Capture: audience; learning/product model; assessment→action; AI features **and how the AI
   itself is governed/improved**; personalization; business model; stated differentiator. Prefer
   2026-current sources and note publish dates.
2. **Reverse-engineer the design choices.** For each notable outcome/claim, trace it back to the
   decision that produces it (e.g., "Khanmigo +2.7% next-item correctness" ← "surfaces unmastered
   prerequisites before the harder problem"). Outcome → cause, every time.
3. **Map against the Recess thesis** — fill the dimension table below in Recess's own terms, not a
   generic feature list.
4. **Separate moat from exposure.**
   - *Moat* = dimensions where the competitor is **learner-only / ungoverned-AI / no enterprise-AI
     product.**
   - *Exposure* = any dimension where the competitor now **does** a thing Recess claims as
     differentiating. Flag these hard — they are the uncomfortable, important findings.
5. **Innovate on top.** Name the specific mechanism to *borrow*, what to *avoid imitating*, and the
   wedge the competitor can't copy quickly. Recommend which battlefield to weight (crowded ed-tech
   vs. nascent AI-governance).

## Comparison dimensions (anchored to Recess's thesis)
| Dimension | Competitor | Recess |
|---|---|---|
| Category — is it a tutoring system / LMS / "AI assistant with educational features" (what Recess says it is **not**)? | | |
| Who is governed & developed — learner only, or **learner + the AI**? | | |
| AI self-correction — documented, per-deployment? or centralized / none? | | |
| Circuit-breaker / drift treated as a governance problem? | | |
| Human authority over the AI's memory | | |
| Prerequisite-chain / gap-origin mapping | | |
| Assessment → action | | |
| Enterprise "govern your own AI" product | | |
| Funding / business model | | |

## Honesty discipline (Recess principle: storage ≠ action, no inflation)
- Report **only** verified facts from an actual source; mark unknowns as unknown — never infer a
  competitor's capabilities (mirrors `CL-2026-06-30-003`).
- Do **not** inflate Recess. Every place a competitor closes a Recess gap is surfaced as
  **exposure**, not buried.
- Quote competitor sources sparingly and attribute with dated links.

## Output template
1. **What it is (current)** — 3–5 dated bullets.
2. **Comparison table** — the dimensions above, filled.
3. **Core finding** — the moat (learner-only rows) and the exposure (rows where they've caught up),
   stated plainly.
4. **Innovate on top** — borrow / avoid / the un-copyable wedge / which battlefield to weight.
5. **ASG-ready node** — formatted to drop straight into
   `src/recess/governance/architectural-state-graph.md`:
   ```
   ### ASG-YYYY-MM-DD-NNN
   - **Decision:** <positioning decision vs. this competitor>
   - **Rationale:** <from the moat / exposure finding>
   - **Dependencies / Links:** <competitor, CL/ASG ids>
   - **Status:** PROPOSED
   ```
6. **Sources** — dated links.

## Composes with
- `pm-skills` → `pm-market-research`, `pm-product-strategy`
- `ai-design-skills/evaluation` → `comparative-evaluation`, `heuristic-evaluation-ai`,
  `failure-taxonomy`
- Live pulls: WebFetch / WebSearch (or Bright Data MCP for scale).

*First run: the 2026-07-15 Kodable + Khan Academy scan. Reuse it; keep it honest.*
