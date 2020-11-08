Querying with Transact-SQL
https://www.youtube.com/watch?v=Tz-0Qe6vCUQ&t=2535s

SQL Server tutorial for beginners
https://www.youtube.com/watch?v=ZNObiptSMSI&list=PL08903FB7ACA1C2FB

# Connecting to SQL Server
Server Type = DataBase Engine\
Server Name = (local) or 127.0.0.1\
Authentication = Windows or SQL Server\
If SQL Server Authentication\
Login\
Password

# Schemas and Object Names
+ Fully-qualified name: [server_name.][database_name.][schema_name.]object_name
+ best practice: schema_name.object_name

# SQL Statement Types
+ Data Manipulation Language (DML)
  + SELECT
  + INSERT
  + UPDATE
  + DELETE
+ Data Definition Language (DDL)
  + CREATE
  + ALTER
  + DROP
+ Data Control Language (DCL)
  + GRANT
  + REVOKE
  + DENY

# DDL
## Creating
to create the database using a query
```SQL
create database sample1
```
two files gests generated
+ MDF - Data File contains actual data
+ LDF - Transaction Log File (used to recover the database)

## Altering
to change a database name
```SQL
alter database sample1 modify name = sample3
```
alternativ, you can use system stored procedure
```SQL
sp_renameDB 'sample3','sample4'
```
## Deleting
```SQL
drop database sample4
```
droping a database, deletes the LDF and MDF files.\
if database is currently in use, you cannot drop a database. You get an error stating.\
you need to put the database in single user mode.
```SQL
alter Database sample4 set single_user with rollback immediate
```
## Creating Tables
![Data Type](/44_SQL_Server/creating_table.JPG)
```SQL
use [Sample]
go

create tblPerson
(
ID int Not Null Primary Key,
Name nvarchar(50) Not Null,
Email nvarchar(50) Not Null,
GenderID int  
)

create table tblGender
(
ID int Not Null Primary Key,
Gender nvarchar(50) Not Null
)

alter table tblPerson add constraint tblPerson_GenderID_FK
foreign Key (GenderID) references tblGender(ID)
```

## Default Constraint
```SQL
Select * from tbtGender
Select * from tbtPerson

Insert into tblPerson (ID, Name, Email) values (7, 'Rich', 'r@r.com')

Alter Table tblPerson
Drop Constraint DF_tblPerson_GenderId

Alter TABLE tblPerson
Add CONSTRAINT DF_tblPerson_GenderID
Default 3 for GENDERID
```


# DML
## SELECT Statement
+ SELECT - defines which columns to return
+ FROM - defines table(s) to query
+ WHERE - filters rows using a predicate
+ GROUP BY - arranges rows by group
+ HAVING - filters group using a predicate
+ ORDER BY - sorts the output

```SQL
SELECT OrderDate, COUNT(OrderID)
FROM Sales.SalesOrder
WHERE Status = 'Shipped'
GROUP BY OrderDate
HAVING COUNT(OrderID) > 1
ORDER BY OrderDate DESC;
```

> Whenever you have a SELECT statement, the result of that is a   virtual table. It´s not a table that is stored in the database but it´s a record set of data.

> master database is a system database this used internally by the system

## Data Types
![Data Type](/44_SQL_Server/DataType.JPG)
+ Implicit Conversion: compatible data types can be automatically converted
+ Explicit Conversion: requires an explicit conversion function
  + CAST / TRY_CAST
  + CONVERT /TRY_CONVERT - use with data
  + PARSE / TRY_PARSE
  + STR

+ Working with NULLS
  + ISNULL: Returns value if the column or variable is NULL
  + NULLIF: Return NULL if the column or variable is value
  + COALESCE: Returns the value of the first non-NULL column of variable in the list

> NULL is used to indicate an unknown or missing value. NULL is not equivalent to zero or an empty string.

## Removing Duplicates
```SQL
Select DISTINCT color
FROM Production.Product;
```
? Test SELECT DISTINCT color, size ? o que acontece?

## Sorting Results
```SQL
--ORDER BY
SELECT ProductCategory AS Category, ProductName
FROM Production.Production
ORDER BY Category, Price DESC;
```
you can specify ASC or DESC (ASC is the default)
```SQL
-- TOP
SELECT TOP 10 ProductName, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;
```
limiting sorted results in number or percentage of rows.
```SQL
-- OFFSET-FETCH
ORDER BY <order_by_list>
OFFSET <offset_value> ROW(S)
FETCH FIRST|NEXT <fetch_value> ROW(S) ONLY
```
to use in a web page.

## Filtering and Using Predicates
+ =<>  : compare values for equality / non-equality
+ IN : determines whether a specified value matches any value in a subquery or a list
+ BETWEEN : specifies an inclusive range to test
+ LIKE : determines whethera specific character string matches a specified pattern, which can include wildcards
+ AND :  combines two Boolean expressions and return TRUE only when both are TRUE
+  OR :  combines two Boolean expressions and returns TRUE if either is TRUE
+ NOT : reverses the result of a search condition

specify predicates in the WHERE clause

# JOINS

+ Syntax ANSI SQL-92 (preferred syntax)
```SQL
SELECT ...
FROM Table1 JOIN Table2
     ON <on_predicate>;
```
+ Syntax ANSI SQL-89 (not recommended Cartesian products)
```SQL
SELECT ...
FROM Table1, Table2
WHERE <where_predicate>;
```

## INNER JOINS
```SQL
SELECT emp.FirstName, ord.Amount
FROM HR.Employee AS emp
[INNER] JOIN Sales.SalesOrder AS order_by_list
ON emp.EmployeeID = ord.EmployeeID
```

## OUTTER JOIN

# UNION
```SQL
SELECT FirstName, LastName, 'Employee' AS Type
FROM SalesLT.Employees
UNION ALL -- only UNION, it behaves the same as a DISTINCT.
SELECT FirstName, LastName, 'Costumers' -- as we mentioned before with aliases, I don´t need to alias this.
FROM SalesLT.Costumers
ORDER BY LastName
```
- we want one record set, all of the output in one place
- By default, UNION eliminates duplicate rows. Specify the ALL option to include duplicates (or to avoid the overhead of checking for duplicates when you know in advance that there are none).

# INTERSECT and EXCEPT

+ INTERSECT: returns only distinct rows that appear in both result sets

```SQL
SELECT conutryregion, city
FROM HR.Employees
INTERSECT
SELECT conutryregion, city
FROM Sales.Costumers;
```
+ EXCEPT: returns only distinct rows that appear in the first set but not the second.

## Using functions
+ Scalar functions return a single value based on zero or more input parameters
  + all built-in Function are actually scalar
  + user defined scalar function
  ```SQL
  CREATE FUNCTION Function_Name(@Parameter1 DataType, @Parameter2 DataType,.....)
  RETURNS Return_Datatype --except text, ntext, image, cursor, and timestamp
  AS
  BEGIN
    --Function Body
    Return Return_Datatype
  END
  ```

+ Logical function return Boolean values (true or false) based on an expression or column value.
+ Window functions are used to rank rows across partitions or "windows". Window functions include RANK, DENSE_RANK, NTILE, and ROW_NUMBER.
+ Aggregate functions are used to provide summary values for mulitple rows - for example, the total cost of products or the maximum number of items in an order. Commonly used aggregate functions include SUM, COUNT, MIN, MAX, and AVG.

# Aggregate functions

+ You can use GROUP BY with aggregate functions to return aggregations grouped by one or more columns or expressions.
+ All columns in the SELECT clause that are not aggregate function expressions must be included in a GROUP BY clause.
+ The order in which columns or expressions are listed in the GROUP BY clause determines the grouping hierarchy.
+ You can filter the groups that are included in the query results by specifying a HAVING clause.

## Subqueries

+ Subqueries are Transact-SQL queries nested within an outer query.
   + non-correlated subquery: sub query is not a dependent on outer query for its values
   + correlated subquery: sub query will get executed for every row for the outer query
+ Scalar subqueries return a single value.
+ Multi-valued subqueries return a single-column rowset.

## APPLY and CROSS APPLY

+ The APPLY operator enables you to execute a table-valued function for each row in a rowset returned by a SELECT statement. Conceptually, this approach is similar to a correlated subquery.
+ CROSS APPLY returns matching rows, similar to an inner join. OUTER APPLY returns all rows in the original SELECT query results with NULL values for rows where no match was found.

# Views
are named queries with definitions stored in a database
+ views can provide abstraction, encapsulation and simplification
+ from an administrative perspective, views can provide a security layer to a database
```SQL
CREATE VIEW Sales.vSalesOrders
AS
SELECT oh.OrderID
FROM Sales.OrderHearders AS oh
JOIN Sales.OrderDetails AS od
ON od.OrderID = oh.OrderID;
```

# Tables, temporary, variables, valued functions

## Temporary tables
+ Temporary tables are prefixed with a # symbol (You can also create global temporary tables that can be accessed by other processes by prefixing the name with ##)
+ Local temporary tables are automatically deleted when the session in which they were created ends. Global temporary tables are deleted when the last user sessions referencing them is closed.

## Table variables
+ Table variables are prefixed with a @ symbol.
+ Table variables are scoped to the batch in which they are created.

## Table-Valued Functions
```SQL
CREATE FUNCTION Sales.fn_GetOrderItems (@OrderID AS Integer)
RETURNS TABLE
AS
RETURN
(SELECT ProductID, UnitPrice, Quantity
FROM Sales.OrderDetails
WHERE OrderID = @OrderID);
...
SELECT * FROM Sales.fn_GetOrderItems (1025)AS LineItems;
```

+ Table-Valued Functions (TVFs) are functions that return a rowset. (kind of view)
+ TVFs can be parameterized.

## Derived Tables

## Common Table Expressions
+ CTEs are named table expressions defined in a query
+ CTEs are similar to derived tables in scope and naming requirements
+ Unlike derived tables, CTEs support multiple references and recursion
```SQL
WITH CTE_year(OrderYear, CustID)
AS
(
  SELECT YEAR(orderdate), custid
  FROM Sales.Orders
)
SELECT OrderYear, COUNT(DISTINCT CustID) AS Cust_Count
FROM CTE_year
GROUP BY orderyear;
```

# GROUPING SET

+ Use GROUPING SETS to define custom groupings.
+ Use ROLLUP to include subtotals and a grand total for hierarchical groupings.
+ Use CUBE to include all possible groupings.

# PIVOTING DATA

+ Use PIVOT to re-orient a rowset by generating mulitple columns from values in a single column.
+ Use UNPIVOT to re-orient mulitple columns in a an existing rowset into a single column.
