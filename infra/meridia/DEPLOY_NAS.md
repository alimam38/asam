# Integra Core — NAS Deployment Guide

## What This Is

Integra Core is the backend API for the WayPoint Financial Positioning System.
It runs as a Docker container on your Synology DS925+ alongside your existing PostgreSQL container.

Once running, Index8.html connects to it and everything comes alive:
Aletheia speaks with real intelligence, reports generate on demand, 
and the guided tour has voice narration.

---

## Prerequisites

- Synology DS925+ NAS (you have this)
- Docker / Container Manager installed on DSM (you have this)
- SSH access to the NAS
- Your Poe API key

---

## Deployment Steps

### 1. Transfer Files to NAS

From your local machine, copy the project folder to the NAS:

```bash
scp -r integra-core/ your-user@NAS-IP:/volume1/docker/integra-core/
```

Or use Synology's File Station to upload the folder to `/volume1/docker/integra-core/`.

The folder should contain:
```
integra-core/
├── main.py
├── api_v1.py
├── models.py
├── data_generator.py
├── aletheia_service.py
├── report_generator.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

### 2. Create the .env File

```bash
ssh your-user@NAS-IP
cd /volume1/docker/integra-core
cp .env.template .env
nano .env
```

Add your Poe API key:
```
POE_API_KEY=EZjOmpLchkbhUocrhRcIhC8-ka1OH_hvQinATIgJuKI
```

### 3. Build and Start

```bash
cd /volume1/docker/integra-core
docker compose up -d --build
```

### 4. Verify It's Running

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Should return: {"status":"healthy","version":"1.0.0-beta",...}

# Test Aletheia
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is my position?"}'

# Test reports
curl http://localhost:8000/api/v1/reports/board
curl http://localhost:8000/api/v1/reports/family
```

### 5. Access From Your Network

The API will be available at:
```
http://[NAS-IP]:8000
```

API documentation:
```
http://[NAS-IP]:8000/docs
```

---

## Connecting Index8.html

In Index8.html, the frontend will call:
```javascript
const API_BASE = 'http://[NAS-IP]:8000/api/v1';
```

Replace `[NAS-IP]` with your NAS's local IP address (e.g., `192.168.1.100`).

---

## Managing the Container

```bash
# View logs
docker compose logs -f integra-core

# Restart
docker compose restart integra-core

# Stop
docker compose down

# Rebuild after code changes
docker compose up -d --build
```

---

## Alternative: DSM Container Manager UI

If you prefer the GUI:

1. Open **Container Manager** in DSM
2. Go to **Project** → **Create**
3. Set path to `/volume1/docker/integra-core`
4. It will detect the `docker-compose.yml`
5. Add environment variable: `POE_API_KEY` = your key
6. Click **Build & Run**

---

## What's Running

| Endpoint | What It Does |
|----------|-------------|
| `/api/v1/position-grid` | Financial position (4 metrics) |
| `/api/v1/trust-index` | Trust Index score + dimensions |
| `/api/v1/entities` | Entity listing + detail |
| `/api/v1/governance-alerts` | Governance cascade |
| `/api/v1/reports/{audience}` | Board / Technical / Regulator / Family reports |
| `/api/v1/chat` | Aletheia (Claude-powered via Poe) |
| `/api/v1/voice/synthesize` | ElevenLabs speech synthesis |
| `/api/v1/voice/tour-narration` | Guided tour voice narration |
| `/api/v1/scenario-engine` | What-if scenario modeling |
| + 14 more | See `/docs` for full list |

**Total: 24 endpoints, all operational.**
