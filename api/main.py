from fastapi import FastAPI
from .routes import features

app = FastAPI(
    title="SmartField NYC311 Feature API",
    description="REST API to serve Gold layer features from Delta Lake via Databricks SQL.",
    version="1.0.0"
)

app.include_router(features.router)

@app.get("/ping")
def ping():
    return {"status": "ok"}
