# crud.py — Database read operations
# All queries are async, typed, and return Pydantic-ready dicts

from datetime import datetime
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc
from models import (
    EntityORM, PositionORM, TrustScoreORM, RelationshipORM,
    CensusTractORM, FredSeriesORM
)
from loguru import logger

# ── CURRENT PERIOD ────────────────────────────────────────
def current_period() -> str:
    now = datetime.utcnow()
    quarter = (now.month - 1) // 3 + 1
    return f"{now.year}-Q{quarter}"

# ── ENTITIES ──────────────────────────────────────────────
async def get_entity(db: AsyncSession, entity_id: str) -> Optional[dict]:
    result = await db.execute(
        select(EntityORM).where(EntityORM.entity_id == entity_id)
    )
    entity = result.scalar_one_or_none()
    if not entity:
        return None
    return {
        "entity_id": str(entity.entity_id),
        "name": entity.name,
        "tier": entity.tier,
        "entity_type": entity.entity_type,
        "geography_state": entity.geography_state,
        "census_tract": entity.census_tract,
    }

async def get_entities_by_institution(db: AsyncSession, institution_id: str) -> List[dict]:
    """Get all clients related to an institution."""
    from models import RelationshipORM
    result = await db.execute(
        select(EntityORM)
        .join(RelationshipORM, RelationshipORM.client_id == EntityORM.entity_id)
        .where(RelationshipORM.institution_id == institution_id)
        .where(RelationshipORM.status == 'active')
    )
    entities = result.scalars().all()
    return [{"entity_id": str(e.entity_id), "name": e.name, "tier": e.tier} for e in entities]

# ── POSITIONS (FPS) ───────────────────────────────────────
async def get_position(db: AsyncSession, entity_id: str, period: Optional[str] = None) -> Optional[dict]:
    period = period or current_period()
    result = await db.execute(
        select(PositionORM)
        .where(and_(PositionORM.entity_id == entity_id, PositionORM.period == period))
    )
    pos = result.scalar_one_or_none()
    if not pos:
        # No data for the requested period — use the most recently calculated position
        fallback = await db.execute(
            select(PositionORM)
            .where(PositionORM.entity_id == entity_id)
            .order_by(desc(PositionORM.calculated_at))
            .limit(1)
        )
        pos = fallback.scalar_one_or_none()
    if not pos:
        return None
    return {
        "fps_score": float(pos.fps_score or 0),
        "net_position": float(pos.net_position or 0),
        "liquidity_coverage": float(pos.liquidity_coverage or 0),
        "dscr_score": float(pos.dscr_score or 0),
        "runway_score": float(pos.runway_score or 0),
        "distribution_align": float(pos.distribution_align or 0),
        "fps_direction": pos.fps_direction,
        "fps_narrative": pos.fps_narrative,
        "period": pos.period,
        "calculated_at": pos.calculated_at,
    }

async def get_position_history(db: AsyncSession, entity_id: str, periods: int = 4) -> List[dict]:
    result = await db.execute(
        select(PositionORM)
        .where(PositionORM.entity_id == entity_id)
        .order_by(desc(PositionORM.period))
        .limit(periods)
    )
    positions = result.scalars().all()
    return [{"period": p.period, "fps_score": float(p.fps_score or 0)} for p in positions]

# ── TRUST INDEX ───────────────────────────────────────────
async def get_trust_score(db: AsyncSession, entity_id: str, period: Optional[str] = None) -> Optional[dict]:
    period = period or current_period()
    result = await db.execute(
        select(TrustScoreORM)
        .where(and_(TrustScoreORM.entity_id == entity_id, TrustScoreORM.period == period))
    )
    trust = result.scalar_one_or_none()
    if not trust:
        fallback = await db.execute(
            select(TrustScoreORM)
            .where(TrustScoreORM.entity_id == entity_id)
            .order_by(desc(TrustScoreORM.calculated_at))
            .limit(1)
        )
        trust = fallback.scalar_one_or_none()
    if not trust:
        return None
    return {
        "trust_index": float(trust.trust_index or 0),
        "behavioral_consistency": float(trust.behavioral_consistency or 0),
        "governance_adherence": float(trust.governance_adherence or 0),
        "communication_reliability": float(trust.communication_reliability or 0),
        "commitment_fulfillment": float(trust.commitment_fulfillment or 0),
        "direction": trust.direction,
        "period": trust.period,
    }

# ── RELATIONSHIPS ─────────────────────────────────────────
async def get_relationships_by_institution(db: AsyncSession, institution_id: str) -> List[dict]:
    result = await db.execute(
        select(RelationshipORM, EntityORM)
        .join(EntityORM, EntityORM.entity_id == RelationshipORM.client_id)
        .where(RelationshipORM.institution_id == institution_id)
        .where(RelationshipORM.status == 'active')
        .order_by(RelationshipORM.risk_score)
    )
    rows = result.all()
    return [{
        "rel_id": str(r.RelationshipORM.rel_id),
        "client_id": str(r.RelationshipORM.client_id),
        "client_name": r.EntityORM.name,
        "client_tier": r.EntityORM.tier,
        "product_type": r.RelationshipORM.product_type,
        "exposure_amount": float(r.RelationshipORM.exposure_amount or 0),
        "risk_direction": r.RelationshipORM.risk_direction,
        "risk_score": float(r.RelationshipORM.risk_score or 0),
    } for r in rows]

async def get_portfolio_summary(db: AsyncSession, institution_id: str) -> dict:
    """Aggregate portfolio stats for Vantage console."""
    rels = await get_relationships_by_institution(db, institution_id)

    if not rels:
        return {"total_relationships": 0, "total_exposure": 0, "portfolio_health_score": 0}

    total = len(rels)
    total_exposure = sum(r["exposure_amount"] for r in rels)
    scores = [r["risk_score"] for r in rels]
    avg_health = sum(scores) / len(scores) if scores else 0

    distribution = {
        "sound": sum(1 for r in rels if r["risk_score"] >= 70),
        "developing": sum(1 for r in rels if 50 <= r["risk_score"] < 70),
        "watch": sum(1 for r in rels if 30 <= r["risk_score"] < 50),
        "at_risk": sum(1 for r in rels if r["risk_score"] < 30),
    }

    bilateral_flags = sum(1 for r in rels if r["risk_direction"] in ["toward_institution", "bilateral"])

    return {
        "institution_id": institution_id,
        "total_relationships": total,
        "total_exposure": total_exposure,
        "portfolio_health_score": round(avg_health, 1),
        "distribution": distribution,
        "cra_activity_mtd": 0,  # Populated from cra_activity table
        "bilateral_flags": bilateral_flags,
        "opportunity_pipeline": 0,  # Populated from opportunity calculation
        "period": current_period(),
    }

# ── CENSUS TRACTS ─────────────────────────────────────────
async def get_tracts_by_state(db: AsyncSession, state_code: str) -> List[dict]:
    result = await db.execute(
        select(CensusTractORM).where(CensusTractORM.state_code == state_code)
    )
    tracts = result.scalars().all()
    return [{
        "geoid": t.geoid,
        "state_code": t.state_code,
        "tract_name": t.tract_name,
        "msa_name": t.msa_name,
        "is_distressed": t.is_distressed,
        "is_underserved": t.is_underserved,
        "is_lmi": t.is_lmi,
        "ffiec_income_pct": float(t.ffiec_income_pct or 0),
        "median_hh_income": t.median_hh_income,
        "poverty_rate": float(t.poverty_rate or 0),
        "opportunity_score": float(t.opportunity_score or 0),
    } for t in tracts]

async def get_hmda_tract_activity(db: AsyncSession, state_code: str) -> List[dict]:
    """Per-tract HMDA loan activity with institution names from the institutions table."""
    from sqlalchemy import text
    result = await db.execute(
        text("""
            SELECT
                ct.geoid,
                ct.tract_name,
                ct.state_code,
                ct.is_lmi,
                ct.is_distressed,
                ct.is_underserved,
                ct.median_hh_income,
                ct.opportunity_score,
                COUNT(h.loan_id)                                                AS loan_count,
                COUNT(h.loan_id) = 0                                            AS zero_activity,
                (COUNT(h.loan_id) = 0 AND (ct.is_lmi OR ct.is_distressed))     AS priority_gap,
                COALESCE(
                    array_agg(DISTINCT i.legal_name)
                        FILTER (WHERE i.legal_name IS NOT NULL),
                    ARRAY[]::TEXT[]
                )                                                               AS active_institutions
            FROM census_tracts ct
            LEFT JOIN hmda_loans h   ON h.census_tract = ct.geoid
            LEFT JOIN institutions i ON i.lei = h.lei
            WHERE ct.state_code = :state_code
            GROUP BY ct.geoid, ct.tract_name, ct.state_code,
                     ct.is_lmi, ct.is_distressed, ct.is_underserved,
                     ct.median_hh_income, ct.opportunity_score
            ORDER BY loan_count ASC, ct.geoid
        """),
        {"state_code": state_code}
    )
    rows = result.fetchall()
    return [{
        "geoid":               r.geoid,
        "tract_name":          r.tract_name,
        "state_code":          r.state_code,
        "is_lmi":              r.is_lmi,
        "is_distressed":       r.is_distressed,
        "is_underserved":      r.is_underserved,
        "median_hh_income":    r.median_hh_income,
        "opportunity_score":   float(r.opportunity_score or 0),
        "loan_count":          r.loan_count,
        "zero_activity":       r.zero_activity,
        "priority_gap":        r.priority_gap,
        "active_institutions": list(r.active_institutions or []),
    } for r in rows]

async def get_coverage_gaps(db: AsyncSession, institution_id: str, state_code: str = "GA") -> List[dict]:
    """Tracts with zero HMDA loan activity. Priority gaps (LMI or distressed) sort first."""
    tracts = await get_hmda_tract_activity(db, state_code)
    gaps = [t for t in tracts if t["zero_activity"]]
    gaps.sort(key=lambda t: (not t["priority_gap"], -t["opportunity_score"]))
    return gaps[:20]

# ── FRED MACRO CONTEXT ────────────────────────────────────
async def get_macro_context(db: AsyncSession) -> dict:
    """Latest macro indicators for position narrative."""
    series_ids = ["FEDFUNDS", "MORTGAGE30US", "UNRATE", "CPIAUCSL"]
    context = {}
    for sid in series_ids:
        result = await db.execute(
            select(FredSeriesORM)
            .where(FredSeriesORM.series_id == sid)
            .order_by(desc(FredSeriesORM.observation_date))
            .limit(1)
        )
        row = result.scalar_one_or_none()
        if row:
            context[sid] = {
                "value": float(row.value),
                "date": row.observation_date.isoformat(),
                "series_name": row.series_name,
            }
    return context
