"""
Mock data generation for the Aegis Financial Positioning System.

This module generates realistic, varied mock data for demonstration purposes.
In production, this would be replaced with actual database queries and
live data integrations.
"""

import random
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any
from faker import Faker

from models import (
    StatusLevel, TrendDirection, SignalPriority, EntityType,
    PositionMetric, PositionGridResponse,
    TrustDimension, TrustIndexResponse,
    Entity, EntityMetric, EntitiesResponse,
    GovernanceRecipient, GovernanceAlert, GovernanceAlertsResponse,
    SignalItem, SignalFeedResponse,
    ChartDataPoint, MetricCard, MetricsDashboardResponse,
    ScenarioInput, ScenarioImpact, ScenarioResponse,
    FlowNode, FlowConnection, FlowDiagramResponse,
    ChatMessage,
    SandboxMetric, DataFeedStatus, TimelineStep, InstitutionalSandboxResponse,
    PathwayItem, RenaissanceMetric, RenaissanceResponse,
    HealthCheckResponse
)

fake = Faker()
Faker.seed(42)  # For consistent demo data


# ============================================================================
# POSITION GRID GENERATION
# ============================================================================

def generate_position_grid() -> PositionGridResponse:
    """Generate the financial position grid data."""
    
    liquidity_value = random.randint(18, 30) / 10  # 1.8M to 3.0M
    net_worth_value = random.randint(160, 220) / 10  # 16M to 22M
    obligations_value = random.randint(280, 420)  # 280K to 420K
    resilience_value = random.randint(88, 96)  # 88 to 96
    
    return PositionGridResponse(
        liquidity=PositionMetric(
            label="Liquidity",
            value=f"${liquidity_value:.1f}M",
            change_text=f"{random.randint(8, 15)}% from Q3",
            change_direction="positive",
            status=StatusLevel.HEALTHY
        ),
        net_worth=PositionMetric(
            label="Net Worth",
            value=f"${net_worth_value:.1f}M",
            change_text=f"{random.randint(3, 6)/10:.1f}% YTD",
            change_direction="positive",
            status=StatusLevel.HEALTHY
        ),
        obligations=PositionMetric(
            label="Obligations",
            value=f"${obligations_value}K",
            change_text="Next 90 days",
            change_direction="negative",
            status=StatusLevel.WATCH if obligations_value > 350 else StatusLevel.HEALTHY
        ),
        resilience=PositionMetric(
            label="Resilience",
            value=str(resilience_value),
            change_text="Strong buffer",
            change_direction="positive",
            status=StatusLevel.HEALTHY
        )
    )


# ============================================================================
# TRUST INDEX GENERATION
# ============================================================================

def generate_trust_index() -> TrustIndexResponse:
    """Generate the Trust Index data."""
    
    financial_score = random.randint(85, 95)
    stewardship_score = random.randint(75, 85)
    mission_score = random.randint(82, 92)
    governance_score = random.randint(88, 95)
    
    overall_score = int((financial_score + stewardship_score + mission_score + governance_score) / 4)
    
    dimensions = [
        TrustDimension(
            label="Financial",
            value=financial_score,
            color="var(--accent-emerald)"
        ),
        TrustDimension(
            label="Stewardship",
            value=stewardship_score,
            color="var(--accent-gold)"
        ),
        TrustDimension(
            label="Mission",
            value=mission_score,
            color="var(--accent-emerald)"
        ),
        TrustDimension(
            label="Governance",
            value=governance_score,
            color="var(--accent-emerald)"
        )
    ]
    
    return TrustIndexResponse(
        overall_score=overall_score,
        dimensions=dimensions,
        trend_direction=TrendDirection.UP,
        trend_change=random.randint(25, 45) / 10
    )


# ============================================================================
# ENTITIES GENERATION
# ============================================================================

def generate_entities() -> EntitiesResponse:
    """Generate financial entities data."""
    
    entities = [
        Entity(
            id="entity-dynasty-trust",
            type=EntityType.DYNASTY_TRUST,
            name="Crown Legacy Trust",
            status=StatusLevel.HEALTHY,
            metrics=[
                EntityMetric(label="Corpus", value=f"${random.randint(110, 135) / 10:.1f}M"),
                EntityMetric(label="Payout", value=f"{random.randint(28, 36) / 10:.1f}%")
            ],
            description="Generational wealth preservation vehicle"
        ),
        Entity(
            id="entity-foundation",
            type=EntityType.FOUNDATION,
            name="Family Impact Foundation",
            status=StatusLevel.WATCH,
            metrics=[
                EntityMetric(label="Assets", value=f"${random.randint(35, 42) / 10:.1f}M"),
                EntityMetric(label="Grant Rate", value=f"{random.randint(68, 76) / 10:.1f}%")
            ],
            description="Mission-driven philanthropic entity"
        ),
        Entity(
            id="entity-holdco",
            type=EntityType.HOLDING_COMPANY,
            name="Crown Holdings LLC",
            status=StatusLevel.HEALTHY,
            metrics=[
                EntityMetric(label="Equity", value=f"${random.randint(75, 90) / 10:.1f}M"),
                EntityMetric(label="Leverage", value=f"{random.randint(3, 5) / 10:.1f}x")
            ],
            description="Operating capital management entity"
        )
    ]
    
    total_aum = sum([
        float(e.metrics[0].value.replace('$', '').replace('M', '')) 
        for e in entities
    ])
    
    return EntitiesResponse(
        entities=entities,
        total_aum=f"${total_aum:.1f}M"
    )


# ============================================================================
# GOVERNANCE ALERTS GENERATION
# ============================================================================

def generate_governance_alerts() -> GovernanceAlertsResponse:
    """Generate governance alerts."""
    
    alert = GovernanceAlert(
        id=str(uuid.uuid4()),
        title="Governance Review Required",
        subtitle="Insight locked pending multi-party approval",
        message="Aletheia has detected a sensitive pattern in the Foundation's grant commitments that exceeds projected inflows by 18 months. This insight requires approval before being surfaced to beneficiaries.",
        priority=SignalPriority.HIGH,
        recipients=[
            GovernanceRecipient(
                role="CEO",
                status="notified",
                timestamp=datetime.now() - timedelta(hours=2)
            ),
            GovernanceRecipient(
                role="Trustee",
                status="notified",
                timestamp=datetime.now() - timedelta(hours=2)
            ),
            GovernanceRecipient(
                role="Architect",
                status="notified",
                timestamp=datetime.now() - timedelta(hours=2)
            )
        ],
        created_at=datetime.now() - timedelta(hours=2),
        requires_approval=True,
        approved=False
    )
    
    return GovernanceAlertsResponse(
        alerts=[alert],
        total_active=1,
        total_pending_approval=1
    )


# ============================================================================
# SIGNAL FEED GENERATION
# ============================================================================

def generate_signal_feed() -> SignalFeedResponse:
    """Generate signal feed items."""
    
    signals = [
        SignalItem(
            id=str(uuid.uuid4()),
            priority=SignalPriority.HIGH,
            text="Foundation grant rate exceeds sustainable threshold (7.1% vs 5% target)",
            metadata="High Priority • 2 hours ago • Family Impact Foundation",
            created_at=datetime.now() - timedelta(hours=2),
            entity_id="entity-foundation"
        ),
        SignalItem(
            id=str(uuid.uuid4()),
            priority=SignalPriority.MEDIUM,
            text="Quarterly liquidity ratio improved to 7.2x coverage — exceeds policy minimum",
            metadata="Medium Priority • 1 day ago • Crown Holdings LLC",
            created_at=datetime.now() - timedelta(days=1),
            entity_id="entity-holdco"
        ),
        SignalItem(
            id=str(uuid.uuid4()),
            priority=SignalPriority.LOW,
            text="Dynasty Trust annual review completed — all governance requirements met",
            metadata="Low Priority • 3 days ago • Crown Legacy Trust",
            created_at=datetime.now() - timedelta(days=3),
            entity_id="entity-dynasty-trust"
        ),
        SignalItem(
            id=str(uuid.uuid4()),
            priority=SignalPriority.LOW,
            text="Net worth milestone reached: $18M threshold crossed for first time",
            metadata="Low Priority • 1 week ago • Portfolio-wide",
            created_at=datetime.now() - timedelta(weeks=1)
        )
    ]
    
    return SignalFeedResponse(
        signals=signals,
        total_count=len(signals),
        unread_count=random.randint(1, 3)
    )


# ============================================================================
# METRICS DASHBOARD GENERATION
# ============================================================================

def generate_chart_data(num_points: int = 9, trend: str = 'up') -> List[ChartDataPoint]:
    """Generate chart data points with a trend."""
    points = []
    base = random.randint(40, 60)
    
    for i in range(num_points):
        if trend == 'up':
            value = base + (i * random.randint(3, 8))
        elif trend == 'down':
            value = base - (i * random.randint(2, 5))
        else:
            value = base + random.randint(-5, 5)
        
        points.append(ChartDataPoint(value=min(100, max(0, value))))
    
    return points


def generate_metrics_dashboard() -> MetricsDashboardResponse:
    """Generate metrics dashboard data."""
    
    metrics = [
        MetricCard(
            id="metric-trust-index",
            label="Trust Index Score",
            value=str(random.randint(84, 90)),
            icon_class="fas fa-shield-halved",
            icon_color="gold",
            trend_direction=TrendDirection.UP,
            trend_text=f"+{random.randint(28, 38) / 10:.1f}%",
            chart_data=generate_chart_data(trend='up')
        ),
        MetricCard(
            id="metric-net-worth",
            label="Total Net Worth",
            value=f"${random.randint(170, 200) / 10:.1f}M",
            icon_class="fas fa-chart-line",
            icon_color="emerald",
            trend_direction=TrendDirection.UP,
            trend_text=f"+${random.randint(10, 15) / 10:.1f}M",
            chart_data=generate_chart_data(trend='up')
        ),
        MetricCard(
            id="metric-liquidity",
            label="Liquid Reserves",
            value=f"${random.randint(22, 28) / 10:.1f}M",
            icon_class="fas fa-droplet",
            icon_color="blue",
            trend_direction=TrendDirection.UP,
            trend_text=f"+{random.randint(10, 15)}%",
            chart_data=generate_chart_data(trend='up')
        ),
        MetricCard(
            id="metric-foundation-rate",
            label="Foundation Grant Rate",
            value=f"{random.randint(68, 74) / 10:.1f}%",
            icon_class="fas fa-hand-holding-heart",
            icon_color="purple",
            trend_direction=TrendDirection.UP,
            trend_text=f"+{random.randint(15, 22) / 10:.1f}%",
            chart_data=generate_chart_data(trend='up')
        )
    ]
    
    return MetricsDashboardResponse(metrics=metrics)


# ============================================================================
# SCENARIO ENGINE CALCULATION
# ============================================================================

def calculate_scenario(inputs: ScenarioInput) -> ScenarioResponse:
    """Calculate scenario impacts based on inputs."""
    
    # Baseline values
    baseline_trust = 87
    baseline_resilience = 94
    baseline_foundation_status = "Watch"
    
    # Calculate impacts
    trust_impact = baseline_trust
    resilience_impact = baseline_resilience
    
    # Distribution rate impact
    if inputs.distribution_rate_change > 0:
        trust_impact -= int(inputs.distribution_rate_change * 0.3)
        resilience_impact -= int(inputs.distribution_rate_change * 0.2)
    else:
        trust_impact += int(abs(inputs.distribution_rate_change) * 0.1)
        resilience_impact += int(abs(inputs.distribution_rate_change) * 0.15)
    
    # Market shock impact
    if inputs.market_shock < 0:
        trust_impact += int(inputs.market_shock * 0.4)
        resilience_impact += int(inputs.market_shock * 0.5)
    else:
        trust_impact += int(inputs.market_shock * 0.1)
        resilience_impact += int(inputs.market_shock * 0.1)
    
    # Foundation corpus impact
    if inputs.foundation_corpus_addition > 0:
        trust_impact += int(inputs.foundation_corpus_addition / 200)
    
    # Constrain to 0-100
    trust_impact = max(0, min(100, trust_impact))
    resilience_impact = max(0, min(100, resilience_impact))
    
    # Foundation status
    foundation_status = "Watch"
    if inputs.foundation_corpus_addition >= 500 or inputs.distribution_rate_change <= -20:
        foundation_status = "Healthy"
    elif inputs.distribution_rate_change >= 30 or inputs.market_shock <= -30:
        foundation_status = "Alert"
    
    # Determine impact types
    def get_impact_type(baseline: int, projected: int) -> str:
        if projected > baseline:
            return "positive"
        elif projected < baseline:
            return "negative"
        return "neutral"
    
    trust_impact_obj = ScenarioImpact(
        label="Trust Index",
        baseline=str(baseline_trust),
        projected=str(trust_impact),
        impact_type=get_impact_type(baseline_trust, trust_impact)
    )
    
    resilience_impact_obj = ScenarioImpact(
        label="Resilience",
        baseline=str(baseline_resilience),
        projected=str(resilience_impact),
        impact_type=get_impact_type(baseline_resilience, resilience_impact)
    )
    
    foundation_impact_obj = ScenarioImpact(
        label="Foundation",
        baseline=baseline_foundation_status,
        projected=foundation_status,
        impact_type=(
            "positive" if foundation_status == "Healthy" 
            else "negative" if foundation_status == "Alert" 
            else "neutral"
        )
    )
    
    return ScenarioResponse(
        inputs=inputs,
        impacts=[trust_impact_obj, resilience_impact_obj, foundation_impact_obj],
        trust_index_impact=trust_impact_obj,
        resilience_impact=resilience_impact_obj,
        foundation_status=foundation_impact_obj,
        scenario_id=str(uuid.uuid4())
    )


# ============================================================================
# FLOW DIAGRAM GENERATION
# ============================================================================

def generate_flow_diagram() -> FlowDiagramResponse:
    """Generate capital flow diagram data."""
    
    nodes = [
        FlowNode(
            id="node-holdings",
            type="primary",
            name="Crown Holdings",
            value=f"${random.randint(75, 90) / 10:.1f}M",
            icon="fas fa-building-columns",
            status=StatusLevel.HEALTHY
        ),
        FlowNode(
            id="node-trust",
            type="trust",
            name="Legacy Trust",
            value=f"${random.randint(110, 135) / 10:.1f}M",
            icon="fas fa-scroll"
        ),
        FlowNode(
            id="node-beneficiaries",
            type="beneficiary",
            name="Beneficiaries",
            value="4 Active",
            icon="fas fa-users"
        ),
        FlowNode(
            id="node-foundation",
            type="foundation",
            name="Foundation",
            value=f"${random.randint(35, 42) / 10:.1f}M",
            icon="fas fa-hand-holding-heart",
            status=StatusLevel.WATCH
        ),
        FlowNode(
            id="node-grants",
            type="grants",
            name="Grants",
            value=f"${random.randint(250, 290)}K/yr",
            icon="fas fa-seedling"
        )
    ]
    
    connections = [
        FlowConnection(from_node="node-holdings", to_node="node-trust"),
        FlowConnection(from_node="node-trust", to_node="node-beneficiaries"),
        FlowConnection(from_node="node-holdings", to_node="node-foundation"),
        FlowConnection(from_node="node-foundation", to_node="node-grants")
    ]
    
    return FlowDiagramResponse(
        nodes=nodes,
        connections=connections,
        total_inflows=f"${random.randint(11, 14) / 10:.1f}M",
        total_outflows=f"${random.randint(65, 75)}K",
        net_flow=f"+${random.randint(48, 62)}K"
    )


# ============================================================================
# INSTITUTIONAL SANDBOX GENERATION
# ============================================================================

def generate_institutional_sandbox() -> InstitutionalSandboxResponse:
    """Generate institutional sandbox data."""
    
    return InstitutionalSandboxResponse(
        partner_name="JPMC Partnership Sandbox",
        pilot_metrics=[
            SandboxMetric(label="Pilot Households", value=str(random.randint(240, 255))),
            SandboxMetric(label="AUM in Sandbox", value=f"${random.randint(40, 48) / 10:.1f}M"),
            SandboxMetric(label="API Uptime", value=f"{random.randint(938, 948) / 10:.1f}%"),
            SandboxMetric(label="Avg Response Time", value=f"{random.randint(10, 15)}ms")
        ],
        data_feeds=[
            DataFeedStatus(name="Account Aggregation", status="connected", last_sync=datetime.now() - timedelta(minutes=5)),
            DataFeedStatus(name="Transaction Stream", status="connected", last_sync=datetime.now() - timedelta(minutes=2)),
            DataFeedStatus(name="Market Data", status="connected", last_sync=datetime.now() - timedelta(seconds=30)),
            DataFeedStatus(name="Credit Bureau", status="pending", last_sync=None)
        ],
        timeline=[
            TimelineStep(label="Discovery", status="complete", order=1),
            TimelineStep(label="Integration", status="complete", order=2),
            TimelineStep(label="Pilot", status="active", order=3),
            TimelineStep(label="Validation", status="pending", order=4),
            TimelineStep(label="Production", status="pending", order=5)
        ],
        governance_compliance=[
            {"label": "Data Residency", "status": "Compliant"},
            {"label": "Encryption (AES-256)", "status": "Compliant"},
            {"label": "SOC 2 Type II", "status": "Certified"},
            {"label": "PCI DSS", "status": "Certified"}
        ]
    )


# ============================================================================
# RENAISSANCE PATHWAY GENERATION
# ============================================================================

def generate_renaissance_pathway() -> RenaissanceResponse:
    """Generate Renaissance pathway data."""
    
    pathway_items = [
        PathwayItem(id="item-1", text="Open secured savings account", completed=True, order=1),
        PathwayItem(id="item-2", text="Set up direct deposit", completed=True, order=2),
        PathwayItem(id="item-3", text="Complete financial literacy module 1", completed=True, order=3),
        PathwayItem(id="item-4", text="Maintain positive balance for 30 days", completed=False, order=4),
        PathwayItem(id="item-5", text="Apply for credit-builder loan", completed=False, order=5),
        PathwayItem(id="item-6", text="Complete financial literacy module 2", completed=False, order=6)
    ]
    
    completed_count = sum(1 for item in pathway_items if item.completed)
    progress = (completed_count / len(pathway_items)) * 100
    
    metrics = [
        RenaissanceMetric(
            label="Credit Score",
            current_value="612",
            starting_value="565",
            trend=TrendDirection.UP
        ),
        RenaissanceMetric(
            label="Emergency Fund Built",
            current_value="$1,240",
            starting_value="$0",
            trend=TrendDirection.UP
        )
    ]
    
    return RenaissanceResponse(
        current_step=3,
        total_steps=5,
        progress_percentage=progress,
        pathway_items=pathway_items,
        metrics=metrics
    )


# ============================================================================
# HEALTH CHECK GENERATION
# ============================================================================

def generate_health_check() -> HealthCheckResponse:
    """Generate health check response."""
    return HealthCheckResponse(
        status="healthy",
        version="1.0.0-beta",
        services={
            "database": "connected",
            "cache": "connected",
            "ai_core": "ready"
        }
    )


# ============================================================================
# CHAT MESSAGE GENERATION
# ============================================================================

def generate_aletheia_response(user_message: str, context: Dict[str, Any] = None) -> ChatMessage:
    """Generate a response from Aletheia based on user message."""
    
    message_lower = user_message.lower()
    
    # Response templates based on keywords
    responses = {
        'position': "Your financial position reflects strength. Net worth: $18.7M with $2.4M liquid. Trust Index: 87. The Foundation requires calibration.",
        'scenario': "A 20% distribution increase would reduce Trust Index to ~79 within 18 months. Foundation would shift to 'alert' status.",
        'alert': "The Foundation's 7.1% grant rate exceeds the ~5% sustainable threshold. Options: reduce grants, supplement corpus, or accept intentional spend-down.",
        'governance': "The multi-party permission cascade engages when sensitive patterns are detected. CEO, Trustee, and Architect each receive role-appropriate reports.",
        'foundation': "The Family Impact Foundation has a current grant rate of 7.1%, which exceeds the sustainable 5% target. This creates a structural gap that requires intervention.",
        'trust': "Your Trust Index stands at 87/100, composed of: Financial (90), Stewardship (80), Mission (87), and Governance (90). All dimensions are healthy.",
        'default': "Your position remains stable — Trust Index at 87. The Foundation grant rate of 7.1% is the primary area requiring stewardship attention."
    }
    
    # Determine response
    response_text = responses['default']
    for keyword, response in responses.items():
        if keyword in message_lower:
            response_text = response
            break
    
    return ChatMessage(
        id=str(uuid.uuid4()),
        content=response_text,
        is_user=False
    )
