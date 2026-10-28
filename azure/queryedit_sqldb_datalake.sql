create schema test
create table test.emp(id int, name VARCHAR(10))
insert into test.emp values(1,'John')
insert into test.emp values(2,'Prakriti')
select * from test.emp;

create view test.emp_v as select name from test.emp where id=1;
select * from test.emp_v

create table test.[emp 1]([emp id] int, [first name] varchar(10)) --encloser- [], in postgres/redshift/snowflake its ""
insert into test.[emp 1] values(1,'John')
insert into test.[emp 1] values(2,'Prakriti')
select * from test.[emp 1] where [emp id] = 1;

create table test.emp3(EmpId int,Name VARCHAR(10)) --maintains the variable cases, meaning is case sensitive
