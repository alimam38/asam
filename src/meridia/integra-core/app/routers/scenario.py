"""Scenario modeling endpoint."""

from fastapi import APIRouter
from ..models import ScenarioRequest, ScenarioProjection
from ..services.scenario_engine import run_scenario

router = APIRouter(prefix="/api/v1", tags=["scenario"])


@router.post("/scenario", response_model=ScenarioProjection)
def model_scenario(request: ScenarioRequest):
    """Run a financial scenario projection."""
    return run_scenario(request)
