"""
Integra Core — Scenario Engine
Projects financial impact of hypothetical changes.
"""

from ..models import ScenarioRequest, ScenarioProjection
from ..mock_data import get_financial_position
from .trust_index import project_trust_index


def run_scenario(request: ScenarioRequest) -> ScenarioProjection:
    """Run a financial scenario projection."""
    position = get_financial_position()

    # Calculate projected figures
    revenue_multiplier = 1 + (request.revenue_change_pct / 100)
    expense_multiplier = 1 + (request.expense_change_pct / 100)

    # Enrollment affects tuition/giving revenue specifically
    enrollment_revenue_impact = position.total_revenue * 0.65 * (request.enrollment_change_pct / 100)

    projected_revenue = (position.total_revenue * revenue_multiplier) + request.grant_amount + enrollment_revenue_impact
    projected_expenses = (position.total_expenses * expense_multiplier) + request.new_program_cost
    projected_net = projected_revenue - projected_expenses
    projected_cash = position.cash_position + projected_net - position.cash_position * 0.1  # reserve adjustment
    monthly_burn = projected_expenses / 12
    projected_runway = round(max(0, projected_cash / monthly_burn), 1) if monthly_burn > 0 else 99

    projected_trust = project_trust_index(
        revenue_change_pct=request.revenue_change_pct + (request.enrollment_change_pct * 0.65),
        expense_change_pct=request.expense_change_pct,
        grant_amount=request.grant_amount,
    )

    # Generate risk flags
    risk_flags = []
    if projected_runway < 2:
        risk_flags.append("Cash runway drops below 2 months — critical liquidity risk")
    elif projected_runway < 3:
        risk_flags.append("Cash runway under 3 months — monitor closely")
    if projected_net < -50_000:
        risk_flags.append("Projected deficit exceeds $50,000 — requires budget revision")
    elif projected_net < 0:
        risk_flags.append("Projected operating deficit — manageable if temporary")
    if request.enrollment_change_pct < -10:
        risk_flags.append("Significant enrollment decline impacts giving base sustainability")
    if request.new_program_cost > 50_000:
        risk_flags.append("New program cost significant — phased rollout recommended")
    if projected_trust < 60:
        risk_flags.append("Trust Index projected below 60 — governance intervention recommended")

    # Generate opportunities
    opportunities = []
    if request.grant_amount > 0:
        opportunities.append(f"Grant of ${request.grant_amount:,.0f} strengthens financial position and mission alignment score")
    if projected_net > 0:
        opportunities.append("Projected surplus allows reserve building or program expansion")
    if request.enrollment_change_pct > 5:
        opportunities.append("Growing enrollment supports revenue diversification and community impact")
    if projected_trust > 80:
        opportunities.append("Trust Index above 80 positions institution well for major grant applications")
    if projected_runway > 6:
        opportunities.append("Strong cash position enables strategic investment in facilities or programs")

    if not opportunities:
        opportunities.append("Scenario presents manageable challenges — no critical opportunities at risk")

    # Build narrative
    scenario_name = request.name or _infer_scenario_name(request)
    narrative = _build_narrative(scenario_name, position, projected_revenue, projected_expenses,
                                 projected_net, projected_cash, projected_runway, projected_trust, risk_flags)

    return ScenarioProjection(
        scenario_name=scenario_name,
        projected_revenue=round(projected_revenue, 2),
        projected_expenses=round(projected_expenses, 2),
        projected_net_income=round(projected_net, 2),
        projected_cash_position=round(projected_cash, 2),
        projected_months_runway=projected_runway,
        projected_trust_score=projected_trust,
        risk_flags=risk_flags,
        opportunities=opportunities,
        narrative=narrative,
    )


def _infer_scenario_name(req: ScenarioRequest) -> str:
    parts = []
    if req.enrollment_change_pct != 0:
        direction = "increase" if req.enrollment_change_pct > 0 else "decline"
        parts.append(f"Enrollment {direction} {abs(req.enrollment_change_pct):.0f}%")
    if req.grant_amount > 0:
        parts.append(f"${req.grant_amount:,.0f} grant received")
    if req.new_program_cost > 0:
        parts.append(f"New program (${req.new_program_cost:,.0f})")
    if req.revenue_change_pct != 0:
        direction = "increase" if req.revenue_change_pct > 0 else "decrease"
        parts.append(f"Revenue {direction} {abs(req.revenue_change_pct):.0f}%")
    if req.expense_change_pct != 0:
        direction = "increase" if req.expense_change_pct > 0 else "reduction"
        parts.append(f"Expense {direction} {abs(req.expense_change_pct):.0f}%")
    return " + ".join(parts) if parts else "Baseline scenario"


def _build_narrative(name, position, rev, exp, net, cash, runway, trust, flags) -> str:
    tone = "favorable" if net > 0 and runway > 3 else "manageable" if runway > 2 else "concerning"

    narrative = f"Under the \"{name}\" scenario, projected revenue is ${rev:,.0f} and projected expenses are ${exp:,.0f}"

    if net >= 0:
        narrative += f", yielding a surplus of ${net:,.0f}. "
    else:
        narrative += f", resulting in a deficit of ${abs(net):,.0f}. "

    narrative += f"Cash position would be approximately ${cash:,.0f} with {runway} months of runway. "
    narrative += f"The projected Trust Index is {trust}/100. "

    if tone == "favorable":
        narrative += "This scenario presents a favorable outlook with room for strategic investment."
    elif tone == "manageable":
        narrative += "This scenario is manageable but warrants monitoring of cash position and seasonal revenue patterns."
    else:
        narrative += "This scenario raises liquidity concerns that would require proactive budget adjustments."

    return narrative
