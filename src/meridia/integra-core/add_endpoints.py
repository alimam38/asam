
f = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\main.py', encoding='utf-8')
content = f.read()
f.close()

ADDITION = """
# ═══════════════════════════════════════════════════════════
# MX + PLAID INTEGRATION ENDPOINTS
# ═══════════════════════════════════════════════════════════

@app.post("/api/v1/connect/mx/{entity_id}", tags=["connections"])
async def connect_mx(entity_id: str, db: AsyncSession = Depends(get_db)):
    \"\"\"
    Connect MX to an entity and calculate live FPS.
    Pulls real account data from MX platform.
    Falls back to tier-calibrated sandbox data if no accounts connected.
    \"\"\"
    from mx_adapter import pull_mx_for_entity
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    result = await pull_mx_for_entity(entity_id, entity["name"], entity["tier"])
    return result


@app.post("/api/v1/connect/plaid/{entity_id}", tags=["connections"])
async def connect_plaid(entity_id: str, db: AsyncSession = Depends(get_db)):
    \"\"\"
    Connect Plaid to an entity and calculate live FPS.
    Runs against Plaid sandbox (switches to production when approved).
    \"\"\"
    from mx_adapter import PlaidAdapter
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    plaid = PlaidAdapter()
    result = await plaid.pull_and_calculate(entity_id, entity["name"], entity["tier"])
    return result


@app.get("/api/v1/connect/status/{entity_id}", tags=["connections"])
async def connection_status(entity_id: str, db: AsyncSession = Depends(get_db)):
    \"\"\"
    Check connection status for an entity — what data source is powering the FPS.
    \"\"\"
    entity = await crud.get_entity(db, entity_id)
    if not entity:
        raise HTTPException(404, f"Entity {entity_id} not found")
    position = await crud.get_position(db, entity_id)
    source = None
    if position:
        import json as _j
        raw = position.get("raw_data")
        if isinstance(raw, dict):
            source = raw.get("source")
        elif raw:
            try:
                source = _j.loads(raw).get("source")
            except Exception:
                pass
    return {
        "entity_id":    entity_id,
        "entity_name":  entity["name"],
        "tier":         entity["tier"],
        "has_position": position is not None,
        "data_source":  source or "seeded",
        "fps_score":    position["fps_score"] if position else None,
        "period":       position["period"] if position else None,
        "last_updated": str(position.get("calculated_at", "")) if position else None,
        "available_connections": ["mx", "plaid"],
    }

"""

# Insert before the RUN block
target = "if __name__ == \"__main__\":"
if target in content:
    content = content.replace(target, ADDITION + target)
    g = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\main.py', 'w', encoding='utf-8')
    g.write(content)
    g.close()
    print("Endpoints added")
else:
    print("Target not found")
