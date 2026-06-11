# Meridia Integra Core — Complete Wiring Package
**Traverse Code Inc. · March 2026**

This package wires the Meridia system end to end. Database schema, six data feed scripts, FastAPI backend connected to PostgreSQL, and instructions to connect the frontends to live endpoints.

---

## What's in this package

```
meridia-wiring/
├── schema.sql          # PostgreSQL schema — run once
├── config.py           # All API keys and connection settings
├── requirements.txt    # Python dependencies
├── database.py         # Async connection pool
├── models.py           # Pydantic + SQLAlchemy models
├── crud.py             # All database read operations
├── main.py             # FastAPI — all endpoints wired to PostgreSQL
├── scheduler.py        # Feed scheduler — all 6 sources on cadence
├── setup.sh            # One-command setup script
├── feeds/
│   └── pull_all.py     # All 6 data source adapters
└── data/
    └── ffiec/          # Place FFIEC flat file here
```

---

## Prerequisites

- Python 3.11+
- PostgreSQL running on NAS (already configured)
- API keys: FRED (active), Census ACS (active)
- No keys needed for: HMDA, FDIC, CFPB, FFIEC

---

## Step 1 — Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 2 — Configure your environment

Copy `.env.example` to `.env` and fill in:

```bash
DB_HOST=192.168.x.x          # Your NAS IP
DB_PORT=5432
DB_NAME=meridia
DB_USER=meridia_app
DB_PASS=your_password

FRED_API_KEY=your_fred_key   # Already have this
CENSUS_API_KEY=your_census_key  # Already have this
SECRET_KEY=generate_random_64_chars
```

---

## Step 3 — Create the database

Connect to your NAS PostgreSQL and run:

```sql
CREATE DATABASE meridia;
CREATE USER meridia_app WITH PASSWORD 'your_password';
GRANT ALL ON DATABASE meridia TO meridia_app;
```

Then load the schema:

```bash
psql -h YOUR_NAS_IP -U meridia_app -d meridia -f schema.sql
```

This creates all tables and seeds the demo entities (Vantage, Hargrove, Marcus, etc.)

---

## Step 4 — Download FFIEC data (manual, one-time)

1. Go to: **https://www.ffiec.gov/censusapp.htm**
2. Select **Census Flat File**
3. Select **Georgia** + **Atlanta-Sandy Springs MSA**
4. Download and save to: `./data/ffiec/georgia_census_flat.csv`

This is the data that powers the CRA heat map. It has the distressed/underserved flags the OCC examiner uses.

---

## Step 5 — Run the initial data pull

```bash
# Run all sources (recommended first time)
python feeds/pull_all.py --all

# Or run individually
python feeds/pull_all.py --source fred       # ~30 seconds
python feeds/pull_all.py --source census     # ~2 minutes (all GA tracts)
python feeds/pull_all.py --source ffiec      # ~1 minute (after download)
python feeds/pull_all.py --source hmda       # ~5-10 minutes (GA loans 2022-23)
python feeds/pull_all.py --source fdic       # ~1 minute
python feeds/pull_all.py --source cfpb       # ~30 seconds
```

---

## Step 6 — Start the API

```bash
python main.py
```

API is live at: **http://localhost:8000**
Interactive docs: **http://localhost:8000/docs**

---

## Step 7 — Start the scheduler (background)

```bash
python scheduler.py
```

Runs all feeds on their cadences automatically:
- FRED: monthly
- Census: annually
- FFIEC: quarterly
- HMDA: annually
- FDIC: annually
- CFPB: daily

---

## API Quick Reference

### Position (FPS) — feeds Index8
```
GET /api/v1/position/{entity_id}
GET /api/v1/position/{entity_id}/history

# Demo entity IDs (seeded in schema.sql):
# Hargrove Family Office (Crown):  a1b2c3d4-0002-0002-0002-000000000002
# Vantage Financial Partners:      a1b2c3d4-0001-0001-0001-000000000001
# Marcus Thompson (Renaissance):   a1b2c3d4-0005-0005-0005-000000000005
```

### Trust Index
```
GET /api/v1/trust-index/{entity_id}
```

### Portfolio — feeds Vantage console
```
GET /api/v1/portfolio/{institution_id}
GET /api/v1/portfolio/{institution_id}/relationships
```

### CRA Heat Map — Andre's requirement
```
GET /api/v1/heatmap/{institution_id}?state_code=GA
```

### Bilateral Risk
```
GET /api/v1/bilateral/{institution_id}
```

### Reports (differentiated by audience)
```
GET /api/v1/reports/{entity_id}/{audience}
# audience: board | technical | regulator | family | governance
```

### Scenario Engine — feeds Index8 sliders
```
POST /api/v1/scenario
{
  "entity_id": "...",
  "scenario_name": "Add $500K liability",
  "adjustments": {
    "net_position_delta": -500000,
    "runway_delta": -5
  }
}
```

### Health
```
GET /health
```

---

## Wiring the Frontends

### Index8 → Live API

Find this in Index8.html and replace the mock data URL:
```javascript
// BEFORE (mock)
const data = MOCK_POSITION_DATA;

// AFTER (live)
const resp = await fetch('http://localhost:8000/api/v1/position/a1b2c3d4-0002-0002-0002-000000000002');
const data = await resp.json();
```

### Vantage → Live API

```javascript
// Portfolio panel
const portfolio = await fetch('http://localhost:8000/api/v1/portfolio/a1b2c3d4-0001-0001-0001-000000000001');

// Heat map
const heatmap = await fetch('http://localhost:8000/api/v1/heatmap/a1b2c3d4-0001-0001-0001-000000000001?state_code=GA');

// Bilateral risk
const bilateral = await fetch('http://localhost:8000/api/v1/bilateral/a1b2c3d4-0001-0001-0001-000000000001');
```

---

## Demo Entity IDs

Seeded in schema.sql for consistent demo use:

| Entity | ID | Tier |
|--------|----|------|
| Vantage Financial Partners | a1b2c3d4-0001-0001-0001-000000000001 | institutional |
| Hargrove Family Office | a1b2c3d4-0002-0002-0002-000000000002 | crown |
| Cornerstone AME Collective | a1b2c3d4-0003-0003-0003-000000000003 | core |
| Gulf South Properties LLC | a1b2c3d4-0004-0004-0004-000000000004 | edge |
| Marcus Thompson | a1b2c3d4-0005-0005-0005-000000000005 | renaissance |

---

## Troubleshooting

**Database connection fails**
- Check NAS IP in .env — run `ping YOUR_NAS_IP` to confirm reachability
- Confirm PostgreSQL container is running in Synology DSM
- Verify port 5432 is not blocked by NAS firewall

**FRED pull fails**
- Verify FRED_API_KEY in .env
- Test at: https://api.stlouisfed.org/fred/series?series_id=FEDFUNDS&api_key=YOUR_KEY&file_type=json

**Census pull returns no data**
- Verify CENSUS_API_KEY in .env
- Test at: https://api.census.gov/data/2022/acs/acs5?get=NAME&for=state:13&key=YOUR_KEY

**HMDA pull is slow**
- Normal — Georgia has ~500K loans per year
- Pull runs in background, will complete in 5-10 minutes

**FFIEC file won't load**
- Check column headers — FFIEC changes them across years
- Script auto-detects column names but logs what it found
- Check: `python feeds/pull_all.py --source ffiec` output for "FFIEC columns mapped"

---

*Meridia · Traverse Code Inc. · March 2026 · Confidential*
