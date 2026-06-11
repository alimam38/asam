# WayPoint Crown — API Wiring Guide

## What Changed

Index8_wired.html replaces all direct window.Poe calls with a unified MeridiaAPI class supporting three providers:

| Provider | How It Works | When It Fires |
|----------|-------------|---------------|
| anthropic | Direct HTTPS to api.anthropic.com | Set API key + provider |
| poe | REST API to api.poe.com | Set API key + provider |
| poe (native) | window.Poe.sendUserMessage() | Auto-detected inside Poe |
| local | Rule-based keyword matching | Default / fallback |

## Quick Start

### Anthropic API (Direct Claude)
Open browser console (F12):
```
MeridiaAPI.configure('anthropic', 'sk-ant-api03-YOUR-KEY');
```

### Poe API (Multi-Model)
```
MeridiaAPI.configure('poe', 'YOUR-POE-API-KEY');
```

### Inside Poe
Upload to Poe as a bot. Auto-detects window.Poe. ElevenLabs voice works automatically.

### Local (Default)
No config needed. Rule-based responses + Web Speech API narration.

## Connect Backend (Integra Core)
```
MeridiaAPI.connectBackend('http://YOUR-NAS-IP:8000/api/v1');
```

## Check Status
```
MeridiaAPI.status();
```

## Hardcode Keys (NAS Deployment)
Edit MERIDIA_CONFIG in the script section. Change provider and add apiKey.

## Architecture
```
User → sendMessage() → MeridiaAPI.chat()
  → anthropic? → api.anthropic.com (Claude direct)
  → poe + key? → api.poe.com (multi-model)
  → poe native? → window.Poe (inside Poe environment)
  → fallback → local rule engine
```

Meridia Holdings LLC — Governance as a Service
