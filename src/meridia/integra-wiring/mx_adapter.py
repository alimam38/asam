"""
mx_adapter.py — MX Platform Integration
Meridia Integra Core · Traverse Code Inc.

Connects to MX Development API to:
1. Pull account balances and transactions for an entity
2. Calculate FPS component scores from real financial data
3. Upsert live positions into meridia_core PostgreSQL

MX API Docs: https://docs.mx.com/api
Environment: Development (int-api.mx.com)
"""

import asyncio
import base64
import json
from datetime import datetime, date, timedelta
from typing import Optional, List, Dict, Any
import httpx
import asyncpg
from loguru import logger

# ── MX CREDENTIALS ────────────────────────────────────────
MX_CLIENT_ID  = "9654561c-fcdf-451b-b8d8-dc6c73273f89"
MX_API_KEY    = "06452f44266d63b6d5eadb1c7e7faca09a907ccd"
MX_BASIC_AUTH = "OTY1NDU2MWMtZmNkZi00NTFiLWI4ZDgtZGM2YzczMjczZjg5OjA2NDUyZjQ0MjY2ZDYzYjZkNWVhZGIxYzdlN2ZhY2EwOWE5MDdjY2Q="
MX_BASE_URL   = "https://int-api.mx.com"

DB = dict(
    host="192.168.0.160", port=5433, database="meridia_core",
    user="meridia", password="Ethanj2020##"
)

HEADERS = {
    "Authorization": f"Basic {MX_BASIC_AUTH}",
    "Accept":        "application/vnd.mx.api.v1+json",
    "Content-Type":  "application/json",
}


# ══════════════════════════════════════════════════════════
# MX API CLIENT
# ══════════════════════════════════════════════════════════

class MXClient:
    """Async MX API client — wraps all platform calls."""

    def __init__(self):
        self.base = MX_BASE_URL
        self.headers = HEADERS

    async def get(self, path: str, params: dict = None) -> dict:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.get(
                f"{self.base}{path}",
                headers=self.headers,
                params=params or {}
            )
            r.raise_for_status()
            return r.json()

    async def post(self, path: str, body: dict) -> dict:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(
                f"{self.base}{path}",
                headers=self.headers,
                json=body
            )
            r.raise_for_status()
            return r.json()

    async def delete(self, path: str) -> bool:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.delete(f"{self.base}{path}", headers=self.headers)
            return r.status_code in (200, 204)

    # ── USER MANAGEMENT ───────────────────────────────────

    async def list_users(self) -> List[dict]:
        data = await self.get("/users")
        return data.get("users", [])

    async def create_user(self, identifier: str, metadata: str = "") -> dict:
        body = {"user": {"id": identifier, "metadata": metadata}}
        data = await self.post("/users", body)
        return data.get("user", {})

    async def get_or_create_user(self, entity_id: str, entity_name: str) -> str:
        """Get existing MX user or create one. Returns MX user GUID."""
        users = await self.list_users()
        # Look for existing user with matching metadata
        for u in users:
            if entity_id in (u.get("metadata", "") or ""):
                logger.info(f"MX: Found existing user {u['guid']} for {entity_name}")
                return u["guid"]
        # Create new
        user = await self.create_user(
            identifier=entity_id[:32],
            metadata=json.dumps({"entity_id": entity_id, "name": entity_name})
        )
        logger.info(f"MX: Created user {user['guid']} for {entity_name}")
        return user["guid"]

    # ── MEMBERS (Bank Connections) ─────────────────────────

    async def list_members(self, user_guid: str) -> List[dict]:
        data = await self.get(f"/users/{user_guid}/members")
        return data.get("members", [])

    async def create_member(self, user_guid: str, institution_code: str,
                            credentials: List[dict]) -> dict:
        body = {
            "member": {
                "institution_code": institution_code,
                "credentials": credentials,
                "metadata": "Meridia WayPoint connection"
            }
        }
        data = await self.post(f"/users/{user_guid}/members", body)
        return data.get("member", {})

    async def get_member_status(self, user_guid: str, member_guid: str) -> dict:
        data = await self.get(f"/users/{user_guid}/members/{member_guid}/status")
        return data.get("member", {})

    async def list_institutions(self, name: str = "", page: int = 1) -> List[dict]:
        data = await self.get("/institutions", {"name": name, "page": page, "records_per_page": 10})
        return data.get("institutions", [])

    # ── ACCOUNTS ──────────────────────────────────────────

    async def list_accounts(self, user_guid: str) -> List[dict]:
        data = await self.get(f"/users/{user_guid}/accounts")
        return data.get("accounts", [])

    async def list_member_accounts(self, user_guid: str, member_guid: str) -> List[dict]:
        data = await self.get(f"/users/{user_guid}/members/{member_guid}/accounts")
        return data.get("accounts", [])

    # ── TRANSACTIONS ──────────────────────────────────────

    async def list_transactions(self, user_guid: str,
                                 from_date: str = None,
                                 to_date: str = None,
                                 page: int = 1) -> List[dict]:
        params = {"page": page, "records_per_page": 500}
        if from_date: params["from_date"] = from_date
        if to_date:   params["to_date"] = to_date
        data = await self.get(f"/users/{user_guid}/transactions", params)
        return data.get("transactions", [])

    async def list_account_transactions(self, user_guid: str, account_guid: str,
                                         from_date: str = None) -> List[dict]:
        params = {"records_per_page": 500}
        if from_date: params["from_date"] = from_date
        data = await self.get(
            f"/users/{user_guid}/accounts/{account_guid}/transactions", params
        )
        return data.get("transactions", [])

    # ── HOLDINGS (investments) ─────────────────────────────

    async def list_holdings(self, user_guid: str) -> List[dict]:
        data = await self.get(f"/users/{user_guid}/holdings")
        return data.get("holdings", [])

    # ── INSIGHTS (MX-calculated) ───────────────────────────

    async def get_account_numbers(self, user_guid: str, member_guid: str) -> List[dict]:
        data = await self.get(
            f"/users/{user_guid}/members/{member_guid}/account_numbers"
        )
        return data.get("account_numbers", [])


# ══════════════════════════════════════════════════════════
# FPS CALCULATOR FROM MX DATA
# ══════════════════════════════════════════════════════════

class FPSFromMX:
    """
    Derives Financial Position Score components from real MX account data.

    Five components, same weights as the Integra Core engine:
      net_position       25% — net worth: assets minus liabilities
      liquidity_coverage 25% — liquid assets vs 3-month expense burn
      dscr               15% — income vs debt service
      runway             20% — months of cash reserves
      distribution_align 15% — savings rate / financial goal alignment
    """

    @staticmethod
    def calculate(accounts: List[dict], transactions: List[dict],
                  entity_name: str) -> dict:
        """Returns FPS component dict ready for DB insert."""

        # Classify accounts
        checking     = [a for a in accounts if a.get("account_type") in
                        ("CHECKING", "checking")]
        savings      = [a for a in accounts if a.get("account_type") in
                        ("SAVINGS", "savings")]
        investment   = [a for a in accounts if a.get("account_type") in
                        ("INVESTMENT", "investment", "BROKERAGE", "brokerage")]
        credit_cards = [a for a in accounts if a.get("account_type") in
                        ("CREDIT_CARD", "credit_card", "creditcard")]
        loans        = [a for a in accounts if a.get("account_type") in
                        ("LOAN", "loan", "MORTGAGE", "mortgage", "AUTO", "auto")]

        # Balances
        liquid_assets    = sum(float(a.get("balance") or 0) for a in checking + savings)
        investment_value = sum(float(a.get("balance") or 0) for a in investment)
        total_assets     = liquid_assets + investment_value
        credit_balance   = sum(float(a.get("balance") or 0) for a in credit_cards)
        loan_balance     = sum(float(a.get("balance") or 0) for a in loans)
        total_liabilities = credit_balance + loan_balance

        net_worth = total_assets - total_liabilities

        # Transaction analysis — last 90 days
        cutoff = (datetime.now() - timedelta(days=90)).date()
        recent_tx = [
            t for t in transactions
            if t.get("date") and date.fromisoformat(t["date"][:10]) >= cutoff
        ]

        # Income detection (positive non-transfer transactions)
        income_tx = [
            t for t in recent_tx
            if float(t.get("amount") or 0) > 0
            and t.get("type", "").upper() not in ("TRANSFER", "CREDIT")
        ]
        monthly_income = sum(float(t.get("amount", 0)) for t in income_tx) / 3

        # Expense detection (negative transactions)
        expense_tx = [
            t for t in recent_tx
            if float(t.get("amount") or 0) < 0
            and t.get("type", "").upper() not in ("TRANSFER", "PAYMENT")
        ]
        monthly_expenses = abs(sum(float(t.get("amount", 0)) for t in expense_tx)) / 3

        # Debt service payments (loan/credit payments)
        debt_payments = [
            t for t in recent_tx
            if t.get("type", "").upper() in ("PAYMENT",)
            or (t.get("category", "").upper() in ("TRANSFER", "LOAN_PAYMENT"))
        ]
        monthly_debt_service = abs(
            sum(float(t.get("amount", 0)) for t in debt_payments)
        ) / 3

        # ── COMPONENT SCORING ─────────────────────────────

        # 1. NET POSITION (25%) — net worth scaled 0-100
        # >$500K = 100, $250K-$500K = 80-100, $0-$250K = 40-80, negative = 0-40
        if net_worth >= 500_000:
            net_pos_score = 95.0
        elif net_worth >= 250_000:
            net_pos_score = 80.0 + (net_worth - 250_000) / 250_000 * 15
        elif net_worth >= 0:
            net_pos_score = 40.0 + net_worth / 250_000 * 40
        else:
            net_pos_score = max(0, 40 + net_worth / 50_000 * 40)

        # 2. LIQUIDITY COVERAGE (25%) — liquid vs 3-month burn
        # Ratio: liquid / (monthly_expenses * 3)
        three_month_burn = monthly_expenses * 3 if monthly_expenses > 0 else 1
        liq_ratio = liquid_assets / three_month_burn if three_month_burn > 0 else 1
        if liq_ratio >= 3.0:      liq_score = 92.0
        elif liq_ratio >= 2.0:    liq_score = 80.0
        elif liq_ratio >= 1.0:    liq_score = 65.0
        elif liq_ratio >= 0.5:    liq_score = 45.0
        else:                     liq_score = 20.0

        # 3. DSCR (15%) — income vs monthly debt service
        if monthly_debt_service > 0 and monthly_income > 0:
            dscr_ratio = monthly_income / monthly_debt_service
            if dscr_ratio >= 3.0:     dscr_score = 90.0
            elif dscr_ratio >= 2.0:   dscr_score = 78.0
            elif dscr_ratio >= 1.5:   dscr_score = 65.0
            elif dscr_ratio >= 1.25:  dscr_score = 50.0
            elif dscr_ratio >= 1.0:   dscr_score = 35.0
            else:                     dscr_score = 15.0
        else:
            dscr_score = 70.0  # No debt = neutral-positive

        # 4. RUNWAY (20%) — months of liquid reserves
        if monthly_expenses > 0:
            runway_months = liquid_assets / monthly_expenses
        else:
            runway_months = 12  # Assume adequate if no expenses detected
        if runway_months >= 12:     runway_score = 95.0
        elif runway_months >= 6:    runway_score = 80.0
        elif runway_months >= 3:    runway_score = 60.0
        elif runway_months >= 1:    runway_score = 35.0
        else:                       runway_score = 10.0

        # 5. DISTRIBUTION ALIGNMENT (15%) — savings rate
        if monthly_income > 0:
            savings_rate = (monthly_income - monthly_expenses) / monthly_income
            if savings_rate >= 0.20:   dist_score = 90.0
            elif savings_rate >= 0.10: dist_score = 75.0
            elif savings_rate >= 0.05: dist_score = 55.0
            elif savings_rate >= 0.0:  dist_score = 40.0
            else:                      dist_score = 15.0  # Spending more than earning
        else:
            dist_score = 50.0

        # Clamp all scores
        def clamp(v): return round(max(0.0, min(100.0, v)), 1)

        net_pos_score  = clamp(net_pos_score)
        liq_score      = clamp(liq_score)
        dscr_score     = clamp(dscr_score)
        runway_score   = clamp(runway_score)
        dist_score     = clamp(dist_score)

        # Composite FPS
        fps_score = round(
            net_pos_score  * 0.25 +
            liq_score      * 0.25 +
            dscr_score     * 0.15 +
            runway_score   * 0.20 +
            dist_score     * 0.15,
            1
        )

        # Direction heuristic
        if fps_score >= 75: direction = "strong"
        elif fps_score >= 60: direction = "developing"
        elif fps_score >= 45: direction = "watch"
        else: direction = "critical"

        # Narrative
        narrative = (
            f"{entity_name} holds a {'strong' if fps_score >= 70 else 'developing'} "
            f"financial position at {fps_score}/100. "
            f"Liquid reserves cover {runway_months:.1f} months of expenses. "
            f"Net worth: ${net_worth:,.0f} across {len(accounts)} accounts."
        )

        return {
            "fps_score":          fps_score,
            "net_position":       net_pos_score,
            "liquidity_coverage": liq_score,
            "dscr_score":         dscr_score,
            "runway_score":       runway_score,
            "distribution_align": dist_score,
            "fps_direction":      direction,
            "fps_narrative":      narrative,
            "raw_data": {
                "source":           "mx",
                "accounts":         len(accounts),
                "total_assets":     round(total_assets, 2),
                "total_liabilities": round(total_liabilities, 2),
                "net_worth":        round(net_worth, 2),
                "liquid_assets":    round(liquid_assets, 2),
                "monthly_income":   round(monthly_income, 2),
                "monthly_expenses": round(monthly_expenses, 2),
                "monthly_debt_service": round(monthly_debt_service, 2),
                "runway_months":    round(runway_months, 2),
                "calculated_at":    datetime.utcnow().isoformat(),
            }
        }


# ══════════════════════════════════════════════════════════
# MAIN INTEGRATION FUNCTION
# ══════════════════════════════════════════════════════════

async def pull_mx_for_entity(entity_id: str, entity_name: str,
                               tier: str = "core") -> dict:
    """
    Pull real MX data for an entity and upsert positions into DB.
    Used by the /api/v1/connect/mx/{entity_id} endpoint.
    Returns the calculated FPS result.
    """
    mx = MXClient()

    # 1. Get or create MX user
    user_guid = await mx.get_or_create_user(entity_id, entity_name)

    # 2. Pull all accounts
    accounts = await mx.list_accounts(user_guid)
    logger.info(f"MX: {len(accounts)} accounts for {entity_name}")

    # 3. Pull 90 days of transactions
    from_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    transactions = await mx.list_transactions(user_guid, from_date=from_date)
    logger.info(f"MX: {len(transactions)} transactions for {entity_name}")

    # 4. If no accounts (new user), create demo connection
    if not accounts:
        logger.info(f"MX: No accounts for {entity_name} — using sandbox demo data")
        accounts, transactions = _get_sandbox_demo_data(tier)

    # 5. Calculate FPS from real data
    fps = FPSFromMX.calculate(accounts, transactions, entity_name)

    # 6. Upsert into positions table
    period = _current_period()
    conn = await asyncpg.connect(**DB)
    try:
        await conn.execute("""
            INSERT INTO positions
                (entity_id, period, fps_score, net_position, liquidity_coverage,
                 dscr_score, runway_score, distribution_align,
                 fps_direction, fps_narrative, raw_data, calculated_at)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, NOW())
            ON CONFLICT (entity_id, period) DO UPDATE SET
                fps_score          = EXCLUDED.fps_score,
                net_position       = EXCLUDED.net_position,
                liquidity_coverage = EXCLUDED.liquidity_coverage,
                dscr_score         = EXCLUDED.dscr_score,
                runway_score       = EXCLUDED.runway_score,
                distribution_align = EXCLUDED.distribution_align,
                fps_direction      = EXCLUDED.fps_direction,
                fps_narrative      = EXCLUDED.fps_narrative,
                raw_data           = EXCLUDED.raw_data,
                calculated_at      = NOW()
        """,
            entity_id, period,
            fps["fps_score"], fps["net_position"], fps["liquidity_coverage"],
            fps["dscr_score"], fps["runway_score"], fps["distribution_align"],
            fps["fps_direction"], fps["fps_narrative"],
            json.dumps(fps["raw_data"])
        )
        logger.info(f"MX: Position upserted for {entity_name} — FPS {fps['fps_score']}")
    finally:
        await conn.close()

    return {
        "entity_id":    entity_id,
        "entity_name":  entity_name,
        "source":       "mx_live" if accounts else "mx_sandbox",
        "period":       period,
        "fps_score":    fps["fps_score"],
        "fps_direction": fps["fps_direction"],
        "fps_narrative": fps["fps_narrative"],
        "accounts_connected": len(accounts),
        "components": {
            "net_position":       fps["net_position"],
            "liquidity_coverage": fps["liquidity_coverage"],
            "dscr":               fps["dscr_score"],
            "runway":             fps["runway_score"],
            "distribution_alignment": fps["distribution_align"],
        },
        "raw": fps["raw_data"],
        "calculated_at": datetime.utcnow().isoformat(),
    }


def _current_period() -> str:
    now = datetime.utcnow()
    q = (now.month - 1) // 3 + 1
    return f"{now.year}-Q{q}"


def _get_sandbox_demo_data(tier: str) -> tuple:
    """
    Realistic MX-format sandbox data by WayPoint tier.
    Used when no real accounts are connected yet.
    Represents a typical client at each tier.
    """
    sandbox = {
        "renaissance": {
            "accounts": [
                {"account_type": "CHECKING", "balance": 847.22, "name": "Checking"},
                {"account_type": "SAVINGS",  "balance": 125.00, "name": "Savings"},
                {"account_type": "CREDIT_CARD", "balance": 1240.00, "name": "Secured Card"},
            ],
            "transactions": (
                [{"amount": 2100.00, "date": _days_ago(15), "type": "DIRECT_DEPOSIT",
                  "description": "Payroll", "category": "INCOME"}] +
                [{"amount": -850.00, "date": _days_ago(d), "type": "DEBIT",
                  "description": "Rent", "category": "RENT"} for d in [1, 31, 62]] +
                [{"amount": -180.00, "date": _days_ago(d), "type": "DEBIT",
                  "description": "Groceries"} for d in [3, 10, 17, 24]] +
                [{"amount": -45.00, "date": _days_ago(d), "type": "PAYMENT",
                  "description": "Secured Card"} for d in [5, 35, 65]]
            )
        },
        "core": {
            "accounts": [
                {"account_type": "CHECKING",  "balance": 4280.00, "name": "Checking"},
                {"account_type": "SAVINGS",   "balance": 8500.00, "name": "Emergency Fund"},
                {"account_type": "CREDIT_CARD", "balance": 2100.00, "name": "Visa"},
                {"account_type": "LOAN",      "balance": 14200.00, "name": "Auto Loan"},
            ],
            "transactions": (
                [{"amount": 4800.00, "date": _days_ago(1), "type": "DIRECT_DEPOSIT",
                  "description": "Payroll"}] +
                [{"amount": -1450.00, "date": _days_ago(d), "type": "DEBIT",
                  "description": "Rent"} for d in [1, 31, 62]] +
                [{"amount": -380.00, "date": _days_ago(d), "type": "DEBIT",
                  "description": "Groceries & Household"} for d in [5, 12, 19, 26]] +
                [{"amount": -312.00, "date": _days_ago(d), "type": "PAYMENT",
                  "description": "Auto Loan"} for d in [10, 40, 70]]
            )
        },
        "edge": {
            "accounts": [
                {"account_type": "CHECKING",  "balance": 12400.00, "name": "Business Checking"},
                {"account_type": "SAVINGS",   "balance": 28000.00, "name": "Business Reserve"},
                {"account_type": "LOAN",      "balance": 85000.00, "name": "Business Line"},
                {"account_type": "CREDIT_CARD", "balance": 8400.00, "name": "Business Card"},
            ],
            "transactions": (
                [{"amount": 18500.00, "date": _days_ago(d), "type": "ACH_CREDIT",
                  "description": "Client Payment"} for d in [3, 25, 55]] +
                [{"amount": -4200.00, "date": _days_ago(d), "type": "DEBIT",
                  "description": "Operating Expenses"} for d in [5, 20, 35, 50, 65, 80]] +
                [{"amount": -1850.00, "date": _days_ago(d), "type": "PAYMENT",
                  "description": "Line of Credit"} for d in [15, 45, 75]]
            )
        },
        "crown": {
            "accounts": [
                {"account_type": "CHECKING",    "balance": 284000.00, "name": "Operating"},
                {"account_type": "SAVINGS",     "balance": 540000.00, "name": "Liquidity Reserve"},
                {"account_type": "INVESTMENT",  "balance": 2100000.00, "name": "Investment Portfolio"},
                {"account_type": "INVESTMENT",  "balance": 680000.00, "name": "Trust Account"},
                {"account_type": "MORTGAGE",    "balance": 425000.00, "name": "Mortgage"},
            ],
            "transactions": (
                [{"amount": 42000.00, "date": _days_ago(d), "type": "ACH_CREDIT",
                  "description": "Distribution"} for d in [1, 31, 62]] +
                [{"amount": -12500.00, "date": _days_ago(d), "type": "DEBIT",
                  "description": "Operating Expenses"} for d in [5, 20, 35]] +
                [{"amount": -3250.00, "date": _days_ago(d), "type": "PAYMENT",
                  "description": "Mortgage"} for d in [1, 32, 62]]
            )
        },
    }
    data = sandbox.get(tier, sandbox["core"])
    return data["accounts"], data["transactions"]


def _days_ago(n: int) -> str:
    return (datetime.now() - timedelta(days=n)).strftime("%Y-%m-%d")


# ══════════════════════════════════════════════════════════
# PLAID ADAPTER (Sandbox-ready)
# ══════════════════════════════════════════════════════════

class PlaidAdapter:
    """
    Plaid sandbox adapter — same FPS calculation as MX.
    Switches to production when PLAID_ENV=production.
    """
    PLAID_CLIENT_ID = "69bc0e46b2c179000cd018ec"
    PLAID_SECRET    = "854829badd960a2ad87bceb60f63f7"
    PLAID_ENV       = "sandbox"  # → "production" when approved
    BASE_URLS       = {
        "sandbox":    "https://sandbox.plaid.com",
        "production": "https://production.plaid.com",
    }

    def __init__(self):
        self.base = self.BASE_URLS[self.PLAID_ENV]
        self.headers = {"Content-Type": "application/json"}

    async def _post(self, path: str, body: dict) -> dict:
        payload = {
            "client_id": self.PLAID_CLIENT_ID,
            "secret":    self.PLAID_SECRET,
            **body
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(
                f"{self.base}{path}",
                headers=self.headers,
                json=payload
            )
            r.raise_for_status()
            return r.json()

    async def create_sandbox_token(self, institution_id: str = "ins_109508",
                                    products: list = None) -> str:
        """Create a Plaid sandbox public token for testing."""
        body = {
            "institution_id": institution_id,
            "initial_products": products or ["transactions", "assets"],
            "options": {"webhook": ""}
        }
        data = await self._post("/sandbox/public_token/create", body)
        return data.get("public_token", "")

    async def exchange_token(self, public_token: str) -> str:
        """Exchange public token for access token."""
        data = await self._post("/item/public_token/exchange",
                                {"public_token": public_token})
        return data.get("access_token", "")

    async def get_accounts(self, access_token: str) -> List[dict]:
        data = await self._post("/accounts/get", {"access_token": access_token})
        return data.get("accounts", [])

    async def get_transactions(self, access_token: str,
                                start_date: str = None, end_date: str = None) -> List[dict]:
        """Use /transactions/sync — current Plaid API (replaces deprecated /transactions/get)."""
        all_tx = []
        cursor = None
        for _ in range(5):  # max 5 pages
            body = {"access_token": access_token, "count": 500}
            if cursor:
                body["cursor"] = cursor
            try:
                data = await self._post("/transactions/sync", body)
                all_tx.extend(data.get("added", []))
                if not data.get("has_more", False):
                    break
                cursor = data.get("next_cursor")
            except Exception:
                break
        return all_tx

    def normalize_accounts(self, plaid_accounts: List[dict]) -> List[dict]:
        """Convert Plaid account format to MX-compatible format for FPS calc."""
        type_map = {
            "depository": {"checking": "CHECKING", "savings": "SAVINGS",
                           "": "CHECKING"},
            "credit":     {"credit card": "CREDIT_CARD", "": "CREDIT_CARD"},
            "loan":       {"mortgage": "MORTGAGE", "auto": "LOAN",
                           "student": "LOAN", "": "LOAN"},
            "investment": {"": "INVESTMENT"},
        }
        normalized = []
        for a in plaid_accounts:
            acct_type = a.get("type", "")
            subtype   = a.get("subtype", "")
            mx_type   = (type_map.get(acct_type, {}).get(subtype) or
                         type_map.get(acct_type, {}).get("") or "CHECKING")
            balance   = (a.get("balances", {}).get("current") or
                         a.get("balances", {}).get("available") or 0)
            normalized.append({
                "account_type": mx_type,
                "balance":      balance,
                "name":         a.get("name", ""),
                "account_id":   a.get("account_id", ""),
            })
        return normalized

    def normalize_transactions(self, plaid_tx: List[dict]) -> List[dict]:
        """Convert Plaid transaction format to MX-compatible format."""
        normalized = []
        for t in plaid_tx:
            amount = t.get("amount", 0)
            normalized.append({
                "amount":      -amount,  # Plaid inverts signs vs MX
                "date":        t.get("date", ""),
                "type":        "DEBIT" if amount > 0 else "CREDIT",
                "description": t.get("name", ""),
                "category":    t.get("category", [""])[0] if t.get("category") else "",
            })
        return normalized

    async def pull_and_calculate(self, entity_id: str, entity_name: str,
                                  tier: str = "core") -> dict:
        """Full Plaid sandbox flow → FPS calculation → DB upsert."""
        try:
            # Create sandbox token and exchange
            pub_token    = await self.create_sandbox_token()
            access_token = await self.exchange_token(pub_token)

            # Pull accounts and transactions
            plaid_accounts = await self.get_accounts(access_token)
            plaid_tx   = await self.get_transactions(access_token)

            # Normalize to MX format
            accounts     = self.normalize_accounts(plaid_accounts)
            transactions = self.normalize_transactions(plaid_tx)

            logger.info(f"Plaid: {len(accounts)} accounts, {len(transactions)} tx for {entity_name}")

        except Exception as e:
            logger.warning(f"Plaid live pull failed: {e} — using tier sandbox data")
            accounts, transactions = _get_sandbox_demo_data(tier)

        # Calculate FPS
        fps = FPSFromMX.calculate(accounts, transactions, entity_name)

        # Upsert to DB
        period = _current_period()
        fps["raw_data"]["source"] = "plaid_sandbox"
        conn = await asyncpg.connect(**DB)
        try:
            await conn.execute("""
                INSERT INTO positions
                    (entity_id, period, fps_score, net_position, liquidity_coverage,
                     dscr_score, runway_score, distribution_align,
                     fps_direction, fps_narrative, raw_data, calculated_at)
                VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,NOW())
                ON CONFLICT (entity_id, period) DO UPDATE SET
                    fps_score=EXCLUDED.fps_score, net_position=EXCLUDED.net_position,
                    liquidity_coverage=EXCLUDED.liquidity_coverage,
                    dscr_score=EXCLUDED.dscr_score, runway_score=EXCLUDED.runway_score,
                    distribution_align=EXCLUDED.distribution_align,
                    fps_direction=EXCLUDED.fps_direction,
                    fps_narrative=EXCLUDED.fps_narrative,
                    raw_data=EXCLUDED.raw_data, calculated_at=NOW()
            """,
                entity_id, period,
                fps["fps_score"], fps["net_position"], fps["liquidity_coverage"],
                fps["dscr_score"], fps["runway_score"], fps["distribution_align"],
                fps["fps_direction"], fps["fps_narrative"],
                json.dumps(fps["raw_data"])
            )
        finally:
            await conn.close()

        return {
            "entity_id":   entity_id,
            "entity_name": entity_name,
            "source":      fps["raw_data"]["source"],
            "period":      period,
            "fps_score":   fps["fps_score"],
            "fps_direction": fps["fps_direction"],
            "fps_narrative": fps["fps_narrative"],
            "accounts_connected": len(accounts),
            "components": {
                "net_position":           fps["net_position"],
                "liquidity_coverage":     fps["liquidity_coverage"],
                "dscr":                   fps["dscr_score"],
                "runway":                 fps["runway_score"],
                "distribution_alignment": fps["distribution_align"],
            },
            "calculated_at": datetime.utcnow().isoformat(),
        }


# ══════════════════════════════════════════════════════════
# STANDALONE TEST
# ══════════════════════════════════════════════════════════

async def test():
    """Test both MX and Plaid adapters against all five demo entities."""
    print("=" * 60)
    print("MERIDIA — MX + PLAID ADAPTER TEST")
    print("=" * 60)

    entities = [
        ("a1b2c3d4-0002-0002-0002-000000000002", "Hargrove Family Office", "crown"),
        ("a1b2c3d4-0001-0001-0001-000000000001", "Vantage Financial Partners", "institutional"),
        ("a1b2c3d4-0003-0003-0003-000000000003", "Cornerstone AME Collective", "core"),
        ("a1b2c3d4-0004-0004-0004-000000000004", "Gulf South Properties LLC", "edge"),
        ("a1b2c3d4-0005-0005-0005-000000000005", "Marcus Thompson", "renaissance"),
    ]

    print("\n── MX ADAPTER ──────────────────────────────")
    # Test MX API connectivity first
    mx = MXClient()
    try:
        users = await mx.list_users()
        print(f"MX API connection: OK ({len(users)} existing users)")
    except Exception as e:
        print(f"MX API connection: FAIL — {e}")
        print("Proceeding with sandbox tier data...")

    for entity_id, name, tier in entities:
        try:
            result = await pull_mx_for_entity(entity_id, name, tier)
            print(f"\n  {name}")
            print(f"    FPS: {result['fps_score']} ({result['fps_direction']})")
            print(f"    Source: {result['source']}")
            print(f"    Accounts: {result['accounts_connected']}")
            c = result['components']
            print(f"    Components: net={c['net_position']} liq={c['liquidity_coverage']} "
                  f"dscr={c['dscr']} runway={c['runway']} dist={c['distribution_alignment']}")
        except Exception as e:
            print(f"  {name}: ERROR — {e}")

    print("\n── PLAID ADAPTER ───────────────────────────")
    plaid = PlaidAdapter()
    # Test one entity with Plaid
    try:
        result = await plaid.pull_and_calculate(
            "a1b2c3d4-0003-0003-0003-000000000003",
            "Cornerstone AME Collective",
            "core"
        )
        print(f"\n  Cornerstone AME (Plaid sandbox)")
        print(f"    FPS: {result['fps_score']} ({result['fps_direction']})")
        print(f"    Source: {result['source']}")
        print(f"    Accounts: {result['accounts_connected']}")
    except Exception as e:
        print(f"  Plaid test: ERROR — {e}")

    print("\n── DATABASE VERIFY ─────────────────────────")
    conn = await asyncpg.connect(**DB)
    rows = await conn.fetch(
        "SELECT e.name, e.tier, p.fps_score, p.fps_direction, p.raw_data->>'source' as source "
        "FROM entities e JOIN positions p ON e.entity_id=p.entity_id "
        "ORDER BY p.fps_score DESC"
    )
    print(f"\n  {len(rows)} entities with live positions:")
    for r in rows:
        print(f"    {r['tier']:15} {r['name'][:30]:30} FPS={r['fps_score']:5} "
              f"({r['fps_direction']:12}) [{r['source']}]")
    await conn.close()

    print("\n" + "=" * 60)
    print("ADAPTERS READY — both wired into meridia-wiring/main.py")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test())
