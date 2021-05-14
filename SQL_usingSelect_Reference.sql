-- SELECT STATEMENTS
-- 1. Projection = choose the columns in the table you want returned
-- 2. Selection = choosing rows in a table you want back
-- 3. Joining = bring data together from different tables

USE BikeStores;

-- ****************** Select Command *************************

-- select all columns from a table
SELECT * FROM sales.customers;

-- select distinct columns from table
SELECT first_name, last_name FROM sales.customers;




-- ****************** Arithmetic Expressions *************************

SELECT * FROM production.products;

-- what price would be if there was a 20% off sale

SELECT
    product_name,
    list_price * 0.80
FROM
    production.products;



-- ****************** Column Alias *************************

-- column alias: temporary name for column when doing selection

SELECT
    product_name,
    list_price * 0.80 AS '20% Off Sale Price'
FROM
    production.products;



-- ****************** Where *************************

-- anything that follows a where clause, is the condition for filtering out rows in selection
-- can also be used in updates and deletes

SELECT * FROM production.products
WHERE list_price > 3000 AND model_year = '2017';




-- ****************** Order By *************************

-- order by -> sorting data by ascending/descending value of a particular column

-- ascending (A-Z, or 1-100[lowest to highest])
SELECT * FROM sales.customers
ORDER BY first_name;

SELECT * FROM sales.customers
ORDER BY first_name ASC;

SELECT * FROM sales.customers
ORDER BY customer_id ASC;

-- descending (Z-A, or 100-1 [highest to lowest])
SELECT * FROM sales.customers
ORDER BY first_name DESC;

SELECT * FROM sales.customers
ORDER BY customer_id DESC;

-- multicolumn sorts

SELECT * FROM sales.customers
ORDER BY first_name, last_name;



-- ****************** Distinct *************************

-- used to eliminate duplicate records for viewing purpose only

-- Adriene shown twice
SELECT first_name
FROM sales.customers
ORDER BY first_name;

-- Adriene listed once
SELECT DISTINCT first_name
FROM sales.customers
ORDER BY first_name;



-- ****************** Logical Conditions *************************

-- AND, OR, NOT (checking conditions)

SELECT * FROM production.products;

-- AND -> filter based on both conditions stated (both must be true)

SELECT * FROM production.products WHERE model_year = 2016 AND list_price > 1000;

-- OR -> at least one must be true

SELECT * FROM production.products WHERE model_year = 2016 OR list_price > 1000;

-- NOT -> if it's true, make it false, both statements below are the same

SELECT * FROM production.products WHERE NOT model_year = 2016;
--or (!= means NOT)
SELECT * FROM production.products WHERE model_year != 2016;



-- ****************** Comparison Conditions *************************

-- Operator Comparisons

-- OPERATORS    MEANING
-- =            Equal to
-- >            Greater than
-- >=           Greater than or equal to
-- <            Less than
-- <=           Less than or equal to
-- <>, !=, ^=   Not equal to
-- !<           Not less than
-- !>           Not greater than

SELECT * FROM production.products WHERE list_price <= 2000;


-- ****************** Between *************************

-- the range for between will include 1000 and 2000

SELECT * FROM production.products WHERE list_price BETWEEN 1000 AND 2000;

SELECT * FROM production.products WHERE product_id BETWEEN 1 AND 4;


-- ****************** In *************************

-- tests if a value is in the list given

SELECT * FROM production.products WHERE brand_id IN(9,5,2);


-- ****************** Like *************************

-- looks for a string pattern that matches it

-- %                denotes zero or more characters
-- _                denotes one character
-- [ ]              denotes any single character in the specified set
-- [ ch - ch ]      denotes any single character (ch) in specified range
-- [^]              denotes any single character not within a list or range

-- find first names that start with an 'a'

SELECT first_name FROM sales.customers WHERE first_name LIKE 'a%' ORDER BY first_name;

-- second letter to be an 'a'

SELECT first_name FROM sales.customers WHERE first_name LIKE '_a%' ORDER BY first_name;

-- search for names that have 'bart'

SELECT first_name FROM sales.customers WHERE first_name LIKE '%bart%' ORDER BY first_name;

-- last letter is an 'a' or 'y'

SELECT first_name FROM sales.customers WHERE first_name LIKE '%[ay]' ORDER BY first_name;

-- starts with letters between x-z (x,y,z)

SELECT first_name FROM sales.customers WHERE first_name LIKE '[x-z]%' ORDER BY first_name;

-- does not start with letters x,y,z

SELECT first_name FROM sales.customers WHERE first_name LIKE '[^x-z]%' ORDER BY first_name;





-- ****************** IS NULL / IS NOT NULL *************************

SELECT * FROM sales.staffs;

-- only one null in manager_id column

SELECT * FROM sales.staffs;

-- select all staff that have a null for manager_id

SELECT * FROM sales.staffs WHERE manager_id IS NULL;

-- checking for if not null 

SELECT * FROM sales.staffs WHERE manager_id IS NOT NULL;









-- ****************** LIMITING ROWS *************************

-- OFFSET FETCH
-- limit rows you get back and skip rows 
-- options when using ORDER BY clause

SELECT * FROM production.brands;

-- skips first 3 rows

SELECT * FROM production.brands
ORDER BY brand_name
OFFSET 3 ROWS;

-- skip first 3 rows, grab next 2 rows 
SELECT * FROM production.brands
ORDER BY brand_name
OFFSET 3 ROWS
FETCH NEXT 2 ROWS ONLY;



-- SELECT TOP
-- limit number of rows or percent of rows returned
-- used with ORDER BY clause

-- 5 most expensive products
SELECT TOP 5 * FROM production.products
ORDER BY list_price DESC;

-- distinct

SELECT DISTINCT TOP 5 list_price FROM production.products ORDER BY list_price DESC;

-- select top percent of rows
-- order this by highest list price, then get the top 5 percent of rows that have the highest list price
-- products table: 321 rows, 5% of 321 is about 17, so will grab first 17 rows
SELECT TOP 5 PERCENT * FROM production.products ORDER BY list_price DESC;
--or if you want to get a more averaged number
SELECT TOP 5 PERCENT WITH TIES * FROM production.products ORDER BY list_price DESC;
