import findspark 
findspark.init()
from pyspark.sql import SparkSession
# Create the sparkSession
sparkSession = SparkSession.builder.getOrCreate() 
# Create the sparkContext
sc = sparkSession.sparkContext 
# Create RDD from file
departmentsRDD = sc.textFile("C:\\data\\departments")
# Print all rows from the RDD
for i in departmentsRDD.collect():
    print(i)
