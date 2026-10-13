from pyspark.sql import SparkSession
from bookDataAnalysis import *

# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    spark:SparkSession = SparkSession.builder.master('local[1]').enableHiveSupport().getOrCreate()
    data_injestion(spark)

