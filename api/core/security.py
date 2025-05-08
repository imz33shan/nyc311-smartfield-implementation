from fastapi import Header, HTTPException
from .config import settings

def verify_token(x_api_key: str = Header(...)):
    if x_api_key not in settings.ALLOWED_API_KEYS.values():
        raise HTTPException(status_code=401, detail="Unauthorized")