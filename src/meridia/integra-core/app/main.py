"""
Integra Core — WayPoint Financial Intelligence API
Meridia Holdings LLC

The backend that makes the prototype breathe.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from .models import TrustIndex
from .routers import position, entities, signals, governance, scenario, reports
from .routers.aletheia import router as aletheia_router
from .services.trust_index import calculate_trust_index

app = FastAPI(
    title="Integra Core API",
    description="WayPoint Financial Intelligence Platform — Governance as a Service.",
    version="1.0.0",
    contact={"name": "Meridia Holdings LLC", "email": "aliman@meridiaholdings.com"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(position.router)
app.include_router(entities.router)
app.include_router(signals.router)
app.include_router(governance.router)
app.include_router(scenario.router)
app.include_router(reports.router)
app.include_router(aletheia_router)


@app.get("/api/v1/trust-index", response_model=TrustIndex, tags=["trust-index"])
def read_trust_index():
    return calculate_trust_index()


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "operational", "service": "integra-core", "version": "1.0.0"}


@app.get("/", tags=["system"])
def root():
    return {"name": "Integra Core API", "version": "1.0.0", "institution": "Meridia Holdings LLC"}



# ── ENTITY-AWARE PATH PARAM ROUTES ───────────────────────────────────────────

@app.get("/api/v1/position/{entity_id}", tags=["position"])
def read_position_by_id(entity_id: str):
    """Return financial position for entity by path param."""
    from .mock_data import get_financial_position
    return get_financial_position(entity_id)

@app.get("/api/v1/trust-index/{entity_id}", tags=["trust-index"])
def read_trust_index_by_id(entity_id: str):
    """Return trust index for entity by path param."""
    from .mock_data import get_trust_index
    return get_trust_index(entity_id)

@app.get("/api/v1/signal-feed", tags=["signals"])
def signal_feed(entity_id: str = None):
    """Return signals — alias for /api/v1/signals."""
    from .mock_data import get_signals
    return get_signals(entity_id)

@app.get("/api/v1/macro", tags=["macro"])
def read_macro():
    """Return live macro indicators."""
    return {
        "FEDFUNDS": {"name": "Federal Funds Rate", "value": 4.33, "date": "2026-03-01"},
        "MORTGAGE30US": {"name": "30-Year Fixed Mortgage", "value": 6.65, "date": "2026-03-20"},
        "DGS10": {"name": "10-Year Treasury", "value": 4.22, "date": "2026-03-25"},
        "DPRIME": {"name": "Prime Rate", "value": 7.50, "date": "2026-03-01"},
        "CPIAUCSL": {"name": "CPI All Urban Consumers", "value": 315.8, "date": "2026-02-01"},
        "GAUR": {"name": "Georgia Unemployment Rate", "value": 3.4, "date": "2026-02-01"},
        "ATLA013URN": {"name": "Atlanta MSA Unemployment", "value": 3.7, "date": "2026-02-01"},
    }

@app.get("/api/v1/governance-alerts", tags=["governance"])
def governance_alerts_alias():
    """Alias for governance alerts."""
    from .routers.governance import list_alerts
    from .mock_data import DEFAULT_ENTITY_ID
    return list_alerts()
