# Aegis Financial Positioning System - Backend API

**Ethical Steward • Dynamic Guidance System • Governed by Design**

This is the backend API server for the Aegis prototype, powering the Financial Positioning System interface with realistic mock data and intelligent scenario modeling.

---

## 🏛️ The Aegis Paradigm

Aegis is built on four core principles:

1. **Stewardship over Extraction** - Multi-party governance, consent-based insights
2. **Clarity over Complexity** - Financial Positioning Score, real-time signals
3. **Governance as Default** - Trust Index, approval cascades, audit trails
4. **Dignity-First Design** - Renaissance pathways, no-judgment re-entry

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the backend directory:**
   ```bash
   cd aegis-backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   python main.py
   ```

4. **Server will start at:**
   ```
   http://localhost:8000
   ```

5. **Access the API documentation:**
   ```
   http://localhost:8000/docs
   ```

---

## 📚 API Documentation

### Core Endpoints

#### Financial Position
- `GET /api/v1/position-grid` - Get the four core position metrics (Liquidity, Net Worth, Obligations, Resilience)
- `GET /api/v1/trust-index` - Get Trust Index score and dimension breakdowns

#### Entities
- `GET /api/v1/entities` - Get all financial entities
- `GET /api/v1/entities/{entity_id}` - Get detailed entity information
- Query params: `?entity_type=Foundation&status=watch`

#### Governance
- `GET /api/v1/governance-alerts` - Get alerts requiring multi-party approval
- `POST /api/v1/governance-alerts/{alert_id}/approve` - Approve an alert

#### Intelligence
- `GET /api/v1/signal-feed` - Get real-time signal feed
- `GET /api/v1/metrics-dashboard` - Get metrics dashboard with trend data

#### Scenario Engine
- `POST /api/v1/scenario-engine` - Run a "what if" scenario
- `GET /api/v1/scenario-engine/presets` - Get pre-configured scenarios

#### Capital Flows
- `GET /api/v1/flow-diagram` - Get capital flow diagram

#### Aletheia (Chat)
- `POST /api/v1/chat` - Send a message to Aletheia, the steward guide

#### Institutional Sandbox
- `GET /api/v1/institutional-sandbox` - Get partner pilot data

#### Renaissance
- `GET /api/v1/renaissance` - Get Renaissance pathway progress
- `POST /api/v1/renaissance/complete-step/{step_id}` - Mark a step complete

#### System
- `GET /api/v1/health` - Health check
- `GET /api/v1/system/modes` - Get available operational modes
- `GET /api/v1/system/stats` - Get system-wide statistics

---

## 🧪 Example API Calls

### Get Position Grid
```bash
curl http://localhost:8000/api/v1/position-grid
```

### Run a Scenario
```bash
curl -X POST http://localhost:8000/api/v1/scenario-engine \
  -H "Content-Type: application/json" \
  -d '{
    "distribution_rate_change": 20,
    "market_shock": -15,
    "foundation_corpus_addition": 500
  }'
```

### Chat with Aletheia
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is my current Trust Index?",
    "context": {}
  }'
```

### Get Governance Alerts
```bash
curl http://localhost:8000/api/v1/governance-alerts?priority=high
```

---

## 🏗️ Architecture

### File Structure

```
aegis-backend/
├── main.py              # FastAPI app initialization, CORS, startup/shutdown
├── api_v1.py            # All API endpoint definitions
├── models.py            # Pydantic data models for request/response validation
├── data_generator.py    # Mock data generation logic
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Key Technologies

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server for running FastAPI
- **Faker** - Generate realistic mock data

---

## 🎯 Scenario Engine

The scenario engine models "what if" scenarios across three parameters:

### Parameters

1. **Distribution Rate Change** (-50% to +50%)
   - Models changes to trust/foundation distribution rates
   - Negative values = reduction, positive = increase

2. **Market Shock** (-40% to +20%)
   - Models market movements and portfolio impacts
   - Negative = downturn, positive = growth

3. **Foundation Corpus Addition** (0 to 2000K)
   - Models adding capital to the foundation
   - In thousands of dollars

### Calculation Logic

The engine calculates impacts on:
- **Trust Index** - Composite score (0-100)
- **Resilience** - Buffer capacity (0-100)
- **Foundation Status** - Healthy, Watch, or Alert

Example impact calculation:
- Increasing distributions reduces Trust Index (more aggressive = lower trust)
- Market downturns reduce resilience significantly
- Adding corpus to foundation improves Trust Index
- Results are constrained to realistic 0-100 ranges

---

## 🧠 Data Models

All API responses use Pydantic models for validation. Key models:

### Position Metrics
```python
class PositionMetric(BaseModel):
    label: str
    value: str
    change_text: str
    change_direction: str
    status: StatusLevel
```

### Trust Index
```python
class TrustIndexResponse(BaseModel):
    overall_score: int  # 0-100
    dimensions: List[TrustDimension]
    trend_direction: TrendDirection
    trend_change: float
```

### Entities
```python
class Entity(BaseModel):
    id: str
    type: EntityType
    name: str
    status: StatusLevel
    metrics: List[EntityMetric]
```

See `models.py` for complete model definitions.

---

## 🔧 Development

### Running in Development Mode

The server runs with auto-reload enabled by default:

```bash
python main.py
```

Any changes to the code will automatically restart the server.

### Testing Endpoints

Use the interactive API documentation at http://localhost:8000/docs to:
- Explore all endpoints
- Test requests with sample data
- View request/response schemas
- Execute API calls directly from the browser

### Adding New Endpoints

1. Define Pydantic models in `models.py`
2. Create data generator function in `data_generator.py`
3. Add endpoint to `api_v1.py`
4. Test via `/docs` interface

---

## 🌐 CORS Configuration

The server is configured to accept requests from:
- `http://localhost:3000`
- `http://localhost:8000`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:8000`
- All origins (`*`) for prototype development

**⚠️ IMPORTANT:** Remove the `*` wildcard in production and specify exact frontend origins.

---

## 📊 Mock Data Generation

All data is generated using intelligent randomization with realistic constraints:

- **Financial values** - Vary within reasonable ranges
- **Status levels** - Distributed realistically (more healthy than alert)
- **Trends** - Show coherent movement over time
- **Entity relationships** - Maintain logical consistency

The `Faker` library is seeded for consistent demo data across server restarts.

---

## 🚦 Health Checks

### Basic Health Check
```bash
curl http://localhost:8000/api/v1/health
```

Returns:
```json
{
  "status": "healthy",
  "version": "1.0.0-beta",
  "timestamp": "2024-01-20T10:00:00Z",
  "services": {
    "database": "connected",
    "cache": "connected",
    "ai_core": "ready"
  }
}
```

---

## 🎨 Integration with Frontend

The frontend (`Index8.html`) can integrate with this API by:

1. **Replace inline mock data with API calls:**
   ```javascript
   // Instead of hardcoded data:
   const positionData = { ... }
   
   // Fetch from API:
   const response = await fetch('http://localhost:8000/api/v1/position-grid');
   const positionData = await response.json();
   ```

2. **Update scenario calculations:**
   ```javascript
   const response = await fetch('http://localhost:8000/api/v1/scenario-engine', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({
       distribution_rate_change: distValue,
       market_shock: marketValue,
       foundation_corpus_addition: corpusValue
     })
   });
   const scenarioResult = await response.json();
   ```

3. **Implement Aletheia chat:**
   ```javascript
   const response = await fetch('http://localhost:8000/api/v1/chat', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({
       message: userMessage,
       context: { current_view: 'dashboard' }
     })
   });
   const chatResponse = await response.json();
   ```

---

## 📝 Next Steps (Phase 2 Preview)

This mock backend will evolve into a production system with:

1. **Database Layer** - PostgreSQL for persistent storage
2. **Live Data Integration** - Plaid/Finicity for real financial data
3. **Multi-Tenant Architecture** - Support multiple organizations/stewards
4. **AI Core Integration** - Council of LLMs for sophisticated reasoning
5. **Authentication & Authorization** - Role-based access control
6. **Audit Trails** - Complete governance logging
7. **Real-time Updates** - WebSocket connections for live data

See the Technical Architecture Document (Phase 2) for full details.

---

## 🛠️ Troubleshooting

### Port Already in Use
If port 8000 is occupied:
```bash
# Find and kill the process
lsof -ti:8000 | xargs kill -9

# Or run on a different port
uvicorn main:app --port 8001
```

### CORS Errors
Ensure the frontend is making requests to:
- `http://localhost:8000` (not HTTPS)
- Correct endpoint paths starting with `/api/v1/`

### Missing Dependencies
```bash
pip install -r requirements.txt --upgrade
```

---

## 📖 Additional Resources

- **FastAPI Documentation:** https://fastapi.tiangolo.com
- **Pydantic Documentation:** https://docs.pydantic.dev
- **Aegis Project Knowledge:** See `/mnt/project/` for full system documentation

---

## 🤝 Support

This is a prototype backend for the Aegis Financial Positioning System. For questions about the architecture, implementation, or next steps, refer to the Technical Architecture Document or contact the Aegis development team.

---

**Built with clarity. Governed by design. Stewarded with care.**
