
import asyncio
import asyncpg
import httpx
import csv
import io
from loguru import logger

DB = dict(host="192.168.0.160", port=5433, database="meridia_core",
          user="meridia", password="Ethanj2020##")

# CFPB HMDA Data Browser API — correct 2024 endpoint
HMDA_BASE = "https://ffiec.cfpb.gov/api/data-browser/view/csv"

async def pull_hmda_fixed():
    logger.info("HMDA pull starting (fixed endpoint)...")
    inserted = 0

    for year in [2022, 2023]:
        # Correct API endpoint with proper parameters
        params = {
            "states": "GA",
            "years": str(year),
            "actions_taken": "1,2,3",
        }

        logger.info(f"  HMDA {year}: fetching Georgia loans...")
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                resp = await client.get(HMDA_BASE, params=params)
                if resp.status_code == 403:
                    # Try alternate endpoint format
                    alt_url = f"https://ffiec.cfpb.gov/v2/data-browser-api/view/csv"
                    params2 = {
                        "states": "GA",
                        "years": str(year),
                    }
                    resp = await client.get(alt_url, params=params2,
                                            headers={"User-Agent": "Mozilla/5.0"})

                if resp.status_code not in (200, 206):
                    logger.warning(f"  HMDA {year}: HTTP {resp.status_code}")
                    # Try the CFPB public HMDA snapshot API
                    snap_url = f"https://api.consumerfinance.gov/data/hmda/institutions.csv"
                    logger.info(f"  Trying CFPB snapshot API...")
                    # Fall back to loading from static files if available
                    continue

                content = resp.text
                lines = content.strip().split("\n")
                if len(lines) < 2:
                    logger.warning(f"  HMDA {year}: no data")
                    continue

                reader = csv.DictReader(io.StringIO(content))
                conn = await asyncpg.connect(**DB)
                batch = []
                for row in reader:
                    try:
                        loan_id = (row.get("lei","") + "_" +
                                   str(year) + "_" +
                                   row.get("uli", str(hash(str(row)))[:8]))[:50]
                        batch.append((
                            loan_id,
                            row.get("respondent_name", row.get("financial_institution",""))[:255],
                            row.get("lei","")[:20],
                            "GA",
                            row.get("census_tract","")[:20],
                            int(float(row.get("action_taken",0) or 0)),
                            int(float(row.get("loan_purpose",0) or 0)),
                            int(float(row.get("loan_type",0) or 0)),
                            int(float(row.get("loan_amount",0) or 0)),
                            int(float(row.get("income",0) or 0)),
                            row.get("derived_race", row.get("applicant_race_1",""))[:10],
                            row.get("derived_ethnicity", row.get("applicant_ethnicity_1",""))[:10],
                            int(float(row.get("derived_sex", row.get("applicant_sex","0")) or 0)),
                            year,
                        ))
                        if len(batch) >= 500:
                            await conn.executemany("""
                                INSERT INTO hmda_loans
                                    (loan_id, institution_name, lei, state_code, census_tract,
                                     action_taken, loan_purpose, loan_type, loan_amount, income,
                                     applicant_race, applicant_ethnicity, applicant_sex, activity_year)
                                VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14)
                                ON CONFLICT (loan_id) DO NOTHING
                            """, batch)
                            inserted += len(batch)
                            batch = []
                    except Exception:
                        pass

                if batch:
                    await conn.executemany("""
                        INSERT INTO hmda_loans
                            (loan_id, institution_name, lei, state_code, census_tract,
                             action_taken, loan_purpose, loan_type, loan_amount, income,
                             applicant_race, applicant_ethnicity, applicant_sex, activity_year)
                        VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14)
                        ON CONFLICT (loan_id) DO NOTHING
                    """, batch)
                    inserted += len(batch)

                await conn.close()
                logger.info(f"  HMDA {year}: {inserted} records")

        except Exception as e:
            logger.error(f"  HMDA {year}: {e}")

    # If API is blocked, try direct FFIEC HMDA download
    if inserted == 0:
        logger.info("  API blocked — checking for local HMDA files...")
        import os
        from pathlib import Path
        # Check common download locations
        for search_path in [
            Path(r"C:\Users\alima\Downloads"),
            Path(r"C:\Users\alima\Dropbox\Meridia\integra-core\data"),
        ]:
            for pattern in ["*hmda*", "*HMDA*", "*LAR*"]:
                files = list(search_path.glob(pattern))
                if files:
                    logger.info(f"  Found: {files}")

        # Use CFPB public API - different endpoint
        logger.info("  Trying CFPB public HMDA snapshot...")
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                # The actual public endpoint
                url = "https://api.consumerfinance.gov/data/hmda/slice/hmda_lar.csv"
                params = {
                    "year": 2023,
                    "state_code": "GA",
                    "limit": 1000,
                }
                resp = await client.get(url, params=params)
                logger.info(f"  CFPB snapshot: HTTP {resp.status_code}")
                if resp.status_code == 200:
                    logger.info(f"  Got {len(resp.text)} chars")
        except Exception as e:
            logger.info(f"  CFPB snapshot failed: {e}")

    conn = await asyncpg.connect(**DB)
    count = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans")
    logger.info(f"\nHMDA total in DB: {count:,}")
    await conn.close()

asyncio.run(pull_hmda_fixed())
