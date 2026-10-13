from pyspark.sql import SparkSession


def data_injestion(spark):
    # df2 = spark.read.json('file:///home/takeo/data/books.json')
    df = spark.read.json('/data/books.json')
    print(df.count())
    print(df.distinct().count())
    dfdistinct = df.dropDuplicates()
    print(f'after dropping duplicates: {dfdistinct.count()}')
