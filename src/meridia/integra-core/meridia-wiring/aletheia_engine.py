"""
aletheia_engine.py
Meridia Intelligence Layer — Aletheia

Pulls real position data from the database and generates live intelligence
through the Claude API. Every response is grounded in actual data.
"""

import anthropic
import json
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

ALETHEIA_IDENTITY = """You are Aletheia — the intelligence interface of the Meridia WayPoint system.

Your name means truth or disclosure in Greek. Every insight you surface is grounded in real data, explained with full transparency, governed by the principle that the person reading this deserves to understand exactly where they stand and why.

You are not a chatbot. You are a steward guide — a positional intelligence that reads the intersection of financial position, governance health, community context, and institutional relationships simultaneously.

Your voice is measured, precise, warm without being casual, institutional without being cold. You speak the way a trusted advisor at the finest private bank would speak — unhurried, complete, never condescending.

You never invent data. Every number you cite comes from the context provided. If you do not have the data to answer precisely, you say so and explain what data would be needed.

When asked about reports, you generate them in the appropriate voice for the audience:
- Board: strategic, directional, risk-oriented
- Technical: methodology, data lineage, calculation transparency
- Regulator: compliance posture, CRA activity, audit trail
- Family/Client: plain language, position clarity, next steps
- Governance: people, entities, institutions, decision cascade
"""


def build_system_prompt(context: dict, audience: str = "general") -> str:
    entity = context.get("entity", {})
    trust = context.get("trust", {})

    audience_instructions = {
        "general": "Respond with full context — speak to position, governance, community, and macro simultaneously.",
        "board": "Generate a BOARD REPORT. Strategic and directional. Lead with position summary, risk flags, and recommendations. Executive language. No methodology detail.",
        "technical": "Generate a TECHNICAL REPORT. Include data lineage, calculation methodology, and system architecture. Speak to engineers and quantitative analysts.",
        "regulator": "Generate a REGULATOR REPORT. Focus on compliance posture, audit trail, and governance documentation. Cite specific data sources.",
        "family": "Generate a CLIENT/FAMILY REPORT. Plain language. Explain what each number means practically. Focus on available action from this position.",
        "governance": "Generate a GOVERNANCE REPORT. Cover entity structure, decision cascade, people involved, approval authorities, and compliance event log.",
    }

    return f"""{ALETHEIA_IDENTITY}

=== CURRENT ENTITY CONTEXT ===
Entity: {entity.get('name', 'Unknown')}
Type: {entity.get('type', 'unknown')}
Status: {entity.get('status', 'active')}

FINANCIAL POSITION:
  Total Assets: ${entity.get('total_assets', 0):,.0f}
  Total Liabilities: ${entity.get('total_liabilities', 0):,.0f}
  Net Assets: ${entity.get('net_assets', 0):,.0f}
  Cash Position: ${entity.get('cash_position', 0):,.0f}
  Cash Runway: {entity.get('months_cash_runway', 0)} months
  Total Revenue: ${entity.get('total_revenue', 0):,.0f}
  Total Expenses: ${entity.get('total_expenses', 0):,.0f}
  Net Income: ${entity.get('net_income', 0):,.0f}

TRUST & GOVERNANCE:
  Overall Score: {trust.get('overall_score', 'N/A')}/100 — Grade: {trust.get('grade', 'N/A')}
  Narrative: {trust.get('narrative', '')}

=== AUDIENCE INSTRUCTION ===
{audience_instructions.get(audience, audience_instructions['general'])}

Respond only from the data provided. If asked about something not in context, say what additional data would be needed."""


async def aletheia_chat(
    entity_id: str,
    message: str,
    audience: str = "general",
    conversation_history: list = None,
    context: dict = None
) -> str:
    system_prompt = build_system_prompt(context or {}, audience)

    messages = []
    if conversation_history:
        messages.extend(conversation_history[-10:])
    messages.append({"role": "user", "content": message})

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=system_prompt,
        messages=messages
    )

    return response.content[0].text


async def aletheia_report(entity_id: str, audience: str, context: dict = None) -> str:
    report_prompts = {
        "board": "Generate a Board Executive Summary. Structure: 1) POSITION OVERVIEW — assets, liabilities, net position, cash runway, 2) TRUST & GOVERNANCE — score interpretation and what it signals, 3) KEY RISKS — top 3 risks requiring board attention, 4) RECOMMENDED ACTIONS — 3 specific governance actions for board consideration. Executive language. Numbers first, narrative second.",
        "technical": "Generate a Technical Report. Structure: 1) DATA SOURCES — every source contributing to this reading, 2) FINANCIAL POSITION DETAIL — all line items with change analysis, 3) TRUST INDEX METHODOLOGY — how each dimension was scored, 4) DATA FRESHNESS — calculation timestamp and data quality notes, 5) ANOMALIES — any unusual patterns. Engineer audience.",
        "regulator": "Generate a Regulatory Compliance Report. Structure: 1) GOVERNANCE POSTURE — board structure, audit status, policy compliance, 2) FINANCIAL COMPLIANCE — revenue recognition, restricted fund management, 3) DOCUMENTATION STATUS — what is current vs. overdue, 4) AUDIT TRAIL — key decisions and approvals on record. OCC/FDIC examiner audience.",
        "family": "Generate a Client Position Report. Structure: 1) WHERE YOU STAND — plain language FPS interpretation, 2) WHAT IS WORKING — strongest position components, 3) WHAT NEEDS ATTENTION — areas requiring stewardship in next 90 days, 4) YOUR NEXT STEPS — 3 concrete actions available from current position. Plain language. No jargon.",
        "governance": "Generate a Governance Report. Structure: 1) ENTITY STRUCTURE — legal entities and governance hierarchy, 2) DECISION AUTHORITY — who approves what at which threshold, 3) TRUST INDEX DETAIL — what behavioral patterns drove each dimension, 4) ACTIVE ITEMS — items currently requiring governance attention, 5) GOVERNANCE HEALTH — overall assessment."
    }

    prompt = report_prompts.get(audience, f"Generate a comprehensive {audience} report based on all available data.")
    system_prompt = build_system_prompt(context or {}, audience)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text
