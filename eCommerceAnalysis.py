# from pyspark.sql import SparkSession

#Initialize SparkSession
# spark = SparkSession.builder.appName("E-Commerce Analysis").getOrCreate()

#Sample Data
data = [    (1, 101, 5001, 'Laptop', 'Electronics', 1000.0, 1),
    (2, 102, 5002, 'Headphones', 'Electronics', 50.0, 2),
    (3, 101, 5003, 'Book', 'Books', 20.0, 3),
    (4, 103, 5004, 'Laptop', 'Electronics', 1000.0, 1),
    (5, 102, 5005, 'Chair', 'Furniture', 150.0, 1)
    ]
columns = ["transaction_id", "customer_id", "product_id", "product_name", "category", "price", "quantity"]


#Create DataFrame

# df = spark.createDataFrame(data,columns)
# df.show()

def filter(spark):
    # Filter transactions where quantity is greater than 1
    df = spark.createDataFrame(data, columns)
    df_filtered = df.filter(df.quantity > 1)
    df_filtered.show()

def dropDuplicate(spark):
    # Drop Duplicate rows based on customer_id and product_id
    df = spark.createDataFrame(data, columns)
    df_no_duplicates = df.dropDuplicates(['customer_id', 'product_id'])
    df_no_duplicates.show()

def select(spark):
    # Select specific columns
    df = spark.createDataFrame(data, columns)
    df_selected = df.select("customer_id", 'product_name', 'price')
    df_selected.show()

def groupBy(spark):
    # Calculate the total spending per customer
    # select customer,sum(price) from table group by customer
    df = spark.createDataFrame(data, columns)
    df_grouped = df.groupBy('customer_id').agg({'price': 'sum'}).orderBy('customer_id')
    df_grouped.show()

def nullVals(spark):
    df = spark.createDataFrame(data,columns)
    avg_price = df.selectExpr('avg(price)').collect()[0][0]
    df_filled = df.na.fill({'price':avg_price})
    df.show()
    df_filled.show()

def joins(spark):
    customer_data = [
        (101, "John Doe", "john@example.com"),
        (102, "Jane Smith", "jane@example.com"),
        (103, "Alice Johnson", "alice@example.com")
    ]

    customer_columns = ["customer_id", "customer_name", "email"]
    df_cust = spark.createDataFrame(customer_data,customer_columns)
    df = spark.createDataFrame(data,columns)
    df_joined = df.join(df_cust, on='customer_id', how = 'inner')
    df_joined.show()


def unions(spark):
    new_data = [
        (6, 104, 5006, 'Table', 'Furniture', 200.0, 1)
    ]
    df_new = spark.createDataFrame(new_data, columns)
    df = spark.createDataFrame(data,columns)
    df_union = df.union(df_new)
    df_union.show()

def tempView(spark):
    df = spark.createDataFrame(data,columns)
    df.createOrReplaceTempView('transactions')
    #RunSQL query
    sql_result = spark.sql("select customer_id, sum(price*quantity) as total_spent from transactions group by customer_id order by customer_id")
    sql_result.show()















