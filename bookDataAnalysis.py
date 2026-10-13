from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def data_injestion(spark):
    # df2 = spark.read.json('file:///home/takeo/data/books.json')
    df = spark.read.json('/data/books.json')
    print(df.count())
    print(df.distinct().count())
    dfdistinct = df.dropDuplicates()
    print(f'after dropping duplicates: {dfdistinct.count()}')
    df.select('title').filter(col('title') == 'ODD HOURS').show()
    df.select('title', when(df.title != 'ODD HOURS',1).otherwise(0).alias('newHours')).show(10)
    df.printSchema()
