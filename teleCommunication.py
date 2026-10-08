from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit,when,trim,lower

#Initialize Spark Session
spark = SparkSession.builder.master('local[1]').appName('TelecomDataProcessing').enableHiveSupport().getOrCreate()
spark.sql("CREATE DATABASE IF NOT EXISTS telecom_db")
spark.sql("USE telecom_db")

#Read call detail records(CDR) data from HDFS
cdr_df = spark.read.option('nullValue','NULL').csv('hdfs:///data/cdr.csv',header=True,inferSchema=True)
#Read Customer Usage Data from HDFS
usage_df = spark.read.option('nullValue','NULL').csv('hdfs:///data/custUsageData.csv',header=True, inferSchema=True)

#Handle Null Values: Replace Nulls with Default Values
cdr_df = cdr_df.withColumn('call_end_time',col('call_end_time').cast('string'))
cdr_df = cdr_df.fillna({'call_end_time':'unknown','call_duration':0,'call_status':'incomplete'})
usage_df = usage_df.fillna({'data_used_gb':0.0,'voice_minutes_used':0,'sms_used':0})

#Standardize Data Formats: Trim Whitespaces and convert to lowerCase
cdr_df = cdr_df.withColumn('call_type',trim(lower(col('call_type'))))
usage_df = usage_df.withColumn('total_charges',when(col('total_charges').isNull(),lit(0.0)).otherwise(col('total_charges')))

#Write cleaned Data to Hive tables
cdr_df.write.mode('overwrite').saveAsTable('telecom_db.cleaned_cdr_data')
usage_df.write.mode('overwrite').saveAsTable('telecom_db.cleaned_usage_data')

#Check Record Counts Between source and target
source_cdr_count = cdr_df.count()
target_cdr_count = spark.sql('select count(*) from telecom_db.cleaned_cdr_data').collect()[0][0]

if source_cdr_count == target_cdr_count:
    print('CDR data is complete and consistent')
else:
    print('Data inconsistency detected in CDR records')

source_usage_count = usage_df.count()
target_usage_count = spark.sql('select count(*) from telecom_db.cleaned_usage_data').collect()[0][0]

if source_usage_count == target_usage_count:
    print('Customer usage data is complete and consistent')
else:
    print('Data inconsistency detected in customer usage records')