# ============================================================
# config.py — Meridia System Configuration
# Copy to config_local.py and fill in your actual values
# Never commit config_local.py to version control
# ============================================================

import os
from dataclasses import dataclass

@dataclass
class Config:
    # ── DATABASE ──────────────────────────────────────────
    # Your NAS PostgreSQL connection
    # Default NAS IP is typically 192.168.x.x — check your DSM
    DB_HOST: str = os.getenv("DB_HOST", "192.168.0.160")
    DB_PORT: int = int(os.getenv("DB_PORT", "5433"))
    DB_NAME: str = os.getenv("DB_NAME", "meridia_core")
    DB_USER: str = os.getenv("DB_USER", "meridia")
    DB_PASS: str = os.getenv("DB_PASS", "Ethanj2020##")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_SYNC(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # ── FRED API ──────────────────────────────────────────
    # Get at: https://fred.stlouisfed.org/docs/api/api_key.html
    FRED_API_KEY: str = os.getenv("FRED_API_KEY", "f0b8d36d1bf405c35820e2ec3e93379f")

    # Fred series to pull (macro context layer)
    FRED_SERIES: list = None
    def __post_init__(self):
        self.FRED_SERIES = [
            "FEDFUNDS",      # Federal funds rate
            "MORTGAGE30US",  # 30-year fixed mortgage rate
            "CPIAUCSL",      # CPI - inflation
            "UNRATE",        # National unemployment rate
            "GDP",           # GDP
            "ATLHOM",        # Atlanta MSA housing index (proxy)
        ]

    # ── CENSUS API ────────────────────────────────────────
    # Get at: https://api.census.gov/data/key_signup.html
    CENSUS_API_KEY: str = os.getenv("CENSUS_API_KEY", "27ccdb0ed92ac87ede38443a31af535ebca4e3b4")

    # ACS 5-year — highest geographic granularity
    CENSUS_YEAR: int = 2022
    CENSUS_DATASET: str = "acs/acs5"

    # Variables to pull per tract
    CENSUS_VARIABLES: list = None
    def __post_init__(self):
        self.FRED_SERIES = [
            "FEDFUNDS", "MORTGAGE30US", "CPIAUCSL", "UNRATE", "GDP"
        ]
        self.CENSUS_VARIABLES = [
            "B19013_001E",  # Median household income
            "B17001_002E",  # Population below poverty level
            "B01003_001E",  # Total population
            "B02001_002E",  # White alone
            "B02001_003E",  # Black or African American alone
            "B25070_010E",  # Gross rent 50%+ of income (housing burden)
        ]

    # ── HMDA / CFPB API ───────────────────────────────────
    # No key required — public API
    HMDA_API_BASE: str = "https://ffiec.cfpb.gov/api/public/reports"
    HMDA_FILING_API: str = "https://ffiec.cfpb.gov/api/filing"
    HMDA_YEARS: list = None

    # ── FDIC API ──────────────────────────────────────────
    # No key required
    FDIC_API_BASE: str = "https://banks.data.fdic.gov/api"

    # ── CFPB Complaints ───────────────────────────────────
    # No key required
    CFPB_API_BASE: str = "https://api.consumerfinance.gov/data/complaints"

    # ── FFIEC ─────────────────────────────────────────────
    # Direct download — no API key
    # Go to: https://www.ffiec.gov/censusapp.htm
    # Download: Census Flat File for your target state/MSA
    FFIEC_DATA_DIR: str = os.getenv("FFIEC_DATA_DIR", "./data/ffiec")

    # ── GEOGRAPHY SCOPE ───────────────────────────────────
    # Demo scope: Georgia + Atlanta MSA
    TARGET_STATES: list = None
    TARGET_MSA: str = "12054"  # Atlanta-Sandy Springs-Roswell MSA FIPS

    # ── API SERVER ────────────────────────────────────────
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True  # Set False in production

    # ── SECURITY ──────────────────────────────────────────
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_THIS_IN_PRODUCTION")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    def __post_init__(self):
        self.FRED_SERIES = [
            "FEDFUNDS", "MORTGAGE30US", "CPIAUCSL", "UNRATE", "GDP"
        ]
        self.CENSUS_VARIABLES = [
            "B19013_001E", "B17001_002E", "B01003_001E",
            "B02001_002E", "B02001_003E", "B25070_010E"
        ]
        self.HMDA_YEARS = [2022, 2023]
        self.TARGET_STATES = ["GA"]

# Singleton
settings = Config()
