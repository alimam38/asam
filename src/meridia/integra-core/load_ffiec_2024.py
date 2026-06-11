
import asyncio
import csv
import asyncpg
from pathlib import Path

DB = dict(host="192.168.0.160", port=5433, database="meridia_core",
          user="meridia", password="Ethanj2020##")

FFIEC_FILE = Path(r"C:\Users\alima\Downloads\CensusFlatFile2024\CensusFlatFile2024\CensusFlatFile2024.csv")

# Column positions confirmed from earlier inspection
# col[0]=year, col[1]=MSA, col[2]=state, col[3]=county, col[4]=tract
# col[6]=income level indicator (S/T), col[7]=distressed(N), col[8]=underserved(D/X)
# col[9]=income level (M=middle,U=upper,L=low,etc), col[12]=MFI%, col[14]=population
# col[11]=tract MFI, col[1]=MSA code

COL_YEAR=0; COL_MSA=1; COL_STATE=2; COL_COUNTY=3; COL_TRACT=4
COL_DIST=7; COL_UNDER=8; COL_INC=9; COL_MFI_PCT=12; COL_MSA_MFI=10
COL_TRACT_MFI=11; COL_POP=14

INCOME_MAP = {'L':'low','M':'moderate','U':'upper','T':'middle',
              'S':'unknown','W':'unknown','':'unknown'}

async def main():
    conn = await asyncpg.connect(**DB)

    ga_rows = []
    total = 0

    with open(FFIEC_FILE, encoding='latin-1') as f:
        reader = csv.reader(f)
        for row in reader:
            total += 1
            if len(row) < 15: continue
            if row[COL_STATE].strip() != '13': continue  # Georgia only

            try:
                state  = row[COL_STATE].strip().zfill(2)
                county = row[COL_COUNTY].strip().zfill(3)
                tract  = row[COL_TRACT].strip().zfill(6)
                geoid  = f"{state}{county}{tract}"
                msa    = row[COL_MSA].strip()

                inc_raw   = row[COL_INC].strip()
                inc_level = INCOME_MAP.get(inc_raw, 'unknown')
                mfi_pct   = float(row[COL_MFI_PCT]) if row[COL_MFI_PCT].strip() else None

                # Derive LMI from MFI % when income level ambiguous
                if inc_raw in ('S','T','','W') and mfi_pct is not None:
                    is_lmi = mfi_pct < 80.0
                    if mfi_pct < 50:     inc_level = 'low'
                    elif mfi_pct < 80:   inc_level = 'moderate'
                    elif mfi_pct < 120:  inc_level = 'middle'
                    else:                inc_level = 'upper'
                else:
                    is_lmi = inc_raw in ('L','M')

                is_dist  = row[COL_DIST].strip()  == 'Y'
                is_under = row[COL_UNDER].strip() == 'Y'

                def si(v):
                    try: return int(float(v)) if v.strip() else None
                    except: return None

                ga_rows.append((
                    geoid, state, county, msa, inc_level, mfi_pct,
                    is_lmi, is_dist, is_under,
                    si(row[COL_MSA_MFI]), si(row[COL_TRACT_MFI]),
                    si(row[COL_POP]), 2024
                ))
            except Exception as e:
                pass

    print(f"Read {total:,} total rows, {len(ga_rows):,} Georgia tracts")

    # Upsert — enriches existing rows with FFIEC flags
    await conn.executemany("""
        INSERT INTO census_tracts
            (geoid, state_code, county_code, msa_code, income_level,
             ffiec_income_pct, is_lmi, is_distressed, is_underserved,
             msa_mfi, tract_mfi, population, data_year)
        VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13)
        ON CONFLICT (geoid) DO UPDATE SET
            income_level     = EXCLUDED.income_level,
            ffiec_income_pct = EXCLUDED.ffiec_income_pct,
            is_lmi           = EXCLUDED.is_lmi,
            is_distressed    = EXCLUDED.is_distressed,
            is_underserved   = EXCLUDED.is_underserved,
            msa_mfi          = EXCLUDED.msa_mfi,
            tract_mfi        = EXCLUDED.tract_mfi,
            population       = EXCLUDED.population,
            data_year        = EXCLUDED.data_year,
            updated_at       = NOW()
    """, ga_rows)

    # Summary
    total_ct  = await conn.fetchval("SELECT COUNT(*) FROM census_tracts WHERE state_code='13'")
    lmi_ct    = await conn.fetchval("SELECT COUNT(*) FROM census_tracts WHERE state_code='13' AND is_lmi=TRUE")
    dist_ct   = await conn.fetchval("SELECT COUNT(*) FROM census_tracts WHERE state_code='13' AND is_distressed=TRUE")
    under_ct  = await conn.fetchval("SELECT COUNT(*) FROM census_tracts WHERE state_code='13' AND is_underserved=TRUE")
    atl_ct    = await conn.fetchval("SELECT COUNT(*) FROM census_tracts WHERE msa_code='12054'")

    print(f"\ncensus_tracts — Georgia:")
    print(f"  Total tracts    : {total_ct:,}")
    print(f"  LMI             : {lmi_ct:,}")
    print(f"  Distressed      : {dist_ct:,}")
    print(f"  Underserved     : {under_ct:,}")
    print(f"  Atlanta MSA     : {atl_ct:,}")
    print(f"\nFFIEC 2024 flags loaded. CRA heat map is live.")

    await conn.close()

asyncio.run(main())
