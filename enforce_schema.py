from pyspark.sql.functions import col
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, ArrayType
from pyspark.sql import SparkSession

def enforce_schema(spark):
    data = [("James", "", "Smith", "36636", "M", 3000),
            ("Michael", "Rose", "", "40288", "M", 4000),
            ("Robert", "", "Williams", "42114", "M", 4000),
            ("Maria", "Anne", "Jones", "39192", "F", 4000),
            ("Jen", "Mary", "Brown", "", "F", -1)
            ]

    schema = StructType([ \
        StructField("firstname", StringType(), True), \
        StructField("middlename", StringType(), True), \
        StructField("lastname", StringType(), True), \
        StructField("id", StringType(), True), \
        StructField("gender", StringType(), True), \
        StructField("salary", IntegerType(), True) \
        ])

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show()

def nested_schema(spark):
    structureData = [
        (("James", "", "Smith"), "36636", "M", 3100),
        (("Michael", "Rose", ""), "40288", "M", 4300),
        (("Robert", "", "Williams"), "42114", "M", 1400),
        (("Maria", "Anne", "Jones"), "39192", "F", 5500),
        (("Jen", "Mary", "Brown"), "", "F", -1)
    ]
    structureSchema = StructType([
        StructField('name', StructType([
            StructField('firstname', StringType(), True),
            StructField('middlename', StringType(), True),
            StructField('lastname', StringType(), True)
        ])),
        StructField('id', StringType(), True),
        StructField('gender', StringType(), True),
        StructField('salary', IntegerType(), True)
    ])

    df2 = spark.createDataFrame(data=structureData, schema=structureSchema)
    df2.printSchema()
    df2.show(truncate=False)

    select_func(spark)


def select_func(spark):
    data = [("James", "Smith", "USA", "CA"),
            ("Michael", "Rose", "USA", "NY"),
            ("Robert", "Williams", "USA", "CA"),
            ("Maria", "Jones", "USA", "FL")
            ]
    columns = ["firstname", "lastname", "country", "state"]
    df = spark.createDataFrame(data=data, schema=columns)
    df.select(df.firstname, df.lastname).show()

    withColum_func(spark)


def withColum_func(spark):
    data = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
            ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
            ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
            ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
            ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
            ]

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]

    df = spark.createDataFrame(data=data, schema=columns)
    ddf = df.withColumn("salary", col("salary").cast("Double"))
    ddf.show()

    filter_func(spark)


def filter_func(spark):
    data = [
        (("James", "", "Smith"), ["Java", "Scala", "C++"], "OH", "M"),
        (("Anna", "Rose", ""), ["Spark", "Java", "C++"], "NY", "F"),
        (("Julia", "", "Williams"), ["CSharp", "VB"], "OH", "F"),
        (("Maria", "Anne", "Jones"), ["CSharp", "VB"], "NY", "M"),
        (("Jen", "Mary", "Brown"), ["CSharp", "VB"], "NY", "M"),
        (("Mike", "Mary", "Williams"), ["Python", "VB"], "OH", "M")
    ]

    schema = StructType([
        StructField('name', StructType([
            StructField('firstname', StringType(), True),
            StructField('middlename', StringType(), True),
            StructField('lastname', StringType(), True)
        ])),
        StructField('languages', ArrayType(StringType()), True),
        StructField('state', StringType(), True),
        StructField('gender', StringType(), True)
    ])

    df = spark.createDataFrame(data=data, schema=schema)
    df.filter(df.state == "OH").show(truncate = False)

    # df.filter(df.state != "OH").show(truncate = False)
