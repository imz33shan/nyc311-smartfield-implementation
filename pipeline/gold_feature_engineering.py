from pyspark.sql.functions import col, hour, dayofweek

silver_df = spark.table("main.processed.nyc311_processed_data")

gold_df = silver_df.select(
    col("complaint_type"),
    col("borough"),
    col("status"),
    col("response_time_hrs"),
    col("created_date")
).dropna()

gold_df = gold_df \
    .withColumn("hour_of_day", hour(col("created_date"))) \
    .withColumn("day_of_week", dayofweek(col("created_date")))

gold_df.write.format("delta").mode("overwrite").saveAsTable("main.analytics.nyc_311_features")

print("✅ Gold layer feature engineering complete.")
