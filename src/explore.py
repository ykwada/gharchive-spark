from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("explore").getOrCreate()
df = spark.read.json("/app/data/raw/*.json.gz")
df.printSchema()
print(df.count())
input("...")