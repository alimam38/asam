
import asyncio
import csv
from pathlib import Path
from datetime import date

DB_URL = "postgresql+asyncpg://meridia:Ethanj2020##@192.168.0.160:5433/meridia_core"
DATA_DIR = Path(r"C:\Users\alima\Dropbox\Meridia\integra-core\data")

FRED_META = {
    "GAUR":           ("Georgia Unemployment Rate", "monthly", "Percent"),
    "ATLA013URN":     ("Atlanta MSA Unemployment Rate", "monthly", "Percent"),
    "ATNHPIUS12060Q": ("Atlanta MSA House Price Index", "quarterly", "Index"),
    "MORTGAGE30US":   ("30-Year Fixed Rate Mortgage Average", "weekly", "Percent"),
    "FEDFUNDS":       ("Federal Funds Effective Rate", "monthly", "Percent"),
    "DGS10":          ("10-Year Treasury Rate", "daily", "Percent"),
    "DPRIME":         ("Bank Prime Loan Rate", "daily", "Percent"),
    "CPIAUCSL":       ("Consumer Price Index", "monthly", "Index"),
    "GABPPRIVSA":     ("Georgia Financial Activities Employment", "monthly", "Thousands"),
    "GANGSP":         ("Georgia Total GDP", "annual", "Millions"),
    "GAPOP":          ("Georgia Resident Population", "annual", "Thousands"),
}

async def run():
    import asyncpg
    conn = await asyncpg.connect(
        host="192.168.0.160", port=5433, database="meridia_core",
        user="meridia", password="Ethanj2020##"
    )

    # ── FRED ──────────────────────────────────────────────
    print("Loading FRED...")
    total_fred = 0
    for sid, (name, freq, units) in FRED_META.items():
        fp = DATA_DIR / "fred" / f"{sid}.csv"
        if not fp.exists(): print(f"  MISSING {sid}"); continue
        rows = []
        with open(fp, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                try:
                    dt = date.fromisoformat(row['date'][:10])
                    val = float(row['value'])
                    rows.append((sid, dt, val, name, freq, units))
                except: pass
        if rows:
            await conn.executemany("""
                INSERT INTO fred_series (series_id, observation_date, value, series_name, frequency, units)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (series_id, observation_date) DO UPDATE SET value=EXCLUDED.value
            """, rows)
            total_fred += len(rows)
            print(f"  {sid}: {len(rows)}")
    print(f"FRED total: {total_fred}")

    # ── CENSUS ────────────────────────────────────────────
    print("\nLoading Census ACS...")
    fp = DATA_DIR / "census" / "atlanta_msa_census_tracts.csv"
    rows = []
    if fp.exists():
        with open(fp, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                try:
                    state = str(row.get('state','')).zfill(2)
                    county = str(row.get('county','')).zfill(3)
                    tract = str(row.get('tract','')).zfill(6)
                    geoid = f"{state}{county}{tract}"
                    def si(v):
                        try: return int(float(v)) if v and str(v) not in ['nan','','None'] else None
                        except: return None
                    def sf(v):
                        try: return float(v) if v and str(v) not in ['nan','','None'] else None
                        except: return None
                    income = si(row.get('median_household_income'))
                    pop = si(row.get('total_population'))
                    poverty = sf(row.get('poverty_rate'))
                    minority = sf(row.get('pct_minority'))
                    is_lmi = income is not None and income < 65000
                    name = str(row.get('NAME',''))[:100]
                    rows.append((geoid, state, county, name, income, poverty, pop, minority, is_lmi, 2022))
                except: pass
        await conn.executemany("""
            INSERT INTO census_tracts
                (geoid, state_code, county_code, tract_name, median_hh_income,
                 poverty_rate, population, pct_minority, is_lmi, data_year)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
            ON CONFLICT (geoid) DO UPDATE SET
                median_hh_income=EXCLUDED.median_hh_income,
                poverty_rate=EXCLUDED.poverty_rate,
                population=EXCLUDED.population,
                pct_minority=EXCLUDED.pct_minority,
                is_lmi=EXCLUDED.is_lmi,
                updated_at=NOW()
        """, rows)
        print(f"Census: {len(rows)} Atlanta MSA tracts")

    # ── FDIC ──────────────────────────────────────────────
    print("\nLoading FDIC branches...")
    fp = DATA_DIR / "fdic" / "georgia_sod.csv"
    rows = []
    if fp.exists():
        with open(fp, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                try:
                    def si(v):
                        try: return int(float(v)) if v and str(v) not in ['nan','','None'] else None
                        except: return None
                    def sf(v):
                        try: return float(v) if v and str(v) not in ['nan','','None'] else None
                        except: return None
                    rows.append((
                        str(row.get('INSTNAME',''))[:255],
                        si(row.get('RSSDID')), si(row.get('CERT')),
                        str(row.get('NAMEBR',''))[:255],
                        str(row.get('CITY',''))[:100], "GA",
                        str(row.get('ZIP',''))[:10],
                        str(row.get('STCNTYBR','')),
                        sf(row.get('DEPSUMBR') or row.get('DEPSUM')),
                        2023
                    ))
                except: pass
        await conn.executemany("""
            INSERT INTO fdic_branches
                (institution_name, rssd_id, cert, branch_name, city,
                 state_code, zip, census_tract, deposits, data_year)
            VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10)
            ON CONFLICT DO NOTHING
        """, rows)
        print(f"FDIC: {len(rows)} branches")

    # ── SUMMARY ───────────────────────────────────────────
    print("\nDatabase summary:")
    for table in ['fred_series','census_tracts','fdic_branches','entities','positions','relationships']:
        count = await conn.fetchval(f"SELECT COUNT(*) FROM {table}")
        print(f"  {table}: {count:,}")

    await conn.close()
    print("\nDone.")

asyncio.run(run())
