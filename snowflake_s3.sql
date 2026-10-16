select * from BOOTCAMP.TEST.SALES_S3;

CREATE WAREHOUSE my_large_wh
WITH
    WAREHOUSE_SIZE = 'LARGE'
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED = TRUE;

ALTER WAREHOUSE MY_LARGE_WH SUSPEND;

list @BOOTCAMP.TEST.S3_STAGE;



create table data(id int, name varchar(50));

copy into bootcamp.test.data from @bootcamp.test.S3_STAGE/snowflake_data/
FILE_FORMAT=(TYPE= 'CSV')
PATTERN= '.*.csv';



create or replace table bootcamp.test.listing(PARQUET_RAW VARIANT);

copy into bootcamp.test.listing from (SELECT $1 from  @bootcamp.test.S3_STAGE/redshift/output/parquet) 
FILE_FORMAT=(TYPE= 'PARQUET')
PATTERN= '.*.parquet';


select * from bootcamp.test.listing;


select $1:dateid, $1:eventid from bootcamp.test.listing;
