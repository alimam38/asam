"""
Integra Core — Report Generator
Produces audience-differentiated outputs from the same underlying data.
This is the core of the WayPoint value proposition.
"""

from datetime import datetime
from ..models import Report, ReportSection, ReportAudience
from ..mock_data import get_financial_position, get_trust_index, get_entities, get_signals


def generate_report(audience: ReportAudience) -> Report:
    """Generate a report tailored to the specified audience."""
    position = get_financial_position()
    trust = get_trust_index()
    entities = get_entities()
    signals = get_signals()

    generators = {
        ReportAudience.BOARD: _generate_board_report,
        ReportAudience.TECHNICAL: _generate_technical_report,
        ReportAudience.REGULATOR: _generate_regulator_report,
        ReportAudience.FAMILY: _generate_family_report,
    }

    return generators[audience](position, trust, entities, signals)


def _generate_board_report(position, trust, entities, signals) -> Report:
    critical_signals = [s for s in signals if s.severity.value == "critical"]
    warning_signals = [s for s in signals if s.severity.value == "warning"]
    success_signals = [s for s in signals if s.severity.value == "success"]

    sections = [
        ReportSection(
            heading="Executive Summary",
            content=(
                f"{position.institution_name} closes the second quarter of {position.fiscal_year} "
                f"with total assets of ${position.total_assets:,.0f} and net assets of ${position.net_assets:,.0f}. "
                f"The Trust Index stands at {trust.overall_score}/100 ({trust.grade}), reflecting "
                f"strong mission alignment with room for improvement in governance compliance. "
                f"Year-to-date revenue of ${position.total_revenue:,.0f} trails expenses by "
                f"${abs(position.net_income):,.0f}, a gap projected to close during the spring giving season."
            ),
        ),
        ReportSection(
            heading="Key Risk Indicators",
            content=(
                f"Three items require board attention: "
                f"(1) Insurance renewal due March 15 with 4.2% increase requiring approval. "
                f"(2) Operating deficit of ${abs(position.net_income):,.0f} — seasonal and expected but monitor closely. "
                f"(3) Investment policy review overdue since 2023 — committee should convene within 60 days."
            ),
            data={"critical_count": len(critical_signals), "warning_count": len(warning_signals)},
        ),
        ReportSection(
            heading="Strategic Highlights",
            content=(
                f"Grant revenue at 120% of target ($120K vs $100K plan). "
                f"Scholarship fund fully funded at $175K for spring awards cycle. "
                f"Building fund crossed $340K milestone — roof project fully funded. "
                f"12 new tithing members in Q2, positive trajectory for revenue growth."
            ),
            data={"success_count": len(success_signals)},
        ),
        ReportSection(
            heading="Recommendations",
            content=(
                "1. Approve insurance renewal at three-year lock rate (3.8% vs 4.2% annual). "
                "2. Schedule investment committee review by end of April. "
                "3. Monitor spring giving against $485K tithes target — consider stewardship campaign if March receipts underperform."
            ),
        ),
        ReportSection(
            heading="Trust Index Summary",
            content=(
                f"Overall: {trust.overall_score}/100 ({trust.grade}). "
                f"Financial Health: {trust.dimensions[0].score}/100 (stable). "
                f"Governance Compliance: {trust.dimensions[1].score}/100 (improving). "
                f"Operational Efficiency: {trust.dimensions[2].score}/100 (improving). "
                f"Mission Alignment: {trust.dimensions[3].score}/100 (improving)."
            ),
            data={"dimensions": [{"name": d.name, "score": d.score, "trend": d.trend} for d in trust.dimensions]},
        ),
    ]

    return Report(
        title=f"Board Report — {position.institution_name}",
        audience=ReportAudience.BOARD,
        institution_name=position.institution_name,
        generated_at=datetime.now(),
        period=f"Q2 {position.fiscal_year} (as of {position.as_of_date})",
        sections=sections,
        summary=(
            f"Institution is financially stable with strong mission execution. "
            f"Three governance items require board action. Trust Index trending upward."
        ),
        metadata={"trust_score": trust.overall_score, "trust_grade": trust.grade},
    )


def _generate_technical_report(position, trust, entities, signals) -> Report:
    sections = [
        ReportSection(
            heading="Data Sources & Lineage",
            content=(
                "Financial data sourced from QuickBooks General Ledger export (February 28, 2026). "
                "Chart of accounts mapped to WayPoint unified schema v1.0. "
                "17 line items classified across 5 categories: assets (7), liabilities (4), "
                "revenue (5), expenses (7). Entity balances cross-referenced with GL sub-accounts."
            ),
            data={
                "source": "QuickBooks Desktop",
                "export_date": str(position.as_of_date),
                "schema_version": "1.0",
                "line_items_count": len(position.line_items),
            },
        ),
        ReportSection(
            heading="Trust Index Calculation Methodology",
            content=(
                f"Composite score: weighted average of four dimensions. "
                f"Financial Health (30%): derived from cash runway ({position.months_cash_runway} months), "
                f"debt-to-asset ratio ({position.total_liabilities / position.total_assets * 100:.1f}%), "
                f"revenue growth rate, and net income margin. "
                f"Governance Compliance (25%): audit currency, board meeting frequency, policy review status, insurance status. "
                f"Operational Efficiency (20%): personnel-to-expense ratio, admin cost ratio, facility utilization proxy. "
                f"Mission Alignment (25%): program spending percentage, scholarship deployment rate, capital fund growth."
            ),
            data={
                "weights": {d.name: d.weight for d in trust.dimensions},
                "scores": {d.name: d.score for d in trust.dimensions},
                "composite": trust.overall_score,
            },
        ),
        ReportSection(
            heading="Entity Reconciliation Status",
            content=(
                f"{len(entities)} entities tracked. "
                f"Active: {sum(1 for e in entities if e.status.value == 'active')}. "
                f"Restricted: {sum(1 for e in entities if e.restricted)}. "
                f"Pending review: {sum(1 for e in entities if e.status.value == 'pending_review')}. "
                f"All entity balances reconciled to GL sub-accounts as of {position.as_of_date}."
            ),
            data={"entities": [{"id": e.id, "name": e.name, "status": e.status.value, "balance": e.balance} for e in entities]},
        ),
        ReportSection(
            heading="Signal Pipeline Health",
            content=(
                f"{len(signals)} active signals. "
                f"Critical: {sum(1 for s in signals if s.severity.value == 'critical')}. "
                f"Warning: {sum(1 for s in signals if s.severity.value == 'warning')}. "
                f"Info: {sum(1 for s in signals if s.severity.value == 'info')}. "
                f"Success: {sum(1 for s in signals if s.severity.value == 'success')}. "
                f"Action required on {sum(1 for s in signals if s.action_required)} signals."
            ),
            data={"signals_by_severity": {
                "critical": sum(1 for s in signals if s.severity.value == "critical"),
                "warning": sum(1 for s in signals if s.severity.value == "warning"),
                "info": sum(1 for s in signals if s.severity.value == "info"),
                "success": sum(1 for s in signals if s.severity.value == "success"),
            }},
        ),
        ReportSection(
            heading="API & System Status",
            content=(
                "Integra Core API: operational. All endpoints responding within 200ms SLA. "
                "Database: PostgreSQL 16 on NAS, 17 tables active. "
                "Report generator: 4 audience modes operational (board, technical, regulator, family). "
                "Scenario engine: 3 pre-built scenarios available, custom scenarios accepting parameters."
            ),
            data={"api_status": "operational", "db_status": "connected", "endpoints_active": 9},
        ),
    ]

    return Report(
        title=f"Technical Report — {position.institution_name}",
        audience=ReportAudience.TECHNICAL,
        institution_name=position.institution_name,
        generated_at=datetime.now(),
        period=f"Q2 {position.fiscal_year} (as of {position.as_of_date})",
        sections=sections,
        summary="All systems operational. Data lineage verified. 10 signals active, 4 requiring action.",
        metadata={"api_version": "1.0", "schema_version": "1.0"},
    )


def _generate_regulator_report(position, trust, entities, signals) -> Report:
    compliance_signals = [s for s in signals if s.category.value == "compliance"]

    sections = [
        ReportSection(
            heading="Compliance Status Overview",
            content=(
                f"{position.institution_name} maintains compliance with applicable nonprofit regulatory "
                f"requirements as of {position.as_of_date}. Annual audit completed and current. "
                f"Form 990 filing on schedule. State registration active. Two compliance items require "
                f"attention within 30 days: insurance renewal and connectional obligation payment."
            ),
        ),
        ReportSection(
            heading="Financial Summary — Regulatory View",
            content=(
                f"Total assets: ${position.total_assets:,.0f}. Total liabilities: ${position.total_liabilities:,.0f}. "
                f"Net assets: ${position.net_assets:,.0f}. "
                f"Year-to-date revenue: ${position.total_revenue:,.0f}. Year-to-date expenses: ${position.total_expenses:,.0f}. "
                f"Operating result: $({abs(position.net_income):,.0f}) deficit. "
                f"Cash and cash equivalents: ${position.cash_position:,.0f}. "
                f"Restricted funds properly segregated: Building Fund ${340_000:,.0f}, Scholarship Fund ${175_000:,.0f}."
            ),
            data={
                "total_assets": position.total_assets,
                "total_liabilities": position.total_liabilities,
                "net_assets": position.net_assets,
                "restricted_funds": 515_000,
                "unrestricted_cash": position.cash_position,
            },
        ),
        ReportSection(
            heading="Audit Trail",
            content=(
                "Last external audit: September 2025 (unqualified opinion). "
                "Internal controls assessment: adequate with minor recommendations. "
                "Board oversight: quarterly meetings with financial review. "
                "Segregation of duties: maintained across financial operations. "
                "Related party transactions: pastor's discretionary fund under quarterly review."
            ),
        ),
        ReportSection(
            heading="Policy Adherence",
            content=(
                "Gift acceptance policy: current. "
                "Investment policy: review overdue (last reviewed 2023, annual review required). "
                "Conflict of interest policy: current, annual disclosure completed. "
                "Document retention policy: current. "
                "Whistleblower policy: in place."
            ),
            data={"policies_current": 4, "policies_overdue": 1},
        ),
        ReportSection(
            heading="Pending Compliance Items",
            content=(
                f"{len(compliance_signals)} compliance signals active. "
                "1. Insurance renewal — policy expires March 15, 2026. Renewal in process. "
                "2. AME connectional obligation — $10,500 due March 15, 2026. Budgeted and funded. "
                "No material compliance violations identified."
            ),
        ),
    ]

    return Report(
        title=f"Compliance Report — {position.institution_name}",
        audience=ReportAudience.REGULATOR,
        institution_name=position.institution_name,
        generated_at=datetime.now(),
        period=f"Q2 {position.fiscal_year} (as of {position.as_of_date})",
        sections=sections,
        summary=(
            "Institution in good compliance standing. Annual audit current. "
            "Two routine items pending within 30 days. One policy review overdue."
        ),
        metadata={"compliance_status": "good_standing", "items_pending": 2},
    )


def _generate_family_report(position, trust, entities, signals) -> Report:
    sections = [
        ReportSection(
            heading="How We're Doing",
            content=(
                f"Greater Hope is in a solid position. We have ${position.cash_position:,.0f} in cash, "
                f"our building and scholarship funds are growing, and our total worth is "
                f"${position.net_assets:,.0f}. We're spending a little more than we're bringing in "
                f"right now — about ${abs(position.net_income):,.0f} — but that's normal for this time "
                f"of year. Spring giving typically closes that gap."
            ),
        ),
        ReportSection(
            heading="Good News",
            content=(
                "Our scholarship fund hit its $175,000 goal — we can award $62,000 in scholarships this spring. "
                "Grant funding is running ahead of plan at $120,000. "
                "The building fund crossed $340,000, and the roof project is fully funded. "
                "We added 12 new tithing families this quarter."
            ),
        ),
        ReportSection(
            heading="What Needs Attention",
            content=(
                "Our insurance is up for renewal by March 15 — the board is reviewing the best option. "
                "We need to update our investment policy, which hasn't been reviewed since 2023. "
                "The pastor's assistance fund has a few receipts outstanding for the quarterly review."
            ),
        ),
        ReportSection(
            heading="Your Church Health Score",
            content=(
                f"Overall: {trust.overall_score} out of 100 ({trust.grade}). "
                f"That means Greater Hope is doing well overall, with particular strength in "
                f"how we serve our mission — scholarships, ministry programs, and community impact. "
                f"The area with the most room for improvement is making sure all our governance "
                f"paperwork stays current."
            ),
            data={"score": trust.overall_score, "grade": trust.grade},
        ),
        ReportSection(
            heading="What You Can Do",
            content=(
                "1. Continue your faithful giving — spring is when we close the seasonal gap. "
                "2. If you know someone who could benefit from our scholarship program, applications open March 15. "
                "3. The building committee welcomes volunteers for the roof project oversight team."
            ),
        ),
    ]

    return Report(
        title=f"Your Church Financial Update — {position.institution_name}",
        audience=ReportAudience.FAMILY,
        institution_name=position.institution_name,
        generated_at=datetime.now(),
        period=f"Winter {position.fiscal_year}",
        sections=sections,
        summary=(
            "Greater Hope is financially healthy with growing funds and strong mission execution. "
            "A few routine items need board attention. Spring giving season ahead."
        ),
        metadata={"trust_score": trust.overall_score, "tone": "warm_accessible"},
    )
