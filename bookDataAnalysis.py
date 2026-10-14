from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def data_injestion(spark):
    # df2 = spark.read.json('file:///home/takeo/data/books.json')
    df = spark.read.json('/data/books.json')
    # print(df.count())
    # print(df.distinct().count())
    # dfdistinct = df.dropDuplicates()
    # print(f'after dropping duplicates: {dfdistinct.count()}')
    # df.select('title').filter(col('title') == 'ODD HOURS').show()
    # df.select('title', when(df.title != 'ODD HOURS',1).otherwise(0).alias('newHours')).show(10)
    # # df.printSchema()
    # df.select('title','author').filter(df.title.like('%THE%')).show(10)
    # df.select(df.author.substr(1,3).alias('newTitle1')).show(10)
    # df.select(df.author.substr(3,6).alias('newTitle2')).show(5)
    # df.select('*').filter((df.author == "John Sandford") | (df.author == "Emily Giffin")).show(10)
    # df.distinct().select('author','title').filter((col('title').like('THE%')) | df.title.like('%IN')).show(2)
    # df = df.withColumnRenamed('amazon_product_url','url')
    # df.printSchema()
    # df.drop('publisher','published_date').show(5)
    # df.select('author').withColumn('book_count',df.group('author'))
    author_book_count = df.groupBy('author').agg(count_distinct('title').alias('book_count'))
    author_book_count.show()