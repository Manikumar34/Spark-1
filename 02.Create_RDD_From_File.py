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

""" Output:

2,Fitness
3,Footwear
4,Apparel
5,Golf
6,Outdoors
7,Fan Shop

"""
