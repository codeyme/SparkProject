from pyspark.sql import SparkSession

spark:SparkSession = SparkSession.builder.master('local[1]').enableHiveSupport().getOrCreate()

url_val= 'jdbc:redshift://default-workgroup.701364614639.us-east-1.redshift-serverless.amazonaws.com:5439/dev'
df = spark.read.format("jdbc").option("url", url_val).option("dbtable", "sample_data_dev.test.listing").option("driver","com.amazon.redshift.jdbc42.Driver").option("user", "admin").option("password", "Admin1234").load()
df = (spark.read.format("jdbc")
      .option("url", "jdbc:redshift://default-workgroup.701364614639.us-east-1.redshift-serverless.amazonaws.com:5439/sample_data_dev")
      .option("dbtable", "sample_data_dev.test.listing")
      .option("driver","com.amazon.redshift.jdbc42.Driver")
      .option("user", "admin")
      .option("password", "Admin1234")
      .load())

df.write.format("jdbc").option("url", "jdbc:redshift://default-workgroup.701364614639.us-east-1.redshift-serverless.amazonaws.com:5439/dev").option("dbtable", "dev.test.employee").option("driver","com.amazon.redshift.jdbc42.Driver").option("user", "admin").option("password", "Admin1234").mode("overwrite").save()

(df.write.format("jdbc")
 .option("url", "jdbc:redshift://default-workgroup.701364614639.us-east-1.redshift-serverless.amazonaws.com:5439/sample_data_dev")
 .option("dbtable", "sample_data_dev.test.employee")
 .option("driver","com.amazon.redshift.jdbc42.Driver")
 .option("user", "admin").option("password", "Admin1234").mode("overwrite").save())


schemas_df = (
    spark.read
        .format("jdbc")
        .option("url", "jdbc:redshift://default-workgroup.701364614639.us-east-1.redshift-serverless.amazonaws.com:5439/sample_data_dev")
        .option(
            "query",
            """
            SELECT database_name, schema_name
            FROM svv_redshift_schemas
            WHERE database_name = 'sample_data_dev'
            ORDER BY schema_name
            """
        )
        .option("driver", "com.amazon.redshift.jdbc42.Driver")
        .option("user", "admin")
        .option("password", "Admin1234")
        .load()
)

schemas_df.show(truncate=False)


schemas_df = (
    spark.read
        .format("jdbc")
        .option("url", "jdbc:redshift://default-workgroup.701364614639.us-east-1.redshift-serverless.amazonaws.com:5439/sample_data_dev")
        .option(
            "query",
            """
            SELECT database_name, schema_name
            FROM sample_data_dev
            WHERE database_name = 'sample_data_dev'
            ORDER BY schema_name
            """
        )
        .option("driver", "com.amazon.redshift.jdbc42.Driver")
        .option("user", "admin")
        .option("password", "Admin1234")
        .load()
)

schemas_df.show(truncate=False)