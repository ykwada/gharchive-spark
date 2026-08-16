from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, to_date, to_timestamp

spark = SparkSession.builder.appName("trasform_parquet").getOrCreate()
df = spark.read.json("/app/data/raw/*.json.gz")
df_get_json = df.select(
    "type",
    col("actor.login").alias("actor_login"),
    col("repo.name").alias("repo_name"),
    col("payload.push_id").alias("push_id"),
    col("payload.ref").alias("ref"),
    to_date(to_timestamp(col("created_at"))).alias("created_date"),
    hour(to_timestamp(col("created_at"))).alias("created_hour"),
)
df_get_json.show()

df_get_json.write.mode("overwrite").partitionBy("created_date", "created_hour").parquet("/app/data/parquet/")

input("...")
