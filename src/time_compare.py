from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("time_compare").getOrCreate()
import time

start_j = time.time()
print(spark.read.json("/app/data/raw/*.json.gz").count())
print(time.time() - start_j)

start_p = time.time()
print(spark.read.parquet("/app/data/parquet/").count())
print(time.time() - start_p)