from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from utils.config_updater import update_config

config_router = APIRouter()

class BulkConfigUpdateRequest(BaseModel):
    updates: Dict[str, str]

@config_router.post("/config/bulk-update")
def bulk_update_config(req: BulkConfigUpdateRequest):
    try:
        update_config(req.updates)
        return {"message": "Configuration updated successfully."}
    except Exception as e:
        return {"error": str(e)}