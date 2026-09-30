data = [('Smith',23,5.3),
        ('Rashmi',27,5.8),
        ('Smith',23,5.3),
        ('Payal',27,5.8),
        ('Megha',27,5.4)]

columns= ['Name','Age' ,'Height']
def clean(spark):
    df = spark.createDataFrame(data = data, schema = columns)
    # df.show()
    df = df.distinct()
    # df.show()
    ddf = df.dropDuplicates(['Age'])
    ddf.show()
    df = df.dropDuplicates(['Height','Age'])
    df.show()