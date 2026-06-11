
import asyncio
import asyncpg
import httpx
import csv
import io
from loguru import logger

DB = dict(host="192.168.0.160", port=5433, database="meridia_core",
          user="meridia", password="Ethanj2020##")

async def pull_hmda():
    logger.info("HMDA pull starting — follow_redirects enabled...")
    inserted = 0

    for year in [2023, 2022]:
        url = "https://ffiec.cfpb.gov/v2/data-browser-api/view/csv"
        params = {"states": "GA", "years": str(year)}
        logger.info(f"  HMDA {year}: downloading Georgia loans...")

        try:
            async with httpx.AsyncClient(
                timeout=300.0,
                follow_redirects=True,
                headers={"User-Agent": "Mozilla/5.0"}
            ) as client:
                resp = await client.get(url, params=params)
                resp.raise_for_status()
                content = resp.text
                logger.info(f"  HMDA {year}: {len(content):,} chars downloaded")

            lines = content.strip().split("\n")
            if len(lines) < 2:
                logger.warning(f"  HMDA {year}: no data rows")
                continue

            logger.info(f"  HMDA {year}: {len(lines)-1:,} loan records")
            reader = csv.DictReader(io.StringIO(content))
            conn = await asyncpg.connect(**DB)

            batch = []
            row_count = 0
            for row in reader:
                try:
                    # Build unique loan ID
                    loan_id = f"{row.get('lei','')}_{year}_{row.get('uli','')}"[:50]
                    if not loan_id.strip('_'):
                        continue

                    def si(v):
                        try: return int(float(v)) if v and str(v).strip() not in ('NA','','None') else 0
                        except: return 0

                    batch.append((
                        loan_id,
                        row.get("respondent_name", "")[:255],
                        row.get("lei", "")[:20],
                        "GA",
                        row.get("census_tract", "")[:20],
                        si(row.get("action_taken")),
                        si(row.get("loan_purpose")),
                        si(row.get("loan_type")),
                        si(row.get("loan_amount")),
                        si(row.get("income")),
                        row.get("derived_race", "")[:10],
                        row.get("derived_ethnicity", "")[:10],
                        si(row.get("derived_sex")),
                        year,
                    ))
                    row_count += 1

                    if len(batch) >= 1000:
                        try:
                            await conn.executemany("""
                                INSERT INTO hmda_loans
                                    (loan_id, institution_name, lei, state_code, census_tract,
                                     action_taken, loan_purpose, loan_type, loan_amount, income,
                                     applicant_race, applicant_ethnicity, applicant_sex, activity_year)
                                VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14)
                                ON CONFLICT (loan_id) DO NOTHING
                            """, batch)
                            inserted += len(batch)
                        except Exception as e:
                            logger.warning(f"  Batch error: {e}")
                        batch = []
                        if row_count % 50000 == 0:
                            logger.info(f"    {row_count:,} rows processed...")

                except Exception:
                    pass

            # Final batch
            if batch:
                try:
                    await conn.executemany("""
                        INSERT INTO hmda_loans
                            (loan_id, institution_name, lei, state_code, census_tract,
                             action_taken, loan_purpose, loan_type, loan_amount, income,
                             applicant_race, applicant_ethnicity, applicant_sex, activity_year)
                        VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14)
                        ON CONFLICT (loan_id) DO NOTHING
                    """, batch)
                    inserted += len(batch)
                except Exception as e:
                    logger.warning(f"  Final batch error: {e}")

            await conn.close()
            logger.info(f"  HMDA {year}: {row_count:,} rows processed, {inserted:,} inserted")

        except Exception as e:
            logger.error(f"  HMDA {year} failed: {e}")

    # Summary
    conn = await asyncpg.connect(**DB)
    total = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans")
    originated = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans WHERE action_taken=1")
    denied = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans WHERE action_taken=3")

    # Top lenders in Georgia by originated loans
    top = await conn.fetch("""
        SELECT institution_name, COUNT(*) as loans, SUM(loan_amount) as volume
        FROM hmda_loans WHERE action_taken=1 AND institution_name != ''
        GROUP BY institution_name ORDER BY loans DESC LIMIT 10
    """)

    logger.info(f"\nHMDA Summary:")
    logger.info(f"  Total records   : {total:,}")
    logger.info(f"  Originated      : {originated:,}")
    logger.info(f"  Denied          : {denied:,}")
    logger.info(f"\nTop Georgia lenders by loan count:")
    for r in top:
        logger.info(f"  {r['institution_name'][:40]:40} {r['loans']:6,} loans")

    await conn.close()
    logger.info("\nHMDA load complete. CRA heat map now has loan-level data.")

asyncio.run(pull_hmda())
