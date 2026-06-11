"""
Integra Core — Mock Data Layer
Five-entity architecture spanning all WayPoint tiers.
All enum values match models.py exactly.
"""

from datetime import date, datetime
from .models import (
    PositionLineItem, FinancialPosition, TrustDimension, TrustIndex,
    Entity, EntityType, EntityStatus,
    Signal, SignalSeverity, SignalCategory,
    GovernanceAlert, GovernanceAlertStatus,
)

DEFAULT_ENTITY_ID = "a1b2c3d4-0002-0002-0002-000000000002"

# ── ENTITY REGISTRY ────────────────────────────────────────────────────────────

ENTITIES_DB = {
    "a1b2c3d4-0002-0002-0002-000000000002": {
        "name": "Hargrove Family Office",
        "tier": "crown",
        "type": EntityType.FUND,
        "status": EntityStatus.ACTIVE,
        "description": "Multi-generational family office. Crown tier governance with three active entities.",
    },
    "a1b2c3d4-0001-0001-0001-000000000001": {
        "name": "Vantage Financial Partners",
        "tier": "institutional",
        "type": EntityType.FUND,
        "status": EntityStatus.ACTIVE,
        "description": "Regional financial institution. $2.4B AUM. WayPoint institutional tier.",
    },
    "a1b2c3d4-0003-0003-0003-000000000003": {
        "name": "Cornerstone AME Collective",
        "tier": "core",
        "type": EntityType.CHURCH,
        "status": EntityStatus.ACTIVE,
        "description": "Faith-based community organization. Core tier financial positioning.",
    },
    "a1b2c3d4-0004-0004-0004-000000000004": {
        "name": "Gulf South Properties LLC",
        "tier": "edge",
        "type": EntityType.FUND,
        "status": EntityStatus.PENDING_REVIEW,
        "description": "Commercial real estate operator. Edge tier — industry in permanent penalty box.",
    },
    "a1b2c3d4-0005-0005-0005-000000000005": {
        "name": "Marcus Thompson",
        "tier": "renaissance",
        "type": EntityType.DISCRETIONARY,
        "status": EntityStatus.ACTIVE,
        "description": "Re-entry client. Rebuilding financial standing. Renaissance tier pathway.",
    },
}

# ── POSITION DATA ──────────────────────────────────────────────────────────────

POSITIONS_DB = {
    "a1b2c3d4-0002-0002-0002-000000000002": {
        "institution_name": "Hargrove Family Office",
        "fiscal_year": "FY2026",
        "as_of_date": date(2026, 3, 31),
        "fps_score": 92.8,
        "fps_direction": "strong",
        "fps_narrative": "Hargrove Family Office holds a commanding position at 92.8/100. The trust corpus is performing above benchmark with exceptional liquidity coverage and distribution alignment.",
        "total_assets": 22_400_000,
        "total_liabilities": 3_700_000,
        "net_assets": 18_700_000,
        "total_revenue": 2_840_000,
        "total_expenses": 1_920_000,
        "net_income": 920_000,
        "cash_position": 2_400_000,
        "months_cash_runway": 15.0,
        "line_items": [
            PositionLineItem(label="Crown Legacy Trust", current=12_400_000, prior=11_800_000, change_pct=5.1, category="assets"),
            PositionLineItem(label="Family Impact Foundation", current=3_800_000, prior=3_600_000, change_pct=5.6, category="assets"),
            PositionLineItem(label="Crown Holdings LLC", current=4_100_000, prior=3_900_000, change_pct=5.1, category="assets"),
            PositionLineItem(label="Liquid Reserves", current=2_400_000, prior=2_100_000, change_pct=14.3, category="assets"),
            PositionLineItem(label="Mortgage Primary", current=2_100_000, prior=2_240_000, change_pct=-6.3, category="liabilities"),
            PositionLineItem(label="Business Line of Credit", current=1_600_000, prior=1_400_000, change_pct=14.3, category="liabilities"),
            PositionLineItem(label="Investment Returns", current=1_840_000, prior=1_640_000, change_pct=12.2, category="revenue"),
            PositionLineItem(label="Business Revenue", current=740_000, prior=680_000, change_pct=8.8, category="revenue"),
            PositionLineItem(label="Rental Income", current=260_000, prior=240_000, change_pct=8.3, category="revenue"),
            PositionLineItem(label="Living & Operating Expenses", current=1_080_000, prior=1_020_000, change_pct=5.9, category="expenses"),
            PositionLineItem(label="Foundation Grants", current=480_000, prior=420_000, change_pct=14.3, category="expenses"),
            PositionLineItem(label="Debt Service", current=360_000, prior=380_000, change_pct=-5.3, category="expenses"),
        ]
    },
    "a1b2c3d4-0001-0001-0001-000000000001": {
        "institution_name": "Vantage Financial Partners",
        "fiscal_year": "FY2026",
        "as_of_date": date(2026, 3, 31),
        "fps_score": 71.2,
        "fps_direction": "stable",
        "fps_narrative": "Vantage Financial Partners maintains a stable institutional position at 71.2/100. Portfolio distribution is balanced across 847 active client relationships. Three bilateral risk flags require governance attention.",
        "total_assets": 2_840_000_000,
        "total_liabilities": 2_480_000_000,
        "net_assets": 360_000_000,
        "total_revenue": 142_000_000,
        "total_expenses": 118_000_000,
        "net_income": 24_000_000,
        "cash_position": 186_000_000,
        "months_cash_runway": 18.9,
        "line_items": [
            PositionLineItem(label="Loan Portfolio", current=1_840_000_000, prior=1_760_000_000, change_pct=4.5, category="assets"),
            PositionLineItem(label="Investment Securities", current=620_000_000, prior=580_000_000, change_pct=6.9, category="assets"),
            PositionLineItem(label="Cash & Due From Banks", current=186_000_000, prior=172_000_000, change_pct=8.1, category="assets"),
            PositionLineItem(label="Other Assets", current=194_000_000, prior=188_000_000, change_pct=3.2, category="assets"),
            PositionLineItem(label="Total Deposits", current=2_180_000_000, prior=2_060_000_000, change_pct=5.8, category="liabilities"),
            PositionLineItem(label="FHLB Borrowings", current=240_000_000, prior=260_000_000, change_pct=-7.7, category="liabilities"),
            PositionLineItem(label="Net Interest Income", current=98_000_000, prior=92_000_000, change_pct=6.5, category="revenue"),
            PositionLineItem(label="Non-Interest Income", current=44_000_000, prior=40_000_000, change_pct=10.0, category="revenue"),
            PositionLineItem(label="Personnel Expense", current=64_000_000, prior=61_000_000, change_pct=4.9, category="expenses"),
            PositionLineItem(label="Provision for Loan Losses", current=28_000_000, prior=22_000_000, change_pct=27.3, category="expenses"),
            PositionLineItem(label="Other Operating Expense", current=26_000_000, prior=24_000_000, change_pct=8.3, category="expenses"),
        ]
    },
    "a1b2c3d4-0003-0003-0003-000000000003": {
        "institution_name": "Cornerstone AME Collective",
        "fiscal_year": "FY2026",
        "as_of_date": date(2026, 3, 31),
        "fps_score": 58.4,
        "fps_direction": "improving",
        "fps_narrative": "Cornerstone AME Collective is improving at 58.4/100. Cash position has strengthened over the last two quarters. Operating reserve target of 3 months is 68% funded.",
        "total_assets": 1_840_000,
        "total_liabilities": 480_000,
        "net_assets": 1_360_000,
        "total_revenue": 620_000,
        "total_expenses": 580_000,
        "net_income": 40_000,
        "cash_position": 148_000,
        "months_cash_runway": 3.1,
        "line_items": []
    },
    "a1b2c3d4-0004-0004-0004-000000000004": {
        "institution_name": "Gulf South Properties LLC",
        "fiscal_year": "FY2026",
        "as_of_date": date(2026, 3, 31),
        "fps_score": 44.1,
        "fps_direction": "declining",
        "fps_narrative": "Gulf South Properties LLC is under watch at 44.1/100. Commercial real estate headwinds and elevated interest rates are compressing margins. DSCR has declined below 1.2x threshold. Governance action required within 60 days.",
        "total_assets": 4_200_000,
        "total_liabilities": 3_100_000,
        "net_assets": 1_100_000,
        "total_revenue": 480_000,
        "total_expenses": 510_000,
        "net_income": -30_000,
        "cash_position": 82_000,
        "months_cash_runway": 1.9,
        "line_items": []
    },
    "a1b2c3d4-0005-0005-0005-000000000005": {
        "institution_name": "Marcus Thompson",
        "fiscal_year": "FY2026",
        "as_of_date": date(2026, 3, 31),
        "fps_score": 31.6,
        "fps_direction": "improving",
        "fps_narrative": "Marcus Thompson is building at 31.6/100. Month 8 of the Renaissance pathway. Bank account opened, direct deposit established, secured card balance current. Employment income stable for 6 consecutive months. On track for Core tier review at month 12.",
        "total_assets": 14_200,
        "total_liabilities": 8_400,
        "net_assets": 5_800,
        "total_revenue": 42_000,
        "total_expenses": 38_400,
        "net_income": 3_600,
        "cash_position": 4_800,
        "months_cash_runway": 1.5,
        "line_items": []
    },
}

# ── TRUST INDEX ────────────────────────────────────────────────────────────────

TRUST_DB = {
    "a1b2c3d4-0002-0002-0002-000000000002": TrustIndex(
        institution_name="Hargrove Family Office",
        overall_score=87.0,
        grade="A",
        dimensions=[
            TrustDimension(name="Behavioral Consistency", score=91.0, weight=0.25, factors=["12 consecutive months aligned", "No missed commitments", "Estate plan current"], trend="improving"),
            TrustDimension(name="Governance Adherence", score=84.0, weight=0.25, factors=["Trust documents executed", "Annual trustee review complete", "Investment policy current"], trend="stable"),
            TrustDimension(name="Communication Reliability", score=89.0, weight=0.25, factors=["Quarterly reviews attended", "Document requests responded within 48hrs"], trend="improving"),
            TrustDimension(name="Commitment Fulfillment", score=84.0, weight=0.25, factors=["Charitable giving targets met", "Business obligations current", "Debt covenants satisfied"], trend="stable"),
        ],
        calculated_at=datetime(2026, 3, 26),
        narrative="Hargrove Family Office demonstrates institutional-grade trust across all four dimensions. Behavioral consistency leads at 91. The Foundation grant rate at 7.1% is approaching the 7.5% sustainability threshold."
    ),
    "a1b2c3d4-0001-0001-0001-000000000001": TrustIndex(
        institution_name="Vantage Financial Partners",
        overall_score=76.8,
        grade="B+",
        dimensions=[
            TrustDimension(name="Behavioral Consistency", score=80.0, weight=0.25, factors=["Lending policy adherence 94%", "Exception rate within limits"], trend="stable"),
            TrustDimension(name="Governance Adherence", score=72.0, weight=0.25, factors=["Board meeting attendance 91%", "Audit findings resolved", "CRA plan current"], trend="improving"),
            TrustDimension(name="Communication Reliability", score=78.0, weight=0.25, factors=["Regulatory filings current", "Client communication SLA 89%"], trend="stable"),
            TrustDimension(name="Commitment Fulfillment", score=78.0, weight=0.25, factors=["CRA commitments on pace", "HMDA data quality 96.8%"], trend="improving"),
        ],
        calculated_at=datetime(2026, 3, 26),
        narrative="Vantage Financial Partners maintains solid institutional governance at 76.8. CRA performance is trending upward. Three open audit findings require resolution before Q2 close."
    ),
    "a1b2c3d4-0003-0003-0003-000000000003": TrustIndex(
        institution_name="Cornerstone AME Collective",
        overall_score=64.2,
        grade="C+",
        dimensions=[
            TrustDimension(name="Behavioral Consistency", score=68.0, weight=0.25, factors=["Budget adherence 82%", "Board turnover 3 members in 12 months"], trend="stable"),
            TrustDimension(name="Governance Adherence", score=60.0, weight=0.25, factors=["Annual audit delayed 90 days", "Investment policy not updated since 2022"], trend="improving"),
            TrustDimension(name="Communication Reliability", score=66.0, weight=0.25, factors=["Funder reports submitted timely", "Two missed board quorums"], trend="stable"),
            TrustDimension(name="Commitment Fulfillment", score=63.0, weight=0.25, factors=["Program deliverables 78% complete", "One grant covenant at risk"], trend="improving"),
        ],
        calculated_at=datetime(2026, 3, 26),
        narrative="Cornerstone AME Collective is in active governance development at 64.2. The delayed annual audit is the priority item. Financial trajectory is positive."
    ),
    "a1b2c3d4-0004-0004-0004-000000000004": TrustIndex(
        institution_name="Gulf South Properties LLC",
        overall_score=51.4,
        grade="C-",
        dimensions=[
            TrustDimension(name="Behavioral Consistency", score=48.0, weight=0.25, factors=["Two late debt service payments", "Operating account overdraft in Q4"], trend="declining"),
            TrustDimension(name="Governance Adherence", score=54.0, weight=0.25, factors=["LLC operating agreement current", "Tax filings current", "One lender covenant breach"], trend="stable"),
            TrustDimension(name="Communication Reliability", score=52.0, weight=0.25, factors=["Lender reporting 60 days late", "Two unanswered covenant cure notices"], trend="declining"),
            TrustDimension(name="Commitment Fulfillment", score=52.0, weight=0.25, factors=["Rent collection 88%", "Maintenance commitments partially met"], trend="stable"),
        ],
        calculated_at=datetime(2026, 3, 26),
        narrative="Gulf South Properties LLC requires active governance intervention at 51.4. The lender covenant breach must be resolved within 30 days to prevent acceleration."
    ),
    "a1b2c3d4-0005-0005-0005-000000000005": TrustIndex(
        institution_name="Marcus Thompson",
        overall_score=42.8,
        grade="D+",
        dimensions=[
            TrustDimension(name="Behavioral Consistency", score=46.0, weight=0.25, factors=["6 months consecutive employment", "No NSF events in 90 days"], trend="improving"),
            TrustDimension(name="Governance Adherence", score=40.0, weight=0.25, factors=["WayPoint program participation current", "Savings goal 24% funded"], trend="improving"),
            TrustDimension(name="Communication Reliability", score=44.0, weight=0.25, factors=["Monthly check-ins attended", "Phone number verified"], trend="stable"),
            TrustDimension(name="Commitment Fulfillment", score=42.0, weight=0.25, factors=["Secured card balance current", "Rent payments on time"], trend="improving"),
        ],
        calculated_at=datetime(2026, 3, 26),
        narrative="Marcus Thompson is in month 8 of the Renaissance pathway and trending upward. Behavioral consistency leads with six consecutive months of employment and no overdraft events in 90 days."
    ),
}

# ── SIGNALS ────────────────────────────────────────────────────────────────────

SIGNALS_DB = {
    "a1b2c3d4-0002-0002-0002-000000000002": [
        Signal(id="sig-h01", title="Foundation Grant Rate Alert", description="Family Impact Foundation grant rate at 7.1% approaching 7.5% sustainability threshold. Board review recommended before next distribution cycle.", severity=SignalSeverity.WARNING, category=SignalCategory.GOVERNANCE, timestamp=datetime(2026, 3, 24), source="Governance Monitor", action_required=True, acknowledged=False),
        Signal(id="sig-h02", title="Trust Corpus Benchmark Exceeded", description="Crown Legacy Trust returned 8.4% YTD vs 7.2% benchmark. Rebalancing review recommended to maintain target allocation.", severity=SignalSeverity.INFO, category=SignalCategory.FINANCIAL, timestamp=datetime(2026, 3, 20), source="Portfolio Monitor", action_required=False, acknowledged=False),
        Signal(id="sig-h03", title="Estate Document Review Due", description="Annual review of estate documents scheduled for Q2. Beneficiary designations last updated 14 months ago.", severity=SignalSeverity.INFO, category=SignalCategory.COMPLIANCE, timestamp=datetime(2026, 3, 15), source="Governance Calendar", action_required=False, acknowledged=True),
    ],
    "a1b2c3d4-0001-0001-0001-000000000001": [
        Signal(id="sig-v01", title="CRA Assessment Area Gap - DeKalb County", description="HMDA analysis shows 23% denial rate in LMI tracts within DeKalb County. Industry average is 14%. CRA strategic plan update recommended.", severity=SignalSeverity.CRITICAL, category=SignalCategory.COMPLIANCE, timestamp=datetime(2026, 3, 22), source="CRA Intelligence Layer", action_required=True, acknowledged=False),
        Signal(id="sig-v02", title="Bilateral Risk Flag - Gulf South Properties", description="Gulf South Properties LLC debt service coverage declined below 1.2x threshold. Bilateral risk direction toward institution. Governance review required.", severity=SignalSeverity.WARNING, category=SignalCategory.GOVERNANCE, timestamp=datetime(2026, 3, 18), source="Bilateral Risk Engine", action_required=True, acknowledged=False),
        Signal(id="sig-v03", title="Provision for Loan Losses Elevated", description="Q1 provision increased 27.3% YoY. Commercial real estate portfolio concentration warrants stress testing.", severity=SignalSeverity.WARNING, category=SignalCategory.FINANCIAL, timestamp=datetime(2026, 3, 10), source="Portfolio Monitor", action_required=False, acknowledged=False),
    ],
    "a1b2c3d4-0003-0003-0003-000000000003": [
        Signal(id="sig-c01", title="Annual Audit Delayed", description="FY2025 audit is 90 days past due. Funder reporting obligations at risk. CPA engagement required immediately.", severity=SignalSeverity.CRITICAL, category=SignalCategory.COMPLIANCE, timestamp=datetime(2026, 3, 20), source="Compliance Monitor", action_required=True, acknowledged=False),
        Signal(id="sig-c02", title="Operating Reserve at 68% of Target", description="3-month operating reserve target is 68% funded at current cash position.", severity=SignalSeverity.WARNING, category=SignalCategory.FINANCIAL, timestamp=datetime(2026, 3, 15), source="Financial Monitor", action_required=False, acknowledged=False),
    ],
    "a1b2c3d4-0004-0004-0004-000000000004": [
        Signal(id="sig-g01", title="Lender Covenant Breach - 30 Day Cure Period", description="DSCR fallen below 1.15x covenant threshold. Lender has issued 30-day cure notice. Governance action required immediately.", severity=SignalSeverity.CRITICAL, category=SignalCategory.GOVERNANCE, timestamp=datetime(2026, 3, 21), source="Covenant Monitor", action_required=True, acknowledged=False),
        Signal(id="sig-g02", title="Two Late Debt Service Payments", description="Q3 and Q4 2025 payments received 8 and 12 days late respectively.", severity=SignalSeverity.WARNING, category=SignalCategory.FINANCIAL, timestamp=datetime(2026, 3, 10), source="Payment Monitor", action_required=False, acknowledged=False),
    ],
    "a1b2c3d4-0005-0005-0005-000000000005": [
        Signal(id="sig-m01", title="Core Tier Review Milestone", description="Month 8 of 12 on Renaissance pathway. On track for Core tier review in 4 months. Employment income stable 6 consecutive months.", severity=SignalSeverity.INFO, category=SignalCategory.GOVERNANCE, timestamp=datetime(2026, 3, 24), source="Pathway Monitor", action_required=False, acknowledged=False),
        Signal(id="sig-m02", title="Savings Goal Progress", description="Emergency fund target 24% funded. Recommended: automatic transfer increase of $50/month.", severity=SignalSeverity.INFO, category=SignalCategory.FINANCIAL, timestamp=datetime(2026, 3, 15), source="Financial Coach", action_required=False, acknowledged=False),
    ],
}

# ── GOVERNANCE ALERTS ──────────────────────────────────────────────────────────

GOVERNANCE_ALERTS = [
    GovernanceAlert(
        id="gov-001",
        title="Foundation Distribution Approval",
        description="Family Impact Foundation annual distribution of $480,000 requires board approval. Grant rate will reach 7.1% upon approval. Trustee review recommended given proximity to 7.5% sustainability threshold.",
        alert_type="approval",
        status=GovernanceAlertStatus.PENDING,
        requested_by="Investment Committee",
        requested_at=datetime(2026, 3, 20),
        amount=480_000,
        entity_id="a1b2c3d4-0002-0002-0002-000000000002",
        requires_quorum=True,
        approvals_needed=3,
        approvals_received=1,
    ),
    GovernanceAlert(
        id="gov-002",
        title="Covenant Cure Response - Gulf South Properties",
        description="Lender covenant breach requires formal response within 30 days. Options: cure payment, covenant waiver request, or restructuring. Governance approval required for any response action.",
        alert_type="approval",
        status=GovernanceAlertStatus.PENDING,
        requested_by="Risk Management",
        requested_at=datetime(2026, 3, 21),
        amount=None,
        entity_id="a1b2c3d4-0004-0004-0004-000000000004",
        requires_quorum=False,
        approvals_needed=1,
        approvals_received=0,
    ),
    GovernanceAlert(
        id="gov-003",
        title="CRA Strategic Plan Update - DeKalb County",
        description="HMDA analysis requires CRA strategic plan update addressing 23% LMI tract denial rate in DeKalb County assessment area. Regulatory submission deadline: Q2 2026.",
        alert_type="review",
        status=GovernanceAlertStatus.PENDING,
        requested_by="Compliance",
        requested_at=datetime(2026, 3, 22),
        amount=None,
        entity_id="a1b2c3d4-0001-0001-0001-000000000001",
        requires_quorum=False,
        approvals_needed=1,
        approvals_received=0,
    ),
]

# ── ACCESSOR FUNCTIONS ─────────────────────────────────────────────────────────

def get_financial_position(entity_id: str = None) -> FinancialPosition:
    eid = entity_id or DEFAULT_ENTITY_ID
    d = POSITIONS_DB.get(eid, POSITIONS_DB[DEFAULT_ENTITY_ID])
    return FinancialPosition(
        institution_name=d["institution_name"],
        as_of_date=d["as_of_date"],
        fiscal_year=d["fiscal_year"],
        line_items=d["line_items"],
        total_assets=d["total_assets"],
        total_liabilities=d["total_liabilities"],
        net_assets=d["net_assets"],
        total_revenue=d["total_revenue"],
        total_expenses=d["total_expenses"],
        net_income=d["net_income"],
        cash_position=d["cash_position"],
        months_cash_runway=d["months_cash_runway"],
    )

def get_trust_index(entity_id: str = None) -> TrustIndex:
    eid = entity_id or DEFAULT_ENTITY_ID
    return TRUST_DB.get(eid, TRUST_DB[DEFAULT_ENTITY_ID])

def get_signals(entity_id: str = None) -> list:
    eid = entity_id or DEFAULT_ENTITY_ID
    return SIGNALS_DB.get(eid, SIGNALS_DB[DEFAULT_ENTITY_ID])

def get_all_entities() -> list:
    return [
        Entity(
            id=eid,
            name=d["name"],
            type=d["type"],
            status=d["status"],
            balance=POSITIONS_DB.get(eid, {}).get("net_assets", 0),
            restricted=False,
            description=d["description"],
            created_date=date(2024, 1, 1),
            last_activity=date(2026, 3, 26),
            governance_notes=f"WayPoint {d['tier'].title()} tier. FPS {POSITIONS_DB.get(eid, {}).get('fps_score', 0)}/100.",
        )
        for eid, d in ENTITIES_DB.items()
    ]

def get_fps_data(entity_id: str = None) -> dict:
    eid = entity_id or DEFAULT_ENTITY_ID
    d = POSITIONS_DB.get(eid, POSITIONS_DB[DEFAULT_ENTITY_ID])
    e = ENTITIES_DB.get(eid, {})
    return {
        "entity_id": eid,
        "entity_name": d["institution_name"],
        "fps_score": d["fps_score"],
        "fps_direction": d["fps_direction"],
        "fps_narrative": d["fps_narrative"],
        "tier": e.get("tier", "core"),
    }

def get_governance_alerts() -> list:
    return GOVERNANCE_ALERTS

def process_governance_approval(alert_id: str, decision: str, approved_by: str):
    for alert in GOVERNANCE_ALERTS:
        if alert.id == alert_id:
            if decision == "approve":
                alert.approvals_received += 1
                if alert.approvals_received >= alert.approvals_needed:
                    alert.status = GovernanceAlertStatus.APPROVED
                else:
                    alert.status = GovernanceAlertStatus.PENDING
            elif decision == "deny":
                alert.status = GovernanceAlertStatus.DENIED
            elif decision == "escalate":
                alert.status = GovernanceAlertStatus.ESCALATED
            return alert
    return None
# Aliases for backward compatibility
def get_entities():
    return get_all_entities()

def get_entity_detail(entity_id: str):
    return None

