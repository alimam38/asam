"""
Meridiem Data Pipeline — Stage 1 (Full)
========================================
Pulls real federal data for the CRA heat map and Integra Core engine.

9 DATA SOURCES:
  1. FRED API (key required)        — 17 economic indicators for Georgia/Atlanta MSA
  2. GeoFRED Maps API (same key)    — GeoJSON shape files + county-level regional data for map rendering
  3. ALFRED Vintage API (same key)  — Historical revision data for audit-grade positioning
  4. FFIEC Census Flat Files        — 1000+ fields per census tract, distressed/underserved flags
  5. FFIEC Georgia Filter           — Extracts Georgia tracts from national file
  6. FDIC BankFind API (no key)     — Institution financials, branch locations, deposits
  7. CFPB Complaints (no key)       — Consumer complaints by product, company, geography
  8. Census Bureau ACS (key req)    — Tract-level demographics: income, poverty, race, housing
  9. Nasdaq Data Link (optional)    — Supplementary economic datasets

Prerequisites:
    pip install requests pandas --break-system-packages

API Keys Needed:
    FRED (required):  https://fred.stlouisfed.org/docs/api/api_key.html
    Census (free):    https://api.census.gov/data/key_signup.html
    Nasdaq (optional): https://data.nasdaq.com/account/api

Usage:
    Full run (all sources):
    python fred_data_pull.py --fred-key YOUR_FRED --census-key YOUR_CENSUS --nasdaq-key YOUR_NASDAQ
    
    Minimum run (FRED + free sources):
    python fred_data_pull.py --fred-key YOUR_FRED

Output:
    ./data/fred/          — FRED economic indicator CSVs
    ./data/geofred/       — GeoJSON shape files + regional economic data for maps
    ./data/alfred/        — ALFRED vintage revision data
    ./data/ffiec/         — FFIEC Census flat files
    ./data/georgia/       — Georgia-filtered census tracts
    ./data/fdic/          — FDIC institution data, branches, deposits
    ./data/cfpb/          — CFPB consumer complaints
    ./data/census/        — Census ACS tract-level demographics
    ./data/nasdaq/        — Nasdaq Data Link supplementary data
    ./data/manifest.json  — Complete manifest of all downloaded data
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, date
from pathlib import Path

try:
    import requests
    import pandas as pd
except ImportError:
    print("Installing required packages...")
    os.system("pip install requests pandas --break-system-packages")
    import requests
    import pandas as pd


# ── Configuration ────────────────────────────────────────────────────

FRED_BASE = "https://api.stlouisfed.org/fred"
NASDAQ_BASE = "https://data.nasdaq.com/api/v3"

# Georgia FIPS: 13
# Atlanta-Sandy Springs-Roswell MSA: 12060
# Fulton County: 13121
# DeKalb County: 13089

# FRED Series IDs for Georgia / Atlanta MSA economic indicators
FRED_SERIES = {
    # Unemployment
    "GAUR": {
        "name": "Georgia Unemployment Rate",
        "frequency": "monthly",
        "category": "labor",
        "use": "CRA distressed tract criteria, FPS scenario engine"
    },
    "ATLA013URN": {
        "name": "Atlanta MSA Unemployment Rate", 
        "frequency": "monthly",
        "category": "labor",
        "use": "CRA heat map metro-level overlay"
    },
    "LAUCN131210000000003": {
        "name": "Fulton County Unemployment Rate",
        "frequency": "monthly",
        "category": "labor",
        "use": "CRA heat map county-level granularity"
    },
    "LAUCN130890000000003": {
        "name": "DeKalb County Unemployment Rate",
        "frequency": "monthly",
        "category": "labor",
        "use": "CRA heat map county-level granularity"
    },
    
    # Income
    "MEHOINUSGA672N": {
        "name": "Georgia Median Household Income",
        "frequency": "annual",
        "category": "income",
        "use": "FPS position engine income benchmarking"
    },
    "2020RATIO012060": {
        "name": "Atlanta MSA Income Inequality Ratio",
        "frequency": "annual",
        "category": "income",
        "use": "CRA underserved area analysis"
    },
    
    # Housing
    "ATNHPIUS12060Q": {
        "name": "Atlanta MSA House Price Index",
        "frequency": "quarterly",
        "category": "housing",
        "use": "FPS scenario engine real estate position"
    },
    "GANSAHOSMEDLISTPRI": {
        "name": "Georgia Median Listing Price (Housing)",
        "frequency": "monthly",
        "category": "housing",
        "use": "CRA heat map housing affordability layer"
    },
    "MORTGAGE30US": {
        "name": "30-Year Fixed Rate Mortgage Average",
        "frequency": "weekly",
        "category": "housing",
        "use": "FPS debt service capacity calculation"
    },
    
    # Banking & Interest Rates
    "FEDFUNDS": {
        "name": "Federal Funds Effective Rate",
        "frequency": "monthly",
        "category": "rates",
        "use": "FPS scenario engine rate shock projection"
    },
    "DGS10": {
        "name": "10-Year Treasury Constant Maturity Rate",
        "frequency": "daily",
        "category": "rates",
        "use": "FPS trust corpus yield benchmarking"
    },
    "DPRIME": {
        "name": "Bank Prime Loan Rate",
        "frequency": "monthly",
        "category": "rates",
        "use": "FPS debt service capacity, Edge lending cost"
    },
    
    # Inflation
    "CPIAUCSL": {
        "name": "Consumer Price Index (All Urban Consumers)",
        "frequency": "monthly",
        "category": "inflation",
        "use": "FPS runway sustainability real-dollar adjustment"
    },
    
    # Banking Access (FDIC-adjacent)
    "GABPPRIVSA": {
        "name": "Georgia All Employees: Financial Activities",
        "frequency": "monthly",
        "category": "banking",
        "use": "CRA heat map financial services employment density"
    },
    
    # Poverty
    "GAPOVRTY": {
        "name": "Georgia Estimated Percent in Poverty",
        "frequency": "annual",
        "category": "poverty",
        "use": "CRA distressed tract criteria"
    },
    
    # GDP
    "GANGSP": {
        "name": "Georgia Total Gross Domestic Product",
        "frequency": "annual",
        "category": "economy",
        "use": "Institutional demo macro context"
    },
    
    # Population
    "GAPOP": {
        "name": "Georgia Resident Population",
        "frequency": "annual",
        "category": "demographics",
        "use": "CRA assessment area sizing"
    },
}

# FFIEC and FDIC download URLs
FFIEC_CENSUS_URL = "https://www.ffiec.gov/census/csv/ffiec_census_file_2024.csv"
FFIEC_CENSUS_DOCS = "https://www.ffiec.gov/census/csv/ffiec_census_file_2024_doc.pdf"
FFIEC_DISTRESSED = "https://www.ffiec.gov/census/csv/distressed_underserved_tracts_2024.csv"
FDIC_SOD_URL = "https://www7.fdic.gov/sod/dynaDownload.asp?baression=ALL&type=csv"  # requires form POST


# ── FRED API Functions ───────────────────────────────────────────────

def fred_get_series(series_id: str, api_key: str, start_date: str = "2020-01-01") -> pd.DataFrame:
    """Pull a single FRED series as a DataFrame."""
    url = f"{FRED_BASE}/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "observation_start": start_date,
        "sort_order": "desc",
    }
    
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    
    if "observations" not in data:
        print(f"  WARNING: No observations found for {series_id}")
        return pd.DataFrame()
    
    df = pd.DataFrame(data["observations"])
    if df.empty:
        return df
    
    # Clean up
    df = df[["date", "value"]].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df = df.sort_values("date").reset_index(drop=True)
    
    return df


def fred_get_series_info(series_id: str, api_key: str) -> dict:
    """Get metadata about a FRED series."""
    url = f"{FRED_BASE}/series"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }
    
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    
    if "seriess" in data and len(data["seriess"]) > 0:
        return data["seriess"][0]
    return {}


def pull_all_fred(api_key: str, output_dir: Path) -> dict:
    """Pull all configured FRED series and save as CSVs."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    
    total = len(FRED_SERIES)
    for i, (series_id, meta) in enumerate(FRED_SERIES.items(), 1):
        print(f"  [{i}/{total}] Pulling {series_id}: {meta['name']}...")
        
        try:
            df = fred_get_series(series_id, api_key)
            
            if df.empty:
                print(f"    -> No data returned. Skipping.")
                manifest[series_id] = {
                    **meta,
                    "status": "no_data",
                    "records": 0,
                }
                continue
            
            # Save CSV
            filename = f"{series_id}.csv"
            filepath = output_dir / filename
            df.to_csv(filepath, index=False)
            
            # Record manifest
            manifest[series_id] = {
                **meta,
                "status": "success",
                "file": str(filepath),
                "records": len(df),
                "date_range": f"{df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}",
                "latest_value": float(df.iloc[-1]["value"]),
                "latest_date": df.iloc[-1]["date"].strftime("%Y-%m-%d"),
            }
            
            print(f"    -> {len(df)} records ({manifest[series_id]['date_range']})")
            print(f"    -> Latest: {manifest[series_id]['latest_value']} ({manifest[series_id]['latest_date']})")
            
        except Exception as e:
            print(f"    -> ERROR: {e}")
            manifest[series_id] = {
                **meta,
                "status": "error",
                "error": str(e),
            }
        
        # Rate limit: FRED allows 120 requests per minute
        time.sleep(0.6)
    
    return manifest


# ── GeoFRED Maps API ─────────────────────────────────────────────────

GEOFRED_BASE = "https://api.stlouisfed.org/geofred"

# Regional series groups for county-level mapping
GEOFRED_SERIES = {
    "unemployment_rate": {
        "series_group": "882",
        "region_type": "county",
        "units": "Percent",
        "frequency": "a",
        "season": "NSA",
        "description": "Unemployment Rate by County",
        "use": "CRA heat map primary economic layer",
    },
    "per_capita_income": {
        "series_group": "882",
        "region_type": "county", 
        "units": "Dollars",
        "frequency": "a",
        "season": "NSA",
        "description": "Per Capita Personal Income by County",
        "use": "CRA heat map income layer",
    },
    "resident_population": {
        "series_group": "1223",
        "region_type": "county",
        "units": "Thousands of Persons",
        "frequency": "a",
        "season": "NSA",
        "description": "Resident Population by County",
        "use": "CRA assessment area population sizing",
    },
}

# Georgia county FIPS codes for Atlanta MSA
ATLANTA_COUNTY_FIPS = [
    "13121",  # Fulton
    "13089",  # DeKalb
    "13135",  # Gwinnett
    "13067",  # Cobb
    "13063",  # Clayton
    "13097",  # Douglas
    "13113",  # Fayette
    "13151",  # Henry
    "13247",  # Rockdale
    "13057",  # Cherokee
    "13085",  # Dawson
    "13117",  # Forsyth
    "13217",  # Newton
    "13297",  # Walton
    "13013",  # Barrow
    "13045",  # Carroll
    "13077",  # Coweta
    "13149",  # Heard
    "13159",  # Jasper
    "13195",  # Madison
    "13199",  # Meriwether
    "13211",  # Morgan
    "13227",  # Pickens
    "13231",  # Pike
    "13255",  # Spalding
]


def pull_geofred_maps(api_key: str, output_dir: Path) -> dict:
    """Pull GeoFRED regional data and shape files for Atlanta MSA mapping."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    
    # 1. Pull shape files (GeoJSON county boundaries)
    print("  Pulling GeoFRED county shape files (GeoJSON)...")
    try:
        url = f"{GEOFRED_BASE}/shapes/file"
        params = {"shape": "county", "api_key": api_key}
        resp = requests.get(url, params=params, timeout=120)
        resp.raise_for_status()
        
        geojson = resp.json()
        filepath = output_dir / "county_shapes.geojson"
        with open(filepath, "w") as f:
            json.dump(geojson, f)
        
        size_mb = filepath.stat().st_size / (1024 * 1024)
        manifest["county_shapes"] = {
            "description": "GeoJSON county boundary shapes for US map rendering",
            "use": "CRA heat map geographic rendering — draw actual county boundaries",
            "status": "success",
            "file": str(filepath),
            "size_mb": round(size_mb, 2),
            "format": "GeoJSON",
        }
        print(f"    -> Downloaded: {size_mb:.2f} MB")
    except Exception as e:
        print(f"    -> ERROR: {e}")
        manifest["county_shapes"] = {"description": "County GeoJSON shapes", "status": "error", "error": str(e)}
    
    time.sleep(0.5)
    
    # 2. Pull state shape file for Georgia outline
    print("  Pulling GeoFRED state shape files (GeoJSON)...")
    try:
        url = f"{GEOFRED_BASE}/shapes/file"
        params = {"shape": "state", "api_key": api_key}
        resp = requests.get(url, params=params, timeout=60)
        resp.raise_for_status()
        
        geojson = resp.json()
        filepath = output_dir / "state_shapes.geojson"
        with open(filepath, "w") as f:
            json.dump(geojson, f)
        
        manifest["state_shapes"] = {
            "description": "GeoJSON state boundary shapes",
            "use": "State-level map rendering for institutional view",
            "status": "success",
            "file": str(filepath),
            "format": "GeoJSON",
        }
        print(f"    -> Downloaded")
    except Exception as e:
        print(f"    -> ERROR: {e}")
        manifest["state_shapes"] = {"description": "State GeoJSON shapes", "status": "error", "error": str(e)}
    
    time.sleep(0.5)
    
    # 3. Pull MSA shape file
    print("  Pulling GeoFRED MSA shape files (GeoJSON)...")
    try:
        url = f"{GEOFRED_BASE}/shapes/file"
        params = {"shape": "msa", "api_key": api_key}
        resp = requests.get(url, params=params, timeout=60)
        resp.raise_for_status()
        
        geojson = resp.json()
        filepath = output_dir / "msa_shapes.geojson"
        with open(filepath, "w") as f:
            json.dump(geojson, f)
        
        manifest["msa_shapes"] = {
            "description": "GeoJSON MSA boundary shapes",
            "use": "Metro area map rendering for CRA assessment areas",
            "status": "success",
            "file": str(filepath),
            "format": "GeoJSON",
        }
        print(f"    -> Downloaded")
    except Exception as e:
        print(f"    -> ERROR: {e}")
        manifest["msa_shapes"] = {"description": "MSA GeoJSON shapes", "status": "error", "error": str(e)}
    
    time.sleep(0.5)
    
    # 4. Pull regional economic data by county (for map coloring)
    for key, config in GEOFRED_SERIES.items():
        print(f"  Pulling GeoFRED regional data: {config['description']}...")
        try:
            url = f"{GEOFRED_BASE}/regional/data"
            params = {
                "api_key": api_key,
                "series_group": config["series_group"],
                "region_type": config["region_type"],
                "units": config["units"],
                "frequency": config["frequency"],
                "season": config["season"],
                "file_type": "json",
            }
            resp = requests.get(url, params=params, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            
            filepath = output_dir / f"regional_{key}.json"
            with open(filepath, "w") as f:
                json.dump(data, f, indent=2)
            
            # Count regions in response
            meta_data = data.get("meta", {})
            region_count = len(data.get("data", {}))
            
            manifest[f"regional_{key}"] = {
                "description": config["description"],
                "use": config["use"],
                "status": "success",
                "file": str(filepath),
                "region_type": config["region_type"],
                "regions": region_count,
                "format": "JSON (GeoFRED regional)",
            }
            print(f"    -> {region_count} regions")
        except Exception as e:
            print(f"    -> ERROR: {e}")
            manifest[f"regional_{key}"] = {
                "description": config["description"],
                "status": "error",
                "error": str(e),
            }
        
        time.sleep(0.6)
    
    return manifest


# ── ALFRED Vintage Data ──────────────────────────────────────────────

# Key series where vintage matters for audit-grade positioning
ALFRED_SERIES = [
    "GAUR",       # Georgia Unemployment — revised regularly
    "CPIAUCSL",   # CPI — revised
    "FEDFUNDS",   # Fed Funds — policy decisions made on the data available at the time
    "GANGSP",     # Georgia GDP — heavily revised
]


def pull_alfred_vintages(api_key: str, output_dir: Path) -> dict:
    """Pull ALFRED vintage data for audit-grade historical positioning.
    
    ALFRED tracks every revision of economic data, answering:
    'What was known when this governance decision was made?'
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    
    for series_id in ALFRED_SERIES:
        print(f"  Pulling ALFRED vintages for {series_id}...")
        
        try:
            # Get vintage dates (when revisions were published)
            url = f"{FRED_BASE}/series/vintagedates"
            params = {
                "series_id": series_id,
                "api_key": api_key,
                "file_type": "json",
            }
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            
            vintage_dates = data.get("vintage_dates", [])
            
            if not vintage_dates:
                print(f"    -> No vintage dates found")
                manifest[f"alfred_{series_id}"] = {
                    "series_id": series_id,
                    "status": "no_vintages",
                }
                continue
            
            # Pull last 12 vintages (roughly 1 year of revisions)
            recent_vintages = vintage_dates[-12:]
            
            all_vintage_data = []
            for vdate in recent_vintages:
                obs_url = f"{FRED_BASE}/series/observations"
                obs_params = {
                    "series_id": series_id,
                    "api_key": api_key,
                    "file_type": "json",
                    "realtime_start": vdate,
                    "realtime_end": vdate,
                    "observation_start": "2023-01-01",
                }
                obs_resp = requests.get(obs_url, params=obs_params, timeout=30)
                if obs_resp.status_code == 200:
                    obs_data = obs_resp.json()
                    for obs in obs_data.get("observations", []):
                        all_vintage_data.append({
                            "date": obs["date"],
                            "value": obs["value"],
                            "vintage_date": vdate,
                            "realtime_start": obs.get("realtime_start", ""),
                            "realtime_end": obs.get("realtime_end", ""),
                        })
                time.sleep(0.6)
            
            if all_vintage_data:
                df = pd.DataFrame(all_vintage_data)
                df["value"] = pd.to_numeric(df["value"], errors="coerce")
                filepath = output_dir / f"alfred_{series_id}.csv"
                df.to_csv(filepath, index=False)
                
                manifest[f"alfred_{series_id}"] = {
                    "series_id": series_id,
                    "description": f"ALFRED vintage data for {series_id} — what was known when",
                    "use": "Audit-grade historical positioning: reproduce the data available on any past date",
                    "status": "success",
                    "file": str(filepath),
                    "records": len(df),
                    "vintages": len(recent_vintages),
                    "vintage_range": f"{recent_vintages[0]} to {recent_vintages[-1]}",
                }
                print(f"    -> {len(df)} observations across {len(recent_vintages)} vintages")
            else:
                manifest[f"alfred_{series_id}"] = {
                    "series_id": series_id,
                    "status": "no_data",
                }
                print(f"    -> No vintage observations retrieved")
                
        except Exception as e:
            print(f"    -> ERROR: {e}")
            manifest[f"alfred_{series_id}"] = {
                "series_id": series_id,
                "status": "error",
                "error": str(e),
            }
    
    return manifest


# ── FFIEC Census Download ────────────────────────────────────────────

def download_ffiec(output_dir: Path) -> dict:
    """Download FFIEC Census flat file and distressed/underserved tract list.
    
    NOTE: FFIEC uses bot protection (Cloudflare/403). If automated download
    fails, the script provides manual download instructions.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    
    downloads = {
        "ffiec_census_2024": {
            "url": "https://www.ffiec.gov/census/csv/ffiec_census_file_2024.csv",
            "description": "FFIEC Census Flat File 2024 — 1000+ fields per census tract",
            "use": "CRA heat map foundation: income levels, demographics, distressed/underserved flags",
        },
        "ffiec_distressed_underserved_2024": {
            "url": "https://www.ffiec.gov/census/csv/distressed_underserved_tracts_2024.csv",
            "description": "CRA Distressed and Underserved Tracts 2024",
            "use": "Direct CRA heat map input: which tracts qualify as distressed or underserved",
        },
    }
    
    for key, info in downloads.items():
        filename = f"{key}.csv"
        filepath = output_dir / filename
        print(f"  Downloading {key}...")
        print(f"    URL: {info['url']}")
        
        try:
            # Use browser-like headers to avoid bot protection
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/csv,text/plain,*/*",
            }
            resp = requests.get(info["url"], timeout=120, stream=True, headers=headers)
            
            # Check if we got blocked (403 or HTML instead of CSV)
            content_type = resp.headers.get("Content-Type", "")
            if resp.status_code == 403 or "text/html" in content_type:
                raise Exception(f"Bot protection (HTTP {resp.status_code}). Manual download required.")
            
            resp.raise_for_status()
            
            with open(filepath, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            size_mb = filepath.stat().st_size / (1024 * 1024)
            
            # Try to count records
            try:
                with open(filepath, "r", encoding="latin-1") as f:
                    lines = sum(1 for _ in f) - 1  # minus header
                record_count = lines
            except:
                record_count = "unknown"
            
            manifest[key] = {
                **info,
                "status": "success",
                "file": str(filepath),
                "size_mb": round(size_mb, 2),
                "records": record_count,
            }
            print(f"    -> Downloaded: {size_mb:.2f} MB, {record_count} records")
            
        except Exception as e:
            print(f"    -> AUTOMATED DOWNLOAD BLOCKED: {e}")
            print(f"    -> MANUAL DOWNLOAD REQUIRED:")
            print(f"       1. Open in browser: {info['url']}")
            print(f"       2. Save file as: {filepath}")
            print(f"       3. Re-run with --skip-ffiec to continue")
            manifest[key] = {
                **info,
                "status": "manual_download_required",
                "save_to": str(filepath),
                "instructions": f"Open {info['url']} in browser, save as {filepath}",
            }
    
    # Check if files already exist from manual download
    for key, info in downloads.items():
        filepath = output_dir / f"{key}.csv"
        if filepath.exists() and manifest.get(key, {}).get("status") == "manual_download_required":
            size_mb = filepath.stat().st_size / (1024 * 1024)
            if size_mb > 0.1:  # Not just an HTML error page
                manifest[key]["status"] = "found_existing"
                manifest[key]["size_mb"] = round(size_mb, 2)
                print(f"  Found existing file: {filepath} ({size_mb:.2f} MB)")
    
    return manifest


# ── Filter Georgia Data ──────────────────────────────────────────────

def filter_georgia_tracts(ffiec_dir: Path, output_dir: Path) -> dict:
    """Filter FFIEC census data to Georgia only (FIPS state code 13)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    
    census_file = ffiec_dir / "ffiec_census_2024.csv"
    if not census_file.exists():
        print("  FFIEC census file not found. Skipping Georgia filter.")
        return manifest
    
    print("  Filtering FFIEC census data for Georgia (FIPS 13)...")
    
    try:
        # Read with latin-1 encoding (FFIEC uses it)
        df = pd.read_csv(census_file, encoding="latin-1", low_memory=False)
        
        # Find state column — FFIEC uses various column names
        state_cols = [c for c in df.columns if "state" in c.lower() and "code" in c.lower()]
        if not state_cols:
            # Try numeric: first column is often MSA, second is state
            # FFIEC flat file typically has State Code as column index 1 or named "State Code"
            state_cols = [c for c in df.columns if c.strip().upper() in ["STATE CODE", "STATE", "STFIPS", "MSA/MD STATE CODE"]]
        
        if state_cols:
            state_col = state_cols[0]
            ga = df[df[state_col].astype(str).str.strip().isin(["13", "13.0"])]
        else:
            # Fallback: try first few columns
            print(f"    Columns found: {list(df.columns[:10])}")
            print("    Attempting to identify state column by position...")
            # In standard FFIEC flat file, column index 1 is typically state code
            col = df.columns[1]
            ga = df[df[col].astype(str).str.strip().isin(["13", "13.0"])]
        
        filepath = output_dir / "georgia_census_tracts_2024.csv"
        ga.to_csv(filepath, index=False)
        
        manifest["georgia_census_tracts"] = {
            "description": "Georgia census tracts filtered from FFIEC 2024 flat file",
            "status": "success",
            "file": str(filepath),
            "records": len(ga),
            "total_us_tracts": len(df),
            "georgia_percentage": round(len(ga) / len(df) * 100, 2),
        }
        print(f"    -> {len(ga)} Georgia tracts out of {len(df)} total US tracts ({manifest['georgia_census_tracts']['georgia_percentage']}%)")
        
    except Exception as e:
        print(f"    -> ERROR: {e}")
        manifest["georgia_census_tracts"] = {
            "status": "error",
            "error": str(e),
        }
    
    return manifest


# ── FDIC BankFind API (No Key Required) ──────────────────────────────

FDIC_API_BASE = "https://banks.data.fdic.gov/api"

FDIC_QUERIES = {
    "georgia_institutions": {
        "endpoint": "/financials",
        "description": "Georgia FDIC-insured institution financial data",
        "params": {
            "filters": "STNAME:Georgia",
            "fields": "REPDTE,CERT,INSTNAME,CITY,STNAME,ZIP,ASSET,DEP,DEPDOM,NETINC,LNLSNET,ROA,ROE,INTINC,NITEFLTOT",
            "sort_by": "ASSET",
            "sort_order": "DESC",
            "limit": 10000,
        },
        "use": "Institution financial profiles for CRA heat map overlay",
    },
    "georgia_branches": {
        "endpoint": "/locations",
        "description": "Georgia bank branch locations",
        "params": {
            "filters": "STALP:GA",
            "fields": "CERT,BRNUM,UNINUMBR,INSTNAME,BRSERTYP,STNAME,CITY,STALPBR,ZIPBR,ADDRESBR,CNTYNAMB,BKCLASS,ASSET,DEPSUM,STCNTYBR",
            "sort_by": "DEPSUM",
            "sort_order": "DESC",
            "limit": 10000,
        },
        "use": "Physical branch access mapping for CRA heat map",
    },
}


def pull_fdic_data(output_dir: Path) -> dict:
    """Pull Georgia banking data from FDIC BankFind API (no key required)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    for key, config in FDIC_QUERIES.items():
        endpoint = config["endpoint"]
        params = config["params"].copy()
        desc = config["description"]

        print(f"  Pulling {key}: {desc}...")

        try:
            url = f"{FDIC_API_BASE}{endpoint}"
            resp = requests.get(url, params=params, timeout=60)
            resp.raise_for_status()
            data = resp.json()

            records = data.get("data", [])
            if not records:
                print(f"    -> No records returned")
                manifest[key] = {"description": desc, "use": config["use"], "status": "no_data", "records": 0}
                continue

            flat_records = [rec.get("data", rec) for rec in records]
            df = pd.DataFrame(flat_records)
            filepath = output_dir / f"{key}.csv"
            df.to_csv(filepath, index=False)

            manifest[key] = {
                "description": desc, "use": config["use"], "status": "success",
                "file": str(filepath), "records": len(df), "columns": list(df.columns),
            }
            print(f"    -> {len(df)} records, {len(df.columns)} columns")

        except Exception as e:
            print(f"    -> ERROR: {e}")
            manifest[key] = {"description": desc, "use": config["use"], "status": "error", "error": str(e)}

        time.sleep(0.5)

    # Summary of Deposits
    print(f"  Pulling FDIC Summary of Deposits for Georgia...")
    try:
        url = f"{FDIC_API_BASE}/sod"
        params = {
            "filters": "STALPBR:GA",
            "fields": "YEAR,CERT,BRNUM,UNINUMBR,INSTNAME,ADDRESBR,CITYBR,STALPBR,ZIPBR,CNTYNAMB,STCNTYBR,MSABR,MSANAMB,DEPSUM,DEPSUMBR,ASSET,BKCLASS",
            "sort_by": "DEPSUM", "sort_order": "DESC", "limit": 10000,
        }
        resp = requests.get(url, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        records = data.get("data", [])
        if records:
            flat = [rec.get("data", rec) for rec in records]
            df = pd.DataFrame(flat)
            filepath = output_dir / "georgia_sod.csv"
            df.to_csv(filepath, index=False)
            manifest["georgia_sod"] = {
                "description": "FDIC Summary of Deposits — Georgia branches",
                "use": "Branch-level deposit data for CRA heat map banking access layer",
                "status": "success", "file": str(filepath), "records": len(df),
            }
            print(f"    -> {len(df)} branch records")
        else:
            manifest["georgia_sod"] = {"description": "FDIC SOD — Georgia", "status": "no_data"}
            print(f"    -> No records returned")
    except Exception as e:
        print(f"    -> ERROR: {e}")
        manifest["georgia_sod"] = {"description": "FDIC SOD — Georgia", "status": "error", "error": str(e)}

    return manifest


# ── CFPB Consumer Complaint Database (No Key Required) ───────────────

CFPB_API = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"

def pull_cfpb_complaints(output_dir: Path) -> dict:
    """Pull consumer complaints for Georgia from CFPB public API."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    products = [
        "Checking or savings account",
        "Credit card or prepaid card",
        "Mortgage",
        "Money transfer, virtual currency, or money service",
        "Debt collection",
        "Credit reporting, credit repair services, or other personal consumer reports",
    ]

    all_complaints = []
    for product in products:
        print(f"  Pulling CFPB complaints: {product[:50]}...")
        try:
            params = {
                "field": "all", "state": "GA", "product": product,
                "date_received_min": "2023-01-01", "date_received_max": "2025-12-31",
                "size": 10000, "sort": "created_date_desc", "format": "json", "no_aggs": "true",
            }
            resp = requests.get(CFPB_API, params=params, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            hits = data.get("hits", {}).get("hits", [])
            total = data.get("hits", {}).get("total", {})
            total_count = total.get("value", 0) if isinstance(total, dict) else total
            for hit in hits:
                all_complaints.append(hit.get("_source", {}))
            print(f"    -> {len(hits)} retrieved (total: {total_count})")
        except Exception as e:
            print(f"    -> ERROR: {e}")
        time.sleep(0.5)

    if all_complaints:
        df = pd.DataFrame(all_complaints)
        filepath = output_dir / "georgia_complaints.csv"
        df.to_csv(filepath, index=False)
        companies = len(df["company"].unique()) if "company" in df.columns else 0
        manifest["georgia_complaints"] = {
            "description": "CFPB Consumer Complaints — Georgia, banking products, 2023-2025",
            "use": "Behavioral layer for CRA heat map — where institutions fail customers",
            "status": "success", "file": str(filepath), "records": len(df), "companies": companies,
        }
        print(f"\n  CFPB Summary: {len(df)} complaints across {companies} companies")
    else:
        manifest["georgia_complaints"] = {"description": "CFPB Complaints — Georgia", "status": "no_data"}
        print(f"\n  CFPB Summary: No complaints retrieved")

    return manifest


# ── Census Bureau ACS API ────────────────────────────────────────────

CENSUS_BASE = "https://api.census.gov/data"

ATLANTA_MSA_COUNTIES = {
    "121": "Fulton", "089": "DeKalb", "135": "Gwinnett", "067": "Cobb",
    "063": "Clayton", "097": "Douglas", "113": "Fayette", "151": "Henry", "247": "Rockdale",
}

ACS_VARIABLES = {
    "B19013_001E": "median_household_income",
    "B17001_001E": "total_poverty_determined", "B17001_002E": "total_below_poverty",
    "B15003_001E": "total_education_25plus", "B15003_022E": "bachelors_degree",
    "B23025_001E": "total_employment_16plus", "B23025_002E": "in_labor_force", "B23025_005E": "unemployed",
    "B25077_001E": "median_home_value", "B25064_001E": "median_gross_rent",
    "B25003_001E": "total_occupied_housing", "B25003_002E": "owner_occupied", "B25003_003E": "renter_occupied",
    "B01003_001E": "total_population", "B01002_001E": "median_age",
    "B02001_001E": "total_race", "B02001_002E": "white_alone", "B02001_003E": "black_alone",
    "B02001_005E": "asian_alone", "B03001_003E": "hispanic_or_latino",
    "B28002_001E": "total_internet_hh", "B28002_002E": "with_internet",
}


def pull_census_acs(api_key: str, output_dir: Path) -> dict:
    """Pull ACS 5-year estimates at tract level for Atlanta MSA counties."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    var_string = ",".join(ACS_VARIABLES.keys())
    all_tracts = []

    for county_fips, county_name in ATLANTA_MSA_COUNTIES.items():
        print(f"  Pulling ACS data for {county_name} County (FIPS 13{county_fips})...")
        try:
            url = f"{CENSUS_BASE}/2022/acs/acs5"
            params = {
                "get": f"NAME,{var_string}",
                "for": "tract:*",
                "in": f"state:13&in=county:{county_fips}",
                "key": api_key,
            }
            resp = requests.get(url, params=params, timeout=60)
            if resp.status_code == 200:
                data = resp.json()
                if len(data) > 1:
                    headers = data[0]
                    rows = data[1:]
                    df = pd.DataFrame(rows, columns=headers)
                    df["county_name"] = county_name
                    all_tracts.append(df)
                    print(f"    -> {len(rows)} tracts")
                else:
                    print(f"    -> No tract data")
            else:
                print(f"    -> HTTP {resp.status_code}: {resp.text[:200]}")
        except Exception as e:
            print(f"    -> ERROR: {e}")
        time.sleep(0.5)

    if all_tracts:
        df = pd.concat(all_tracts, ignore_index=True)
        rename_map = {code: name for code, name in ACS_VARIABLES.items()}
        df = df.rename(columns=rename_map)
        for col in rename_map.values():
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Computed fields
        if "total_below_poverty" in df.columns and "total_poverty_determined" in df.columns:
            df["poverty_rate"] = (df["total_below_poverty"] / df["total_poverty_determined"] * 100).round(2)
        if "unemployed" in df.columns and "in_labor_force" in df.columns:
            df["unemployment_rate"] = (df["unemployed"] / df["in_labor_force"] * 100).round(2)
        if "owner_occupied" in df.columns and "total_occupied_housing" in df.columns:
            df["homeownership_rate"] = (df["owner_occupied"] / df["total_occupied_housing"] * 100).round(2)
        if "with_internet" in df.columns and "total_internet_hh" in df.columns:
            df["internet_access_rate"] = (df["with_internet"] / df["total_internet_hh"] * 100).round(2)

        filepath = output_dir / "atlanta_msa_census_tracts.csv"
        df.to_csv(filepath, index=False)
        manifest["atlanta_msa_tracts"] = {
            "description": "ACS 5-Year (2022) — Atlanta MSA census tracts",
            "use": "Tract-level demographics: income, poverty, education, employment, housing, race, internet access",
            "status": "success", "file": str(filepath), "records": len(df),
            "counties": list(ATLANTA_MSA_COUNTIES.values()), "variables": len(ACS_VARIABLES),
            "computed_fields": ["poverty_rate", "unemployment_rate", "homeownership_rate", "internet_access_rate"],
        }
        print(f"\n  Census ACS Summary: {len(df)} tracts across {len(ATLANTA_MSA_COUNTIES)} counties")
    else:
        manifest["atlanta_msa_tracts"] = {"description": "ACS — Atlanta MSA", "status": "no_data"}
        print(f"\n  Census ACS Summary: No data retrieved")

    return manifest


# ── Nasdaq Data Link (Optional) ──────────────────────────────────────

def pull_nasdaq_tables(api_key: str, output_dir: Path) -> dict:
    """Pull available economic tables from Nasdaq Data Link."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    
    # FRED data is also mirrored on Nasdaq Data Link
    # These are the table-based datasets that supplement FRED
    tables_to_try = {
        "FRED/GDP": "US Gross Domestic Product",
        "FRED/UNRATE": "US National Unemployment Rate",
        "FRED/CPIAUCSL": "Consumer Price Index",
        "FRED/FEDFUNDS": "Federal Funds Rate",
    }
    
    for table_code, description in tables_to_try.items():
        print(f"  Trying Nasdaq: {table_code} ({description})...")
        
        try:
            # Nasdaq Data Link time-series API
            url = f"{NASDAQ_BASE}/datasets/{table_code}/data.json"
            params = {
                "api_key": api_key,
                "start_date": "2020-01-01",
                "order": "asc",
            }
            
            resp = requests.get(url, params=params, timeout=30)
            
            if resp.status_code == 200:
                data = resp.json()
                if "dataset_data" in data:
                    cols = data["dataset_data"].get("column_names", [])
                    rows = data["dataset_data"].get("data", [])
                    df = pd.DataFrame(rows, columns=cols)
                    
                    filename = table_code.replace("/", "_") + ".csv"
                    filepath = output_dir / filename
                    df.to_csv(filepath, index=False)
                    
                    manifest[table_code] = {
                        "description": description,
                        "status": "success",
                        "file": str(filepath),
                        "records": len(df),
                    }
                    print(f"    -> {len(df)} records")
                else:
                    manifest[table_code] = {"description": description, "status": "no_data"}
                    print(f"    -> No dataset_data in response")
            elif resp.status_code == 403:
                manifest[table_code] = {"description": description, "status": "premium_required"}
                print(f"    -> Premium subscription required")
            else:
                manifest[table_code] = {"description": description, "status": f"http_{resp.status_code}"}
                print(f"    -> HTTP {resp.status_code}")
                
        except Exception as e:
            manifest[table_code] = {"description": description, "status": "error", "error": str(e)}
            print(f"    -> ERROR: {e}")
        
        time.sleep(0.5)
    
    return manifest


# ── Main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Meridiem Data Pipeline — Stage 1")
    parser.add_argument("--fred-key", required=True, help="FRED API key from fred.stlouisfed.org")
    parser.add_argument("--census-key", default=None, help="Census Bureau API key from api.census.gov")
    parser.add_argument("--nasdaq-key", default=None, help="Optional Nasdaq Data Link API key")
    parser.add_argument("--output-dir", default="./data", help="Output directory (default: ./data)")
    parser.add_argument("--skip-ffiec", action="store_true", help="Skip FFIEC census download (large file)")
    args = parser.parse_args()
    
    base_dir = Path(args.output_dir)
    base_dir.mkdir(parents=True, exist_ok=True)
    
    total_steps = 9
    print("=" * 70)
    print("  MERIDIEM DATA PIPELINE — STAGE 1 (FULL)")
    print("  FRED + GeoFRED Maps + ALFRED + FFIEC + FDIC + CFPB + Census + Nasdaq")
    print("=" * 70)
    print(f"  Output: {base_dir.resolve()}")
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  FRED Key: {'set' if args.fred_key else 'MISSING'}")
    print(f"  Census Key: {'set' if args.census_key else 'not provided (skipping ACS)'}")
    print(f"  Nasdaq Key: {'set' if args.nasdaq_key else 'not provided (skipping)'}")
    print("=" * 70)
    
    full_manifest = {
        "pipeline": "meridiem_stage_1_full",
        "generated_at": datetime.now().isoformat(),
        "sections": {},
    }
    
    # 1. FRED Economic Data
    print(f"\n[1/{total_steps}] PULLING FRED ECONOMIC DATA FOR GEORGIA / ATLANTA MSA")
    print("-" * 50)
    fred_manifest = pull_all_fred(args.fred_key, base_dir / "fred")
    full_manifest["sections"]["fred"] = fred_manifest
    success = sum(1 for v in fred_manifest.values() if v.get("status") == "success")
    print(f"\n  FRED Summary: {success}/{len(FRED_SERIES)} series pulled successfully")
    
    # 2. GeoFRED Maps API (shapes + regional data for map rendering)
    print(f"\n[2/{total_steps}] PULLING GEOFRED MAPS DATA (SHAPES + REGIONAL)")
    print("-" * 50)
    geofred_manifest = pull_geofred_maps(args.fred_key, base_dir / "geofred")
    full_manifest["sections"]["geofred"] = geofred_manifest
    
    # 3. ALFRED Vintage Data (audit-grade historical positioning)
    print(f"\n[3/{total_steps}] PULLING ALFRED VINTAGE DATA (WHAT WAS KNOWN WHEN)")
    print("-" * 50)
    alfred_manifest = pull_alfred_vintages(args.fred_key, base_dir / "alfred")
    full_manifest["sections"]["alfred"] = alfred_manifest
    
    # 4. FFIEC Census
    if not args.skip_ffiec:
        print(f"\n[4/{total_steps}] DOWNLOADING FFIEC CENSUS DATA")
        print("-" * 50)
        ffiec_manifest = download_ffiec(base_dir / "ffiec")
        full_manifest["sections"]["ffiec"] = ffiec_manifest
        
        # 5. Filter Georgia
        print(f"\n[5/{total_steps}] FILTERING GEORGIA CENSUS TRACTS")
        print("-" * 50)
        ga_manifest = filter_georgia_tracts(base_dir / "ffiec", base_dir / "georgia")
        full_manifest["sections"]["georgia_ffiec"] = ga_manifest
    else:
        print(f"\n[4/{total_steps}] SKIPPING FFIEC CENSUS DOWNLOAD (--skip-ffiec)")
        print(f"\n[5/{total_steps}] SKIPPING GEORGIA FILTER")
    
    # 6. FDIC BankFind + Summary of Deposits
    print(f"\n[6/{total_steps}] PULLING FDIC BANKING DATA (NO KEY REQUIRED)")
    print("-" * 50)
    fdic_manifest = pull_fdic_data(base_dir / "fdic")
    full_manifest["sections"]["fdic"] = fdic_manifest
    
    # 7. CFPB Consumer Complaints
    print(f"\n[7/{total_steps}] PULLING CFPB CONSUMER COMPLAINTS (NO KEY REQUIRED)")
    print("-" * 50)
    cfpb_manifest = pull_cfpb_complaints(base_dir / "cfpb")
    full_manifest["sections"]["cfpb"] = cfpb_manifest
    
    # 8. Census Bureau ACS
    if args.census_key:
        print(f"\n[8/{total_steps}] PULLING CENSUS ACS TRACT DATA FOR ATLANTA MSA")
        print("-" * 50)
        census_manifest = pull_census_acs(args.census_key, base_dir / "census")
        full_manifest["sections"]["census_acs"] = census_manifest
    else:
        print(f"\n[8/{total_steps}] SKIPPING CENSUS ACS (no --census-key provided)")
        print("  Get a free key at: https://api.census.gov/data/key_signup.html")
    
    # 9. Nasdaq Data Link (optional)
    if args.nasdaq_key:
        print(f"\n[9/{total_steps}] PULLING NASDAQ DATA LINK (SUPPLEMENTARY)")
        print("-" * 50)
        nasdaq_manifest = pull_nasdaq_tables(args.nasdaq_key, base_dir / "nasdaq")
        full_manifest["sections"]["nasdaq"] = nasdaq_manifest
    else:
        print(f"\n[9/{total_steps}] SKIPPING NASDAQ DATA LINK (no key provided)")
    
    # Write manifest
    manifest_path = base_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(full_manifest, f, indent=2, default=str)
    
    print("\n" + "=" * 70)
    print("  PIPELINE COMPLETE")
    print("=" * 70)
    print(f"  Manifest: {manifest_path}")
    print(f"  Data dir: {base_dir.resolve()}")
    print()
    
    # Print summary
    total_records = 0
    total_files = 0
    print("  FILES CREATED:")
    for section, data in full_manifest["sections"].items():
        for key, info in data.items():
            status = info.get("status", "unknown")
            records = info.get("records", 0)
            if status == "success":
                print(f"    [OK] {info.get('file', key)} ({records} records)")
                total_records += records if isinstance(records, int) else 0
                total_files += 1
            elif status == "manual_download_required":
                print(f"    [!!] {key}: MANUAL DOWNLOAD NEEDED — {info.get('instructions', '')}")
            else:
                print(f"    [--] {key}: {status}")
    
    print(f"\n  TOTALS: {total_files} files, {total_records:,} records")
    print()
    print("  USAGE:")
    print("    Full run (all sources):")
    print("    python fred_data_pull.py --fred-key YOUR_FRED --census-key YOUR_CENSUS --nasdaq-key YOUR_NASDAQ")
    print()
    print("    Minimum run (FRED + free sources only):")
    print("    python fred_data_pull.py --fred-key YOUR_FRED")
    print()
    print("  NEXT STEPS:")
    print("  1. If FFIEC download was blocked, download manually from browser")
    print("  2. Copy ./data/ to NAS: cp -r ./data/ Z:\\meridiem_data\\")
    print("  3. Run: python load_to_postgres.py (next script to build)")
    print("  4. Wire CRA heat map endpoint into Integra Core")
    print()
    
    return full_manifest


if __name__ == "__main__":
    main()
