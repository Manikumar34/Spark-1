import findspark 
findspark.init()
from pyspark.sql import SparkSession
# Create the sparkSession
sparkSession = SparkSession.builder.getOrCreate() 
# Create the sparkContext
sc = sparkSession.sparkContext 
# Create RDD from file
ordersRDD = sc.textFile("C:\\data\\orders")
# Print top 10 rows from the ordersRDD
for i in ordersRDD.take(5):
    print(i)
# Create new RDD from existing RDD
print("\n ************************************ \n")
completeOrdersRDD = ordersRDD.filter(lambda o: o.split(",")[3] == "COMPLETE")
# Print top 10 rows from the completeOrdersRDD
for i in completeOrdersRDD.take(5):
    print(i)
    

""" Output:

1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE

 ************************************ 

3,2013-07-25 00:00:00.0,12111,COMPLETE
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,4530,COMPLETE
15,2013-07-25 00:00:00.0,2568,COMPLETE

"""
