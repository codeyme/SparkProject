def readFromHadoop(spark):
    df = spark.read.csv('/data/spark/test/zipcodes1.csv')
    df.printSchema()
    df.show()
    parDF = spark.read.parquet('/data/spark/test/parquet/people_parquet')
    parDF.show()
    df3 = spark.read.options(header='True',inferSchema='True',delimiter=',').csv('/data/spark/test/zipcodes1.csv')
    df3.take(2)

def writeToHadoop(spark):
    df = spark.read.csv('/data/spark/test/zipcodes1.csv')
    df.write.parquet('/data/spark/test/parquet/people_parquet1')

def writeHiveTable(spark):
    df3 = spark.read.options(header='True', inferSchema='True', delimiter=',').csv("/data/spark/test/zipcodes1.csv")
    df3.write.mode('overwrite').saveAsTable('xyz.zip_table')
    tabDF = spark.sql('select * from xyz.zip_table')
    tabDF.show()

def writePartHive(spark):
    df3 = spark.read.options(header='True', inferSchema='True', delimiter=',').csv("/data/spark/test/zipcodes1.csv")
    df3.write.mode('overwrite').partitionBy('city').saveAsTable('xyz.city_part')
    spark.sql('select * from xyz.city_part limit 2;').show()

def
