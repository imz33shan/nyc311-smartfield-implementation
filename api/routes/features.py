from fastapi import APIRouter, Depends, HTTPException
from ..core.security import verify_token
from ..services.databricks_query import fetch_gold_features

router = APIRouter()

@router.get("/features", dependencies=[Depends(verify_token)])
def get_features(limit: int = 10):
    try:
        return fetch_gold_features(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))