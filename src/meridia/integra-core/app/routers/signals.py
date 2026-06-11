"""Signal feed endpoint — entity-aware."""

from fastapi import APIRouter, Query
from ..models import Signal, SignalSeverity, SignalCategory
from ..mock_data import get_signals

router = APIRouter(prefix="/api/v1", tags=["signals"])


@router.get("/signals", response_model=list[Signal])
def list_signals(
    entity_id: str = Query(default=None),
    severity: SignalSeverity | None = Query(None),
    category: SignalCategory | None = Query(None),
    action_required: bool | None = Query(None),
):
    """Return the signal feed for an entity."""
    signals = get_signals(entity_id)

    if severity:
        signals = [s for s in signals if s.severity == severity]
    if category:
        signals = [s for s in signals if s.category == category]
    if action_required is not None:
        signals = [s for s in signals if s.action_required == action_required]

    return signals
