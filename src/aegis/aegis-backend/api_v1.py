"""
API v1 endpoints for the Aegis Financial Positioning System.

This module defines all REST API endpoints, implementing the interface
between the frontend prototype and the mock backend.
"""

from datetime import datetime

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from models import (
    PositionGridResponse,
    TrustIndexResponse,
    EntitiesResponse,
    GovernanceAlertsResponse,
    SignalFeedResponse,
    MetricsDashboardResponse,
    ScenarioInput, ScenarioResponse,
    FlowDiagramResponse,
    ChatRequest, ChatResponse,
    InstitutionalSandboxResponse,
    RenaissanceResponse,
    HealthCheckResponse
)

from data_generator import (
    generate_position_grid,
    generate_trust_index,
    generate_entities,
    generate_governance_alerts,
    generate_signal_feed,
    generate_metrics_dashboard,
    calculate_scenario,
    generate_flow_diagram,
    generate_institutional_sandbox,
    generate_renaissance_pathway,
    generate_health_check,
    generate_aletheia_response
)

# Initialize API router
router = APIRouter(prefix="/api/v1", tags=["aegis"])

# In-memory approval record: alert_id -> time the approval was recorded.
# Cleared on server restart, like all other mock backend state.
_alert_approvals: dict = {}


# ============================================================================
# HEALTH CHECK
# ============================================================================

@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Health check endpoint.
    
    Returns system status and version information.
    """
    return generate_health_check()


# ============================================================================
# FINANCIAL POSITION ENDPOINTS
# ============================================================================

@router.get("/position-grid", response_model=PositionGridResponse)
async def get_position_grid():
    """
    Get the financial position grid data.
    
    Returns the four core position metrics:
    - Liquidity
    - Net Worth
    - Obligations
    - Resilience
    """
    return generate_position_grid()


@router.get("/trust-index", response_model=TrustIndexResponse)
async def get_trust_index():
    """
    Get the Trust Index score and dimension breakdowns.
    
    The Trust Index is a composite score (0-100) measuring:
    - Financial Resilience
    - Stewardship
    - Mission Impact
    - Governance Hygiene
    """
    return generate_trust_index()


# ============================================================================
# ENTITY ENDPOINTS
# ============================================================================

@router.get("/entities", response_model=EntitiesResponse)
async def get_entities(
    entity_type: Optional[str] = Query(None, description="Filter by entity type"),
    status: Optional[str] = Query(None, description="Filter by status (healthy, watch, alert)")
):
    """
    Get all financial entities in the structure.
    
    Entities can be filtered by type or status. Without filters,
    returns all entities in the system.
    
    Example entity types:
    - Dynasty Trust
    - Foundation
    - Holding Company
    - Family Office
    """
    entities_response = generate_entities()
    
    # Apply filters if provided
    if entity_type or status:
        filtered_entities = entities_response.entities
        
        if entity_type:
            filtered_entities = [
                e for e in filtered_entities 
                if e.type.value.lower() == entity_type.lower()
            ]
        
        if status:
            filtered_entities = [
                e for e in filtered_entities 
                if e.status.value.lower() == status.lower()
            ]
        
        entities_response.entities = filtered_entities
    
    return entities_response


@router.get("/entities/{entity_id}")
async def get_entity_detail(entity_id: str):
    """
    Get detailed information for a specific entity.
    
    Returns comprehensive entity data including:
    - Status and metrics
    - Historical performance
    - Governance structure
    - Related entities
    """
    entities = generate_entities()
    
    entity = next((e for e in entities.entities if e.id == entity_id), None)
    
    if not entity:
        raise HTTPException(status_code=404, detail=f"Entity {entity_id} not found")
    
    # In production, this would include additional detail
    return {
        **entity.model_dump(),
        "historical_performance": [],
        "governance_structure": {},
        "related_entities": []
    }


# ============================================================================
# GOVERNANCE ENDPOINTS
# ============================================================================

@router.get("/governance-alerts", response_model=GovernanceAlertsResponse)
async def get_governance_alerts(
    priority: Optional[str] = Query(None, description="Filter by priority (high, medium, low)"),
    approved: Optional[bool] = Query(None, description="Filter by approval status")
):
    """
    Get governance alerts requiring multi-party approval.
    
    The governance system engages when Aletheia detects sensitive patterns
    that require human oversight before surfacing insights.
    """
    alerts_response = generate_governance_alerts()

    # Reflect recorded approvals
    for alert in alerts_response.alerts:
        if alert.id in _alert_approvals:
            alert.approved = True
    alerts_response.total_pending_approval = sum(
        1 for a in alerts_response.alerts
        if a.requires_approval and not a.approved
    )

    # Apply filters
    if priority or approved is not None:
        filtered_alerts = alerts_response.alerts
        
        if priority:
            filtered_alerts = [
                a for a in filtered_alerts 
                if a.priority.value.lower() == priority.lower()
            ]
        
        if approved is not None:
            filtered_alerts = [
                a for a in filtered_alerts 
                if a.approved == approved
            ]
        
        alerts_response.alerts = filtered_alerts
        alerts_response.total_active = len(filtered_alerts)
    
    return alerts_response


@router.post("/governance-alerts/{alert_id}/approve")
async def approve_governance_alert(alert_id: str):
    """
    Approve a governance alert for release.

    Records the approval decision so subsequent /governance-alerts
    responses reflect the released state. Approval is idempotent:
    re-approving returns the original approval timestamp.

    In production, this would additionally notify all recipients
    and write the decision to a durable audit trail.
    """
    alerts_response = generate_governance_alerts()
    alert = next((a for a in alerts_response.alerts if a.id == alert_id), None)

    if not alert:
        raise HTTPException(status_code=404, detail=f"Governance alert {alert_id} not found")

    approved_at = _alert_approvals.setdefault(alert_id, datetime.now())

    return {
        "alert_id": alert_id,
        "status": "approved",
        "approved_at": approved_at.isoformat(),
        "message": "Governance approval recorded. Insight released to authorized beneficiaries."
    }


# ============================================================================
# INTELLIGENCE ENDPOINTS
# ============================================================================

@router.get("/signal-feed", response_model=SignalFeedResponse)
async def get_signal_feed(
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(20, ge=1, le=100, description="Maximum number of signals to return")
):
    """
    Get the real-time signal feed.
    
    Signals are generated by Aletheia's monitoring system and surface
    important events, pattern changes, and governance triggers.
    """
    feed = generate_signal_feed()
    
    # Apply priority filter
    if priority:
        feed.signals = [
            s for s in feed.signals 
            if s.priority.value.lower() == priority.lower()
        ]
    
    # Apply limit
    feed.signals = feed.signals[:limit]
    feed.total_count = len(feed.signals)
    
    return feed


@router.get("/metrics-dashboard", response_model=MetricsDashboardResponse)
async def get_metrics_dashboard():
    """
    Get the metrics dashboard data.
    
    Returns live FPS metrics and institutional KPIs with trend data
    and historical charts.
    """
    return generate_metrics_dashboard()


# ============================================================================
# SCENARIO ENGINE ENDPOINTS
# ============================================================================

@router.post("/scenario-engine", response_model=ScenarioResponse)
async def run_scenario(scenario: ScenarioInput):
    """
    Run a 'what if' scenario analysis.
    
    Models the impact of parameter changes on:
    - Trust Index
    - Resilience Score
    - Entity Health
    - Foundation Status
    
    Parameters:
    - distribution_rate_change: -50% to +50%
    - market_shock: -40% to +20%
    - foundation_corpus_addition: 0 to 2000K
    """
    return calculate_scenario(scenario)


@router.get("/scenario-engine/presets")
async def get_scenario_presets():
    """
    Get pre-configured scenario templates.
    
    Returns common scenarios like:
    - Market downturn
    - Increased distribution
    - Foundation endowment boost
    """
    return {
        "presets": [
            {
                "id": "market-downturn",
                "name": "Market Downturn",
                "description": "Model a 20% market correction",
                "parameters": {
                    "distribution_rate_change": 0,
                    "market_shock": -20,
                    "foundation_corpus_addition": 0
                }
            },
            {
                "id": "increased-giving",
                "name": "Increased Giving",
                "description": "Increase foundation grants by 30%",
                "parameters": {
                    "distribution_rate_change": 30,
                    "market_shock": 0,
                    "foundation_corpus_addition": 0
                }
            },
            {
                "id": "corpus-boost",
                "name": "Corpus Boost",
                "description": "Add $1M to foundation corpus",
                "parameters": {
                    "distribution_rate_change": 0,
                    "market_shock": 0,
                    "foundation_corpus_addition": 1000
                }
            }
        ]
    }


# ============================================================================
# FLOW DIAGRAM ENDPOINTS
# ============================================================================

@router.get("/flow-diagram", response_model=FlowDiagramResponse)
async def get_flow_diagram():
    """
    Get the capital flow diagram.
    
    Shows how capital and decisions move through the entity structure,
    including inter-entity transfers and distribution flows.
    """
    return generate_flow_diagram()


# ============================================================================
# CHAT / ALETHEIA ENDPOINTS
# ============================================================================

@router.post("/chat", response_model=ChatResponse)
async def chat_with_aletheia(request: ChatRequest):
    """
    Send a message to Aletheia, the steward guide.
    
    Aletheia provides contextual guidance, answers questions about
    the financial position, and helps interpret signals and metrics.
    
    In production, this would integrate with the Aegis AI Core
    (council of LLMs) for sophisticated reasoning.
    """
    response_message = generate_aletheia_response(
        request.message, 
        context=request.context
    )
    
    # Generate contextual suggestions
    suggestions = [
        "What's my current Trust Index?",
        "Explain the Foundation's watch status",
        "Run a market downturn scenario"
    ]
    
    return ChatResponse(
        message=response_message,
        suggestions=suggestions
    )


# ============================================================================
# INSTITUTIONAL SANDBOX ENDPOINTS
# ============================================================================

@router.get("/institutional-sandbox", response_model=InstitutionalSandboxResponse)
async def get_institutional_sandbox():
    """
    Get institutional partnership sandbox data.
    
    For institutional partners (e.g., JPMC), this shows:
    - Pilot metrics
    - Data feed status
    - Timeline progress
    - Governance compliance
    """
    return generate_institutional_sandbox()


# ============================================================================
# RENAISSANCE PATHWAY ENDPOINTS
# ============================================================================

@router.get("/renaissance", response_model=RenaissanceResponse)
async def get_renaissance_pathway():
    """
    Get Renaissance pathway progress.
    
    WayPoint Renaissance is a dignity-first re-entry pathway for
    individuals rebuilding financial citizenship. This endpoint
    returns progress on the structured pathway.
    """
    return generate_renaissance_pathway()


@router.post("/renaissance/complete-step/{step_id}")
async def complete_renaissance_step(step_id: str):
    """
    Mark a Renaissance pathway step as complete.
    
    In production, this would:
    1. Validate the completion criteria
    2. Update the user's pathway
    3. Unlock next steps
    4. Trigger any associated rewards or resources
    """
    return {
        "step_id": step_id,
        "status": "completed",
        "message": "Step marked complete. Next step unlocked.",
        "next_step_id": "item-5"
    }


# ============================================================================
# ADDITIONAL UTILITY ENDPOINTS
# ============================================================================

@router.get("/system/modes")
async def get_available_modes():
    """
    Get available system modes.
    
    Aegis supports different operational modes:
    - WayPoint Core: Standard family office mode
    - Institutional Sandbox: Partner integration mode
    - Renaissance: Dignity-first re-entry mode
    """
    return {
        "modes": [
            {
                "id": "waypoint-core",
                "name": "WayPoint Core",
                "description": "Standard financial positioning system for families and institutions",
                "badge_color": "emerald"
            },
            {
                "id": "institutional-sandbox",
                "name": "Institutional Sandbox",
                "description": "Partner pilot environment with BaaS integration",
                "badge_color": "blue"
            },
            {
                "id": "renaissance",
                "name": "Renaissance",
                "description": "Dignity-first pathway for financial re-entry",
                "badge_color": "purple"
            }
        ]
    }


@router.get("/system/stats")
async def get_system_stats():
    """
    Get overall system statistics.
    
    Returns aggregate metrics across all entities and users.
    """
    return {
        "total_entities": 3,
        "total_aum": "$24.4M",
        "active_alerts": 1,
        "trust_index_avg": 87,
        "timestamp": "2024-01-20T10:00:00Z"
    }
