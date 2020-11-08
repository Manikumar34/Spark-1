import findspark 
findspark.init()
from pyspark.sql import SparkSession
# Create the sparkSession
sparkSession = SparkSession.builder.getOrCreate() 
# Create the sparkContext
sc = sparkSession.sparkContext 
# Create RDD from a range
intRDD = sc.range(11,21)
# Print all the elements from RDD
intRDD.collect()

#Output: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
