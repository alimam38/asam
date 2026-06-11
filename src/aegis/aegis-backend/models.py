"""
Pydantic data models for the Aegis Financial Positioning System.

These models define the structure of all data flowing through the API,
ensuring type safety and validation at the API boundary.
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator


# ============================================================================
# ENUMS & CONSTANTS
# ============================================================================

class StatusLevel(str, Enum):
    """Health status levels for entities and metrics."""
    HEALTHY = "healthy"
    WATCH = "watch"
    ALERT = "alert"


class TrendDirection(str, Enum):
    """Trend direction for metrics."""
    UP = "up"
    DOWN = "down"
    NEUTRAL = "neutral"


class SignalPriority(str, Enum):
    """Priority levels for signal feed items."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class EntityType(str, Enum):
    """Types of financial entities."""
    DYNASTY_TRUST = "Dynasty Trust"
    FOUNDATION = "Foundation"
    HOLDING_COMPANY = "Holding Company"
    FAMILY_OFFICE = "Family Office"
    OPERATING_ENTITY = "Operating Entity"


# ============================================================================
# FINANCIAL POSITION MODELS
# ============================================================================

class PositionMetric(BaseModel):
    """Individual metric in the position grid."""
    label: str
    value: str
    change_text: str
    change_direction: str  # 'positive', 'negative', 'neutral'
    status: StatusLevel
    icon: Optional[str] = None


class PositionGridResponse(BaseModel):
    """Response model for /api/v1/position-grid endpoint."""
    liquidity: PositionMetric
    net_worth: PositionMetric
    obligations: PositionMetric
    resilience: PositionMetric
    timestamp: datetime = Field(default_factory=datetime.now)


# ============================================================================
# TRUST INDEX MODELS
# ============================================================================

class TrustDimension(BaseModel):
    """Individual dimension of the Trust Index."""
    label: str
    value: int = Field(ge=0, le=100)
    color: str  # CSS color variable name


class TrustIndexResponse(BaseModel):
    """Response model for /api/v1/trust-index endpoint."""
    overall_score: int = Field(ge=0, le=100)
    dimensions: List[TrustDimension]
    timestamp: datetime = Field(default_factory=datetime.now)
    trend_direction: TrendDirection
    trend_change: float


# ============================================================================
# ENTITY MODELS
# ============================================================================

class EntityMetric(BaseModel):
    """Individual metric within an entity card."""
    label: str
    value: str


class Entity(BaseModel):
    """Financial entity (trust, foundation, holding company, etc.)."""
    id: str
    type: EntityType
    name: str
    status: StatusLevel
    metrics: List[EntityMetric]
    description: Optional[str] = None


class EntitiesResponse(BaseModel):
    """Response model for /api/v1/entities endpoint."""
    entities: List[Entity]
    total_aum: str
    timestamp: datetime = Field(default_factory=datetime.now)


# ============================================================================
# GOVERNANCE MODELS
# ============================================================================

class GovernanceRecipient(BaseModel):
    """Recipient of a governance notification."""
    role: str
    status: str  # 'notified', 'approved', 'pending'
    timestamp: Optional[datetime] = None


class GovernanceAlert(BaseModel):
    """Governance alert requiring multi-party approval."""
    id: str
    title: str
    subtitle: str
    message: str
    priority: SignalPriority
    recipients: List[GovernanceRecipient]
    created_at: datetime
    expires_at: Optional[datetime] = None
    requires_approval: bool = True
    approved: bool = False


class GovernanceAlertsResponse(BaseModel):
    """Response model for /api/v1/governance-alerts endpoint."""
    alerts: List[GovernanceAlert]
    total_active: int
    total_pending_approval: int


# ============================================================================
# SIGNAL FEED MODELS
# ============================================================================

class SignalItem(BaseModel):
    """Individual signal in the feed."""
    id: str
    priority: SignalPriority
    text: str
    metadata: str  # Time + entity context
    created_at: datetime
    entity_id: Optional[str] = None


class SignalFeedResponse(BaseModel):
    """Response model for /api/v1/signal-feed endpoint."""
    signals: List[SignalItem]
    total_count: int
    unread_count: int


# ============================================================================
# METRICS DASHBOARD MODELS
# ============================================================================

class ChartDataPoint(BaseModel):
    """Single data point in a chart."""
    value: float
    label: Optional[str] = None
    timestamp: Optional[datetime] = None


class MetricCard(BaseModel):
    """Individual metric card on the dashboard."""
    id: str
    label: str
    value: str
    icon_class: str
    icon_color: str  # 'gold', 'emerald', 'blue', 'purple'
    trend_direction: TrendDirection
    trend_text: str
    chart_data: List[ChartDataPoint]


class MetricsDashboardResponse(BaseModel):
    """Response model for /api/v1/metrics-dashboard endpoint."""
    metrics: List[MetricCard]
    timestamp: datetime = Field(default_factory=datetime.now)


# ============================================================================
# SCENARIO ENGINE MODELS
# ============================================================================

class ScenarioInput(BaseModel):
    """Input parameters for scenario modeling."""
    distribution_rate_change: float = Field(
        ge=-50, le=50, 
        description="Percentage change in distribution rate (-50% to +50%)"
    )
    market_shock: float = Field(
        ge=-40, le=20,
        description="Market movement percentage (-40% to +20%)"
    )
    foundation_corpus_addition: int = Field(
        ge=0, le=2000,
        description="Additional foundation corpus in thousands (0 to 2000K)"
    )


class ScenarioImpact(BaseModel):
    """Individual impact metric from scenario."""
    label: str
    baseline: str
    projected: str
    impact_type: str  # 'positive', 'negative', 'neutral'


class ScenarioResponse(BaseModel):
    """Response model for /api/v1/scenario-engine endpoint."""
    inputs: ScenarioInput
    impacts: List[ScenarioImpact]
    trust_index_impact: ScenarioImpact
    resilience_impact: ScenarioImpact
    foundation_status: ScenarioImpact
    timestamp: datetime = Field(default_factory=datetime.now)
    scenario_id: str


# ============================================================================
# FLOW DIAGRAM MODELS
# ============================================================================

class FlowNode(BaseModel):
    """Node in the capital flow diagram."""
    id: str
    type: str
    name: str
    value: str
    icon: str
    status: Optional[StatusLevel] = None


class FlowConnection(BaseModel):
    """Connection between flow nodes."""
    from_node: str
    to_node: str
    label: Optional[str] = None
    value: Optional[str] = None


class FlowDiagramResponse(BaseModel):
    """Response model for /api/v1/flow-diagram endpoint."""
    nodes: List[FlowNode]
    connections: List[FlowConnection]
    total_inflows: str
    total_outflows: str
    net_flow: str


# ============================================================================
# CHAT/ALETHEIA MODELS
# ============================================================================

class ChatMessage(BaseModel):
    """Message in the Aletheia chat interface."""
    id: str
    content: str
    is_user: bool
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Optional[Dict[str, Any]] = None


class ChatRequest(BaseModel):
    """Request to send a message to Aletheia."""
    message: str
    context: Optional[Dict[str, Any]] = None


class ChatResponse(BaseModel):
    """Response from Aletheia chat endpoint."""
    message: ChatMessage
    suggestions: Optional[List[str]] = None


# ============================================================================
# INSTITUTIONAL SANDBOX MODELS
# ============================================================================

class SandboxMetric(BaseModel):
    """Metric in the institutional sandbox."""
    label: str
    value: str


class DataFeedStatus(BaseModel):
    """Status of a data feed connection."""
    name: str
    status: str  # 'connected', 'pending', 'error'
    last_sync: Optional[datetime] = None


class TimelineStep(BaseModel):
    """Step in the pilot timeline."""
    label: str
    status: str  # 'complete', 'active', 'pending'
    order: int


class InstitutionalSandboxResponse(BaseModel):
    """Response model for /api/v1/institutional-sandbox endpoint."""
    partner_name: str
    pilot_metrics: List[SandboxMetric]
    data_feeds: List[DataFeedStatus]
    timeline: List[TimelineStep]
    governance_compliance: List[Dict[str, str]]


# ============================================================================
# RENAISSANCE PATHWAY MODELS
# ============================================================================

class PathwayItem(BaseModel):
    """Item in the Renaissance pathway checklist."""
    id: str
    text: str
    completed: bool
    order: int


class RenaissanceMetric(BaseModel):
    """Metric for Renaissance journey."""
    label: str
    current_value: str
    starting_value: str
    trend: TrendDirection


class RenaissanceResponse(BaseModel):
    """Response model for /api/v1/renaissance endpoint."""
    current_step: int
    total_steps: int
    progress_percentage: float
    pathway_items: List[PathwayItem]
    metrics: List[RenaissanceMetric]


# ============================================================================
# HEALTH CHECK
# ============================================================================

class HealthCheckResponse(BaseModel):
    """Response model for /api/v1/health endpoint."""
    status: str
    version: str
    timestamp: datetime = Field(default_factory=datetime.now)
    services: Dict[str, str]
