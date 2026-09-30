from pyspark.sql.functions import col,lit

data = [('Ford Torino', 140, 3449, 'US'),
        ('Chevrolet Monte Carlo', 150, 3761, 'US'),
        ('BMW 2002', 113, 2234, 'Europe')
        ]

columns = ['carr','horsepower','weight','origin']


def trans_withColumn(spark):
    df = spark.createDataFrame(data=data, schema=columns)
    df.show()
    df = df.withColumn('AvgWeight', lit(200)).withColumn('kilowatt_power', col('horsepower')*1000).withColumnRenamed('carr','car')
    df.show()

