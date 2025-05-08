import requests
import json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, MapType

nyc311_schema = StructType([
    StructField("unique_key", StringType()),
    StructField("created_date", TimestampType()),
    StructField("agency", StringType()),
    StructField("agency_name", StringType()),
    StructField("complaint_type", StringType()),
    StructField("descriptor", StringType()),
    StructField("incident_zip", StringType()),
    StructField("incident_address", StringType()),
    StructField("street_name", StringType()),
    StructField("cross_street_1", StringType()),
    StructField("cross_street_2", StringType()),
    StructField("intersection_street_1", StringType()),
    StructField("intersection_street_2", StringType()),
    StructField("address_type", StringType()),
    StructField("city", StringType()),
    StructField("facility_type", StringType()),
    StructField("status", StringType()),
    StructField("resolution_description", StringType()),
    StructField("resolution_action_updated_date", TimestampType()),
    StructField("community_board", StringType()),
    StructField("borough", StringType()),
    StructField("open_data_channel_type", StringType()),
    StructField("park_facility_name", StringType()),
    StructField("park_borough", StringType()),
    StructField("location_type", StringType()),
    StructField("landmark", StringType()),
    StructField("bbl", StringType()),
    StructField("x_coordinate_state_plane", StringType()),
    StructField("y_coordinate_state_plane", StringType()),
    StructField("latitude", DoubleType()),
    StructField("longitude", DoubleType()),
    StructField("location", MapType(StringType(), StringType())),
    StructField(":@computed_region_efsh_h5xi", StringType()),
    StructField(":@computed_region_f5dn_yrer", StringType()),
    StructField(":@computed_region_yeji_bk3q", StringType()),
    StructField(":@computed_region_92fq_4b7q", StringType()),
    StructField(":@computed_region_sbqj_enih", StringType()),
    StructField(":@computed_region_7mpf_4k6g", StringType()),
])

url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=1000"  # Limit for example
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")

records = response.json()

bronze_df = spark.createDataFrame(
    data=records,
    schema=nyc311_schema
)

bronze_df.write.format("delta").mode("overwrite").saveAsTable("main.raw.nyc311_raw_data")

print("✅ NYC 311 API data ingested into Bronze layer.")
