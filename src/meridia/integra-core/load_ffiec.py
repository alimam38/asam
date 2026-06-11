"""
FFIEC Census Flat File Loader — 2025
Loads Georgia tracts into meridia_core PostgreSQL

Run: python load_ffiec.py
"""

import csv
import psycopg2
from psycopg2.extras import execute_batch

# -- CONFIG --------------------------------------------
DB_HOST = "192.168.0.160"
DB_PORT = 5433
DB_NAME = "meridia_core"
DB_USER = "meridia"
DB_PASS = "Ethanj2020##"

FFIEC_FILE = r"C:\Users\alima\Downloads\CensusFlatFile2025\CensusFlatFile2025.csv"
TARGET_STATE = "13"   # Georgia
YEAR = 2025

# -- FFIEC 2025 COLUMN POSITIONS -----------------------
# Confirmed from file inspection
COL_YEAR       = 0
COL_MSA        = 1
COL_STATE      = 2
COL_COUNTY     = 3
COL_TRACT      = 4
COL_SMALL_CTY  = 5
COL_SMALL_IND  = 6   # S = small county
COL_DIST_FLAG  = 7   # Y/N distressed
COL_UNDER_FLAG = 8   # D = underserved designation
COL_INC_LEVEL  = 9   # L/M/U/T = low/moderate/upper/middle
COL_MSA_MFI    = 10  # MSA median family income
COL_TRACT_MFI  = 11  # Tract median family income
COL_MFI_PCT    = 12  # Tract MFI as % of MSA
COL_AREA_MFI   = 13  # Area MFI
COL_POPULATION = 14  # Total population

# Income level mapping
INCOME_MAP = {
    'L': 'low',
    'M': 'moderate',
    'U': 'upper',
    'T': 'middle',
    'S': 'unknown',
    'W': 'unknown',
    '': 'unknown'
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS census_tracts (
    geoid           VARCHAR(11) PRIMARY KEY,
    state_code      VARCHAR(2),
    county_code     VARCHAR(3),
    tract_code      VARCHAR(6),
    msa_code        VARCHAR(10),
    income_level    VARCHAR(20),
    mfi_pct         DECIMAL(6,2),
    is_lmi          BOOLEAN DEFAULT FALSE,
    is_distressed   BOOLEAN DEFAULT FALSE,
    is_underserved  BOOLEAN DEFAULT FALSE,
    msa_mfi         INTEGER,
    tract_mfi       INTEGER,
    population      INTEGER,
    data_year       INTEGER DEFAULT 2025,
    updated_at      TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_census_state ON census_tracts(state_code);
CREATE INDEX IF NOT EXISTS idx_census_msa ON census_tracts(msa_code);
CREATE INDEX IF NOT EXISTS idx_census_lmi ON census_tracts(is_lmi);
CREATE INDEX IF NOT EXISTS idx_census_distressed ON census_tracts(is_distressed);
"""

def build_geoid(state, county, tract):
    s = str(state).strip().zfill(2)
    c = str(county).strip().zfill(3)
    t = str(tract).strip().replace('.', '').zfill(6)
    return f"{s}{c}{t}"

def safe_int(val):
    try:
        return int(float(str(val).strip()))
    except:
        return None

def safe_float(val):
    try:
        return float(str(val).strip())
    except:
        return None

def main():
    print("=" * 60)
    print("FFIEC 2025 Georgia Census Tract Loader")
    print("=" * 60)

    # -- Connect ------------------------------------------
    print(f"\nConnecting to {DB_HOST}:{DB_PORT}/{DB_NAME}...")
    try:
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
            user=DB_USER, password=DB_PASS,
            connect_timeout=10
        )
        conn.autocommit = False
        cur = conn.cursor()
        print("OK Connected successfully")
    except Exception as e:
        print(f"FAIL Connection failed: {e}")
        print("\nCheck:")
        print("  - NAS is on and accessible at 192.168.0.160")
        print("  - PostgreSQL container is running in DSM")
        print("  - Port 5432 is open on the NAS firewall")
        return

    # -- Create table -------------------------------------
    print("\nCreating census_tracts table if needed...")
    try:
        cur.execute(CREATE_TABLE_SQL)
        conn.commit()
        print("OK Table ready")
    except Exception as e:
        print(f"FAIL Table creation failed: {e}")
        conn.rollback()
        conn.close()
        return

    # -- Read and load FFIEC file --------------------------
    print(f"\nReading {FFIEC_FILE}")
    print("Filtering to Georgia (state=13)...")

    records = []
    skipped = 0
    total_read = 0

    with open(FFIEC_FILE, 'r', encoding='latin-1') as f:
        reader = csv.reader(f)
        for row in reader:
            total_read += 1
            if len(row) < 15:
                skipped += 1
                continue
            if row[COL_STATE].strip() != TARGET_STATE:
                continue

            try:
                state  = row[COL_STATE].strip()
                county = row[COL_COUNTY].strip()
                tract  = row[COL_TRACT].strip()
                geoid  = build_geoid(state, county, tract)
                msa    = row[COL_MSA].strip()

                inc_raw   = row[COL_INC_LEVEL].strip()
                income_lv = INCOME_MAP.get(inc_raw, 'unknown')
                is_lmi    = inc_raw in ['L', 'M']

                dist_raw  = row[COL_DIST_FLAG].strip()
                is_dist   = dist_raw == 'Y'

                under_raw  = row[COL_UNDER_FLAG].strip()
                is_under   = under_raw == 'Y'

                mfi_pct   = safe_float(row[COL_MFI_PCT])
                # If income level unknown, derive from MFI %
                if inc_raw in ['S', 'T', ''] and mfi_pct is not None:
                    is_lmi = mfi_pct < 80.0
                    if mfi_pct < 50:
                        income_lv = 'low'
                    elif mfi_pct < 80:
                        income_lv = 'moderate'
                    elif mfi_pct < 120:
                        income_lv = 'middle'
                    else:
                        income_lv = 'upper'

                records.append((
                    geoid, state, county, tract, msa,
                    income_lv, mfi_pct, is_lmi,
                    is_dist, is_under,
                    safe_int(row[COL_MSA_MFI]),
                    safe_int(row[COL_TRACT_MFI]),
                    safe_int(row[COL_POPULATION]),
                    YEAR
                ))
            except Exception as e:
                skipped += 1

    print(f"OK Read {total_read:,} total rows")
    print(f"  Georgia tracts found: {len(records):,}")
    print(f"  Skipped: {skipped}")

    if not records:
        print("FAIL No Georgia records found. Check file path.")
        conn.close()
        return

    # -- Insert --------------------------------------------
    print(f"\nLoading {len(records):,} Georgia tracts into census_tracts...")

    UPSERT = """
        INSERT INTO census_tracts
            (geoid, state_code, county_code, tract_code, msa_code,
             income_level, mfi_pct, is_lmi, is_distressed, is_underserved,
             msa_mfi, tract_mfi, population, data_year, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        ON CONFLICT (geoid) DO UPDATE SET
            income_level  = EXCLUDED.income_level,
            mfi_pct       = EXCLUDED.mfi_pct,
            is_lmi        = EXCLUDED.is_lmi,
            is_distressed = EXCLUDED.is_distressed,
            is_underserved = EXCLUDED.is_underserved,
            msa_mfi       = EXCLUDED.msa_mfi,
            tract_mfi     = EXCLUDED.tract_mfi,
            population    = EXCLUDED.population,
            data_year     = EXCLUDED.data_year,
            updated_at    = NOW()
    """

    try:
        execute_batch(cur, UPSERT, records, page_size=500)
        conn.commit()
        print("OK All records loaded")
    except Exception as e:
        print(f"FAIL Load failed: {e}")
        conn.rollback()
        conn.close()
        return

    # -- Verify --------------------------------------------
    cur.execute("SELECT COUNT(*) FROM census_tracts WHERE state_code = '13'")
    count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM census_tracts WHERE state_code = '13' AND is_lmi = TRUE")
    lmi_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM census_tracts WHERE state_code = '13' AND msa_code = '12054'")
    atlanta_count = cur.fetchone()[0]

    print(f"\n{'=' * 60}")
    print("LOAD COMPLETE")
    print(f"{'=' * 60}")
    print(f"  Total Georgia tracts loaded : {count:,}")
    print(f"  LMI tracts (CRA-relevant)   : {lmi_count:,}")
    print(f"  Atlanta MSA (12054) tracts  : {atlanta_count:,}")
    print(f"\nThe CRA heat map is now powered by real FFIEC data.")

    conn.close()

if __name__ == "__main__":
    main()
