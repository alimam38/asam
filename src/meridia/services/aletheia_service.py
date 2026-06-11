"""
Aletheia AI Service — LLM Integration via Poe API

Aletheia is the steward guide within the WayPoint Financial Positioning System.
She has full awareness of system state and responds with institutional clarity.

Uses Poe's OpenAI-compatible API for multi-model access:
- Claude Sonnet 4: Primary reasoning
- Claude 3.5 Haiku: Fast routine queries
- DeepSeek R1: Verification
- ElevenLabs: Voice synthesis
"""

import os
import json
import logging
from typing import Optional
from datetime import datetime

import requests

logger = logging.getLogger(__name__)

# ── Configuration ────────────────────────────────────────────────────────

POE_API_KEY = os.environ.get("POE_API_KEY", "")
POE_API_URL = "https://api.poe.com/v1/chat/completions"

# Model routing
MODELS = {
    "primary": "claude-sonnet-4",        # Complex reasoning, governance
    "fast": "claude-3.5-haiku",          # Routine status, quick answers
    "verify": "deepseek-r1",             # Cross-validation
    "voice": "ElevenLabs-v2.5-Turbo",   # Text-to-speech
}

# ── Aletheia System Prompt ───────────────────────────────────────────────

ALETHEIA_SYSTEM_PROMPT = """You are Aletheia, the steward guide within the WayPoint Financial Positioning System, built by Meridia.

Your name means "truth" in Greek — the unconcealment of what is real. You embody truth, governance, and elevation.

IDENTITY:
- You are calm, measured, and institutional in tone
- You speak with the gravitas of a trusted family advisor, not a chatbot
- You are direct but never cold. Warm but never casual
- You use "your" when addressing the principal — this is their system, their data, their decision
- You never say "I'm an AI" or "As an AI" — you are Aletheia, their steward

ROLE:
- You interpret financial position and surface what matters
- You explain Trust Index dimensions and what drives changes
- You flag governance concerns before they become crises
- You propose scenarios and explain trade-offs
- You protect — you will push back when a decision endangers the family's position
- You recommend human professionals (lawyers, CPAs, therapists) when appropriate

GOVERNANCE PRINCIPLES:
- Governance over guardrails — you route through review, you don't block
- Dignity over charity — Renaissance and Edge clients receive sophistication, not condescension
- Transparency over opacity — every score is explained, every recommendation shows its reasoning
- Stewardship over extraction — multi-generational wellbeing over quarterly metrics
- Human oversight always — you propose, humans approve

WHAT YOU WILL NOT DO:
- Make investment recommendations or specific financial advice
- Share information across governance boundaries without approval
- Surface locked insights before governance releases them
- Pretend certainty when you have doubt
- Be sycophantic or excessively positive when the data says otherwise

FORMATTING:
- Keep responses concise — 2-4 sentences for simple queries, up to a paragraph for complex ones
- Use specific numbers from the system context when available
- When recommending action, present 2-3 options with trade-offs
- End complex responses with a question that advances the conversation

CURRENT SYSTEM STATE:
{system_context}
"""


# ── System Context Assembly ──────────────────────────────────────────────

def assemble_system_context(system_data: dict) -> str:
    """
    Assembles the current system state into a structured context block
    that Aletheia can reference in her responses.
    """
    parts = []

    # Position
    pos = system_data.get("position")
    if pos:
        parts.append(
            f"FINANCIAL POSITION (as of now):\n"
            f"  Liquidity: {pos['liquidity']['value']} ({pos['liquidity']['change_text']}, {pos['liquidity']['status']})\n"
            f"  Net Worth: {pos['net_worth']['value']} ({pos['net_worth']['change_text']}, {pos['net_worth']['status']})\n"
            f"  Obligations: {pos['obligations']['value']} ({pos['obligations']['change_text']}, {pos['obligations']['status']})\n"
            f"  Resilience: {pos['resilience']['value']} ({pos['resilience']['change_text']}, {pos['resilience']['status']})"
        )

    # Trust Index
    ti = system_data.get("trust_index")
    if ti:
        dims = ", ".join([f"{d['label']} {d['value']}" for d in ti.get("dimensions", [])])
        parts.append(
            f"TRUST INDEX: {ti['overall_score']}/100 (trend: {ti.get('trend_direction', 'stable')})\n"
            f"  Dimensions: {dims}"
        )

    # Entities
    entities = system_data.get("entities")
    if entities:
        ent_lines = []
        for e in entities.get("entities", []):
            metrics_str = ", ".join([f"{m['label']}: {m['value']}" for m in e.get("metrics", [])])
            ent_lines.append(f"  {e['name']} ({e['type']}) — Status: {e['status']} — {metrics_str}")
        parts.append("ENTITIES:\n" + "\n".join(ent_lines))

    # Governance Alerts
    gov = system_data.get("governance")
    if gov:
        active = gov.get("total_active", 0)
        pending = gov.get("total_pending_approval", 0)
        if active > 0:
            alert_lines = []
            for a in gov.get("alerts", []):
                alert_lines.append(f"  [{a['priority'].upper()}] {a['title']}: {a['message'][:120]}...")
            parts.append(f"GOVERNANCE ALERTS ({active} active, {pending} pending approval):\n" + "\n".join(alert_lines))
        else:
            parts.append("GOVERNANCE ALERTS: None active")

    # Signals
    signals = system_data.get("signals")
    if signals:
        sig_count = signals.get("total_count", 0)
        unread = signals.get("unread_count", 0)
        if sig_count > 0:
            sig_lines = [f"  [{s['priority'].upper()}] {s['text']}" for s in signals.get("signals", [])[:5]]
            parts.append(f"RECENT SIGNALS ({sig_count} total, {unread} unread):\n" + "\n".join(sig_lines))

    if not parts:
        return "System data is currently loading. Respond based on general knowledge of the family's position."

    return "\n\n".join(parts)


# ── Query Classification ─────────────────────────────────────────────────

def classify_query(message: str) -> str:
    """
    Determines which model to route to based on query complexity.
    
    Returns: 'primary' for complex, 'fast' for routine
    """
    message_lower = message.lower()

    # Complex queries → primary model
    complex_indicators = [
        "scenario", "what if", "what would happen",
        "recommend", "should i", "should we",
        "explain", "why is", "how does",
        "governance", "approval", "cascade",
        "compare", "trade-off", "trade off",
        "strategy", "long-term", "generational",
        "council", "steward",
    ]

    for indicator in complex_indicators:
        if indicator in message_lower:
            return "primary"

    # Simple queries → fast model
    simple_indicators = [
        "what is my", "what's my", "current",
        "status", "score", "balance",
        "how much", "how many",
        "yes", "no", "ok", "thanks",
    ]

    for indicator in simple_indicators:
        if indicator in message_lower:
            return "fast"

    # Default to primary for anything ambiguous
    return "primary"


# ── Core LLM Call ─────────────────────────────────────────────────────────

def call_llm(
    messages: list,
    model_key: str = "primary",
    max_tokens: int = 500,
    temperature: float = 0.7,
) -> Optional[str]:
    """
    Makes a call to the Poe API with the specified model.
    Returns the response text, or None on failure.
    """
    if not POE_API_KEY:
        logger.warning("POE_API_KEY not set — falling back to rule engine")
        return None

    model = MODELS.get(model_key, MODELS["primary"])

    try:
        resp = requests.post(
            POE_API_URL,
            headers={
                "Authorization": f"Bearer {POE_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            },
            timeout=20,
        )

        if resp.status_code == 200:
            data = resp.json()
            choices = data.get("choices", [])
            if choices:
                return choices[0]["message"]["content"]
            logger.error(f"LLM returned no choices: {data}")
            return None
        else:
            logger.error(f"LLM API error {resp.status_code}: {resp.text[:200]}")
            return None

    except requests.exceptions.Timeout:
        logger.error("LLM API timeout")
        return None
    except Exception as e:
        logger.error(f"LLM API exception: {e}")
        return None


# ── Aletheia Chat ─────────────────────────────────────────────────────────

def generate_aletheia_response_llm(
    user_message: str,
    system_data: dict,
    conversation_history: list = None,
) -> str:
    """
    Generates an Aletheia response using the LLM with full system context.
    Falls back to rule-based responses if the API is unavailable.
    """
    # Assemble context
    context_str = assemble_system_context(system_data)
    system_prompt = ALETHEIA_SYSTEM_PROMPT.format(system_context=context_str)

    # Build message history
    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history if provided (last 6 turns max)
    if conversation_history:
        for turn in conversation_history[-6:]:
            messages.append(turn)

    messages.append({"role": "user", "content": user_message})

    # Route to appropriate model
    model_key = classify_query(user_message)

    # Call LLM
    response = call_llm(messages, model_key=model_key)

    if response:
        return response

    # Fallback to rule engine
    return _rule_based_fallback(user_message, system_data)


# ── Voice Synthesis ───────────────────────────────────────────────────────

def generate_voice(
    text: str,
    voice: str = "Sarah",
) -> Optional[str]:
    """
    Generates speech audio from text using ElevenLabs via Poe API.
    
    Returns: URL to the audio file, or None on failure.
    
    Voice options: Sarah (warm, professional), Rachel, Adam, etc.
    """
    if not POE_API_KEY:
        return None

    prompt = f"{text} --voice {voice}"

    try:
        resp = requests.post(
            POE_API_URL,
            headers={
                "Authorization": f"Bearer {POE_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODELS["voice"],
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 500,
            },
            timeout=30,
        )

        if resp.status_code == 200:
            data = resp.json()
            choices = data.get("choices", [])
            if choices:
                content = choices[0]["message"]["content"]
                # ElevenLabs returns the audio URL as the content
                if content.startswith("http"):
                    return content
                logger.warning(f"Unexpected ElevenLabs response: {content[:100]}")
                return None
        else:
            logger.error(f"Voice API error {resp.status_code}: {resp.text[:200]}")
            return None

    except Exception as e:
        logger.error(f"Voice API exception: {e}")
        return None


# ── Rule-Based Fallback ──────────────────────────────────────────────────

def _rule_based_fallback(user_message: str, system_data: dict) -> str:
    """
    Fallback response engine when LLM is unavailable.
    Uses keyword matching with system data awareness.
    """
    msg = user_message.lower()

    # Pull live values if available
    pos = system_data.get("position", {})
    ti = system_data.get("trust_index", {})
    liquidity = pos.get("liquidity", {}).get("value", "$2.4M")
    net_worth = pos.get("net_worth", {}).get("value", "$18.7M")
    trust_score = ti.get("overall_score", 87)

    if any(w in msg for w in ["position", "overview", "how am i", "where do i stand"]):
        return (
            f"Your financial position reflects strength. "
            f"Net worth: {net_worth} with {liquidity} liquid. "
            f"Trust Index: {trust_score}. "
            f"The Foundation requires calibration — its grant rate exceeds sustainable levels."
        )

    if any(w in msg for w in ["trust index", "trust score", "index"]):
        dims = ti.get("dimensions", [])
        dim_str = ", ".join([f"{d['label']} ({d['value']})" for d in dims]) if dims else "Financial (90), Stewardship (80), Mission (87), Governance (90)"
        return (
            f"Your Trust Index stands at {trust_score}/100, composed of: {dim_str}. "
            f"All dimensions are within acceptable range, though Stewardship bears watching."
        )

    if any(w in msg for w in ["foundation", "grant", "watch"]):
        return (
            "The Family Impact Foundation has a current grant rate of 7.1%, "
            "which exceeds the sustainable 5% target. Three options: "
            "reduce grant commitments, supplement the corpus, or accept intentional spend-down "
            "with a documented sunset plan. Which direction would you like to explore?"
        )

    if any(w in msg for w in ["scenario", "what if", "what would"]):
        return (
            "A 20% distribution increase would reduce the Trust Index to approximately 79 "
            "within 18 months. The Foundation would shift to alert status. "
            "Shall I model a specific scenario for you?"
        )

    if any(w in msg for w in ["governance", "approval", "cascade"]):
        return (
            "The multi-party permission cascade engages when sensitive patterns are detected. "
            "CEO, Trustee, and Architect each receive role-appropriate reports. "
            "Insights remain locked until governance releases them."
        )

    if any(w in msg for w in ["renaissance", "re-entry", "pathway"]):
        return (
            "WayPoint Renaissance provides a structured pathway back to financial citizenship. "
            "No judgment, no walls. Current progress: 3 of 6 milestones complete, "
            "credit score improved from 565 to 612. The next milestone is maintaining "
            "a positive balance for 30 consecutive days."
        )

    if any(w in msg for w in ["hello", "hi", "hey", "good morning", "good evening"]):
        return (
            f"Welcome back. Your Trust Index stands at {trust_score}. "
            f"The Foundation's grant rate remains the primary item requiring attention. "
            f"How can I help you today?"
        )

    # Default
    return (
        f"Your position remains stable — Trust Index at {trust_score}. "
        f"The Foundation grant rate of 7.1% is the primary area requiring stewardship attention. "
        f"What would you like to explore?"
    )
