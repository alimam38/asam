#!/usr/bin/env python3
"""
Turner Theological Seminary -- Authorize.Net Reporting / Reconciliation Feed

Pulls settled batches and their transactions from Authorize.Net's
Transaction Details API and writes two CSV files for reconciliation:

  1. Batch summary      -> one row per settled batch  (match to QuickBooks deposits)
  2. Transaction detail -> one row per transaction    (match to Populi payments)

Credentials are read from environment variables and are NEVER stored in this
file. Set them in your shell or OS secret store on the machine that runs this:

  ANET_API_LOGIN_ID     your API Login ID
  ANET_TRANSACTION_KEY  your Transaction Key
  ANET_ENV              "sandbox" (default) or "production"

Usage:
  python tts_authnet_reporting.py --start 2026-02-01 --end 2026-02-28
  python tts_authnet_reporting.py                 # defaults to month-to-date

Requires only the standard library plus `requests`:
  pip install requests
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
from typing import Any

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
ENDPOINTS = {
    "sandbox": "https://apitest.authorize.net/xml/v1/request.api",
    "production": "https://api.authorize.net/xml/v1/request.api",
}

MAX_BATCH_WINDOW_DAYS = 31   # getSettledBatchList range limit per call
PAGE_LIMIT = 1000            # getTransactionList maximum page size
MAX_PAGES = 1000             # safety cap to avoid runaway paging loops
HTTP_TIMEOUT = 30            # seconds
HTTP_RETRIES = 3


def load_config() -> tuple[str, str, dict[str, str]]:
    """Return (environment_name, endpoint_url, merchant_auth) from env vars."""
    try:
        auth = {
            "name": os.environ["ANET_API_LOGIN_ID"],
            "transactionKey": os.environ["ANET_TRANSACTION_KEY"],
        }
    except KeyError as missing:
        sys.exit(
            f"Missing environment variable {missing}. "
            "Set ANET_API_LOGIN_ID and ANET_TRANSACTION_KEY before running."
        )
    env = os.environ.get("ANET_ENV", "sandbox").lower()
    if env not in ENDPOINTS:
        sys.exit(f"ANET_ENV must be 'sandbox' or 'production', got '{env}'.")
    return env, ENDPOINTS[env], auth


# ---------------------------------------------------------------------------
# Transport
# ---------------------------------------------------------------------------
class AnetError(RuntimeError):
    """Raised when Authorize.Net returns a top-level error result."""


def anet_post(endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
    """POST a request object and return the parsed JSON response.

    Handles the two Authorize.Net JSON quirks:
      * the response is prefixed with a UTF-8 BOM that breaks json.loads
        (decoded here with utf-8-sig)
      * merchantAuthentication must be the first key in the request object;
        Python 3.7+ dicts preserve insertion order, so build payloads with it
        first, as the functions below do.
    """
    last_err: Exception | None = None
    data: dict[str, Any] | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        try:
            resp = requests.post(
                endpoint,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=HTTP_TIMEOUT,
            )
            resp.raise_for_status()
            data = json.loads(resp.content.decode("utf-8-sig"))
            break
        except (requests.RequestException, json.JSONDecodeError) as err:
            last_err = err
            if attempt < HTTP_RETRIES:
                time.sleep(2 * attempt)
    if data is None:
        raise AnetError(
            f"Network/parse failure after {HTTP_RETRIES} attempts: {last_err}"
        )

    messages = data.get("messages", {})
    if messages.get("resultCode") != "Ok":
        first = (messages.get("message") or [{}])[0]
        raise AnetError(
            f"{first.get('code', '?')}: {first.get('text', 'Unknown error')}"
        )
    return data


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------
def authenticate_test(endpoint: str, auth: dict[str, str]) -> None:
    """Verify the credentials are valid. Raises AnetError if not."""
    anet_post(endpoint, {"authenticateTestRequest": {"merchantAuthentication": auth}})


def get_settled_batches(
    endpoint: str, auth: dict[str, str], first_dt: dt.datetime, last_dt: dt.datetime
) -> list[dict]:
    """Return settled batches in the range, splitting into <=31-day windows."""
    batches: list[dict] = []
    window_start = first_dt
    while window_start < last_dt:
        window_end = min(
            window_start + dt.timedelta(days=MAX_BATCH_WINDOW_DAYS), last_dt
        )
        payload = {
            "getSettledBatchListRequest": {
                "merchantAuthentication": auth,
                "includeStatistics": True,
                "firstSettlementDate": window_start.strftime("%Y-%m-%dT%H:%M:%S"),
                "lastSettlementDate": window_end.strftime("%Y-%m-%dT%H:%M:%S"),
            }
        }
        data = anet_post(endpoint, payload)
        batches.extend(data.get("batchList", []) or [])
        window_start = window_end
    return batches


def get_transaction_list(
    endpoint: str, auth: dict[str, str], batch_id: str
) -> list[dict]:
    """Return ALL transactions in a settled batch, paging until exhausted."""
    transactions: list[dict] = []
    offset = 1  # Authorize.Net paging offset is the 1-based page number
    for _ in range(MAX_PAGES):
        payload = {
            "getTransactionListRequest": {
                "merchantAuthentication": auth,
                "batchId": str(batch_id),
                "sorting": {"orderBy": "submitTimeUTC", "orderDescending": False},
                "paging": {"limit": PAGE_LIMIT, "offset": offset},
            }
        }
        data = anet_post(endpoint, payload)
        page = data.get("transactions", []) or []
        transactions.extend(page)
        if len(page) < PAGE_LIMIT:  # last (or only) page
            break
        offset += 1
    return transactions


def get_transaction_details(
    endpoint: str, auth: dict[str, str], trans_id: str
) -> dict:
    """Full detail for a single transaction (use for drill-down on exceptions)."""
    data = anet_post(
        endpoint,
        {
            "getTransactionDetailsRequest": {
                "merchantAuthentication": auth,
                "transId": str(trans_id),
            }
        },
    )
    return data.get("transaction", {})


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def _sum_stat(stats: list[dict], field: str) -> float:
    return round(sum(float(s.get(field, 0) or 0) for s in stats), 2)


BATCH_COLUMNS = [
    "batch_id", "settlement_local", "settlement_utc", "settlement_state",
    "charge_count", "charge_amount", "refund_count", "refund_amount",
    "void_count", "decline_count", "error_count",
    "gross_charges_less_refunds", "txn_count_pulled", "txn_settle_sum",
    "variance", "integrity_flag",
]

TXN_COLUMNS = [
    "batch_id", "trans_id", "submit_local", "submit_utc", "status",
    "account_type", "account_number", "settle_amount",
    "first_name", "last_name", "invoice_number", "has_returned_items",
]


def build_reports(
    endpoint: str, auth: dict[str, str], start_dt: dt.datetime, end_dt: dt.datetime
) -> tuple[list[dict], list[dict]]:
    batches = get_settled_batches(endpoint, auth, start_dt, end_dt)
    batch_rows: list[dict] = []
    txn_rows: list[dict] = []

    for b in batches:
        batch_id = b.get("batchId", "")
        stats = b.get("statistics", []) or []
        charge_amount = _sum_stat(stats, "chargeAmount")
        refund_amount = _sum_stat(stats, "refundAmount")
        gross_net = round(charge_amount - refund_amount, 2)

        txns = get_transaction_list(endpoint, auth, batch_id)
        txn_settle_sum = round(
            sum(float(t.get("settleAmount", 0) or 0) for t in txns), 2
        )
        # Cross-check: the sum of per-transaction settleAmount should reconcile
        # to (charges - refunds). A non-zero variance flags a batch to review.
        # NOTE: confirm the refund sign convention against one known batch on
        # first run -- if refunds come back unsigned, refunded batches will
        # show a variance equal to 2x the refund total rather than a real gap.
        variance = round(txn_settle_sum - gross_net, 2)

        batch_rows.append({
            "batch_id": batch_id,
            "settlement_local": b.get("settlementTimeLocal", ""),
            "settlement_utc": b.get("settlementTimeUTC", ""),
            "settlement_state": b.get("settlementState", ""),
            "charge_count": int(_sum_stat(stats, "chargeCount")),
            "charge_amount": charge_amount,
            "refund_count": int(_sum_stat(stats, "refundCount")),
            "refund_amount": refund_amount,
            "void_count": int(_sum_stat(stats, "voidCount")),
            "decline_count": int(_sum_stat(stats, "declineCount")),
            "error_count": int(_sum_stat(stats, "errorCount")),
            "gross_charges_less_refunds": gross_net,
            "txn_count_pulled": len(txns),
            "txn_settle_sum": txn_settle_sum,
            "variance": variance,
            "integrity_flag": "OK" if abs(variance) <= 0.01 else "REVIEW",
        })

        for t in txns:
            txn_rows.append({
                "batch_id": batch_id,
                "trans_id": t.get("transId", ""),
                "submit_local": t.get("submitTimeLocal", ""),
                "submit_utc": t.get("submitTimeUTC", ""),
                "status": t.get("transactionStatus", ""),
                "account_type": t.get("accountType", ""),
                "account_number": t.get("accountNumber", ""),
                "settle_amount": t.get("settleAmount", ""),
                "first_name": t.get("firstName", ""),
                "last_name": t.get("lastName", ""),
                "invoice_number": t.get("invoiceNumber", ""),
                "has_returned_items": t.get("hasReturnedItems", ""),
            })

    return batch_rows, txn_rows


def write_csv(path: str, columns: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    today = dt.date.today()
    parser = argparse.ArgumentParser(
        description="Pull Authorize.Net settled batches and transactions to CSV."
    )
    parser.add_argument(
        "--start", default=today.replace(day=1).isoformat(),
        help="Period start date YYYY-MM-DD (default: first of current month).",
    )
    parser.add_argument(
        "--end", default=today.isoformat(),
        help="Period end date YYYY-MM-DD inclusive (default: today).",
    )
    parser.add_argument(
        "--outdir", default=".",
        help="Directory to write the CSV files into (default: current dir).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        start_date = dt.date.fromisoformat(args.start)
        end_date = dt.date.fromisoformat(args.end)
    except ValueError as err:
        sys.exit(f"Invalid date: {err}")
    if end_date < start_date:
        sys.exit("--end cannot be before --start.")

    start_dt = dt.datetime.combine(start_date, dt.time.min)
    end_dt = dt.datetime.combine(end_date, dt.time.max)

    env, endpoint, auth = load_config()
    print(f"Environment: {env.upper()}")
    if env == "sandbox":
        print("  (sandbox -- this is NOT production data)")
    print(f"Reporting period: {start_date} through {end_date}")

    authenticate_test(endpoint, auth)
    print("Credentials verified.")

    batch_rows, txn_rows = build_reports(endpoint, auth, start_dt, end_dt)

    tag = end_date.isoformat()
    batch_path = os.path.join(args.outdir, f"TTS_AuthNet_Batch_Summary_{tag}.csv")
    txn_path = os.path.join(args.outdir, f"TTS_AuthNet_Transaction_Detail_{tag}.csv")
    write_csv(batch_path, BATCH_COLUMNS, batch_rows)
    write_csv(txn_path, TXN_COLUMNS, txn_rows)

    review = [r for r in batch_rows if r["integrity_flag"] == "REVIEW"]
    total_charges = round(sum(r["charge_amount"] for r in batch_rows), 2)
    total_refunds = round(sum(r["refund_amount"] for r in batch_rows), 2)

    print("-" * 60)
    print(f"Batches:            {len(batch_rows)}")
    print(f"Transactions:       {len(txn_rows)}")
    print(f"Total charges:      {total_charges:,.2f}")
    print(f"Total refunds:      {total_refunds:,.2f}")
    print(f"Batches to review:  {len(review)}")
    if review:
        for r in review:
            print(f"  REVIEW batch {r['batch_id']} "
                  f"({r['settlement_local']}): variance {r['variance']:,.2f}")
    print("-" * 60)
    print(f"Wrote: {batch_path}")
    print(f"Wrote: {txn_path}")


if __name__ == "__main__":
    main()
