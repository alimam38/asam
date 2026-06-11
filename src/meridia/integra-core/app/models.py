"""
Integra Core — Pydantic Models
All data structures for WayPoint financial intelligence platform.
"""

from __future__ import annotations
from datetime import date, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


# ── Enums ────────────────────────────────────────────────────

class EntityType(str, Enum):
    CHURCH = "church"
    FOUNDATION = "foundation"
    FUND = "fund"
    SCHOLARSHIP = "scholarship"
    DISCRETIONARY = "discretionary"
    PROGRAM = "program"

class EntityStatus(str, Enum):
    ACTIVE = "active"
    RESTRICTED = "restricted"
    PENDING_REVIEW = "pending_review"
    INACTIVE = "inactive"

class SignalSeverity(str, Enum):
    CRITICAL = "critical"
    WARNING = "warning"
    INFO = "info"
    SUCCESS = "success"

class SignalCategory(str, Enum):
    GOVERNANCE = "governance"
    FINANCIAL = "financial"
    COMPLIANCE = "compliance"
    OPERATIONAL = "operational"

class GovernanceAlertStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    DENIED = "denied"
    ESCALATED = "escalated"

class ReportAudience(str, Enum):
    BOARD = "board"
    TECHNICAL = "technical"
    REGULATOR = "regulator"
    FAMILY = "family"


# ── Financial Position ───────────────────────────────────────

class PositionLineItem(BaseModel):
    label: str
    current: float
    prior: float
    change_pct: float
    category: str  # assets, liabilities, equity, revenue, expenses

class FinancialPosition(BaseModel):
    institution_name: str
    as_of_date: date
    fiscal_year: str
    line_items: list[PositionLineItem]
    total_assets: float
    total_liabilities: float
    net_assets: float
    total_revenue: float
    total_expenses: float
    net_income: float
    cash_position: float
    months_cash_runway: float


# ── Trust Index ──────────────────────────────────────────────

class TrustDimension(BaseModel):
    name: str
    score: float = Field(ge=0, le=100)
    weight: float
    factors: list[str]
    trend: str  # "improving", "stable", "declining"

class TrustIndex(BaseModel):
    institution_name: str
    overall_score: float = Field(ge=0, le=100)
    grade: str  # A through F
    dimensions: list[TrustDimension]
    calculated_at: datetime
    narrative: str


# ── Entities ─────────────────────────────────────────────────

class Entity(BaseModel):
    id: str
    name: str
    type: EntityType
    status: EntityStatus
    balance: float
    restricted: bool
    description: str
    created_date: date
    last_activity: date
    governance_notes: Optional[str] = None

class EntityDetail(Entity):
    transactions_ytd: int
    inflows_ytd: float
    outflows_ytd: float
    monthly_activity: list[dict]  # [{month, inflow, outflow}]
    compliance_status: str
    next_review_date: Optional[date] = None
    related_entities: list[str] = []


# ── Signals ──────────────────────────────────────────────────

class Signal(BaseModel):
    id: str
    title: str
    description: str
    severity: SignalSeverity
    category: SignalCategory
    timestamp: datetime
    source: str
    action_required: bool
    acknowledged: bool = False


# ── Governance ───────────────────────────────────────────────

class GovernanceAlert(BaseModel):
    id: str
    title: str
    description: str
    alert_type: str  # "approval", "review", "escalation"
    status: GovernanceAlertStatus
    requested_by: str
    requested_at: datetime
    amount: Optional[float] = None
    entity_id: Optional[str] = None
    requires_quorum: bool = False
    approvals_needed: int = 1
    approvals_received: int = 0

class GovernanceApprovalRequest(BaseModel):
    alert_id: str
    decision: str = Field(pattern="^(approve|deny|escalate)$")
    approved_by: str
    notes: Optional[str] = None

class GovernanceApprovalResponse(BaseModel):
    alert_id: str
    new_status: GovernanceAlertStatus
    message: str


# ── Scenario Engine ──────────────────────────────────────────

class ScenarioRequest(BaseModel):
    name: Optional[str] = None
    revenue_change_pct: float = 0.0
    expense_change_pct: float = 0.0
    grant_amount: float = 0.0
    new_program_cost: float = 0.0
    enrollment_change_pct: float = 0.0

class ScenarioProjection(BaseModel):
    scenario_name: str
    projected_revenue: float
    projected_expenses: float
    projected_net_income: float
    projected_cash_position: float
    projected_months_runway: float
    projected_trust_score: float
    risk_flags: list[str]
    opportunities: list[str]
    narrative: str


# ── Reports ──────────────────────────────────────────────────

class ReportSection(BaseModel):
    heading: str
    content: str
    data: Optional[dict] = None

class Report(BaseModel):
    title: str
    audience: ReportAudience
    institution_name: str
    generated_at: datetime
    period: str
    sections: list[ReportSection]
    summary: str
    metadata: dict = {}
