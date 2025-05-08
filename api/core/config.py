import os

class Settings:
    DATABRICKS_HOST = os.getenv("DATABRICKS_HOST")
    DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")
    DATABRICKS_WAREHOUSE_ID = os.getenv("DATABRICKS_WAREHOUSE_ID")
    GOLD_TABLE = os.getenv("GOLD_TABLE")
    ALLOWED_API_KEYS = {"admin": "secret123"}

settings = Settings()