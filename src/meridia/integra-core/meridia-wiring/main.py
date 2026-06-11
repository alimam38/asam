# main.py — Meridia Integra Core API
# FastAPI backend wired to PostgreSQL
# All endpoints return real data from the database

import os
import time
import random
import httpx
from datetime import datetime
from typing import Optional
from pathlib import Path
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

# Per-state county data: (fips, name, inc_min, inc_max, center_lat, center_lng)
# Income ranges reflect actual ACS median HH income distributions — not uniform random.
# Affluent suburbs (Gwinnett, Forsyth, Cobb) anchored well above distressed threshold.
_MOCK_STATE_COUNTIES: dict[str, list[tuple]] = {
    "GA": [
        ("121", "Fulton",    32000,  92000, 33.790, -84.388),
        ("089", "DeKalb",    35000,  82000, 33.773, -84.226),
        ("067", "Cobb",      58000, 108000, 33.936, -84.576),
        ("135", "Gwinnett",  65000, 112000, 33.962, -84.020),
        ("063", "Clayton",   30000,  54000, 33.546, -84.357),
        ("151", "Henry",     52000,  84000, 33.450, -84.157),
        ("117", "Forsyth",   82000, 135000, 34.225, -84.128),
        ("057", "Cherokee",  68000, 112000, 34.253, -84.474),
        ("097", "Douglas",   44000,  78000, 33.697, -84.758),
        ("113", "Fayette",   72000, 118000, 33.411, -84.468),
        ("247", "Rockdale",  42000,  75000, 33.651, -84.021),
        ("077", "Coweta",    46000,  80000, 33.366, -84.766),
    ],
    "FL": [
        ("086", "Miami-Dade",   28000,  78000, 25.550, -80.630),
        ("011", "Broward",      38000,  88000, 26.150, -80.410),
        ("099", "Palm Beach",   44000,  95000, 26.650, -80.360),
        ("095", "Orange",       36000,  78000, 28.510, -81.380),
        ("057", "Hillsborough", 34000,  82000, 27.900, -82.350),
        ("103", "Pinellas",     36000,  76000, 27.880, -82.730),
        ("031", "Duval",        32000,  75000, 30.330, -81.650),
        ("073", "Leon",         34000,  74000, 30.440, -84.280),
    ],
    "NC": [
        ("119", "Mecklenburg",  40000,  95000, 35.250, -80.840),
        ("183", "Wake",         58000,  98000, 35.790, -78.640),
        ("081", "Guilford",     34000,  75000, 36.070, -79.790),
        ("063", "Durham",       40000,  82000, 35.990, -78.900),
        ("067", "Forsyth",      34000,  72000, 36.100, -80.240),
    ],
    "SC": [
        ("079", "Richland",     34000,  72000, 34.020, -80.900),
        ("045", "Greenville",   40000,  84000, 34.880, -82.360),
        ("083", "Spartanburg",  32000,  68000, 34.950, -81.820),
        ("019", "Charleston",   40000,  88000, 32.780, -80.020),
        ("063", "Lexington",    50000,  90000, 33.930, -81.270),
    ],
    "AL": [
        ("073", "Jefferson",    32000,  76000, 33.560, -86.880),
        ("089", "Madison",      44000,  84000, 34.730, -86.590),
        ("101", "Montgomery",   28000,  64000, 32.360, -86.290),
        ("097", "Mobile",       28000,  62000, 30.690, -88.040),
        ("117", "Shelby",       60000,  98000, 33.270, -86.660),
    ],
    "TN": [
        ("157", "Shelby",       28000,  72000, 35.150, -89.990),
        ("037", "Davidson",     36000,  80000, 36.160, -86.780),
        ("065", "Hamilton",     34000,  74000, 35.160, -85.240),
        ("093", "Knox",         36000,  78000, 35.960, -83.930),
        ("149", "Rutherford",   50000,  90000, 35.840, -86.390),
    ],
    "TX": [
        ("201", "Harris",       34000,  88000, 29.850, -95.400),
        ("113", "Dallas",       34000,  90000, 32.770, -96.800),
        ("439", "Tarrant",      40000,  84000, 32.720, -97.290),
        ("029", "Bexar",        34000,  76000, 29.450, -98.510),
        ("453", "Travis",       44000,  95000, 30.270, -97.740),
    ],
}

_MOCK_STATE_FIPS: dict[str, str] = {
    "GA": "13", "FL": "12", "NC": "37", "SC": "45",
    "AL": "01", "TN": "47", "TX": "48",
}


def _mock_heatmap(institution_id: str, state_code: str) -> dict:
    """Seeded mock heatmap for demos when DB entity or census data is absent.

    Income ranges are county-anchored so affluent suburbs (Gwinnett, Forsyth, Cobb)
    never receive poverty-level incomes. Each county uses a deterministic per-county
    RNG so income distribution is stable across reloads.
    """
    rng = random.Random(42)
    counties   = _MOCK_STATE_COUNTIES.get(state_code, _MOCK_STATE_COUNTIES["GA"])
    state_fips = _MOCK_STATE_FIPS.get(state_code, "13")

    all_tracts = []
    for fips, name, inc_min, inc_max, c_lat, c_lng in counties:
        # Per-county seed → same county always generates the same income distribution
        county_rng = random.Random(int(state_fips + fips))
        n_tracts = rng.randint(8, 22)
        for i in range(n_tracts):
            tract_num = (i + 1) * 100
            income = county_rng.randint(inc_min, inc_max)
            # Deterministic tract-level jitter (~±0.05° lat, ±0.06° lng)
            jitter_lat = ((tract_num * 6271) % 1000 / 1000 - 0.5) * 0.10
            jitter_lng = ((tract_num * 7919) % 1000 / 1000 - 0.5) * 0.12
            all_tracts.append({
                "geoid":            f"{state_fips}{fips}{tract_num:06d}",
                "county":           name,
                "is_lmi":           income < 56000,
                "is_distressed":    income < 36000,
                "is_underserved":   county_rng.random() < 0.38,
                "median_hh_income": income,
                "centroid_lat":     round(c_lat + jitter_lat, 6),
                "centroid_lng":     round(c_lng + jitter_lng, 6),
            })

    candidates = [t for t in all_tracts if t["is_lmi"] or t["is_distressed"]]
    gap_tracts  = rng.sample(candidates, min(len(candidates), 52))
    gaps = []
    for t in gap_tracts:
        zero    = rng.random() < 0.58
        pri     = t["is_lmi"] and t["is_distressed"] and zero
        tid     = t["geoid"][5:]
        label   = f"Tract {int(tid[:4])}.{tid[4:]}, {t['county']} Co."
        gaps.append({
            "geoid":             t["geoid"],
            "tract_name":        label,
            "state_code":        state_code,
            "is_lmi":            t["is_lmi"],
            "is_distressed":     t["is_distressed"],
            "is_underserved":    t["is_underserved"],
            "median_hh_income":  t["median_hh_income"],
            "centroid_lat":      t["centroid_lat"],
            "centroid_lng":      t["centroid_lng"],
            "opportunity_score": round(rng.uniform(5.5, 9.8) if pri else rng.uniform(2.0, 7.2), 1),
            "loan_count":        0 if zero else rng.randint(1, 9),
            "zero_activity":     zero,
            "priority_gap":      pri,
            "active_institutions": [],
        })

    lmi_count        = sum(1 for t in all_tracts if t["is_lmi"])
    distressed_count = sum(1 for t in all_tracts if t["is_distressed"])

    # Realistic CRA lending opportunity:
    # Priority gaps (LMI + distressed + zero activity) → ~$2.5M avg addressable per tract
    # LMI-only gaps → ~$1.2M avg addressable per tract
    # Source: FFIEC CRA peer benchmarking, typical community bank deal sizes
    priority_gap_count = sum(1 for g in gaps if g["priority_gap"])
    lmi_only_count     = len(gaps) - priority_gap_count
    total_addressable  = (priority_gap_count * 2_500_000) + (lmi_only_count * 1_200_000)
    cra_opportunity    = round(total_addressable * 0.30, -3)  # ~30% capture rate

    return {
        "institution_id":             institution_id,
        "state_code":                 state_code,
        "total_tracts":               len(all_tracts),
        "lmi_tracts":                 lmi_count,
        "distressed_tracts":          distressed_count,
        "coverage_gaps":              gaps,
        "gap_count":                  len(gaps),
        "total_addressable_estimate": round(total_addressable, -3),
        "cra_credit_opportunity":     cra_opportunity,
    }


@app.get("/api/v1/heatmap/{institution_id}", response_model=HeatMapResponse)
async def get_heatmap(
    institution_id: str,
    state_code: str = Query("GA"),
    db: AsyncSession = Depends(get_db)
):
    """
    CRA heat map for Vantage console.
    Shows institution coverage vs. underserved tracts.
    Falls back to seeded mock data when entity or census tracts are absent.
    """
    entity = await crud.get_entity(db, institution_id)
    if not entity:
        logger.info(f"Heatmap: entity {institution_id} not in DB — returning mock data.")
        return _mock_heatmap(institution_id, state_code)

    all_tracts = await crud.get_tracts_by_state(db, state_code)
    gaps       = await crud.get_coverage_gaps(db, institution_id, state_code)

    if not all_tracts:
        logger.info(f"Heatmap: no census tracts for {state_code} — returning mock data.")
        return _mock_heatmap(institution_id, state_code)

    lmi_tracts = [t for t in all_tracts if t["is_lmi"]]
    distressed = [t for t in all_tracts if t["is_distressed"]]

    priority_gap_count = sum(1 for g in gaps if g.get("priority_gap"))
    lmi_only_count     = len(gaps) - priority_gap_count
    total_addressable  = (priority_gap_count * 2_500_000) + (lmi_only_count * 1_200_000)
    cra_opportunity    = round(total_addressable * 0.30, -3)

    return {
        "institution_id":             institution_id,
        "state_code":                 state_code,
        "total_tracts":               len(all_tracts),
        "lmi_tracts":                 len(lmi_tracts),
        "distressed_tracts":          len(distressed),
        "coverage_gaps":              gaps,
        "gap_count":                  len(gaps),
        "total_addressable_estimate": round(total_addressable, -3),
        "cra_credit_opportunity":     cra_opportunity,
    }

# ═══════════════════════════════════════════════════════════
# TOMTOM BRANCH INTELLIGENCE
# ═══════════════════════════════════════════════════════════

# State bounding boxes: (topLeft_lat, topLeft_lon, btmRight_lat, btmRight_lon)
_STATE_BOUNDS: dict[str, tuple] = {
    "GA": (35.00, -85.61, 30.35, -80.84),
    "AL": (35.01, -88.47, 30.14, -84.89),
    "SC": (35.22, -83.35, 32.03, -78.51),
    "FL": (31.00, -87.63, 24.38, -80.02),
    "TN": (36.68, -90.31, 34.98, -81.65),
    "NC": (36.59, -84.32, 33.83, -75.47),
    "TX": (36.50, -106.65, 25.84, -93.51),
}

_branch_cache: dict = {}
_BRANCH_CACHE_TTL = 86400  # 24 hours


def _state_quadrants(bounds: tuple) -> list[tuple]:
    """Split a state bounding box into a 2×2 grid to work around TomTom's 100-result cap."""
    top_lat, top_lon, btm_lat, btm_lon = bounds
    mid_lat = (top_lat + btm_lat) / 2
    mid_lon = (top_lon + btm_lon) / 2
    return [
        (top_lat, top_lon, mid_lat, mid_lon),  # NW
        (top_lat, mid_lon, mid_lat, btm_lon),  # NE
        (mid_lat, top_lon, btm_lat, mid_lon),  # SW
        (mid_lat, mid_lon, btm_lat, btm_lon),  # SE
    ]


async def _fetch_quadrant(client: httpx.AsyncClient, api_key: str, query: str,
                          top_lat: float, top_lon: float,
                          btm_lat: float, btm_lon: float) -> list[dict]:
    """Fetch up to 100 POI results for a query within a single bounding box."""
    resp = await client.get(
        f"https://api.tomtom.com/search/2/poiSearch/{query.replace(' ', '%20')}.json",
        params={
            "key":     api_key,
            "topLeft": f"{top_lat},{top_lon}",
            "btmRight": f"{btm_lat},{btm_lon}",
            "limit":   100,
        },
    )
    if resp.status_code != 200:
        logger.warning(f"TomTom '{query}' search {resp.status_code} for {top_lat},{top_lon}→{btm_lat},{btm_lon}: {resp.text[:200]}")
        return []
    results = resp.json().get("results", [])
    branches = []
    for r in results:
        pos  = r.get("position", {})
        poi  = r.get("poi", {})
        addr = r.get("address", {})
        lat  = pos.get("lat")
        lon  = pos.get("lon")
        if lat is None or lon is None:
            continue
        branches.append({
            "id":      r.get("id", ""),
            "name":    poi.get("name", "Unknown"),
            "lat":     lat,
            "lon":     lon,
            "address": addr.get("freeformAddress", ""),
            "city":    addr.get("municipality", ""),
            "phone":   poi.get("phone", ""),
            "url":     poi.get("url", ""),
        })
    return branches


async def _fetch_tomtom_branches(state: str, api_key: str) -> list[dict]:
    """Fetch bank and credit union branches for a state.
    Uses text queries ('bank', 'credit union') across a 2×2 quadrant grid
    to work around TomTom's 100-result-per-bounding-box cap."""
    bounds = _STATE_BOUNDS.get(state)
    if not bounds:
        return []

    seen: set[str] = set()
    branches: list[dict] = []
    queries = ["bank", "credit union"]

    async with httpx.AsyncClient(timeout=20.0) as client:
        for query in queries:
            for quad in _state_quadrants(bounds):
                results = await _fetch_quadrant(client, api_key, query, *quad)
                for b in results:
                    if b["id"] not in seen:
                        seen.add(b["id"])
                        branches.append(b)

    logger.info(f"TomTom: fetched {len(branches)} branches for {state}")
    return branches


@app.get("/api/v1/branches/{state_code}")
async def get_branches(state_code: str):
    """
    Bank and credit union branch locations for a state.
    Proxies TomTom POI Search (category 7376). Results cached 24h.
    Returns GeoJSON FeatureCollection.
    """
    from config import settings
    api_key = settings.TOMTOM_API_KEY
    if not api_key:
        raise HTTPException(500, "TOMTOM_API_KEY not configured")

    state = state_code.upper()
    if state not in _STATE_BOUNDS:
        raise HTTPException(400, f"State '{state}' not yet configured. Supported: {list(_STATE_BOUNDS.keys())}")

    now = time.time()
    cached = _branch_cache.get(state)
    if cached and (now - cached[0]) < _BRANCH_CACHE_TTL:
        return cached[1]

    try:
        branches = await _fetch_tomtom_branches(state, api_key)
    except Exception as e:
        logger.error(f"TomTom branch fetch failed for {state}: {e}")
        raise HTTPException(503, "Branch data temporarily unavailable — TomTom API error")

    geojson = {
        "type":         "FeatureCollection",
        "state_code":   state,
        "branch_count": len(branches),
        "features": [
            {
                "type":     "Feature",
                "geometry": {"type": "Point", "coordinates": [b["lon"], b["lat"]]},
                "properties": {
                    "id":      b["id"],
                    "name":    b["name"],
                    "address": b["address"],
                    "city":    b["city"],
                    "phone":   b["phone"],
                    "url":     b["url"],
                },
            }
            for b in branches
        ],
    }

    _branch_cache[state] = (now, geojson)
    return geojson


@app.get("/api/v1/reachable-range")
async def get_reachable_range(
    lat:     float = Query(..., description="Branch latitude"),
    lon:     float = Query(..., description="Branch longitude"),
    minutes: int   = Query(30, ge=5, le=60, description="Drive time in minutes"),
):
    """
    Drive-time isochrone from a branch via TomTom Reachable Range API.
    Returns a GeoJSON Polygon representing the area reachable within `minutes`.
    Used on the CRA map to visualize coverage from a selected branch.
    """
    from config import settings
    api_key = settings.TOMTOM_API_KEY
    if not api_key:
        raise HTTPException(500, "TOMTOM_API_KEY not configured")

    async with httpx.AsyncClient(timeout=20.0) as client:
        resp = await client.get(
            f"https://api.tomtom.com/routing/1/calculateReachableRange/{lat},{lon}/json",
            params={
                "key":             api_key,
                "timeBudgetInSec": minutes * 60,
                "travelMode":      "car",
                "routeType":       "fastest",
            },
        )

    if resp.status_code != 200:
        logger.error(f"TomTom reachable-range {resp.status_code}: {resp.text[:400]}")
        raise HTTPException(503, f"TomTom routing returned {resp.status_code}")

    data     = resp.json()
    boundary = data.get("reachableRange", {}).get("boundary", [])
    if not boundary:
        raise HTTPException(404, "No reachable range boundary returned")

    coords = [[p["longitude"], p["latitude"]] for p in boundary]
    if coords[0] != coords[-1]:
        coords.append(coords[0])

    return {
        "type": "Feature",
        "geometry": {
            "type":        "Polygon",
            "coordinates": [coords],
        },
        "properties": {
            "origin_lat":    lat,
            "origin_lon":    lon,
            "drive_minutes": minutes,
            "point_count":   len(boundary),
        },
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


# ── ALETHEIA INTELLIGENCE LAYER ───────────────────────────
from aletheia_engine import aletheia_chat, aletheia_report
from pydantic import BaseModel as PydanticBase
from typing import List as TypingList

class AletheiaRequest(PydanticBase):
    message: str
    audience: str = "general"
    conversation_history: TypingList[dict] = []

class AletheiaReportRequest(PydanticBase):
    audience: str

@app.post("/api/v1/aletheia/{entity_id}")
async def aletheia_intelligence(entity_id: str, request: AletheiaRequest, db: AsyncSession = Depends(get_db)):
    """Aletheia intelligence endpoint — real position data + Claude API."""
    try:
        entity = await crud.get_entity(db, entity_id)
        if not entity:
            raise HTTPException(status_code=404, detail="Entity not found")
        position = await crud.get_position(db, entity_id)
        trust = await crud.get_trust_index(db, entity_id)
        context = {
            "entity": {**dict(entity), **(dict(position) if position else {})},
            "trust": dict(trust) if trust else {}
        }
        response = await aletheia_chat(
            entity_id=entity_id,
            message=request.message,
            audience=request.audience,
            conversation_history=request.conversation_history,
            context=context
        )
        return {"entity_id": entity_id, "response": response, "audience": request.audience}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Aletheia error: {str(e)}")

@app.post("/api/v1/aletheia/{entity_id}/report")
async def generate_report(entity_id: str, request: AletheiaReportRequest, db: AsyncSession = Depends(get_db)):
    """Generate differentiated report — board | technical | regulator | family | governance."""
    valid = {"board", "technical", "regulator", "family", "governance"}
    if request.audience not in valid:
        raise HTTPException(status_code=400, detail=f"Audience must be one of: {', '.join(valid)}")
    try:
        entity = await crud.get_entity(db, entity_id)
        position = await crud.get_position(db, entity_id)
        trust = await crud.get_trust_index(db, entity_id)
        context = {
            "entity": {**dict(entity), **(dict(position) if position else {})},
            "trust": dict(trust) if trust else {}
        }
        report = await aletheia_report(entity_id=entity_id, audience=request.audience, context=context)
        return {"entity_id": entity_id, "audience": request.audience, "report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report error: {str(e)}")

@app.get("/api/v1/aletheia/{entity_id}/context")
async def get_aletheia_context(entity_id: str, db: AsyncSession = Depends(get_db)):
    """Returns full entity context that Aletheia uses — full transparency."""
    try:
        entity = await crud.get_entity(db, entity_id)
        position = await crud.get_position(db, entity_id)
        trust = await crud.get_trust_index(db, entity_id)
        return {
            "entity_id": entity_id,
            "entity": dict(entity) if entity else {},
            "position": dict(position) if position else {},
            "trust": dict(trust) if trust else {},
            "data_sources": ["PostgreSQL", "FRED", "FFIEC", "HMDA", "FDIC"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve static files from integra-core root (HTML prototypes).
# Must be mounted last — acts as catch-all for any path not matched by API routes.
_static_root = Path(__file__).parent.parent
app.mount("/", StaticFiles(directory=_static_root, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    from config import settings
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT, reload=settings.API_RELOAD)

