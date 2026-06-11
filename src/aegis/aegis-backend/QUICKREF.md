# 📋 AEGIS BACKEND - QUICK REFERENCE

## 🚀 Starting the Server

```bash
# 1. Navigate to the folder
cd path/to/aegis-backend

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 3. Start server
python main.py

# You should see: Server starting on http://localhost:8000
```

## 🛑 Stopping the Server

```bash
# Press Ctrl+C in the terminal
```

## 🌐 Quick Test URLs

Open these in your browser while server is running:

| URL | What It Shows |
|-----|---------------|
| `http://localhost:8000` | API root info |
| `http://localhost:8000/docs` | Interactive API docs (BEST!) |
| `http://localhost:8000/manifest` | System manifest |
| `http://localhost:8000/api/v1/health` | Health check |
| `http://localhost:8000/api/v1/position-grid` | Financial position |
| `http://localhost:8000/api/v1/trust-index` | Trust Index score |
| `http://localhost:8000/api/v1/entities` | All entities |

## 🧪 Testing Scenarios

### Using the Interactive Docs (Easiest):
1. Go to `http://localhost:8000/docs`
2. Find "POST /api/v1/scenario-engine"
3. Click "Try it out"
4. Edit the JSON request body
5. Click "Execute"

### Example Scenario Request:
```json
{
  "distribution_rate_change": 20,
  "market_shock": -15,
  "foundation_corpus_addition": 500
}
```

## 📝 Common Commands

```bash
# Check Python version
python --version

# Create virtual environment (first time only)
python -m venv venv

# Install dependencies (first time only)
pip install -r requirements.txt

# List installed packages
pip list

# Update a package
pip install --upgrade fastapi

# Deactivate virtual environment
deactivate
```

## 🆘 Emergency Fixes

```bash
# Server won't start - kill existing process
# Windows: Use Task Manager, end Python processes
# Mac: lsof -ti:8000 | xargs kill -9

# Dependencies broken - reinstall
pip install -r requirements.txt --force-reinstall

# Virtual environment broken - delete and recreate
# Delete the 'venv' folder
python -m venv venv
# Then activate and reinstall dependencies
```

## 📂 File Structure Quick Guide

| File | Purpose |
|------|---------|
| `main.py` | Server startup, CORS, routes |
| `api_v1.py` | All API endpoints |
| `models.py` | Data structures (Pydantic) |
| `data_generator.py` | Mock data creation |
| `requirements.txt` | Dependencies list |
| `venv/` | Virtual environment (don't edit) |

## 🔌 Connecting to Frontend

In your HTML/JavaScript:

```javascript
// Fetch position data
fetch('http://localhost:8000/api/v1/position-grid')
  .then(response => response.json())
  .then(data => console.log(data));

// Post scenario
fetch('http://localhost:8000/api/v1/scenario-engine', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    distribution_rate_change: 20,
    market_shock: 0,
    foundation_corpus_addition: 0
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## ✅ Daily Workflow

```bash
# Morning: Start server
cd aegis-backend
venv\Scripts\activate    # or source venv/bin/activate on Mac
python main.py

# Work on frontend/testing
# Server runs in background

# Evening: Stop server
# Ctrl+C in terminal
```

## 🎯 Endpoints Cheat Sheet

| Method | Endpoint | Returns |
|--------|----------|---------|
| GET | `/api/v1/position-grid` | 4 position metrics |
| GET | `/api/v1/trust-index` | Trust Index + dimensions |
| GET | `/api/v1/entities` | All entities |
| GET | `/api/v1/entities/{id}` | Single entity details |
| GET | `/api/v1/governance-alerts` | Governance alerts |
| POST | `/api/v1/governance-alerts/{id}/approve` | Approve alert |
| GET | `/api/v1/signal-feed` | Real-time signals |
| GET | `/api/v1/metrics-dashboard` | Metrics + charts |
| POST | `/api/v1/scenario-engine` | Scenario results |
| GET | `/api/v1/flow-diagram` | Capital flows |
| POST | `/api/v1/chat` | Aletheia response |
| GET | `/api/v1/institutional-sandbox` | Partner data |
| GET | `/api/v1/renaissance` | Renaissance pathway |

## 🐛 Common Errors & Fixes

| Error | Fix |
|-------|-----|
| "Port 8000 in use" | Change port in main.py or kill process |
| "Module not found" | Activate venv, pip install -r requirements.txt |
| "Python not recognized" | Reinstall Python, check PATH |
| "Can't activate venv" | Windows: PowerShell execution policy |
| CORS error in browser | Check server is running on :8000 |

## 🎓 Learning Resources

- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Python Virtual Envs**: https://docs.python.org/3/tutorial/venv.html
- **REST APIs Explained**: https://restfulapi.net/
- **JSON Format**: https://www.json.org/

---

**Pro Tip**: Always keep the interactive docs (`/docs`) open in a browser tab while developing!
