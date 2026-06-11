"""Report generation endpoint — same data, different audiences."""

from fastapi import APIRouter, HTTPException
from ..models import Report, ReportAudience
from ..services.report_generator import generate_report

router = APIRouter(prefix="/api/v1", tags=["reports"])


@router.get("/reports/{audience}", response_model=Report)
def get_report(audience: ReportAudience):
    """Generate a report for the specified audience.

    Audience options:
    - **board**: Strategic summary, risk indicators, recommendations
    - **technical**: Data lineage, calculation methodology, API health
    - **regulator**: Compliance status, audit trail, policy adherence
    - **family**: Plain-language position, action items, Aletheia guidance
    """
    return generate_report(audience)
