"""Governance endpoints — alerts and approvals."""

from fastapi import APIRouter, HTTPException
from ..models import GovernanceAlert, GovernanceApprovalRequest, GovernanceApprovalResponse
from ..mock_data import get_governance_alerts, process_governance_approval

router = APIRouter(prefix="/api/v1/governance", tags=["governance"])


@router.get("/alerts", response_model=list[GovernanceAlert])
def list_governance_alerts():
    """Return all governance alerts requiring attention."""
    return get_governance_alerts()


@router.post("/approve", response_model=GovernanceApprovalResponse)
def approve_governance_alert(request: GovernanceApprovalRequest):
    """Process a governance approval, denial, or escalation."""
    alert = process_governance_approval(
        alert_id=request.alert_id,
        decision=request.decision,
        approved_by=request.approved_by,
    )
    if alert is None:
        raise HTTPException(status_code=404, detail=f"Governance alert {request.alert_id} not found")

    messages = {
        "approved": f"Alert '{alert.title}' has been approved.",
        "denied": f"Alert '{alert.title}' has been denied.",
        "escalated": f"Alert '{alert.title}' has been escalated for further review.",
        "pending": f"Approval recorded ({alert.approvals_received}/{alert.approvals_needed}). Additional approvals needed.",
    }

    return GovernanceApprovalResponse(
        alert_id=alert.id,
        new_status=alert.status,
        message=messages.get(alert.status.value, "Status updated."),
    )
