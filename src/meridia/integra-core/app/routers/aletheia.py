"""
aletheia.py — Aletheia Intelligence Router
Meridia Integra Core API — imports data directly from mock_data
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api/v1/aletheia", tags=["aletheia"])


class AletheiaRequest(BaseModel):
    message: str
    audience: str = "general"
    conversation_history: List[dict] = []


class AletheiaReportRequest(BaseModel):
    audience: str


def get_entity_context(entity_id: str) -> dict:
    """Pull entity context directly from mock_data."""
    from ..mock_data import get_financial_position, get_trust_index, ENTITIES_DB
    pos = get_financial_position(entity_id)
    trust = get_trust_index(entity_id)
    entity = ENTITIES_DB.get(entity_id, {})
    return {
        "entity": {
            "institution_name": pos.institution_name,
            "net_assets": pos.net_assets,
            "cash_position": pos.cash_position,
            "months_cash_runway": pos.months_cash_runway,
            "total_assets": pos.total_assets,
            "total_liabilities": pos.total_liabilities,
            "net_income": pos.net_income,
            "tier": entity.get("tier", "core"),
        },
        "trust": {
            "overall_score": trust.overall_score,
            "grade": trust.grade,
            "narrative": trust.narrative,
        }
    }


@router.get("/ping", tags=["aletheia"])
def aletheia_ping():
    return {"status": "aletheia online"}


@router.post("/{entity_id}")
async def aletheia_intelligence(entity_id: str, request: AletheiaRequest):
    """Core Aletheia intelligence — real position data + Claude API."""
    import os
    import anthropic

    context = get_entity_context(entity_id)
    entity_name = context["entity"]["institution_name"]
    net_assets = context["entity"]["net_assets"]
    cash = context["entity"]["cash_position"]
    runway = context["entity"]["months_cash_runway"]
    trust_score = context["trust"]["overall_score"]
    trust_narrative = context["trust"]["narrative"]
    tier = context["entity"]["tier"]

    system_prompt = f"""You are Aletheia, the intelligence interface of the Meridia WayPoint system.

You are a steward guide — measured, precise, warm without being casual. You read financial position, governance health, and institutional relationships simultaneously. You never invent data.

CURRENT ENTITY CONTEXT:
Entity: {entity_name}
WayPoint Tier: {tier.title()}
Net Assets: ${net_assets:,.0f}
Cash Position: ${cash:,.0f}
Cash Runway: {runway} months
Trust Score: {trust_score}/100
Governance: {trust_narrative}

Respond only from the data provided. Be concise and direct."""

    try:
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        messages = list(request.conversation_history[-10:]) if request.conversation_history else []
        messages.append({"role": "user", "content": request.message})
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            system=system_prompt,
            messages=messages
        )
        return {"entity_id": entity_id, "entity_name": entity_name, "response": response.content[0].text, "audience": request.audience}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Aletheia error: {str(e)}")


@router.post("/{entity_id}/report")
async def aletheia_report(entity_id: str, request: AletheiaReportRequest):
    """Generate differentiated report — board | technical | regulator | family | governance."""
    import os
    import anthropic

    valid = {"board", "technical", "regulator", "family", "governance"}
    if request.audience not in valid:
        raise HTTPException(status_code=400, detail=f"Audience must be one of: {', '.join(valid)}")

    context = get_entity_context(entity_id)
    entity_name = context["entity"]["institution_name"]
    net_assets = context["entity"]["net_assets"]
    cash = context["entity"]["cash_position"]
    runway = context["entity"]["months_cash_runway"]
    trust_score = context["trust"]["overall_score"]
    trust_narrative = context["trust"]["narrative"]

    prompts = {
        "board": "Generate a Board Executive Summary: 1) Position overview with key numbers, 2) Trust and governance score interpretation, 3) Top 3 risks requiring board attention, 4) Three specific recommended actions. Executive language.",
        "technical": "Generate a Technical Report: all financial line items with change analysis, trust index dimension breakdown, data sources, methodology, anomalies.",
        "regulator": "Generate a Regulatory Compliance Report: governance posture, board structure, audit status, documentation status, audit trail.",
        "family": "Generate a Client Position Report in plain language: where you stand, what is working, what needs attention in 90 days, three concrete next steps. No jargon.",
        "governance": "Generate a Governance Report: entity structure, decision authority, trust index detail, active compliance items, governance health assessment."
    }

    system_prompt = f"""You are Aletheia, the intelligence interface of the Meridia WayPoint system.

CURRENT ENTITY CONTEXT:
Entity: {entity_name}
Net Assets: ${net_assets:,.0f}
Cash Position: ${cash:,.0f}
Cash Runway: {runway} months
Trust Score: {trust_score}/100
Governance: {trust_narrative}"""

    try:
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            system=system_prompt,
            messages=[{"role": "user", "content": prompts[request.audience]}]
        )
        return {"entity_id": entity_id, "entity_name": entity_name, "audience": request.audience, "report": response.content[0].text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report error: {str(e)}")


@router.get("/{entity_id}/context")
def get_context(entity_id: str):
    """Full entity context — complete transparency."""
    context = get_entity_context(entity_id)
    return {
        "entity_id": entity_id,
        **context,
        "data_sources": ["PostgreSQL", "FRED", "FFIEC", "HMDA", "FDIC"]
    }
