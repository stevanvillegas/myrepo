-- ********************************** JOIN ********************************************
-- used to combine data from two or more tables through a common field (usually a foreign key)

USE Practice_DB;

CREATE TABLE tmp.customer
(
    cust_id INT PRIMARY KEY IDENTITY,
    f_name VARCHAR(30) NOT NULL,
    l_name VARCHAR(30) NOT NULL
);
INSERT INTO 
    tmp.customer(f_name, l_name)
VALUES
    ('Sam', 'Miller'),
    ('Juan', 'Del Mar'),
    ('Gina', 'Stokes'),
    ('Dorothy', 'Crawford'),
    ('Michael', 'Allen'),
    ('Lori', 'Gutierrez'),
    ('Terrell', 'Wood');
SELECT * FROM tmp.customer;
CREATE TABLE tmp.orders
(
    o_id INT PRIMARY KEY IDENTITY,
    order_date DATE NOT NULL,
    cust_id INT,
    FOREIGN KEY (cust_id) REFERENCES tmp.customer(cust_id)
);
INSERT INTO
    tmp.orders(order_date, cust_id)
VALUES
    (GETDATE(), 2),
    (GETDATE(), 2),
    (GETDATE(), 5),
    (GETDATE(), 6),
    (GETDATE(), 3),
    (GETDATE(), 3),
    (GETDATE(), 2),
    (GETDATE(), 2),
    (GETDATE(), NULL),
    (GETDATE(), 6),
    (GETDATE(), 5),
    (GETDATE(), NULL);
SELECT * FROM tmp.orders;






--*********************************** INNER JOIN *****************************************
-- select all rows between tables if there is a common field between them

-- missing two orders b/c no customer associated with them
-- missing customers who don't have any orders linked to them
SELECT
    *
FROM
    tmp.orders o -- an alias for the table is created = 'o'
INNER JOIN
    tmp.customer c -- an alias for the table is created = 'c'
ON
    o.cust_id = c.cust_id;








--*********************************** LEFT JOIN *****************************************
-- returns all the rows from the left table and only the matching rows from the right table

-- left table  -> table listed first in the query
-- right table -> table listed second in the query

-- all records from left table (orders) are shown, will display nulls where no customer info can be given

SELECT
    *
FROM
    tmp.orders o -- an alias for the table is created = 'o'
LEFT JOIN
    tmp.customer c -- an alias for the table is created = 'c'
ON
    o.cust_id = c.cust_id;





--*********************************** RIGHT JOIN *****************************************
-- returns all rows from right table and only matching rows from the left table

-- all customers shown, no orders shown if they don't have a link to a customer
SELECT
    *
FROM
    tmp.orders o 
RIGHT JOIN
    tmp.customer c 
ON
    o.cust_id = c.cust_id;

-- select exact data as above but with left join
SELECT
    *
FROM
    tmp.customer c 
LEFT JOIN
    tmp.orders o 
ON
    o.cust_id = c.cust_id;








--*********************************** FULL OUTER JOIN *****************************************
-- returns all rows, regardless of if there is a common field between them

-- shows records for all orders
-- as well, lists ALL customers
SELECT
    *
FROM
    tmp.orders o
FULL JOIN
    tmp.customer c
ON
    o.cust_id = c.cust_id;









--*********************************** MULTI JOIN *****************************************
-- if you need to join multiple tables

USE BikeStores;

SELECT * FROM  production.products;
SELECT * FROM production.brands;
SELECT * FROM production.categories;

-- get the product id, name, brand name

SELECT
    product_id,
    product_name,
    brand_name
FROM 
    production.products p
LEFT JOIN
    production.brands b
ON
    p.brand_id = b.brand_id;

-- get the product id, name, brand name, category name

SELECT
    product_id,
    product_name,
    brand_name,
    category_name
FROM 
    production.products p -- left table
LEFT JOIN
    production.brands b -- joining on the product table (right table)
ON
    p.brand_id = b.brand_id
LEFT JOIN
    production.categories c -- joining on the product table (right table)
ON
    p.category_id = c.category_id;


-- can add in order by, group by, where, etc.

SELECT
    product_id,
    product_name,
    brand_name,
    category_name,
    list_price
FROM 
    production.products p
LEFT JOIN
    production.brands b
ON
    p.brand_id = b.brand_id
LEFT JOIN
    production.categories c
ON
    p.category_id = c.category_id
WHERE
    list_price < 1000;










--*********************************** SELF JOIN *****************************************
-- self joins are when join a table to itself
-- compare rows within the same table

SELECT * FROM sales.staffs;

SELECT
    e.first_name + ' ' + e.last_name 'staff member',
    m.first_name + ' ' + m.last_name 'manager'
FROM
    sales.staffs e -- foreign key: manager_id
LEFT JOIN
    sales.staffs m -- referenced foreign key: staff_id
ON
    e.manager_id = m.staff_id;
