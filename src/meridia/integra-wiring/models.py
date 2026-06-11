# models.py — Pydantic response models + SQLAlchemy ORM
from __future__ import annotations
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Numeric, Boolean, Integer, Date, DateTime, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from database import Base
import uuid

# ══════════════════════════════════════════════════════════
# SQLAlchemy ORM Models
# ══════════════════════════════════════════════════════════

class EntityORM(Base):
    __tablename__ = "entities"
    entity_id       = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name            = Column(String(255), nullable=False)
    tier            = Column(String(20), nullable=False)
    entity_type     = Column(String(50), nullable=False)
    geography_state = Column(String(2))
    geography_msa   = Column(String(50))
    census_tract    = Column(String(20))
    created_at      = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at      = Column(DateTime(timezone=True), default=datetime.utcnow)

class PositionORM(Base):
    __tablename__ = "positions"
    position_id         = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id           = Column(PGUUID(as_uuid=True), ForeignKey("entities.entity_id"))
    period              = Column(String(10), nullable=False)
    fps_score           = Column(Numeric(5,2))
    net_position        = Column(Numeric(5,2))
    liquidity_coverage  = Column(Numeric(5,2))
    dscr_score          = Column(Numeric(5,2))
    runway_score        = Column(Numeric(5,2))
    distribution_align  = Column(Numeric(5,2))
    fps_direction       = Column(String(20))
    fps_narrative       = Column(Text)
    raw_data            = Column(JSON)
    calculated_at       = Column(DateTime(timezone=True), default=datetime.utcnow)

class TrustScoreORM(Base):
    __tablename__ = "trust_scores"
    trust_id                    = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id                   = Column(PGUUID(as_uuid=True), ForeignKey("entities.entity_id"))
    period                      = Column(String(10), nullable=False)
    trust_index                 = Column(Numeric(5,2))
    behavioral_consistency      = Column(Numeric(5,2))
    governance_adherence        = Column(Numeric(5,2))
    communication_reliability   = Column(Numeric(5,2))
    commitment_fulfillment      = Column(Numeric(5,2))
    direction                   = Column(String(20))
    calculated_at               = Column(DateTime(timezone=True), default=datetime.utcnow)

class RelationshipORM(Base):
    __tablename__ = "relationships"
    rel_id              = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    institution_id      = Column(PGUUID(as_uuid=True), ForeignKey("entities.entity_id"))
    client_id           = Column(PGUUID(as_uuid=True), ForeignKey("entities.entity_id"))
    product_type        = Column(String(50))
    exposure_amount     = Column(Numeric(15,2))
    risk_direction      = Column(String(20))
    risk_score          = Column(Numeric(5,2))
    status              = Column(String(20), default="active")
    opened_at           = Column(Date)
    updated_at          = Column(DateTime(timezone=True), default=datetime.utcnow)

class CensusTractORM(Base):
    __tablename__ = "census_tracts"
    geoid               = Column(String(20), primary_key=True)
    state_code          = Column(String(2))
    county_code         = Column(String(5))
    tract_name          = Column(String(100))
    msa_name            = Column(String(100))
    is_distressed       = Column(Boolean, default=False)
    is_underserved      = Column(Boolean, default=False)
    is_lmi              = Column(Boolean, default=False)
    ffiec_income_pct    = Column(Numeric(6,2))
    median_hh_income    = Column(Integer)
    poverty_rate        = Column(Numeric(5,2))
    population          = Column(Integer)
    pct_minority        = Column(Numeric(5,2))
    opportunity_score   = Column(Numeric(5,2))
    data_year           = Column(Integer)
    updated_at          = Column(DateTime(timezone=True), default=datetime.utcnow)

class FredSeriesORM(Base):
    __tablename__ = "fred_series"
    series_id           = Column(String(30), primary_key=True)
    observation_date    = Column(Date, primary_key=True)
    value               = Column(Numeric(15,6))
    series_name         = Column(String(255))
    frequency           = Column(String(20))
    units               = Column(String(100))
    updated_at          = Column(DateTime(timezone=True), default=datetime.utcnow)

# ══════════════════════════════════════════════════════════
# Pydantic Response Models
# ══════════════════════════════════════════════════════════

class FPSComponent(BaseModel):
    score: float
    weight: float
    weighted_contribution: float
    direction: str  # strong, developing, watch, critical

class FPSResponse(BaseModel):
    entity_id: str
    entity_name: str
    tier: str
    period: str
    fps_score: float
    fps_direction: str
    fps_narrative: str
    components: Dict[str, FPSComponent]
    calculated_at: datetime

    class Config:
        from_attributes = True

class TrustIndexResponse(BaseModel):
    entity_id: str
    entity_name: str
    trust_index: float
    direction: str
    behavioral_consistency: float
    governance_adherence: float
    communication_reliability: float
    commitment_fulfillment: float
    period: str

class EntityResponse(BaseModel):
    entity_id: str
    name: str
    tier: str
    entity_type: str
    geography_state: Optional[str]
    census_tract: Optional[str]
    fps_score: Optional[float] = None
    trust_index: Optional[float] = None
    risk_status: Optional[str] = None

class RelationshipResponse(BaseModel):
    rel_id: str
    institution_name: str
    client_name: str
    product_type: str
    exposure_amount: float
    risk_direction: str
    risk_score: float
    status: str

class PortfolioSummaryResponse(BaseModel):
    institution_id: str
    institution_name: str
    total_relationships: int
    total_exposure: float
    portfolio_health_score: float
    distribution: Dict[str, int]  # sound/developing/watch/at_risk counts
    cra_activity_mtd: float
    bilateral_flags: int
    opportunity_pipeline: float
    period: str

class CensusTractResponse(BaseModel):
    geoid: str
    state_code: str
    tract_name: Optional[str]
    msa_name: Optional[str]
    is_distressed: bool
    is_underserved: bool
    is_lmi: bool
    ffiec_income_pct: Optional[float]
    median_hh_income: Optional[int]
    poverty_rate: Optional[float]
    opportunity_score: Optional[float]

class CoverageGapResponse(BaseModel):
    geoid: str
    tract_name: Optional[str]
    state_code: str
    is_lmi: bool
    is_distressed: bool
    is_underserved: bool
    median_hh_income: Optional[int]
    opportunity_score: float
    loan_count: int
    zero_activity: bool
    priority_gap: bool
    active_institutions: List[str]

class HeatMapResponse(BaseModel):
    institution_id: str
    state_code: str
    total_tracts: int
    lmi_tracts: int
    distressed_tracts: int
    coverage_gaps: List[CoverageGapResponse]
    gap_count: int
    total_addressable_estimate: float
    cra_credit_opportunity: float

class ReportResponse(BaseModel):
    entity_id: str
    audience: str
    period: str
    generated_at: datetime
    sections: Dict[str, Any]

class SignalResponse(BaseModel):
    signal_id: str
    rel_id: str
    signal_type: str
    severity: str
    message: str
    resolved: bool
    created_at: datetime

class GovernanceAlertResponse(BaseModel):
    alert_id: str
    entity_id: str
    alert_type: str
    priority: str
    title: str
    detail: str
    action_required: bool
    created_at: datetime

class ScenarioRequest(BaseModel):
    entity_id: str
    adjustments: Dict[str, float]
    scenario_name: Optional[str] = "Unnamed Scenario"

class ScenarioResponse(BaseModel):
    entity_id: str
    scenario_name: str
    baseline_fps: float
    projected_fps: float
    fps_delta: float
    impact_narrative: str
    component_changes: Dict[str, float]
