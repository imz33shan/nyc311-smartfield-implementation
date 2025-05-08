from pyspark.sql.functions import col, to_timestamp
from pyspark.sql.types import DoubleType

bronze_df = spark.table("main.raw.nyc311_raw_data")

silver_df = bronze_df \
    .withColumn("created_date", to_timestamp(col("created_date"))) \
    .withColumn("closed_date", to_timestamp(col("resolution_action_updated_date"))) \
    .withColumn("response_time_hrs",
        (col("closed_date").cast("long") - col("created_date").cast("long")) / 3600
    )

silver_df = silver_df.filter(
    col("complaint_type").isNotNull() &
    col("borough").isNotNull() &
    col("status").isNotNull() &
    col("created_date").isNotNull()
)

silver_df = silver_df.filter(
    (col("response_time_hrs") >= 0) &
    (col("response_time_hrs") <= 720)
)

silver_df = silver_df.withColumn("response_time_hrs", col("response_time_hrs").cast(DoubleType()))

silver_df.write.format("delta").mode("overwrite").saveAsTable("main.processed.nyc311_processed_data")

print("✅ Silver layer transformation and validation complete.")
