import databricks.sql as dbsql
import pandas as pd
from ..core.config import settings

def fetch_gold_features(limit: int = 10):
    try:
        with dbsql.connect(
            server_hostname=settings.DATABRICKS_HOST,
            http_path=f"/sql/1.0/warehouses/{settings.DATABRICKS_WAREHOUSE_ID}",
            access_token=settings.DATABRICKS_TOKEN,
        ) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                SELECT complaint_type, borough, status, response_time_hrs, hour_of_day, day_of_week
                FROM {settings.GOLD_TABLE}
                LIMIT {limit}
            """)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(rows, columns=columns)
            return df.to_dict(orient="records")
    except Exception as e:
        raise RuntimeError(f"Failed to query Databricks: {e}")
