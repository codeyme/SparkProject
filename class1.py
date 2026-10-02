from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql import SparkSession
from enforce_schema import enforce_schema, nested_schema, select_func, withColum_func, filter_func
from carPowerAnalysis import trans_withColumn
from customerDataCleaning import clean
from eCommerceAnalysis import *
from withHadoop import *

def number_rdd():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rdd = spark.sparkContext.parallelize(data)
    print(rdd.collect())
    print("hello")





if __name__ == '__main__':
    spark:SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").enableHiveSupport().getOrCreate()

    # number_rdd()

    # enforce_schema(spark)
    # nested_schema(spark)

    # select,withColumn and filter
    # select_func(spark)
    # withColum_func(spark)
    # filter_func(spark)
    # trans_withColumn(spark)
    # clean(spark)
    # filter()
    # groupBy(spark)
    # nullVals(spark)
    # joins(spark)
    # unions(spark)
    # tempView(spark)
    # readFromHadoop(spark)
    # writeToHadoop(spark)
    # writeHiveTable(spark)
    writePartHive(spark)