"""Entity endpoints — entity-aware."""

from fastapi import APIRouter, HTTPException, Query
from ..models import Entity, EntityDetail
from ..mock_data import get_all_entities, get_fps_data, ENTITIES_DB, POSITIONS_DB, TRUST_DB

router = APIRouter(prefix="/api/v1", tags=["entities"])


@router.get("/entities", response_model=list[Entity])
def list_entities():
    """Return all tracked entities."""
    return get_all_entities()


@router.get("/entities/{entity_id}")
def read_entity(entity_id: str):
    """Return detail for a specific entity."""
    if entity_id not in ENTITIES_DB:
        raise HTTPException(status_code=404, detail=f"Entity {entity_id} not found")
    e = ENTITIES_DB[entity_id]
    p = POSITIONS_DB.get(entity_id, {})
    t = TRUST_DB.get(entity_id)
    return {
        "entity_id": entity_id,
        "name": e["name"],
        "tier": e["tier"],
        "type": e["type"],
        "status": e["status"],
        "description": e["description"],
        "fps_score": p.get("fps_score"),
        "fps_direction": p.get("fps_direction"),
        "fps_narrative": p.get("fps_narrative"),
        "trust_index": t.overall_score if t else None,
        "net_assets": p.get("net_assets"),
        "cash_position": p.get("cash_position"),
    }


@router.get("/fps/{entity_id}")
def read_fps(entity_id: str):
    """Return FPS score and components for an entity."""
    if entity_id not in ENTITIES_DB:
        raise HTTPException(status_code=404, detail=f"Entity {entity_id} not found")
    return get_fps_data(entity_id)
