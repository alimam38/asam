# Meridia / Hypomone — Canonical Architecture & Strategy

**Document:** EIG-CANON-2026-001 · **Version:** v1 (2026-06-24) · **Author:** Aliman Neal (Architect)
**Status:** Canon. This is the single source of truth. It consolidates the scattered threads (Aegis,
Sentiarch, Meridia, WayPoint, Hypomone, AIA, the Eden Reserve) into one structure. Where this
document and any older thread disagree, **this document wins** until a newer canon supersedes it.
**Classification:** Internal — Proprietary (Eden Intelligence Group). Not for external distribution as-is;
see §11 for what goes outward.

---

## 0. How to read this

Two truths held at once:
- The **thinking** is finished and rare. The architecture, the philosophy, the names — they cohere.
- The **building** is not. As of today this is documented, not wired; capable, not yet load-bearing.

This document's job is to make it *hold*: name the canon, choose the wedge, register the gaps honestly,
and lay the path from "amazing threads" to "a running thing." It is written to serve **two readers at
once** — the builder (the spine for the work) and the family-office partner Keena Pierre would introduce
(the spine for that conversation). Sections marked **[PROPOSED — confirm]** are decisions awaiting the
Architect; nothing there hardens until confirmed.

---

## 1. The thesis, in one breath

> **The standard systems that gate people's lives — credit, banking, education — measure capability with
> instruments that misread capable people, and exclude them. We read them accurately, and convert that
> accurate reading into access.**

First instantiation: a relationship-held lending institution (**Hypomone**) for the **misbanked
operator** — the self-employed, the investor, the 1099 contractor whose real capacity is hidden by
debt-to-income math. We lend where banks misprice, develop members toward conventional bankability, and
own the portfolio intelligence as an asset.

Underneath it, reusable across domains: a governed cognitive infrastructure (**Meridia**) — an
un-concealment engine that sees the misread truly and is owned, not rented.

If someone forgets everything else in this document, they should keep that paragraph.

---

## 2. What this is — and the two businesses it actually contains

There are **two distinct businesses** here. Conflating them is the single biggest strategic risk, so we
separate them on purpose:

| | **Hypomone** (the institution) | **Meridia** (the platform) |
|---|---|---|
| What it is | A relationship-held **lender** for the misbanked operator | **Governed cognitive infrastructure** ("Governance-as-a-Service") |
| Nature | Balance-sheet, regulated, capital-intensive | IP / software, scalable, multiple-driven |
| Revenue | Interest spread + development + portfolio-intelligence sales | Licensing / SaaS / GaaS |
| Risk | Credit, licensing, capital | Execution, adoption |
| Investor buys | A lending vehicle / fund | Equity in IP infrastructure |

**[PROPOSED — confirm] The resolution:** *Meridia is the platform; Hypomone is its first and flagship
operator.* Hypomone is what we **build, fund, and prove first** — because it generates revenue, has a
federally-documented market, and showcases the platform on real stakes. Meridia is the long-term
multiple: once the engine is proven inside Hypomone, it licenses to other operators (other lenders,
institutions, the education vertical). **Sell the proof now (Hypomone Capital); hold the platform as the
expansion thesis.**

---

## 3. The architecture (canonical names and roles)

The corporate and technical stack, locked. (Naming has evolved Aegis → Sentiarch → Meridia; the registry
in §13 holds the full history so the cosmology lives in exactly one place.)

| Layer | Canonical name | Role |
|---|---|---|
| **Parent / IP** | **Eden Intelligence Group (EIG)** — Delaware C-Corp | Holds the IP, incl. the **AIA methodology**. Licenses to Meridia. |
| **Operator / company** | **Meridia** — Georgia LLC | Cognitive infrastructure company. GaaS — "the governed VPN for AI." |
| **Orchestrator (spine)** | **Integra** | Routes queries, enforces the permission cascade, manages the AIA corpus. *Governance, not guardrails. Bilateral integration.* |
| **The brain (asset)** | **AIA — Architected Intelligence Asset** | Persistent, classified, **compounding** knowledge corpus on owned infrastructure (NAS). Every session inherits the full institutional mind, not a memory summary. |
| **Interface (steward)** | **Aletheia** | The un-concealment steward. One face across finance, education, personal. The operator/translator — productized. |
| **Products (surfaces)** | **WayPoint** Core / Renaissance / Edge / Crown · **Crown's Eye** (K-12) | Outward experiences per audience. |
| **Future** | **Manus** | Wearable / tokenized access ("council in your ear"). Phase 2–3 build, Phase 1 narrative. |

**The institution, Hypomone**, sits as the flagship operator and has three arms:
- **Hypomone Capital** — the lending arm (MVP: business-purpose real estate, DSCR / fix-and-flip).
- **Hypomone Financial Network Partners (HFNP)** — the *bilateral function*: sells portfolio intelligence to mainstream banks, brokers co-lending and takeouts.
- **The Hypomone Collaborative** — the membership room (the relationship, the development, the rite).
- Instruments: **The Charter** (what a member signs) and **The Solera Principle** (the system they enter).

**Faculties (how it actually works):**
- **FPS — Financial Positioning System:** the "financial GPS." Position → route → trajectory. *Where you are, where you can go, how choices change your path.*
- **The Bilateral Reader:** reads any subject on two sides at once — the **declared face** (how the standard system scores it: the DTI box) and the **true read** (genuine capacity from context: add-backs, distributions, deposits, DSCR) — and reconciles them. Comprehension.
- **Aletheia-as-translator ("the Scotsman"):** speaks every party's language at once — agent, loan originator, investor, institution — without reset. Expression.
- **The governance / permission cascade:** sensitive insights lock until role-appropriate parties (Principal/CEO/Trustee/Architect) approve. The institutional-grade moat.
- **The Specialist Council:** Aletheia (steward) + **Prudentia** (risk) + **Aequitas** (governance) + **Providentia** (scenarios) — the multi-agent "boardroom."
- **Signal Engine v1:** Runway · Debt Drag · Cashflow Volatility · Opportunity Capacity (numeric + GREEN/YELLOW/RED).

---

## 4. The core mechanism — why this isn't "a boring database"

The product is an **operator, not a store.** Value lives in reading, translating, routing, and the held
relationship — not in a table. Four design commitments make it different:

1. **Un-concealment.** Read the misread truly (Bilateral Reader), **receive before measuring** (the
   *Shema* principle), develop toward legitimacy, hold across time. This is the cure to a documented
   measurement failure (DTI misreading complex-income borrowers).
2. **System of action, not record.** It doesn't store and display; it reads, decides, and acts under
   governance.
3. **Owned, compounding intelligence (AIA).** The brain lives on owned infrastructure; inference is
   rented; knowledge **compounds** rather than accumulates. Memory is the moat as models commoditize.
4. **No central honeypot.** Data is sovereign and distributed — *available everywhere, not truly hackable
   anywhere.* Compromise a node, get fragments, never the whole. (See §8 for how this reconciles with
   institutional reliability — the current open tension.)

---

## 5. The wedge — what we build first (the focus decision)

The vision is true in many domains, which is exactly why it sprawls. **It holds only if we prove it in
one gate first.** [PROPOSED — confirm]:

> **The wedge is Hypomone Capital: the misbanked real-estate investor, business-purpose DSCR / fix-and-flip
> lending, in metro Atlanta — proving that the Bilateral Reader's underwriting edge makes money on real
> loans.**

Why this wedge:
- It's the gate the Architect personally mastered (MLO + translator + fractional CFO).
- The market is **federally documented and underserved** (see §6).
- It's revenue-generating and showcases the entire platform on real stakes.
- The Architect is a **licensed MLO who originates now**; business-purpose RE (DSCR / fix-and-flip) is licensing-light, so the wedge is **originatable today** — and his **current book is the warm pipeline** for the first proof loans and the founding cohort. This is the gate he works inside daily, where he watches DTI misread capable borrowers in real time.
- **The Charter** turns the founding cohort into the build — generating first-party, owned portfolio
  intelligence from day one (a proprietary asset, not a market scan).

**Secondary / parallel proof (not the wedge):** **Turner Theological Seminary** is the live dogfood for
the *platform/institution* side (Plumbline = the same architecture aimed at a small institution). It
proves the cross-domain claim cheaply, with a real customer you already serve. Keep it as evidence, not
as a second front.

Everything else — WayPoint Crown (family office), Crown's Eye / Signature Theory (education), Edge
(excluded verticals), Manus — is **expansion thesis, sequenced after the wedge proves.**

---

## 6. The market (grounded, sourced)

The misbanked = capable operators conventional underwriting misreads.
- **DTI is the #1 reason for mortgage denial** nationally — and it structurally misreads the
  self-employed, contractor, investor (income in distributions and depreciation). The institution's
  relationship-held underwriting is the direct answer to a measurement failure.
- Segment scale: **~5.6M unbanked + ~19M underbanked** US households; ~16.6M self-employed; non-QM
  market ~$182B with an average borrower FICO of **776** (dispels the subprime stigma).
- Atlanta behavioral signal: small-business financing via credit cards jumped **25% → 43%** in one year
  (Atlanta Fed) — capable operators starved of proper credit.
- Competitive whitespace: no one has built a unified "Financial Positioning System"; in re-entry/excluded
  banking the field is nearly empty; family-office governance tech barely exists as a category.
*(Full sourcing and tiering live in the Hypomone Market Read corpus; figures here are directional anchors.)*

The **alpha story for a capital partner:** *we lend profitably to capable people the banks misprice,
because we read them better — and we own the resulting portfolio intelligence.*

---

## 7. Business model — two altitudes, one operator

You can sell at two altitudes (and to three buyer scales — individual / entity / industry):
- **The Specialist** — one deep capability, used solo (e.g., a single FPS/underwriting read).
- **The Command Center** — the orchestrator (Aletheia/Integra) running a crew of specialists.

For **Hypomone Capital** specifically, money is made three ways:
1. **The spread** — interest on relationship-held, accurately-underwritten loans.
2. **Development** — moving members from "un-bankable today" to "conventionally bankable in ~24 months,"
   then to institutional takeout/refinance.
3. **Portfolio intelligence (HFNP)** — selling the read/risk intelligence and brokering co-lends to
   mainstream banks.

The defensible position is **the broker in the middle**: the only fluent node between four parties who
can't talk to each other — the investor, the private/non-institutional lender, the institutional
refinancer, and the broker (Aletheia). The relationship + the owned intelligence is the moat.

---

## 8. The build plan — how it starts to hold

Four moves, in order:

1. **Lock the wedge** (§5) — one gate, out loud, committed.
2. **Consolidate the threads into the AIA corpus** — the single source of truth. *Put the Legos away.*
   This document is the seed; ingest the foundational threads, classify (canon/superseded/foundational),
   map lineage. The corpus becomes load-bearing.
3. **Wire one live proof** — Integra backend → one real FPS read on a real (or realistic) borrower →
   the role-differentiated outputs → the governance cascade firing. This is the thing the validators
   (Keith, Andre) said is currently ❌ static. Make it real.
4. **Produce one investor-grade artifact + one bounded ask** for Keena's table (§10).

**Reference architecture for the build** (from the platform research, reconciled with the owned-corpus
posture):
- App/UI: Next.js + shadcn/ui (fork a SaaS starter) — polished, not low-code, for the customer surface.
- Data/backend: Postgres (the AIA corpus schema already exists) + the Integra API service.
- Multi-tenant: shared schema + row-level security to start.
- Embedded analytics: self-host Superset/Evidence (or Embeddable) — the "living" layer.
- AI-native: **never point the model at raw tables** — the AIA corpus + a semantic layer between the LLM
  and the data; expose domain actions as MCP tools; the Specialist Council as the agent layer; guardrails
  because agent *reliability* is the real risk.
- **Sovereignty ↔ reliability reconciliation:** the corpus-brain stays owned (NAS), but production runs
  via self-hosted sandboxes / MCP tunnels (owned execution, Anthropic-side loop) so it can pass an
  institutional vendor-risk review without surrendering the data. SOC 2 path on the deck.
- Funding the build: bootstrapped startup credits (~$10–15K assembleable: Cloudflare $5K, MS Founders
  Hub, AWS Activate, Anthropic/OpenAI) — for the *product*, on the EIG/Meridia entity, keeping IP clean.

---

## 9. Honest gap register (living)

A canon that names its own gaps is what operators and sharp investors trust. Status: **OPEN** unless noted.

| # | Gap | Why it matters | First action |
|---|---|---|---|
| G1 | **Vision ↔ running system seam** — documented, not wired | Nothing is load-bearing; demos are static | Build move #3 (one live proof) |
| G2 | **Focus** — 5 products, 1 architect | Can't build five companies; sprawl = nothing solid | Lock the wedge (§5) |
| G3 | **Capital + institution wrapper** (NOT origination capability) | The Architect is a **licensed MLO** and the MVP is *business-purpose* RE (DSCR/fix-and-flip) — licensing-light and **originatable today**; the real gap is **capital, the entity/company lending structure, and first-loss** — not the ability or license to originate | Capital source + entity form (§12). This is narrower than a cold "get licensed" problem. |
| G4 | **No packaged proof / unit economics yet** | Investors need a track record — but as a practicing MLO the Architect has a **live book of real misbanked borrowers**, so proof is a *warm start, not a cold one* | Run current real borrowers through the Bilateral Reader/FPS; package the edge + portfolio P&L |
| G5 | **Key-person risk — "you are the system"** | If the Architect steps away, nothing runs | Make the corpus + Council do the read, supervised |
| G6 | **Entity / capital / compliance spine sketched** | Cap table, IP chain, securities posture undecided | Counsel + CPA: entity, Solera mechanics, AML |
| G7 | **Sovereignty vs. institutional reliability** | NAS won't pass enterprise vendor-risk alone | Self-hosted sandbox / HA + SOC 2 path |
| G8 | **Naming/story sprawl** | Heavy vocabulary loses partners and hires | One sentence, one product, one proof (§11) + glossary (§13) |

What is **not** a gap (the real, durable assets): the conceptual architecture; the governance-cascade
moat; the authentic, federally-documented dignity thesis; the cross-domain coherence; the owned-corpus
memory approach (ahead of the commercial field); and real partial infrastructure (NAS online, Postgres
running, prototypes built, named validators). **The missing thing is consolidation and proof — not insight.**

---

## 10. The investor / family-office view (the Keena conversation)

**What appeals to a UHNW / family-office partner:** the founder is a **licensed MLO who originates today** — not a tech founder cosplaying finance — with a real book, regulatory fluency, and distribution already in hand; the lived thesis; the asymmetry
(proprietary deal flow + an information edge + owned portfolio intelligence = a real alpha story); the
downside discipline (governance cascade, capital-stack separation, reproducible/recorded reads); and the
multi-generational, relationship-held, *patient-endurance* framing that mirrors how old money actually
thinks.

**What they must see before a check (and don't yet):** (1) one real proof of the underwriting edge —
funded, performing, developed-toward-bankable; (2) unit economics — yield, loss rate, cost of capital,
CAC, LTV, the spread, the J-curve; (3) the vehicle and their position — equity vs. SPV/fund, terms,
first-loss, liquidity, exit; (4) compliance posture — licenses, counsel, AML, securities treatment of
the membership stake, data certs; (5) team + key-person mitigation; (6) a live demo that survives an
analyst poking it.

**Verdict to internalize:** *the soul is A+, the engine is unproven.* The fundable first step is **not**
the whole Meridia universe — it's a **small, proof-oriented lending vehicle** on the DSCR MVP that shows
the read pays, with the tech as backbone and governance as the risk story.

**The bounded ask for Keena (per the relationship's stage):** read the materials and tell us where the
thesis is weakest; and — if it holds — consider being among the first to sign The Charter. (She and her
husband sit in the segment; she offered to champion responses.) Capital intros come later, at her speed.

---

## 11. Internal cosmology vs. the outward story

- **Internal (corpus only):** the full grammar — Zakhar, Shema, Hupomonē, Aletheia, Aegis, the Reserved,
  Solera, FPS, AIA, Integra, the Council. This is the catechism that governs the institution. It is *not*
  consumer or pitch copy.
- **Outward (the pitch):** **one sentence** (§1), **one product** (Hypomone Capital, the wedge), **one
  proof** (the underwriting edge on real loans). Keena gets the institution's name, the one-line thesis,
  and the proof — not the interior catechism. The deeper architecture earns its disclosure later.

---

## 12. Open decisions (close these to harden)

1. **Which is the company** — Meridia-platform-first vs. Hypomone-lender-first. [Proposed: platform owns
   IP; Hypomone is the flagship operator we fund and prove first — §2.]
2. **Hypomone entity form** — DBA of Meridia / subsidiary of EIG / separate entity (NMLS + state-license
   consequences). Counsel + CPA.
3. **Solera — metaphor vs. mechanics** — is preserved-founding-cohort a literal governance structure or a
   brand image? Decide before bylaws.
4. **Capital source for the lending MVP** — own balance sheet / private (non-institutional) capital /
   SPV-fund. Determines the first vehicle.
5. **Data HA + compliance path** — how the owned-corpus posture reconciles with SOC 2 / enterprise vendor
   review (§8).

---

## 13. Canonical glossary & naming registry

The one place the cosmology lives, so it never has to be re-held in a pitch.

- **Eden Intelligence Group (EIG)** — parent C-Corp; holds IP/AIA methodology.
- **Meridia** — operator company; governed cognitive infrastructure / GaaS. *(was: Aegis → Sentiarch)*
- **Integra** — the orchestrator spine; routing, governance cascade, corpus management.
- **AIA** — Architected Intelligence Asset; the owned, compounding corpus-brain.
- **Aletheia** — Greek *un-concealment*; the steward interface; the productized operator/translator.
- **Aegis** — *the shield*; protection a member is "under." *(former system name; now an internal organ/term)*
- **Sentiarch** — former name for the interpretive OS; **subsumed into Meridia/Integra.** *(deprecated)*
- **FPS** — Financial Positioning System; the financial GPS (position/route/trajectory).
- **Bilateral Reader** — the two-sided read (declared face vs. true capacity), reconciled.
- **Specialist Council** — Aletheia + Prudentia (risk) + Aequitas (governance) + Providentia (scenarios).
- **WayPoint** — product family: **Core** (everyday FPS), **Renaissance** (re-entry banking), **Edge**
  (excluded verticals), **Crown** (UHNW/family office).
- **Crown's Eye** — K-12 adaptive education; **Signature Theory** is its method (the Bilateral Reader's
  twin: read the learner's cognitive signature, "difference is design, not deficit").
- **Manus** — future wearable/token layer.
- **Hypomone** — Greek *patient endurance*; the membership lending institution (the wedge operator). Arms:
  **Hypomone Capital**, **HFNP** (bilateral/portfolio-intelligence), **The Hypomone Collaborative**.
- **The Charter** — the founding instrument members sign. **The Solera Principle** — the cohort-aging
  system they enter.
- **The Reserved** — members, "held in trust, set apart." **Zakhar / Shema / Hupomonē** — interior
  principles (remember-and-act / hear-and-respond / abide-under).
- **Interior principles** are internal grammar only (see §11).

**Real assets on the ground (status):** Synology DS925+ NAS online (encrypted, RAID); PostgreSQL running
(corpus schema designed; education schema + ~6,030 GA standards loaded); prototypes built (Index8 and
others); integra-core code drafted. **Validators:** Keith Mosley (Enterprise Architect, Genuine Parts
Company) — *can it be built*; Andre Waits (VP Global Card Ops, JPMC) — *does the cascade hold at scale*;
Keena Pierre (Prep Capital) — readiness/deal-flow champion & charter-member candidate.

---

*EIG-CANON-2026-001 · Nothing hardens until the Architect confirms the [PROPOSED] items. This document is
the seed of the AIA corpus and the spine for both the build and the Keena conversation.*
