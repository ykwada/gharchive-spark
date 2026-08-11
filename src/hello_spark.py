from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('test').getOrCreate()
spark.read.json("/app/data/hello_spark.json").show()
input("Press Enter to stop Spark...")