# feeds/pull_all.py
# ============================================================
# Meridia Feed Layer — All Six Data Sources
# Run individually or via scheduler.py
#
# Usage:
#   python feeds/pull_all.py --source ffiec
#   python feeds/pull_all.py --source hmda
#   python feeds/pull_all.py --source fred
#   python feeds/pull_all.py --source census
#   python feeds/pull_all.py --source fdic
#   python feeds/pull_all.py --source cfpb
#   python feeds/pull_all.py --all
# ============================================================

import asyncio
import argparse
import sys
import os
import csv
import json
from datetime import datetime, date
from pathlib import Path
from typing import List, Dict, Optional

import httpx
import pandas as pd
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import settings

# Async engine for feed scripts
engine = create_async_engine(settings.DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# ══════════════════════════════════════════════════════════
# LOG HELPER
# ══════════════════════════════════════════════════════════

async def log_pull(db: AsyncSession, source: str, status: str,
                   inserted: int = 0, updated: int = 0, error: str = None):
    await db.execute(text("""
        INSERT INTO data_pull_log (source, pull_type, status, records_inserted, records_updated, error_message, completed_at)
        VALUES (:source, 'full', :status, :inserted, :updated, :error, NOW())
    """), {"source": source, "status": status, "inserted": inserted,
           "updated": updated, "error": error})
    await db.commit()

# ══════════════════════════════════════════════════════════
# FRED — Federal Reserve Economic Data
# ══════════════════════════════════════════════════════════

async def pull_fred():
    """
    Pull macro economic series from FRED API.
    API Key configured in config.py
    Series: Fed funds rate, mortgage rate, CPI, unemployment, GDP
    Update cadence: Monthly
    """
    logger.info("FRED pull starting...")
    try:
        from fredapi import Fred
        fred = Fred(api_key=settings.FRED_API_KEY)
    except ImportError:
        logger.error("fredapi not installed. Run: pip install fredapi")
        return

    series_meta = {
        "FEDFUNDS":    ("Federal Funds Rate", "monthly", "Percent"),
        "MORTGAGE30US":("30-Year Fixed Mortgage Rate", "weekly", "Percent"),
        "CPIAUCSL":    ("Consumer Price Index (All Urban)", "monthly", "Index 1982-84=100"),
        "UNRATE":      ("Unemployment Rate", "monthly", "Percent"),
        "GDP":         ("Gross Domestic Product", "quarterly", "Billions of Dollars"),
    }

    inserted = 0
    async with AsyncSessionLocal() as db:
        for series_id, (name, freq, units) in series_meta.items():
            try:
                data = fred.get_series(series_id, observation_start="2022-01-01")
                for obs_date, value in data.dropna().items():
                    if hasattr(obs_date, 'date'):
                        obs_date = obs_date.date()
                    await db.execute(text("""
                        INSERT INTO fred_series (series_id, observation_date, value, series_name, frequency, units)
                        VALUES (:sid, :dt, :val, :name, :freq, :units)
                        ON CONFLICT (series_id, observation_date) DO UPDATE
                        SET value = EXCLUDED.value, updated_at = NOW()
                    """), {"sid": series_id, "dt": obs_date, "val": float(value),
                           "name": name, "freq": freq, "units": units})
                    inserted += 1
                logger.info(f"  FRED {series_id}: {len(data)} observations")
            except Exception as e:
                logger.warning(f"  FRED {series_id} failed: {e}")

        await db.commit()
        await log_pull(db, "fred", "success", inserted=inserted)
    logger.info(f"FRED pull complete: {inserted} records")

# ══════════════════════════════════════════════════════════
# CENSUS ACS — American Community Survey
# ══════════════════════════════════════════════════════════

async def pull_census():
    """
    Pull tract-level demographic data from Census ACS API.
    API Key configured in config.py
    Scope: Georgia (state 13), all tracts
    Variables: median income, poverty rate, population, race
    Update cadence: Annual (5-year ACS)
    """
    logger.info("Census ACS pull starting...")

    STATE_FIPS = "13"   # Georgia FIPS code — used for Census API calls
    STATE_ABBR = "GA"   # State abbreviation — stored in DB to match entity geography_state
    YEAR = settings.CENSUS_YEAR
    BASE_URL = f"https://api.census.gov/data/{YEAR}/acs/acs5"

    variables = [
        "B19013_001E",  # Median household income
        "B17001_002E",  # Population below poverty
        "B01003_001E",  # Total population
        "B02001_002E",  # White alone
        "B02001_003E",  # Black/African American alone
        "NAME",
    ]

    params = {
        "get": ",".join(variables),
        "for": "tract:*",
        "in": f"state:{STATE_FIPS}",
        "key": settings.CENSUS_API_KEY,
    }

    inserted = 0
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            resp = await client.get(BASE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error(f"Census API failed: {e}")
            return

    headers = data[0]
    rows = data[1:]
    logger.info(f"Census: {len(rows)} tracts returned")

    async with AsyncSessionLocal() as db:
        for row in rows:
            record = dict(zip(headers, row))
            state = record.get("state", "")
            county = record.get("county", "")
            tract = record.get("tract", "")
            geoid = f"{state}{county}{tract}"

            try:
                med_income = int(record["B19013_001E"]) if record["B19013_001E"] not in ["-666666666", None] else None
                population = int(record["B01003_001E"]) if record["B01003_001E"] not in ["-666666666", None] else None
                poverty_pop = int(record["B17001_002E"]) if record["B17001_002E"] not in ["-666666666", None] else 0
                white = int(record["B02001_002E"]) if record["B02001_002E"] not in ["-666666666", None] else 0
                black = int(record["B02001_003E"]) if record["B02001_003E"] not in ["-666666666", None] else 0

                poverty_rate = round((poverty_pop / population * 100), 2) if population and population > 0 else None
                pct_minority = round(((population - white) / population * 100), 2) if population and population > 0 else None

                # LMI approximation until FFIEC data loaded
                is_lmi = med_income is not None and med_income < 65000

                await db.execute(text("""
                    INSERT INTO census_tracts
                        (geoid, state_code, county_code, tract_name, median_hh_income,
                         poverty_rate, population, pct_minority, is_lmi, data_year)
                    VALUES (:geoid, :state, :county, :name, :income,
                            :poverty, :pop, :minority, :lmi, :year)
                    ON CONFLICT (geoid) DO UPDATE SET
                        median_hh_income = EXCLUDED.median_hh_income,
                        poverty_rate = EXCLUDED.poverty_rate,
                        population = EXCLUDED.population,
                        pct_minority = EXCLUDED.pct_minority,
                        is_lmi = EXCLUDED.is_lmi,
                        updated_at = NOW()
                """), {
                    "geoid": geoid, "state": STATE_ABBR, "county": county,
                    "name": record.get("NAME", ""), "income": med_income,
                    "poverty": poverty_rate, "pop": population,
                    "minority": pct_minority, "lmi": is_lmi, "year": YEAR
                })
                inserted += 1
            except Exception as e:
                logger.warning(f"  Census tract {geoid} failed: {e}")

        await db.commit()
        await log_pull(db, "census", "success", inserted=inserted)
    logger.info(f"Census pull complete: {inserted} tracts")

# ══════════════════════════════════════════════════════════
# FFIEC — Census Flat Files
# ══════════════════════════════════════════════════════════

async def pull_ffiec():
    """
    Load FFIEC Census Flat Files into census_tracts table.
    Adds distressed/underserved flags and income percentage.

    MANUAL STEP REQUIRED:
    1. Go to: https://www.ffiec.gov/censusapp.htm
    2. Download the Census Flat File for Georgia
    3. Save to: ./data/ffiec/georgia_census_flat.csv
    4. Then run this script

    The FFIEC file enriches what Census ACS provides with the
    official regulatory flags used in CRA examination.
    """
    data_dir = Path(settings.FFIEC_DATA_DIR)
    ffiec_file = data_dir / "georgia_census_flat.csv"

    if not ffiec_file.exists():
        logger.warning(f"""
╔══════════════════════════════════════════════════════════╗
║  FFIEC DATA NOT YET DOWNLOADED                           ║
║                                                          ║
║  1. Go to: https://www.ffiec.gov/censusapp.htm           ║
║  2. Select: Georgia + Atlanta MSA                        ║
║  3. Download: Census Flat File                           ║
║  4. Save to: {str(ffiec_file):<42}║
║  5. Re-run: python feeds/pull_all.py --source ffiec      ║
╚══════════════════════════════════════════════════════════╝
        """)
        return

    logger.info(f"FFIEC: loading {ffiec_file}")

    # FFIEC flat file columns vary by year — key columns:
    # STATEFP, COUNTYFP, TRACTCE, DISTRESSED, UNDERSERVED,
    # TRACTINCOME (income as % of MSA median)
    try:
        df = pd.read_csv(ffiec_file, dtype=str, low_memory=False)
    except Exception as e:
        logger.error(f"Cannot read FFIEC file: {e}")
        return

    # Normalize column names (FFIEC uses various formats across years)
    df.columns = [c.upper().strip() for c in df.columns]

    # Try to identify key columns — FFIEC uses different names across years
    col_map = {}
    for col in df.columns:
        if "STATE" in col and "FP" in col: col_map["state"] = col
        elif "COUNTY" in col and "FP" in col: col_map["county"] = col
        elif "TRACT" in col and ("CE" in col or "CODE" in col): col_map["tract"] = col
        elif "DISTRESS" in col: col_map["distressed"] = col
        elif "UNDERSERV" in col: col_map["underserved"] = col
        elif "INCOME" in col and "PCT" in col: col_map["income_pct"] = col

    logger.info(f"FFIEC columns mapped: {col_map}")

    inserted = 0
    async with AsyncSessionLocal() as db:
        for _, row in df.iterrows():
            try:
                state = str(row.get(col_map.get("state",""), "")).zfill(2)
                county = str(row.get(col_map.get("county",""), "")).zfill(3)
                tract = str(row.get(col_map.get("tract",""), "")).zfill(6)
                geoid = f"{state}{county}{tract}"

                is_distressed = str(row.get(col_map.get("distressed",""), "0")) in ["1", "Y", "YES", "TRUE"]
                is_underserved = str(row.get(col_map.get("underserved",""), "0")) in ["1", "Y", "YES", "TRUE"]

                income_pct_raw = row.get(col_map.get("income_pct",""), None)
                income_pct = float(income_pct_raw) if income_pct_raw and str(income_pct_raw) not in ["", "N/A"] else None
                is_lmi = income_pct is not None and income_pct < 80  # LMI = below 80% of MSA median

                await db.execute(text("""
                    INSERT INTO census_tracts (geoid, state_code, county_code, is_distressed, is_underserved, is_lmi, ffiec_income_pct, data_year)
                    VALUES (:geoid, :state, :county, :dist, :underserv, :lmi, :income_pct, 2024)
                    ON CONFLICT (geoid) DO UPDATE SET
                        is_distressed = EXCLUDED.is_distressed,
                        is_underserved = EXCLUDED.is_underserved,
                        is_lmi = EXCLUDED.is_lmi,
                        ffiec_income_pct = EXCLUDED.ffiec_income_pct,
                        updated_at = NOW()
                """), {"geoid": geoid, "state": state, "county": county,
                       "dist": is_distressed, "underserv": is_underserved,
                       "lmi": is_lmi, "income_pct": income_pct})
                inserted += 1
            except Exception as e:
                logger.debug(f"  FFIEC row failed: {e}")

        await db.commit()
        await log_pull(db, "ffiec", "success", inserted=inserted)
    logger.info(f"FFIEC pull complete: {inserted} tracts updated")

# ══════════════════════════════════════════════════════════
# HMDA — Home Mortgage Disclosure Act
# ══════════════════════════════════════════════════════════

async def pull_hmda():
    """
    Pull HMDA loan-level data from CFPB API.
    Scope: Georgia, 2022-2023
    No API key required.
    Update cadence: Annual
    """
    logger.info("HMDA pull starting...")

    # HMDA Data Browser API
    BASE_URL = "https://ffiec.cfpb.gov/v2/data-browser-api/view/csv"

    inserted = 0
    for year in settings.HMDA_YEARS if hasattr(settings, 'HMDA_YEARS') and settings.HMDA_YEARS else [2022, 2023]:
        params = {
            "states": "GA",
            "years": str(year),
            "actions_taken": "1,2,3",   # originated, approved not accepted, denied
        }

        logger.info(f"  HMDA {year}: fetching Georgia loans...")
        async with httpx.AsyncClient(timeout=120.0) as client:
            try:
                resp = await client.get(BASE_URL, params=params)
                resp.raise_for_status()

                lines = resp.text.strip().split("\n")
                if len(lines) < 2:
                    logger.warning(f"  HMDA {year}: no data returned")
                    continue

                reader = csv.DictReader(lines)
                async with AsyncSessionLocal() as db:
                    batch = []
                    for row in reader:
                        batch.append({
                            "loan_id": row.get("lei","") + "_" + row.get("activity_year","") + "_" + str(hash(str(row)))[:8],
                            "institution_name": row.get("respondent_name", ""),
                            "lei": row.get("lei", ""),
                            "state_code": "GA",
                            "census_tract": row.get("census_tract", ""),
                            "action_taken": int(row.get("action_taken", 0) or 0),
                            "loan_purpose": int(row.get("loan_purpose", 0) or 0),
                            "loan_type": int(row.get("loan_type", 0) or 0),
                            "loan_amount": int(float(row.get("loan_amount", 0) or 0)),
                            "income": int(float(row.get("income", 0) or 0)),
                            "applicant_race": row.get("derived_race", ""),
                            "applicant_ethnicity": row.get("derived_ethnicity", ""),
                            "applicant_sex": int(row.get("derived_sex", 0) or 0),
                            "activity_year": int(row.get("activity_year", year) or year),
                        })

                        if len(batch) >= 500:
                            await _insert_hmda_batch(db, batch)
                            inserted += len(batch)
                            batch = []

                    if batch:
                        await _insert_hmda_batch(db, batch)
                        inserted += len(batch)

                    await db.commit()
                    await log_pull(db, "hmda", "success", inserted=inserted)
                    logger.info(f"  HMDA {year}: {inserted} records inserted")

            except Exception as e:
                logger.error(f"  HMDA {year} failed: {e}")

    logger.info(f"HMDA pull complete: {inserted} total records")

async def _insert_hmda_batch(db: AsyncSession, batch: List[dict]):
    for record in batch:
        try:
            await db.execute(text("""
                INSERT INTO hmda_loans
                    (loan_id, institution_name, lei, state_code, census_tract,
                     action_taken, loan_purpose, loan_type, loan_amount, income,
                     applicant_race, applicant_ethnicity, applicant_sex, activity_year)
                VALUES
                    (:loan_id, :institution_name, :lei, :state_code, :census_tract,
                     :action_taken, :loan_purpose, :loan_type, :loan_amount, :income,
                     :applicant_race, :applicant_ethnicity, :applicant_sex, :activity_year)
                ON CONFLICT (loan_id) DO NOTHING
            """), record)
        except Exception:
            pass  # Skip duplicates silently

# ══════════════════════════════════════════════════════════
# FDIC — Summary of Deposits
# ══════════════════════════════════════════════════════════

async def pull_fdic():
    """
    Pull FDIC branch and deposit data for Georgia.
    No API key required.
    Update cadence: Annual
    """
    logger.info("FDIC pull starting...")

    url = f"{settings.FDIC_API_BASE}/summary"
    params = {
        "filters": "STNAME:Georgia",
        "fields": "NAME,RSSDID,CERT,BRNUM,NAMEBR,CITY,STALP,ZIP,TRACT,UNINAME,DEPSUM",
        "limit": 2000,
        "offset": 0,
        "output": "json",
    }

    inserted = 0
    async with httpx.AsyncClient(timeout=60.0) as client:
        while True:
            try:
                resp = await client.get(url, params=params)
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                logger.error(f"FDIC API failed: {e}")
                break

            records = data.get("data", [])
            if not records:
                break

            async with AsyncSessionLocal() as db:
                for item in records:
                    d = item.get("data", {})
                    await db.execute(text("""
                        INSERT INTO fdic_branches
                            (institution_name, rssd_id, cert, branch_name, city,
                             state_code, zip, census_tract, deposits, data_year)
                        VALUES
                            (:name, :rssd, :cert, :branch, :city,
                             :state, :zip, :tract, :deposits, :year)
                        ON CONFLICT DO NOTHING
                    """), {
                        "name": d.get("NAME", ""),
                        "rssd": d.get("RSSDID"),
                        "cert": d.get("CERT"),
                        "branch": d.get("NAMEBR", ""),
                        "city": d.get("CITY", ""),
                        "state": "GA",
                        "zip": d.get("ZIP", ""),
                        "tract": d.get("TRACT", ""),
                        "deposits": float(d.get("DEPSUM", 0) or 0),
                        "year": 2023,
                    })
                    inserted += 1
                await db.commit()

            total = data.get("meta", {}).get("total", 0)
            params["offset"] += len(records)
            if params["offset"] >= total:
                break
            logger.info(f"  FDIC: {params['offset']}/{total}")

    async with AsyncSessionLocal() as db:
        await log_pull(db, "fdic", "success", inserted=inserted)
    logger.info(f"FDIC pull complete: {inserted} branches")

# ══════════════════════════════════════════════════════════
# CFPB — Consumer Complaint Database
# ══════════════════════════════════════════════════════════

async def pull_cfpb():
    """
    Pull consumer complaints from CFPB for Georgia.
    No API key required. Daily update cycle.
    Used for bilateral risk signals.
    """
    logger.info("CFPB pull starting...")

    url = settings.CFPB_API_BASE
    params = {
        "state": "GA",
        "size": 1000,
        "frm": 0,
        "sort": "created_date_desc",
        "no_aggs": True,
    }

    inserted = 0
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error(f"CFPB API failed: {e}")
            return

    hits = data.get("hits", {}).get("hits", [])
    logger.info(f"CFPB: {len(hits)} complaints returned")

    async with AsyncSessionLocal() as db:
        for hit in hits:
            src = hit.get("_source", {})
            complaint_id = str(hit.get("_id", ""))
            if not complaint_id:
                continue

            date_received_raw = src.get("date_received", None)
            date_received = None
            if date_received_raw:
                try:
                    date_received = datetime.strptime(date_received_raw[:10], "%Y-%m-%d").date()
                except:
                    pass

            try:
                await db.execute(text("""
                    INSERT INTO cfpb_complaints
                        (complaint_id, product, sub_product, issue, company,
                         state_code, zip, submitted_via, date_received,
                         company_response, timely_response, consumer_disputed)
                    VALUES
                        (:id, :product, :sub, :issue, :company,
                         :state, :zip, :via, :date_rec,
                         :response, :timely, :disputed)
                    ON CONFLICT (complaint_id) DO NOTHING
                """), {
                    "id": complaint_id,
                    "product": src.get("product", ""),
                    "sub": src.get("sub_product", ""),
                    "issue": src.get("issue", "")[:255],
                    "company": src.get("company", ""),
                    "state": src.get("state", ""),
                    "zip": src.get("zip_code", "")[:5] if src.get("zip_code") else "",
                    "via": src.get("submitted_via", ""),
                    "date_rec": date_received,
                    "response": src.get("company_response", ""),
                    "timely": src.get("timely", False),
                    "disputed": src.get("consumer_disputed", False),
                })
                inserted += 1
            except Exception as e:
                logger.debug(f"  CFPB record failed: {e}")

        await db.commit()
        await log_pull(db, "cfpb", "success", inserted=inserted)
    logger.info(f"CFPB pull complete: {inserted} complaints")

# ══════════════════════════════════════════════════════════
# RUNNER
# ══════════════════════════════════════════════════════════

SOURCES = {
    "fred":   pull_fred,
    "census": pull_census,
    "ffiec":  pull_ffiec,
    "hmda":   pull_hmda,
    "fdic":   pull_fdic,
    "cfpb":   pull_cfpb,
}

async def run_all():
    """Run all sources in dependency order."""
    logger.info("=== Meridia Full Feed Pull ===")
    # Order matters: census first (creates tracts), ffiec enriches, then hmda references tracts
    for source in ["fred", "census", "ffiec", "hmda", "fdic", "cfpb"]:
        logger.info(f"\n── {source.upper()} ──")
        try:
            await SOURCES[source]()
        except Exception as e:
            logger.error(f"{source} pull failed: {e}")
    logger.info("\n=== Feed Pull Complete ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meridia Feed Layer")
    parser.add_argument("--source", choices=list(SOURCES.keys()), help="Single source to pull")
    parser.add_argument("--all", action="store_true", help="Run all sources")
    args = parser.parse_args()

    if args.all:
        asyncio.run(run_all())
    elif args.source:
        asyncio.run(SOURCES[args.source]())
    else:
        print("Usage: python feeds/pull_all.py --source [fred|census|ffiec|hmda|fdic|cfpb]")
        print("       python feeds/pull_all.py --all")
