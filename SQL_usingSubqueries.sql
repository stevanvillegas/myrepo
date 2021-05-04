-- SUBQUERIES
-- a query within another query
-- a subquery returns some data that can be used by an outer query

USE BikeStores;



-- ******************************* SUBQUERIES *********************************************

-- find the order id, order date, and customer id of all customers 
-- who have a phone number (phone isn't NULL)
SELECT * FROM sales.orders;
SELECT * FROM sales.customers;

-- step 1: write query to find customers with phone numbers (not null)
SELECT
    *
FROM sales.customers
WHERE
    phone IS NOT NULL;

-- step 2: write query to get order id, order date, and customer id within orders table
SELECT
    order_id,
    order_id,
    customer_id
FROM 
    sales.orders;

-- step 3: combine queries
-- to combine and set up link between two queries (customer id)
-- use IN clause b/c get back a list of customer ids that will have a phone number
SELECT
    order_id,
    order_date,
    customer_id
FROM    
    sales.orders
WHERE
    customer_id IN (
        SELECT
            customer_id
        FROM
            sales.customers
        WHERE
            phone IS NOT NULL
    );


-- products table has list prices
-- select all the products that have a list price above the average list price for table

-- average list price for the entire table
SELECT
    AVG(list_price)
FROM
    production.products;



-- using subquery for calculations
-- products above average list price for whole table
SELECT 
    product_name,
    list_price
FROM
    production.products
WHERE 
    list_price > (
            SELECT
                AVG(list_price)
            FROM
                production.products
    );




-- ******************************* CORRELATED SUBQUERIES *********************************************
-- an inner query that depends on the outer query for its values
-- inner query will have accress to information from the outer query

-- find all the products whose list price above the average for their category
-- ex: category 1 has an average of 2000, every row that has a category of 1 will only
-- display if they have a list price above that

-- information for each product that has the highest list price for its category
SELECT
    product_name,
    list_price,
    category_id
FROM
    production.products p1
WHERE
    list_price IN (
        SELECT
            MAX(p2.list_price)
        FROM
            production.products p2
        WHERE
            p2.category_id = p1.category_id
        GROUP BY
            p2.category_id
    );
