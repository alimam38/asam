"""
Integra Core — Trust Index Service
Calculates composite institutional health score across four dimensions.
"""

from ..mock_data import get_trust_index
from ..models import TrustIndex


def calculate_trust_index() -> TrustIndex:
    """Return the current Trust Index for the demo institution."""
    return get_trust_index()


def project_trust_index(
    revenue_change_pct: float = 0.0,
    expense_change_pct: float = 0.0,
    grant_amount: float = 0.0,
) -> float:
    """
    Project what the Trust Index would be under modified conditions.
    Returns adjusted overall score.
    """
    base = get_trust_index()
    score = base.overall_score

    # Revenue changes affect Financial Health dimension
    if revenue_change_pct < -10:
        score -= 6
    elif revenue_change_pct < -5:
        score -= 3
    elif revenue_change_pct > 10:
        score += 4
    elif revenue_change_pct > 5:
        score += 2

    # Expense changes
    if expense_change_pct > 10:
        score -= 4
    elif expense_change_pct > 5:
        score -= 2
    elif expense_change_pct < -5:
        score += 2

    # Grants improve Mission Alignment and Financial Health
    if grant_amount > 100_000:
        score += 5
    elif grant_amount > 50_000:
        score += 3
    elif grant_amount > 0:
        score += 1

    return round(max(0, min(100, score)), 1)
