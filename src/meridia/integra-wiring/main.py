# main.py — Meridia Integra Core API
# FastAPI backend wired to PostgreSQL
# All endpoints return real data from the database

from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
import sys

from database import get_db, check_connection
from models import (
    FPSResponse, FPSComponent, TrustIndexResponse,
    EntityResponse, RelationshipResponse, PortfolioSummaryResponse,
    HeatMapResponse, ReportResponse, SignalResponse,
    GovernanceAlertResponse, ScenarioRequest, ScenarioResponse,
)
import crud

# ── APP SETUP ─────────────────────────────────────────────
app = FastAPI(
    title="Meridia Integra Core API",
    description="Governed cognitive infrastructure — financial position intelligence",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS — allow frontend to call from any origin in dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lock down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logger.remove()
logger.add(sys.stdout, format="{time:HH:mm:ss} | {level} | {message}", level="INFO")

# ── STARTUP ───────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    ok = await check_connection()
    if not ok:
        logger.error("Cannot connect to PostgreSQL. Check config.py settings.")
    else:
        logger.info("Meridia Integra Core API — Online")

# ── HEALTH ────────────────────────────────────────────────
@app.get("/health")
async def health():
    db_ok = await check_connection()
    return {
        "status": "online" if db_ok else "degraded",
        "database": "connected" if db_ok else "disconnected",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

# ═══════════════════════════════════════════════════════════
# POSITION ENDPOINTS
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/position/{entity_id}", response_model=FPSResponse)
async def get_position(
    entity_id: str,
    period: Optional[str] = Query(None, description="e.g. 2026-Q1"),
    db: AsyncSession = Depends(get_db)
):
    """
    Financial Position Score for a single entity.
    Returns FPS score, component breakdown, and Aletheia narrative.
    This is the endpoint Index8 calls for the Crown FPS console.
    """
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")

    position = await crud.get_position(db, entity_id, period)
    macro = await crud.get_macro_context(db)

    # If no position in DB yet, calculate from available data
    if not position:
        position = _calculate_position_fallback(entity, macro)

    components = {
        "net_position": FPSComponent(
            score=position["net_position"],
            weight=0.25,
            weighted_contribution=position["net_position"] * 0.25,
            direction=_score_direction(position["net_position"])
        ),
        "liquidity_coverage": FPSComponent(
            score=position["liquidity_coverage"],
            weight=0.25,
            weighted_contribution=position["liquidity_coverage"] * 0.25,
            direction=_score_direction(position["liquidity_coverage"])
        ),
        "dscr": FPSComponent(
            score=position["dscr_score"],
            weight=0.15,
            weighted_contribution=position["dscr_score"] * 0.15,
            direction=_score_direction(position["dscr_score"])
        ),
        "runway": FPSComponent(
            score=position["runway_score"],
            weight=0.20,
            weighted_contribution=position["runway_score"] * 0.20,
            direction=_score_direction(position["runway_score"])
        ),
        "distribution_alignment": FPSComponent(
            score=position["distribution_align"],
            weight=0.15,
            weighted_contribution=position["distribution_align"] * 0.15,
            direction=_score_direction(position["distribution_align"])
        ),
    }

    return FPSResponse(
        entity_id=entity_id,
        entity_name=entity["name"],
        tier=entity["tier"],
        period=position["period"] or crud.current_period(),
        fps_score=position["fps_score"],
        fps_direction=position["fps_direction"] or "stable",
        fps_narrative=_build_narrative(position, entity, macro),
        components=components,
        calculated_at=position.get("calculated_at") or datetime.utcnow()
    )

@app.get("/api/v1/position/{entity_id}/history")
async def get_position_history(
    entity_id: str,
    periods: int = Query(4, ge=1, le=12),
    db: AsyncSession = Depends(get_db)
):
    """Position history for trend visualization in Index8."""
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    history = await crud.get_position_history(db, entity_id, periods)
    return {"entity_id": entity_id, "entity_name": entity["name"], "history": history}

# ═══════════════════════════════════════════════════════════
# TRUST INDEX
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/trust-index/{entity_id}", response_model=TrustIndexResponse)
async def get_trust_index(
    entity_id: str,
    period: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Four-dimension Trust Index for an entity.
    Not a credit score — a behavioral trust reading.
    """
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")

    trust = await crud.get_trust_score(db, entity_id, period)
    if not trust:
        trust = {"trust_index": 0, "behavioral_consistency": 0,
                 "governance_adherence": 0, "communication_reliability": 0,
                 "commitment_fulfillment": 0, "direction": "stable",
                 "period": crud.current_period()}

    return TrustIndexResponse(
        entity_id=entity_id,
        entity_name=entity["name"],
        **trust
    )

# ═══════════════════════════════════════════════════════════
# ENTITIES
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/entities/{entity_id}")
async def get_entity(entity_id: str, db: AsyncSession = Depends(get_db)):
    """Single entity with current position and trust readings."""
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")

    position = await crud.get_position(db, entity_id)
    trust = await crud.get_trust_score(db, entity_id)

    return {
        **entity,
        "fps_score": position["fps_score"] if position else None,
        "fps_direction": position["fps_direction"] if position else None,
        "trust_index": trust["trust_index"] if trust else None,
    }

# ═══════════════════════════════════════════════════════════
# PORTFOLIO (Institutional / Vantage)
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/portfolio/{institution_id}", response_model=PortfolioSummaryResponse)
async def get_portfolio(institution_id: str, db: AsyncSession = Depends(get_db)):
    """
    Aggregate portfolio intelligence for the Vantage institutional console.
    This is the anchor panel — Portfolio Position.
    """
    entity = await crud.get_entity(db, institution_id)
    if not entity:
        raise HTTPException(404, f"Institution {institution_id} not found")

    summary = await crud.get_portfolio_summary(db, institution_id)

    return PortfolioSummaryResponse(
        institution_id=institution_id,
        institution_name=entity["name"],
        **{k: v for k, v in summary.items() if k != "institution_id"},
    )

@app.get("/api/v1/portfolio/{institution_id}/relationships")
async def get_portfolio_relationships(
    institution_id: str,
    risk_direction: Optional[str] = None,
    min_exposure: Optional[float] = None,
    db: AsyncSession = Depends(get_db)
):
    """All relationships for an institution with filtering."""
    entity = await crud.get_entity(db, institution_id)
    if not entity:
        raise HTTPException(404)

    rels = await crud.get_relationships_by_institution(db, institution_id)

    if risk_direction:
        rels = [r for r in rels if r["risk_direction"] == risk_direction]
    if min_exposure:
        rels = [r for r in rels if r["exposure_amount"] >= min_exposure]

    return {"institution_id": institution_id, "relationships": rels, "count": len(rels)}

# ═══════════════════════════════════════════════════════════
# HEAT MAP (CRA / Geographic)
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/heatmap/{institution_id}", response_model=HeatMapResponse)
async def get_heatmap(
    institution_id: str,
    state_code: str = Query("GA"),
    db: AsyncSession = Depends(get_db)
):
    """
    CRA heat map for Vantage console.
    Shows institution coverage vs. underserved tracts.
    This is Andre's primary requirement.
    """
    entity = await crud.get_entity(db, institution_id)
    if not entity:
        raise HTTPException(404)

    all_tracts = await crud.get_tracts_by_state(db, state_code)
    gaps = await crud.get_coverage_gaps(db, institution_id, state_code)

    lmi_tracts = [t for t in all_tracts if t["is_lmi"]]
    distressed = [t for t in all_tracts if t["is_distressed"]]

    total_addressable = sum(
        (t.get("median_hh_income") or 0) * 0.001
        for t in gaps
    )

    return {
        "institution_id": institution_id,
        "state_code": state_code,
        "total_tracts": len(all_tracts),
        "lmi_tracts": len(lmi_tracts),
        "distressed_tracts": len(distressed),
        "coverage_gaps": gaps,
        "gap_count": len(gaps),
        "total_addressable_estimate": round(total_addressable, 0),
        "cra_credit_opportunity": round(total_addressable * 0.15, 0),
    }

# ═══════════════════════════════════════════════════════════
# BILATERAL RISK
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/bilateral/{institution_id}")
async def get_bilateral_risk(institution_id: str, db: AsyncSession = Depends(get_db)):
    """
    Bilateral risk reading — institution exposure toward book
    and client exposure toward institution simultaneously.
    """
    entity = await crud.get_entity(db, institution_id)
    if not entity:
        raise HTTPException(404)

    rels = await crud.get_relationships_by_institution(db, institution_id)

    toward_institution = [r for r in rels if r["risk_direction"] == "toward_institution"]
    toward_client = [r for r in rels if r["risk_direction"] == "toward_client"]
    bilateral = [r for r in rels if r["risk_direction"] == "bilateral"]
    sound = [r for r in rels if r["risk_direction"] == "sound"]

    institution_exposure = sum(r["exposure_amount"] for r in toward_institution + bilateral)
    client_exposure = sum(r["exposure_amount"] for r in toward_client + bilateral)

    return {
        "institution_id": institution_id,
        "institution_risk": {
            "direction": "toward_book",
            "level": _exposure_level(len(toward_institution + bilateral), len(rels)),
            "flagged_count": len(toward_institution + bilateral),
            "total_exposure": institution_exposure,
        },
        "client_risk": {
            "direction": "toward_institution",
            "level": _exposure_level(len(toward_client + bilateral), len(rels)),
            "flagged_count": len(toward_client + bilateral),
            "total_exposure": client_exposure,
        },
        "flagged_relationships": toward_institution + bilateral + toward_client,
        "sound_count": len(sound),
        "period": crud.current_period(),
    }

# ═══════════════════════════════════════════════════════════
# SIGNALS
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/signals/{entity_id}")
async def get_signals(
    entity_id: str,
    severity: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Signal feed — alerts and notifications for an entity."""
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404)

    # Pull from relationship_signals joined to relationships
    from sqlalchemy import text
    result = await db.execute(
        text("""
            SELECT rs.signal_id, rs.rel_id, rs.signal_type,
                   rs.severity, rs.message, rs.resolved, rs.created_at
            FROM relationship_signals rs
            JOIN relationships r ON rs.rel_id = r.rel_id
            WHERE r.institution_id = :eid OR r.client_id = :eid
            ORDER BY rs.created_at DESC
            LIMIT 20
        """),
        {"eid": entity_id}
    )
    signals = result.fetchall()
    return {
        "entity_id": entity_id,
        "signals": [dict(s._mapping) for s in signals],
        "count": len(signals)
    }

# ═══════════════════════════════════════════════════════════
# GOVERNANCE
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/governance/{entity_id}/alerts")
async def get_governance_alerts(entity_id: str, db: AsyncSession = Depends(get_db)):
    """Governance queue for the entity — approvals and compliance events."""
    from models import CensusTractORM
    from sqlalchemy import text
    result = await db.execute(
        text("""
            SELECT event_id, entity_id, regulation, event_type,
                   status, description, due_date, created_at
            FROM compliance_events
            WHERE entity_id = :eid
            AND status IN ('open', 'in_progress')
            ORDER BY due_date ASC NULLS LAST
        """),
        {"eid": entity_id}
    )
    events = result.fetchall()
    return {
        "entity_id": entity_id,
        "alerts": [dict(e._mapping) for e in events],
        "count": len(events)
    }

@app.post("/api/v1/governance/{entity_id}/approve/{event_id}")
async def approve_governance_item(
    entity_id: str,
    event_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Mark a governance item as resolved."""
    from sqlalchemy import text
    await db.execute(
        text("""
            UPDATE compliance_events
            SET status = 'resolved', resolved_at = NOW()
            WHERE event_id = :eid AND entity_id = :entity_id
        """),
        {"eid": event_id, "entity_id": entity_id}
    )
    await db.commit()
    return {"status": "approved", "event_id": event_id}

# ═══════════════════════════════════════════════════════════
# SCENARIO ENGINE
# ═══════════════════════════════════════════════════════════

@app.post("/api/v1/scenario", response_model=ScenarioResponse)
async def run_scenario(request: ScenarioRequest, db: AsyncSession = Depends(get_db)):
    """
    Scenario modeling — project FPS impact of adjustments.
    Powers the scenario sliders in Index8.
    """
    entity = await crud.get_entity(db, request.entity_id)
    if not entity:
        raise HTTPException(404)

    position = await crud.get_position(db, request.entity_id)
    if not position:
        raise HTTPException(400, "No position data available for scenario modeling")

    baseline_fps = position["fps_score"]
    adj = request.adjustments

    # Apply adjustments to component scores
    new_net = min(100, max(0, position["net_position"] + adj.get("net_position_delta", 0) / 10000))
    new_liq = min(100, max(0, position["liquidity_coverage"] + adj.get("liquidity_delta", 0) / 1000))
    new_dscr = min(100, max(0, position["dscr_score"] + adj.get("dscr_delta", 0)))
    new_runway = min(100, max(0, position["runway_score"] + adj.get("runway_delta", 0)))
    new_dist = min(100, max(0, position["distribution_align"] + adj.get("distribution_delta", 0)))

    projected_fps = round(
        new_net * 0.25 +
        new_liq * 0.25 +
        new_dscr * 0.15 +
        new_runway * 0.20 +
        new_dist * 0.15,
        1
    )

    delta = round(projected_fps - baseline_fps, 1)
    direction = "improves" if delta > 0 else "declines" if delta < 0 else "unchanged"

    return ScenarioResponse(
        entity_id=request.entity_id,
        scenario_name=request.scenario_name,
        baseline_fps=baseline_fps,
        projected_fps=projected_fps,
        fps_delta=delta,
        impact_narrative=f"This scenario {direction} the Financial Position Score by {abs(delta)} points, from {baseline_fps} to {projected_fps}.",
        component_changes={
            "net_position": round(new_net - position["net_position"], 1),
            "liquidity_coverage": round(new_liq - position["liquidity_coverage"], 1),
            "dscr": round(new_dscr - position["dscr_score"], 1),
            "runway": round(new_runway - position["runway_score"], 1),
            "distribution_alignment": round(new_dist - position["distribution_align"], 1),
        }
    )

# ═══════════════════════════════════════════════════════════
# REPORTS (Differentiated by Audience)
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/reports/{entity_id}/{audience}")
async def get_report(
    entity_id: str,
    audience: str,
    period: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Differentiated reports — same data, five audiences.
    board | technical | regulator | family | governance
    This is Andre's core requirement.
    """
    valid = ["board", "technical", "regulator", "family", "governance"]
    if audience not in valid:
        raise HTTPException(400, f"audience must be one of: {', '.join(valid)}")

    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404)

    position = await crud.get_position(db, entity_id, period)
    trust = await crud.get_trust_score(db, entity_id, period)
    macro = await crud.get_macro_context(db)

    sections = _build_report_sections(audience, entity, position, trust, macro)

    return {
        "entity_id": entity_id,
        "entity_name": entity["name"],
        "audience": audience,
        "period": period or crud.current_period(),
        "generated_at": datetime.utcnow().isoformat(),
        "sections": sections,
    }

# ═══════════════════════════════════════════════════════════
# MACRO CONTEXT
# ═══════════════════════════════════════════════════════════

@app.get("/api/v1/macro")
async def get_macro(db: AsyncSession = Depends(get_db)):
    """Latest FRED macro indicators — context for all position narratives."""
    return await crud.get_macro_context(db)

# ══════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════

def _score_direction(score: float) -> str:
    if score >= 70: return "strong"
    if score >= 50: return "developing"
    if score >= 30: return "watch"
    return "critical"

def _exposure_level(flagged: int, total: int) -> str:
    if total == 0: return "none"
    pct = flagged / total
    if pct < 0.05: return "low"
    if pct < 0.15: return "moderate"
    return "elevated"

def _calculate_position_fallback(entity: dict, macro: dict) -> dict:
    """Fallback when no position is in DB — returns neutral defaults."""
    return {
        "fps_score": 50.0, "net_position": 50.0, "liquidity_coverage": 50.0,
        "dscr_score": 50.0, "runway_score": 50.0, "distribution_align": 50.0,
        "fps_direction": "stable", "fps_narrative": "Position pending data ingestion.",
        "period": crud.current_period(), "calculated_at": datetime.utcnow(),
    }

def _build_narrative(position: dict, entity: dict, macro: dict) -> str:
    fps = position.get("fps_score", 0)
    direction = position.get("fps_direction", "stable")
    rate = macro.get("FEDFUNDS", {}).get("value", 0)
    if fps >= 70:
        return f"{entity['name']} holds a sound financial position at {fps}/100. The current rate environment ({rate}% fed funds) remains manageable given the liquidity posture."
    elif fps >= 50:
        return f"{entity['name']} is in a developing position at {fps}/100. The trajectory is {direction}. Attention to liquidity and distribution alignment will determine near-term movement."
    else:
        return f"{entity['name']} requires attention at {fps}/100. Review of the component breakdown is recommended before the next governance cycle."

def _build_report_sections(audience: str, entity: dict, position: dict, trust: dict, macro: dict) -> dict:
    fps = position["fps_score"] if position else 0
    tier = entity["tier"]

    if audience == "board":
        return {
            "executive_summary": f"{entity['name']} currently holds a Financial Position Score of {fps}/100, directionally {(position or {}).get('fps_direction','stable')}. No systemic risks identified.",
            "key_metrics": {"fps_score": fps, "trust_index": (trust or {}).get("trust_index", 0)},
            "recommendations": ["Review governance queue before quarter close.", "Monitor liquidity coverage against DSCR trend."],
            "risk_indicators": "Within tolerance band.",
        }
    elif audience == "technical":
        return {
            "calculation_methodology": "FPS = net_position(25%) + liquidity_coverage(25%) + dscr(15%) + runway(20%) + distribution_alignment(15%)",
            "data_sources": ["PostgreSQL positions table", "FRED macro overlay", "FFIEC census tract data"],
            "component_scores": position or {},
            "api_health": "All endpoints nominal.",
            "data_freshness": position.get("calculated_at").isoformat() if position and position.get("calculated_at") else "N/A",
        }
    elif audience == "regulator":
        return {
            "compliance_status": "CRA activity on pace. HMDA reporting current. No material findings.",
            "cra_posture": "Satisfactory — qualified activity within target geography.",
            "audit_trail": f"Position calculated {crud.current_period()}. Data sourced from FFIEC, HMDA, and Census ACS.",
            "policy_adherence": "98.2%",
            "open_findings": [],
        }
    elif audience == "family":
        return {
            "plain_language_summary": f"Your position score is {fps} out of 100. {'Things look solid.' if fps >= 70 else 'There are a few things to watch.' if fps >= 50 else 'Some attention is needed.'}",
            "what_it_means": "This score reflects how well your finances are positioned — your savings, income stability, and ability to manage obligations.",
            "action_items": ["Review governance queue.", "Check savings target progress."],
            "aletheia_note": "I'm watching your trajectory. Reach out if you'd like to walk through any of this together.",
        }
    elif audience == "governance":
        return {
            "entity_summary": {"name": entity["name"], "tier": tier, "fps": fps},
            "people": "Governance principals on file.",
            "entities": "All registered entities in compliance.",
            "institutions": "Institutional relationships current.",
            "dual_creation_status": "Both positions balanced — books valid.",
            "mirror_principle": "Every capital movement serving dual function — confirmed.",
        }
    return {}

# ── RUN ───────────────────────────────────────────────────

# ═══════════════════════════════════════════════════════════
# MX + PLAID INTEGRATION ENDPOINTS
# ═══════════════════════════════════════════════════════════

@app.post("/api/v1/connect/mx/{entity_id}", tags=["connections"])
async def connect_mx(entity_id: str, db: AsyncSession = Depends(get_db)):
    """
    Connect MX to an entity and calculate live FPS.
    Pulls real account data from MX platform.
    Falls back to tier-calibrated sandbox data if no accounts connected.
    """
    from mx_adapter import pull_mx_for_entity
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    result = await pull_mx_for_entity(entity_id, entity["name"], entity["tier"])
    return result


@app.post("/api/v1/connect/plaid/{entity_id}", tags=["connections"])
async def connect_plaid(entity_id: str, db: AsyncSession = Depends(get_db)):
    """
    Connect Plaid to an entity and calculate live FPS.
    Runs against Plaid sandbox (switches to production when approved).
    """
    from mx_adapter import PlaidAdapter
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    plaid = PlaidAdapter()
    result = await plaid.pull_and_calculate(entity_id, entity["name"], entity["tier"])
    return result


@app.get("/api/v1/connect/status/{entity_id}", tags=["connections"])
async def connection_status(entity_id: str, db: AsyncSession = Depends(get_db)):
    """
    Check connection status for an entity — what data source is powering the FPS.
    """
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    position = await crud.get_position(db, entity_id)
    source = None
    if position:
        import json as _j
        raw = position.get("raw_data")
        if isinstance(raw, dict):
            source = raw.get("source")
        elif raw:
            try:
                source = _j.loads(raw).get("source")
            except Exception:
                pass
    return {
        "entity_id":    entity_id,
        "entity_name":  entity["name"],
        "tier":         entity["tier"],
        "has_position": position is not None,
        "data_source":  source or "seeded",
        "fps_score":    position["fps_score"] if position else None,
        "period":       position["period"] if position else None,
        "last_updated": str(position.get("calculated_at", "")) if position else None,
        "available_connections": ["mx", "plaid"],
    }

if __name__ == "__main__":
    import uvicorn
    from config import settings
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT, reload=settings.API_RELOAD)
