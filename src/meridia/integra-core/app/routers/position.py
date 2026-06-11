"""Financial Position endpoint — entity-aware."""

from fastapi import APIRouter, Query
from ..models import FinancialPosition
from ..mock_data import get_financial_position

router = APIRouter(prefix="/api/v1", tags=["position"])


@router.get("/position", response_model=FinancialPosition)
def read_position(entity_id: str = Query(default=None)):
    """Return the current financial position for an entity."""
    return get_financial_position(entity_id)
