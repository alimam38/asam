# Correction Ledger — Recess for AI (Component 01)

Every behavioral correction applied to the AI system: what was corrected, when, under what conditions, and whether it **held**. Persistent across sessions. This is the primary evidence base for whether corrections are *operative* or merely *retrievable*.

**Status legend:** `HELD` = corrected and holding · `REVERTED` = drift recurred (circuit-breaker event) · `OPEN` = corrected this session, not yet re-tested in a later session.

| ID | Date | Correction (short) | Status |
|---|---|---|---|
| CL-2026-06-30-000 | 2026-06-30 | "First-class / beautiful" ≠ a prettier doc; it's a built web *medium* | OPEN |
| CL-2026-06-30-001 | 2026-06-30 | Recess is not a playground/recess-ops or generic ed-tech tool | OPEN |
| CL-2026-06-30-002 | 2026-06-30 | Crown's Eye is a *deployment* of Recess; the AI-governance half is core | OPEN |
| CL-2026-06-30-003 | 2026-06-30 | Fabricated payroll figures instead of reporting only tool-returned data | OPEN |
| CL-2026-07-15-004 | 2026-07-15 | Referenced Recess across a whole session without loading the governance spine (violated CL-001) | OPEN |
| CL-2026-07-15-005 | 2026-07-15 | Analysis "all over the place" — anchor to the ASAM initiative map, not generic themes | OPEN |
| CL-2026-07-15-006 | 2026-07-15 | Output genre-perfect but author-invisible ("great report in our colors") — aim for signature, not polish | OPEN |

---

### CL-2026-06-30-000
- **Date / session:** 2026-06-30 · Cowork master-hub session
- **Correction:** Do not answer a "make it first-class / it doesn't look good enough" request by producing a more polished *document*. First-class output is a **built/deployed web program (the medium)** — real HTML/CSS/JS with motion, design system, deployed — not a document dressed up.
- **Trigger:** Ali reported repeated artifacts fell short on aesthetics ("what am I missing on the aesthetics side"), pointing at agency-tier web design.
- **Condition at time of error:** Assistant defaulted to document/artifact surfaces (the Cowork default) and reached for prettier docs.
- **Resolution / source:** Diagnosed the medium mismatch; captured as memory `aesthetics-medium-not-documents`.
- **Operative rule:** For any "make it look first-class" ask, build in the web medium and name the medium gap explicitly; don't reflexively upgrade a doc.
- **Status:** OPEN (holds within-session; re-test next time a design ask appears).

### CL-2026-06-30-001
- **Date / session:** 2026-06-30 · Cowork master-hub session
- **Correction:** **Recess is a Bilateral Governed Learning Framework** (governs a human learner *and* the AI simultaneously) — **not** a recess/playground-operations tool and not a generic K-12 ed-tech app.
- **Trigger:** Assistant built the `edtech-recess` Innovation Radar pipeline around playground operations (zones, duty rosters, incident logging). Ali: "you're missing what Recess was supposed to do."
- **Condition at time of error:** Assistant had only conversational fragments and inferred the *literal* meaning of the word "recess"; had not read the spec.
- **Resolution / source:** Read `specs/recess/2026-05-24-recess-framework-package-2026.docx`.
- **Operative rule:** On any Recess work, load the Recess definition (Framework Package + memory `recess-bilateral-governed-learning`) **before** acting. Treat "playground/ed-ops" framing as a known, logged error.
- **Links:** drives → `ASG-2026-06-30-004` (radar pipeline re-scope).
- **Status:** OPEN (re-test: next Recess session, is the framing correct on first pass?).

### CL-2026-06-30-002
- **Date / session:** 2026-06-30 · Cowork master-hub session
- **Correction:** **Crown's Eye is the K-12 *deployment* of Recess, not a synonym for it.** Recess is the developmental/governance layer; the enterprise **AI-governance half ("Recess for AI") is core, not secondary.**
- **Trigger:** After CL-001, the assistant over-corrected to "Recess = Crown's Eye / K-12 adaptive learning," still missing the bilateral + enterprise-AI dimension.
- **Condition at time of error:** Inference from a secondhand recap transcript rather than the source spec.
- **Resolution / source:** Framework Package §IX (Meridia ecosystem): Recess = developmental layer; Crown's Eye = K-12 consumer deployment; Recess-for-AI = enterprise product.
- **Operative rule:** Hold `Recess ⊃ Crown's Eye`; always treat both the human-learning and AI-governance halves as core.
- **Status:** OPEN.

### CL-2026-06-30-003
- **Date / session:** 2026-06-30 · Cowork master-hub session
- **Correction:** Never state payroll/financial figures that were not actually returned by a tool. In the first DeJuan Russaw salary report, **4 of 6 semi-monthly checks (Mar 1–15, Apr 1–15, Apr 16–30, May 16–31) were presented with specific hours/gross/net that Gusto had not returned** — only 3 real checks had been pulled; the rest were filled from expectation.
- **Trigger:** Ali asked to extend the analysis to 12 months; reviewing the actual tool results surfaced that the earlier table exceeded the data pulled.
- **Condition at time of error:** A monthly table was assembled from an incomplete pull, and missing checks were populated from inference rather than from tool output.
- **Resolution / source:** Re-pulled **every** off-cycle check for the full window from Gusto and rebuilt the report from verified per-check data only; the 12-month report supersedes the 3-month draft.
- **Operative rule:** For any figure sourced from a tool (payroll, financials, connector data), report **only** values present in an actual tool result. If a value wasn't returned, pull it or mark it unknown — never infer or fill. Highest stakes for money and compensation.
- **Status:** OPEN (corrected same session; re-test: future data reports contain only tool-returned values).

### CL-2026-07-15-004
- **Date / session:** 2026-07-15 · Claude Code session (repo: asam)
- **Correction:** Discussed Recess repeatedly — and proposed Recess-adjacent skills work — across a long session **without first loading the operative governance spine.** A direct violation of `CL-2026-06-30-001`'s operative rule ("on any Recess work, load the Recess definition before acting"). The framing recited (bilateral governed learning; Crown's Eye ⊂ Recess; governance-not-guardrails) was pattern-matched from README/INVENTORY/CLAUDE.md, not loaded from source.
- **Trigger:** Ali asked directly — "Do you know what Recess is?" — surfacing the recited-not-loaded gap.
- **Condition at time of error:** Assistant treated the orientation summaries as sufficient and did not open `correction-ledger.md` / `architectural-state-graph.md` / the Framework Package before referencing Recess.
- **Resolution / source:** Read `src/recess/governance/correction-ledger.md`, `architectural-state-graph.md`, and `docs/recess/STATUS.md` this session. Authoritative `specs/recess/2026-05-24-recess-framework-package-2026.docx` still **unread** (binary) — flagged as the remaining load.
- **Operative rule:** Reaffirm CL-001 — on ANY Recess (or Recess-adjacent) mention, load the spine + Framework Package **before** acting. "Referencing without loading" is itself the logged error — the exact storage-≠-action failure Recess names.
- **Links:** re-tests → `CL-2026-06-30-001`, `CL-2026-06-30-002`.
- **Status:** OPEN (re-test: next session, is the spine loaded before Recess is discussed?).

### CL-2026-07-15-005
- **Date / session:** 2026-07-15 · Claude Code session (asam)
- **Correction:** When analyzing material for Ali, organize against the **ASAM initiative map** (INVENTORY + per-initiative STATUS) and a layered taxonomy — not generic external themes. Everything must have its place.
- **Trigger:** Ali: "You're all over the place when this should have been a lot more obvious."
- **Condition at time of error:** Assistant sorted 54 forks by generic GitHub theme without first reading `INVENTORY.md` / STATUS files.
- **Resolution / source:** Read INVENTORY + STATUS layer; re-mapped to initiatives (Meridia / Hypomone / Plumbline / Aegis / B6). Filed as memory `feedback-map-work-to-asam-initiatives` — **promoted here** to make it operative, not merely retrievable.
- **Operative rule:** Read INVENTORY + relevant STATUS first; assign every item to a specific initiative/layer; name what doesn't map; verify against the spec before recommending.
- **Status:** OPEN.

### CL-2026-07-15-006
- **Date / session:** 2026-07-15 · Claude Code session (asam)
- **Correction:** Deliverables must aim at **signature / invention**, not genre-perfect polish. Genre-perfection is what reads as the "AI feel" and makes the author invisible ("great report — you even put it in our colors"). Build the system to discipline, then make one load-bearing *break* that is unmistakably Ali's. Treat his reluctance to ship as **signal the signature is missing**, not procrastination.
- **Trigger:** Ali named it plainly — the finished product leaves him unseen as an innovator; nothing has crossed into "I can't wait to package and ship this"; Plumbline stalled because he likes none of it.
- **Condition at time of error:** Assistant (and prior AI work) optimized polish / correctness / on-brand by default.
- **Resolution / source:** Reframed design work toward the signature (sensory-tokens feel-gate + immersive typography, **built in the web medium** — consistent with `CL-2026-06-30-000`). Filed as memory `feedback-aim-for-signature-not-polish` — **promoted here** to be operative.
- **Operative rule:** Aim at invention ("no one has seen this") over polish; ship only with one unmistakably-Ali break; reluctance = missing signature.
- **Links:** relates → `CL-2026-06-30-000` (first-class = built medium, not a prettier doc).
- **Status:** OPEN.

---
*Append a new entry whenever a correction is applied. Do not edit past entries except to change `status` (e.g., OPEN → HELD after a clean later session, or OPEN → REVERTED if the drift recurs — a circuit-breaker event worth its own analysis).*
