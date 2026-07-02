# Hypomone — Specification v1 (Gate 1)

Date: 2026-06-21. First buildable spec for the Hypomone venture. Synthesized from the strategy
corpus — Market Read v1 + Georgia/Atlanta addendum v2, Naming & Architecture v1, The Charter v2,
Founding Member Survey v1 (see `Open Items/Hypomone/` and `docs/asam/hypomone/`). This spec
defines the venture stack and scopes the **first buildable artifact: The Charter as a live intake
instrument.** The regulated lending product is explicitly deferred (see §8 and §10).

## 0. How to read this

Two things are true at once. The *institution* Hypomone is a for-profit, relationship-held
**lending** business carrying heavy regulatory weight. The *first thing we build* is a
compliance-safe data-and-enrollment instrument that touches none of that. **Gate 1 is the second
thing.** The lending arm is Gate-0-blocked on legal/licensing (§10).

Internal-grammar note: the interior vocabulary (Aletheia, Aegis, Zakhar, Shema, "the Reserve") is
**internal only** — per the founder's instruction it is "not consumer-facing marketing copy" and
must not appear on any member-facing surface. The Naming & Architecture document is internal grammar
and not part of any outbound package.

## 1. Venture stack

| Layer | Entity | What it is | Repo sub-system |
|---|---|---|---|
| Parent | **Eden Intelligence Group** (Delaware C-Corp) | IP holding entity. "Holds the AIA methodology. Licenses to Meridia." | **Eden Crown** (was "not yet defined") |
| Operator | **Meridia LLC** (Georgia) | "The commercialization vehicle. Carries the licensed IP into market." | **Meridia** (`integra-core` prototype) |
| Institution | **Hypomone** | "The membership institution itself. The Reserve. The room." A for-profit, relationship-held lending institution. | **Hypomone** (new) |
| Founding instrument | **The Charter** | "The document the founding cohort signs. The first rite." | — |
| Founding system | **The Solera Principle** | "The architecture into which The Charter enrolls members." | — |

Hypomone's three arms (named, not all in scope): **Hypomone Capital** (lending; MVP = business-purpose
real estate — DSCR / fix-and-flip), **Hypomone Financial Network Partners** (sells portfolio
intelligence to mainstream banks), **The Hypomone Collaborative** (the membership room).

## 2. The user

**Primary segment — the "misbanked operator":** "financially capable operators whose income or
business structure doesn't map cleanly onto conventional underwriting. They have accounts. They have
assets. They have real cash flow… 'misbanked' — served by institutions whose underwriting models
can't read them." Explicitly **not** the FDIC unbanked/underbanked — conflating them "would undercut
your credibility immediately."

**Gate-1 user roles:**
- **Respondent / prospective charter member** — completes The Charter.
- **Founding champion** (Keena) — signs the invitation as champion/charter-circle member and
  propagates it through her network; not a co-author of the instrument.
- **Operator / admin** — reviews the dataset, manages the founding cohort.

## 3. Core problem & evidence

**Mechanism:** "DTI is precisely the metric that misreads the misbanked borrower." A self-employed
operator, 1099 contractor, RE investor, or business owner "present[s] a distorted DTI… even when
their genuine capacity to pay is strong. This is not a population that fails on the merits. It is a
population that fails on the *model*."

Strongest cited evidence (defend or discount by tier):
- DTI is the #1 mortgage denial reason [T1, Atlanta Fed HMDA 2025; T2, LendingTree — "34.02% of all denials"].
- Atlanta behavioral signal: most-sought financing source was "credit cards at 43%, up from 25% the year before" [T1, Atlanta Fed SBCS; caveat: N=150 convenience sample — directional].
- Sixth District firms "more likely to apply… less likely to receive partial or full approval" [T1].
- Southeast carries the heaviest denial load — "~404,000 denials — 20% of all denials nationally" [T1].
- Size anchors: ~16.6M self-employed, ~33M business owners, non-QM market ~$182B/~9% (revised down from $239B; "non-QM has no standardized definition"); average non-QM borrower carried a **776 FICO** (dispels the subprime stigma).

**Launch geography:** metro Atlanta — "the single most concentrated overlap in the country" of the
target operator, the DTI denial mechanism, the heaviest denial load, and a growing non-subprime
non-QM market, with incumbents (ACE, Invest Atlanta, ANDP) that "prove the demand and the gap… [but]
do not occupy the position."

## 4. Gate-1 product — The Charter (live intake instrument)

The 19-question, five-section instrument (**Recognition → Experience → Behavior → Membership →
Charter**), deployed as a hosted, phone-first web form with consented contact capture (Q19) and a
built-in referral/share link (Q18). The Founding Member Survey v1 is the earlier draft of the same
instrument and is **deprecated**; The Charter v2 is the live spec (superset).

It produces three assets at once:
1. **Citable first-party data the institution owns from day one** — the [DATA] questions (Q1, Q2, Q4, Q6–Q11, Q13, Q14, Q16).
2. **An enrolled founding cohort** — respondents who opt in become named "charter members."
3. **The institutional-sales evidence base** — built from "Q8 + Q9 + Q10 + Q11 together."

**Hard compliance rule (non-negotiable):** The Charter "must not promise specific financial products,
rates, or approval… Language throughout stays at the level of interest and experience, **never
offer.**" This guards against "implied offer of credit… before licensing and structure are in place,"
which matters acutely given the founder's NMLS standing.

## 5. Core workflow

1. The champion (Keena) signs the invitation; the Charter link propagates through her network.
2. A respondent opens The Charter → completes the five sections → [DATA] answers are captured.
3. Section 5 converts: Q16 (be a charter member on the founding line?), Q17 (participation mode,
   incl. "Sign The Charter when it formally opens"), Q18 (refer via share link), Q19 (consented contact).
4. The operator reviews responses → produces the cohort list + the dataset → feeds the next capital
   and bank-partnership conversations. "This is not a pitch and there is nothing to buy. It is a
   charter — a founding document."

## 6. Data model

- `respondent` — anonymous until Q19 consent.
- `charter_response` — the 19 answers, typed per question; `[DATA]` flag per citable item.
- `charter_member` — a respondent who opted in (Q16/Q17); eligible for the founding line.
- `referral` — share-link edges; the propagation graph (referrer → completion).
- `consent` — the Q19 contact capture (name/email/work) and its scope.

**PII rule:** name/email/work are captured **only** under an explicit Q19 consent action; responses
without consent remain unattributed. Storage/retention obligations are an open item (§10).

## 7. Acceptance behavior (binary, v1)

1. The Charter is reachable as a hosted form; a respondent completes all five sections on phone or desktop.
2. Every `[DATA]` question's responses are stored in a queryable, exportable form.
3. No screen states or implies an offer of credit, a rate, or approval — a compliance review passes.
4. Q19 contact is captured only on an explicit consent action; non-consented responses stay unattributed.
5. Q18 produces a unique share link per respondent, and referred completions trace to the referrer.
6. From the dataset the operator can produce (a) the charter-member cohort list and (b) the
   institutional-sales cut (Q8+Q9+Q10+Q11).

## 8. Scope boundary — explicitly NOT in Gate 1

- **No lending, deposits, capital, or product offer of any kind.** Hypomone Capital is Gate-0-blocked
  on legal/licensing (§10).
- **No paid membership / "stake" collection.** Q14 probes price posture only; nothing is charged.
- **No mechanical Solera implementation** (preserved seats, tiered governance) — deferred to the
  bylaws / membership-rules phase.

## 9. Build approach

Per The Charter v2's one open build decision: **self-hosted on the EIG/Meridia stack vs. Typeform** —
recommend self-hosted if standup is under a week, else Typeform to start. Non-negotiable either way:
the dataset must be **exportable and owned** (never locked in a vendor). Phone-first, responsive.

## 10. Open items (gate to close)

| # | Item | Question that closes it | Owner | Default until closed |
|---|---|---|---|---|
| 1 | **Lending arm (Hypomone Capital) — Gate-0 legal dependency** | State lending/NMLS licensing, implied-offer-of-credit, business-purpose vs. mortgage split, sponsor-bank model risk, and whether a paid "membership stake" tied to lending implicates securities/consumer-finance characterization — all scoped by counsel before any build touching credit. | Aliman + counsel | Charter stays at "interest, never offer"; no credit surface ships |
| 2 | AIA methodology | What is the AIA methodology (EIG's core IP)? Defined only in a non-confidential Architecture Overview not in this corpus. | Aliman | Treated as opaque IP for Gate 1 |
| 3 | Hypomone entity form | DBA of Meridia / subsidiary of EIG / separate entity — tax + licensing consequences. | Legal + CPA | Decide before any lending |
| 4 | Solera: mechanical vs. metaphorical | "What does solera mean structurally, not poetically?" — governs whether membership rights are real architecture. | Aliman | Metaphor only for Gate 1 |
| 5 | Capital source / structural path | Own licenses vs. sponsor-bank vs. hybrid. | Aliman + counsel | Unresolved; not needed for Gate 1 |
| 6 | Product mechanics | Underwriting model, rates, sizing, capital — Market Read explicitly excludes unit economics/default/portfolio performance. | Aliman | Out of scope for Gate 1 |
| 7 | Membership pricing | Q14 probes posture; no price set. | Cohort input | None charged in Gate 1 |
| 8 | Data protection / retention | Q19 PII storage, retention, and sample-disclosure discipline for citability. | Aliman | Define before launch |
| 9 | Charter tech platform | Self-hosted vs. Typeform (§9). | Aliman | Self-hosted if standup < 1 week |
| 10 | Keena co-branding | Does her name / firm appear on the live form? | Aliman + Keena | Champion/signer, not co-author |

## 11. Phasing (mapped to GATES.md)

- **Gate 1 — SPEC (this doc):** The Charter instrument is specified; the first buildable artifact is
  named. Closes when the build decision (§9) is made and counsel confirms the instrument-as-specified
  carries no offer-of-credit exposure.
- **Gate 2 — BUILD:** The Charter is live, collecting consented responses and enrolling the cohort,
  with an exportable owned dataset.
- **Gate 3+ — the institution:** Hypomone Capital and the regulated lending model — gated entirely on
  §10 legal/licensing; out of scope here.

## 12. Note on the corpus

This spec is a synthesis for review, not a re-statement of the strategy. The Market Reads remain the
evidence base; The Charter v2 remains the instrument of record; Naming & Architecture remains internal
grammar. Nothing here hardens until Aliman confirms — and the lending institution does not advance past
strategy until counsel has scoped item #1.
