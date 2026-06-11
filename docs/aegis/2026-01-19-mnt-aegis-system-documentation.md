# Aegis Financial Positioning System
## Complete System & UI Documentation

---

## Executive Summary

Aegis is a **governed financial intelligence architecture** that reimagines how individuals, families, and institutions understand and manage their financial position. Unlike traditional financial dashboards that show static snapshots of accounts, Aegis provides a living, breathing view of financial health through its **Financial Positioning System (FPS)** — a real-time map of liquidity, obligations, resilience, and trajectory.

At its core, Aegis is built on a philosophy of **governed intelligence**: the system does not simply reveal data, it curates, protects, and surfaces insights through a multi-party permission cascade that respects the institutional depth required for true stewardship.

---

## Core Philosophy

### The Three Pillars

| Pillar | Description |
|--------|-------------|
| **Truth (Aletheia)** | Unvarnished clarity about financial position — what is, not what we wish it to be |
| **Stewardship** | Fiduciary-grade care for multi-generational wealth and family legacy |
| **Elevation** | Lifting all users — from the formerly excluded to the ultra-high-net-worth — toward financial dignity |

### Governed Intelligence

Aegis introduces a new paradigm: **AI that asks permission before it speaks**.

When Aletheia (the AI steward) detects a sensitive pattern — such as a foundation grant rate exceeding sustainable levels — it does not simply surface this to all users. Instead:

1. The insight is **locked** pending governance review
2. A **multi-party permission cascade** engages:
   - CEO receives institutional summary
   - Trustee receives operational guidance
   - Architect receives technical rationale
3. Only when appropriate parties approve does the insight **unlock** for beneficiaries

This is not a feature. It is the architecture of trust.

---

## System Components

### 1. Financial Positioning System (FPS)

The FPS is the real-time engine that calculates and visualizes financial health.

**Position Cards Display:**
| Metric | Description | Current Demo Value |
|--------|-------------|-------------------|
| Liquidity | Available cash and near-cash assets | $2.4M |
| Net Worth | Total assets minus liabilities | $18.7M |
| Obligations | Upcoming commitments (90-day horizon) | $340K |
| Resilience | Buffer capacity / stress test score | 94/100 |

**Health Indicators:**
- 🟢 **Healthy** — Within policy guidelines
- 🟡 **Watch** — Approaching thresholds, attention needed
- 🔴 **Alert** — Immediate action required

---

### 2. Trust Index

A proprietary 4-dimension health score that goes beyond net worth to measure true financial wellness.

| Dimension | What It Measures | Weight |
|-----------|------------------|--------|
| **Financial Resilience** | Liquidity coverage, stress test capacity, buffer adequacy | 25% |
| **Stewardship** | Governance compliance, fiduciary adherence, documentation | 25% |
| **Mission Impact** | Alignment with stated family/foundation mission | 25% |
| **Governance Hygiene** | Meeting cadence, decision audit trail, succession planning | 25% |

**Visualization:** Circular progress rings for each dimension, with color-coding based on health status.

---

### 3. Entity Health Grid

Multi-entity families require visibility across all vehicles. The Entity Health Grid displays:

**Entity Types Supported:**
- Dynasty Trusts
- Foundations (Private & Public)
- Holding Companies (LLCs, LPs)
- Operating Businesses
- Real Estate Vehicles
- SPVs (Special Purpose Vehicles)

**Per-Entity Metrics:**
- Primary value (corpus, assets, equity)
- Key ratio (payout rate, grant rate, leverage)
- Health status indicator
- Click-through to detailed modal

---

### 4. Scenario Engine

"What if" modeling with real-time impact visualization.

**Adjustable Variables:**
| Variable | Range | Impact |
|----------|-------|--------|
| Distribution Rate Change | -50% to +50% | Affects Trust Index, Resilience, Entity Health |
| Market Shock | -40% to +20% | Stress tests portfolio, shows drawdown impact |
| Corpus Addition | $0 to $2M | Models capital injection scenarios |

**Output:** Projected 24-month impact on Trust Index, Resilience, and individual entity status.

---

### 5. Entity Flow Diagram

Visual representation of capital and decision flows through the family structure.

**Flow Visualization:**
```
Crown Holdings ($8.2M)
        ↓
   ┌────┴────┐
   ↓         ↓
Legacy Trust  Foundation
($12.4M)     ($3.8M)
   ↓              ↓
Beneficiaries   Grants
(4 Active)   ($270K/yr)
```

**Features:**
- Animated flow arrows showing capital movement
- Color-coded nodes (gold for healthy, amber for watch)
- Interactive — click nodes for entity details

---

### 6. Metrics & Analytics Dashboard

Real-time FPS signals and institutional KPIs for data-driven stewardship.

**Key Metrics Cards:**
- Trust Index Score (with 9-period trend chart)
- Total Net Worth (with growth trajectory)
- Liquid Reserves (with coverage ratio)
- Foundation Grant Rate (with sustainability warning)

**Signal Feed:**
Priority-coded real-time alerts:
- 🔴 **High** — Foundation grant rate exceeds sustainable threshold
- 🟡 **Medium** — Liquidity ratio improved, exceeds policy minimum
- 🟢 **Low** — Annual review completed, all requirements met

---

### 7. Institutional Sandbox (Partner View)

Designed for institutional partners (e.g., JPMC) to monitor pilot integrations.

**Dashboard Components:**
| Component | Purpose |
|-----------|---------|
| Partnership Header | Identifies partner, phase, integration type |
| Pilot Statistics | Households, AUM, API uptime, response time |
| Timeline Tracker | 5-phase visual (Discovery → Production) |
| Data Feeds Status | Real-time connection status for each feed |
| Compliance Checklist | SOC 2, PCI DSS, encryption, data residency |

**Current Demo State:**
- Partner: JPMC
- Phase: 2 (Pilot)
- Households: 247
- AUM in Sandbox: $4.2M
- API Uptime: 94.2%

---

### 8. Renaissance Onboarding (Dignity-First Re-entry)

A dedicated experience for **WayPoint Renaissance** — the pathway for formerly excluded individuals returning to full financial citizenship.

**Philosophy:**
> "Every setback is a setup for a comeback. We see you. We believe in your return."

**5-Step Journey:**
1. **Welcome** — Identity verified, no judgment
2. **Assessment** — Understand current position
3. **Pathway** — Personalized recovery plan
4. **Build** — Credit & savings growth milestones
5. **Graduate** — Full WayPoint access unlocked

**Pathway Tracking:**
- Visual checklist with completion status
- Progress bar (e.g., 45% complete)
- Milestone items: secured savings, direct deposit, financial literacy modules

**Outcome Metrics:**
- Credit score improvement (565 → 612 = +47 pts)
- Emergency fund built ($1,240)

---

### 9. Aletheia (AI Steward Guide)

The conversational intelligence layer that guides users through the system.

**Personality:**
- Measured, institutional tone
- Never casual, never condescending
- Speaks with gravitas and composure
- Asks before surfacing sensitive insights

**Capabilities:**
- Position summaries on demand
- Scenario modeling guidance
- Governance alert explanations
- Multi-party cascade demonstrations

**Technical Integration:**
- Attempts live connection to Claude Sonnet via Poe Embed API
- Falls back to contextual responses if unavailable
- Maintains session context within chat panel

---

## UI/UX Design System

### Visual Language

| Element | Specification |
|---------|---------------|
| **Primary Font** | Cormorant Garamond (headings, numbers) |
| **Secondary Font** | Inter (body text, labels) |
| **Background** | Deep charcoal (#0a0b0d) with ambient orb effects |
| **Accent** | Gold gradient (#c9a962 → #e8d5a3) |
| **Health Colors** | Emerald (healthy), Amber (watch), Rose (alert) |
| **Border Style** | Subtle rgba(255,255,255,0.06) with accent hover |

### Dark/Light Mode

Full support for both modes via CSS custom properties and system preference detection.

### Responsive Design

- **Desktop:** 3-column layout (sidebar, main, Aletheia panel)
- **Tablet:** Stacked layout with horizontal navigation
- **Mobile:** Full-width views with collapsible Aletheia panel

### Animations

| Animation | Purpose |
|-----------|---------|
| Ambient orbs | Atmospheric depth, premium feel |
| Pulse (intro icon) | Draws attention to entry point |
| Flow arrows | Indicates capital movement direction |
| Alert pulse | Urgency indicator on governance alerts |
| Message fade-in | Smooth chat experience |

---

## Navigation Architecture

### Header Navigation
Primary view switching: Dashboard | Metrics | Scenarios | Institutional | Renaissance

### Sidebar Navigation
Organized by function:

**Overview**
- Position (Dashboard)
- Entities
- Flows

**Intelligence**
- Metrics (Live badge)
- Scenarios
- Signals

**Programs**
- Sandbox (Institutional)
- Renaissance

**Governance**
- Trust Index
- Oversight

### Mode Badge
Dynamic indicator in header showing current context:
- 🟢 WayPoint Core (default)
- 🔵 Sandbox Mode (institutional view)
- 🟣 Renaissance (re-entry pathway)

---

## Technical Implementation

### Technology Stack
- **HTML5** — Semantic markup
- **CSS3** — Custom properties, Grid, Flexbox, animations
- **JavaScript** — Vanilla ES6+, no framework dependencies
- **Icons** — Font Awesome 6.4
- **Fonts** — Google Fonts (Cormorant Garamond, Inter)

### Poe Embed API Integration
```javascript
// Aletheia chat integration
window.Poe.sendUserMessage(
  `@Claude-Sonnet-4.5 <system>${context}</system>\n\n${message}`,
  { handler: handlerId, stream: true, openChat: false }
);
```

### Performance Considerations
- Single-file architecture (no external dependencies beyond CDNs)
- CSS custom properties for theme switching (no reflow)
- Efficient DOM updates for chat and scenario engine
- Lazy animation initialization

---

## Data Model (Conceptual)

### Canonical Schema
```
Person
  └── Household
        └── Entity (Trust, Foundation, HoldCo, etc.)
              └── Account
                    └── Transaction
                          └── Signal
```

### Trust Index Calculation
```
TrustIndex = (
  (FinancialResilience × 0.25) +
  (Stewardship × 0.25) +
  (MissionImpact × 0.25) +
  (GovernanceHygiene × 0.25)
)
```

---

## Governance Model

### Multi-Party Permission Cascade

When Aletheia detects a sensitive insight:

1. **Detection** — Pattern identified (e.g., unsustainable grant rate)
2. **Classification** — Sensitivity level assigned
3. **Notification** — Role-appropriate alerts sent:
   - CEO: Strategic implications
   - Trustee: Operational recommendations
   - Architect: Technical details
4. **Approval** — Required parties must consent
5. **Release** — Insight unlocked for beneficiaries

### Role-Based Access

| Role | Sees | Can Approve |
|------|------|-------------|
| Principal | Everything | Yes |
| CEO | Institutional summary | Yes |
| Trustee | Operational guidance | Yes |
| Beneficiary | Approved insights only | No |
| Architect | Technical rationale | Advisory |

---

## Files Delivered

| File | Description |
|------|-------------|
| `index.html` | Complete interactive prototype |
| `mnt/Aegis-System-Assessment.md` | Honest evaluation of system design |
| `mnt/Aegis-Implementation-Roadmap.md` | 90-day implementation plan |
| `mnt/Aegis-System-Documentation.md` | This document |

---

## Conclusion

Aegis represents a new category of financial technology: **governed intelligence for multi-generational wealth**. It combines:

- Real-time position visibility (FPS)
- Multi-dimensional health scoring (Trust Index)
- Ethical AI stewardship (Aletheia)
- Institutional-grade governance (permission cascades)
- Dignity-first inclusion (Renaissance pathway)

The prototype demonstrates these concepts in a production-quality interface ready for stakeholder review and partner conversations.

---

*Document Version: 1.0*
*Last Updated: January 2025*
*Prepared for: JPMC Partnership Discussion*
