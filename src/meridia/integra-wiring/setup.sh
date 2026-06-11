#!/bin/bash
# setup.sh — Meridia System Setup
# Run once on your NAS or workstation
# Usage: bash setup.sh

set -e

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  MERIDIA INTEGRA CORE — SETUP                           ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# ── 1. CHECK PYTHON ───────────────────────────────────────
echo "→ Checking Python version..."
PYTHON=$(python3 --version 2>&1)
echo "  $PYTHON"
if python3 -c "import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)" 2>/dev/null; then
    echo "  ✓ Python 3.11+ confirmed"
else
    echo "  ✗ Python 3.11+ required. Install from python.org"
    exit 1
fi

# ── 2. INSTALL DEPENDENCIES ───────────────────────────────
echo ""
echo "→ Installing Python dependencies..."
pip install -r requirements.txt --quiet
echo "  ✓ Dependencies installed"

# ── 3. ENVIRONMENT FILE ───────────────────────────────────
echo ""
echo "→ Checking environment configuration..."
if [ ! -f ".env" ]; then
    echo "  Creating .env from template..."
    cat > .env << 'EOF'
# Meridia Environment Configuration
# Fill in your actual values

# ── DATABASE (your NAS PostgreSQL) ──
DB_HOST=192.168.1.100
DB_PORT=5432
DB_NAME=meridia
DB_USER=meridia_app
DB_PASS=CHANGE_ME

# ── API KEYS (already configured) ──
FRED_API_KEY=YOUR_FRED_KEY_HERE
CENSUS_API_KEY=YOUR_CENSUS_KEY_HERE

# ── SECURITY ──
SECRET_KEY=GENERATE_A_RANDOM_64_CHAR_STRING_HERE

# ── PATHS ──
FFIEC_DATA_DIR=./data/ffiec
EOF
    echo "  ✓ .env created — EDIT THIS FILE with your real values before continuing"
    echo ""
    echo "  Required values to fill in:"
    echo "    DB_HOST     — your NAS IP address"
    echo "    DB_PASS     — your PostgreSQL password"
    echo "    FRED_API_KEY — from fred.stlouisfed.org/docs/api/api_key.html"
    echo "    CENSUS_API_KEY — from api.census.gov/data/key_signup.html"
    echo ""
    read -p "  Press Enter after editing .env to continue..."
else
    echo "  ✓ .env found"
fi

# ── 4. DATA DIRECTORIES ───────────────────────────────────
echo ""
echo "→ Creating data directories..."
mkdir -p data/ffiec data/hmda data/logs
echo "  ✓ Directories created"

# ── 5. DATABASE ───────────────────────────────────────────
echo ""
echo "→ Setting up PostgreSQL database..."
echo "  You need to run this manually against your NAS PostgreSQL:"
echo ""
echo "    psql -h \$DB_HOST -U postgres -c 'CREATE DATABASE meridia;'"
echo "    psql -h \$DB_HOST -U postgres -c \"CREATE USER meridia_app WITH PASSWORD 'your_password';\""
echo "    psql -h \$DB_HOST -U postgres -c 'GRANT ALL ON DATABASE meridia TO meridia_app;'"
echo "    psql -h \$DB_HOST -U meridia_app -d meridia -f schema.sql"
echo ""
read -p "  Press Enter after database is created and schema.sql has been run..."

# ── 6. TEST DATABASE CONNECTION ───────────────────────────
echo ""
echo "→ Testing database connection..."
python3 -c "
import asyncio
import sys
sys.path.insert(0, '.')
from database import check_connection
result = asyncio.run(check_connection())
sys.exit(0 if result else 1)
" && echo "  ✓ Database connection successful" || {
    echo "  ✗ Database connection failed"
    echo "  Check your .env file DB_HOST, DB_USER, DB_PASS settings"
    exit 1
}

# ── 7. INITIAL DATA PULL ──────────────────────────────────
echo ""
echo "→ Running initial data pull..."
echo "  This will pull FRED, Census, FDIC, and CFPB data."
echo "  FFIEC requires manual download (instructions in README)."
echo "  HMDA may take 5-10 minutes for Georgia."
echo ""
read -p "  Run initial data pull now? (y/n): " run_pull

if [ "$run_pull" = "y" ]; then
    echo "  Pulling FRED..."
    python3 feeds/pull_all.py --source fred
    echo "  Pulling Census ACS..."
    python3 feeds/pull_all.py --source census
    echo "  Pulling FDIC..."
    python3 feeds/pull_all.py --source fdic
    echo "  Pulling CFPB..."
    python3 feeds/pull_all.py --source cfpb
    echo "  ✓ Initial pull complete"
    echo ""
    echo "  Remaining manual steps:"
    echo "  1. Download FFIEC flat file from ffiec.gov/censusapp.htm"
    echo "  2. Save to: ./data/ffiec/georgia_census_flat.csv"
    echo "  3. Run: python3 feeds/pull_all.py --source ffiec"
    echo "  4. Run: python3 feeds/pull_all.py --source hmda"
fi

# ── 8. START API ──────────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  SETUP COMPLETE                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "  Start the API:      python3 main.py"
echo "  API docs:           http://localhost:8000/docs"
echo "  Health check:       http://localhost:8000/health"
echo "  Start scheduler:    python3 scheduler.py"
echo ""
echo "  Test position:      curl http://localhost:8000/api/v1/position/a1b2c3d4-0002-0002-0002-000000000002"
echo "  Test portfolio:     curl http://localhost:8000/api/v1/portfolio/a1b2c3d4-0001-0001-0001-000000000001"
echo ""
