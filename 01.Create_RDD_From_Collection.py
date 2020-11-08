import findspark 
findspark.init()
from pyspark.sql import SparkSession
sparkSession = SparkSession.builder.getOrCreate() # Create the sparkSession
sc = sparkSession.sparkContext # Create the sparkContext
lst = [11, 22, 33, 44, 55] 
intRDD = sc.parallelize(lst) # Create RDD from a collection(example: list)
intRDD.collect()

# Output: [11, 22, 33, 44, 55]
