
import asyncio
import asyncpg
import httpx
import csv
import io
import hashlib
from loguru import logger

DB = dict(host="192.168.0.160", port=5433, database="meridia_core",
          user="meridia", password="Ethanj2020##")

async def pull_hmda():
    logger.info("HMDA pull — unique row IDs...")

    # Clear existing sparse data first
    conn = await asyncpg.connect(**DB)
    await conn.execute("TRUNCATE hmda_loans")
    await conn.close()
    logger.info("Cleared existing HMDA records")

    inserted = 0
    for year in [2023, 2022]:
        url = "https://ffiec.cfpb.gov/v2/data-browser-api/view/csv"
        params = {"states": "GA", "years": str(year)}
        logger.info(f"  HMDA {year}: downloading...")

        try:
            async with httpx.AsyncClient(timeout=300.0, follow_redirects=True,
                                          headers={"User-Agent": "Mozilla/5.0"}) as client:
                resp = await client.get(url, params=params)
                resp.raise_for_status()
                content = resp.text
                logger.info(f"  HMDA {year}: {len(content):,} chars — parsing...")

            reader = csv.DictReader(io.StringIO(content))
            conn = await asyncpg.connect(**DB)
            batch = []
            row_num = 0

            for row in reader:
                try:
                    row_num += 1
                    # Robust unique ID: hash of key fields + row number
                    key = f"{row.get('lei','')}_{year}_{row.get('uli','')}_{row_num}"
                    loan_id = hashlib.md5(key.encode()).hexdigest()[:50]

                    def si(v, max_val=2147483647):
                        try:
                            val = int(float(v)) if v and str(v).strip() not in ('NA','','None','Exempt') else 0
                            return min(val, max_val)  # clamp to int32
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

                    if len(batch) >= 2000:
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
                        if row_num % 100000 == 0:
                            logger.info(f"    {row_num:,} / {inserted:,} inserted...")

                except Exception as e:
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
            logger.info(f"  HMDA {year}: {row_num:,} rows, {inserted:,} cumulative")

        except Exception as e:
            logger.error(f"  HMDA {year} failed: {e}")

    # Final summary
    conn = await asyncpg.connect(**DB)
    total = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans")
    originated = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans WHERE action_taken=1")
    denied = await conn.fetchval("SELECT COUNT(*) FROM hmda_loans WHERE action_taken=3")
    top = await conn.fetch("""
        SELECT institution_name, COUNT(*) as loans
        FROM hmda_loans WHERE action_taken=1 AND institution_name != ''
        GROUP BY institution_name ORDER BY loans DESC LIMIT 8
    """)
    logger.info(f"\nHMDA Final Summary:")
    logger.info(f"  Total records : {total:,}")
    logger.info(f"  Originated    : {originated:,}")
    logger.info(f"  Denied        : {denied:,}")
    logger.info(f"\nTop Georgia lenders:")
    for r in top:
        logger.info(f"  {r['institution_name'][:45]:45} {r['loans']:,}")
    await conn.close()

asyncio.run(pull_hmda())
