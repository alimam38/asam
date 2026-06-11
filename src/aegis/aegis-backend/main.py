"""
Main FastAPI application for the Aegis Financial Positioning System.

This is the entry point for the Aegis backend API server.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from api_v1 import router as api_v1_router

# Initialize FastAPI application
app = FastAPI(
    title="Aegis Financial Positioning System",
    description="Backend API for the Aegis prototype - an Ethical Steward and Dynamic Guidance System",
    version="1.0.0-beta",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ============================================================================
# CORS Configuration
# ============================================================================

# Configure CORS to allow the frontend prototype to communicate with the API
# In production, this should be restricted to specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "*"  # Allow all origins for prototype - REMOVE IN PRODUCTION
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Mount API Routers
# ============================================================================

app.include_router(api_v1_router)

# ============================================================================
# Root Endpoints
# ============================================================================

@app.get("/")
async def root():
    """
    Root endpoint - API information.
    """
    return {
        "name": "Aegis Financial Positioning System API",
        "version": "1.0.0-beta",
        "description": "Backend server for the Aegis prototype",
        "documentation": "/docs",
        "paradigm": "Ethical Steward • Dynamic Guidance System • Governed by Design",
        "principles": [
            "Stewardship over Extraction",
            "Clarity over Complexity",
            "Governance as Default",
            "Dignity-First Design"
        ],
        "endpoints": {
            "health": "/api/v1/health",
            "position": "/api/v1/position-grid",
            "trust_index": "/api/v1/trust-index",
            "entities": "/api/v1/entities",
            "governance": "/api/v1/governance-alerts",
            "signals": "/api/v1/signal-feed",
            "metrics": "/api/v1/metrics-dashboard",
            "scenarios": "/api/v1/scenario-engine",
            "flows": "/api/v1/flow-diagram",
            "chat": "/api/v1/chat",
            "institutional": "/api/v1/institutional-sandbox",
            "renaissance": "/api/v1/renaissance"
        }
    }


@app.get("/manifest")
async def manifest():
    """
    System manifest - core principles and architecture.
    
    This endpoint expresses the Aegis Paradigm in machine-readable form.
    """
    return {
        "system": "Aegis",
        "subtitle": "Financial Positioning System",
        "paradigm": "Ethical Steward • Dynamic Guidance System",
        "core_principles": {
            "stewardship": {
                "description": "Stewardship over extraction",
                "implementation": "Multi-party governance, consent-based insights, dignity-first design"
            },
            "clarity": {
                "description": "Clarity over complexity",
                "implementation": "Financial Positioning Score, real-time signals, visual flows"
            },
            "governance": {
                "description": "Governance as default, not afterthought",
                "implementation": "Trust Index, multi-party approval cascade, audit trails"
            },
            "dignity": {
                "description": "Dignity-first, especially for the vulnerable",
                "implementation": "Renaissance pathways, no-judgment re-entry, opportunity restoration"
            }
        },
        "trust_index_dimensions": [
            "Financial Resilience",
            "Stewardship",
            "Mission Impact",
            "Governance Hygiene"
        ],
        "supported_modes": [
            "WayPoint Core",
            "Institutional Sandbox",
            "Renaissance"
        ],
        "architecture": {
            "frontend": "HTML/CSS/JS (Claude.ai Artifact)",
            "backend": "FastAPI + Python",
            "ai_core": "Council of LLMs (Anthropic Claude)",
            "database": "PostgreSQL (planned)",
            "data_integration": "Plaid/Finicity (planned)"
        }
    }


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Custom 404 handler."""
    return JSONResponse(
        status_code=404,
        content={
            "error": "Resource not found",
            "message": "The requested endpoint does not exist",
            "available_endpoints": "/docs"
        }
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Custom 500 handler."""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred. Please try again.",
            "support": "Contact the Aegis team for assistance"
        }
    )


# ============================================================================
# Startup/Shutdown Events
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """
    Execute on server startup.
    
    In production, this would:
    - Initialize database connections
    - Set up caching layer
    - Connect to external services
    - Load configuration
    """
    print("=" * 80)
    print("AEGIS FINANCIAL POSITIONING SYSTEM")
    print("Ethical Steward • Dynamic Guidance System")
    print("=" * 80)
    print("✓ Server starting...")
    print("✓ API v1 loaded")
    print("✓ CORS configured")
    print("✓ Mock data generators ready")
    print("")
    print("Documentation: http://localhost:8000/docs")
    print("Manifest: http://localhost:8000/manifest")
    print("")
    print("Ready to receive requests.")
    print("=" * 80)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Execute on server shutdown.
    
    In production, this would:
    - Close database connections
    - Flush caches
    - Complete pending requests
    - Clean up resources
    """
    print("\n" + "=" * 80)
    print("AEGIS SERVER SHUTTING DOWN")
    print("=" * 80)


# ============================================================================
# Development Server Entry Point
# ============================================================================

if __name__ == "__main__":
    """
    Run the development server.
    
    Usage:
        python main.py
    
    The server will start on http://localhost:8000
    """
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
