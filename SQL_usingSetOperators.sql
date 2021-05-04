-- SET OPERATORS
-- combine data from two or more queries

USE Practice_DB;

CREATE SCHEMA setop;
GO

CREATE TABLE setop.student
(
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(30) NOT NULL,
    dob DATE,
    dept VARCHAR(30) NOT NULL
);

INSERT INTO setop.student(name, dob, dept)
VALUES
    ('Raphael', '1984-09-23', 'Computer Science'),
    ('Donatello', '1984-07-20', 'Computer Science'),
    ('Michaelangelo', '1984-09-23', 'Accounting'),
    ('Leonardo', '1984-11-17', 'History');

SELECT * FROM setop.student;

CREATE TABLE setop.professor
(
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(30) NOT NULL,
    dob DATE,
    dept VARCHAR(30) NOT NULL,
    phone VARCHAR(10)
);

INSERT INTO setop.professor(name, dob, dept, phone)
VALUES
    ('Blossum', '1984-09-23', 'Computer Science', '111-1111'),
    ('Buttercup', '1995-04-13', 'History', '121-1221'),
    ('Bubbles', '1991-12-01', 'Computer Science', '211-1112'),
    ('Mojo Jojo', '1984-09-23', 'Art', '222-1111'),
    ('Leonardo', '1984-11-17', 'History', '111-2222');

SELECT * FROM setop.professor;







--************************* UNION ***************************************************
-- combine results from two SELECT statements into a single result set

-- Requirements:
-- 1. number and order of columns from two statements are same
-- 2. data types of columns must be same or compatible

SELECT * FROM setop.student;
SELECT * FROM setop.professor;

-- get all the names of the students and professors
SELECT name, dept FROM setop.student
    UNION
SELECT name, dept FROM setop.professor;

-- UNION won't contain any duplicate values
SELECT name FROM setop.student
    UNION
SELECT name FROM setop.professor;

-- UNION ALL allows for duplicates
SELECT name FROM setop.student
    UNION ALL
SELECT name FROM setop.professor;







--************************* INTERSECT ***************************************************
-- combines reults of two queries and returns only the rows that are the same between them

SELECT * FROM setop.student; -- CS, Accounting, History
SELECT * FROM setop.professor; -- CS, History, Art

SELECT dept FROM setop.student
    INTERSECT
SELECT dept FROM setop.professor;




--************************* EXCEPT ***************************************************
-- take first query and remove any rows that are the same as the second query provided

-- departments that are unique to student and ot listed in the professor table
SELECT dept FROM setop.student
    EXCEPT
SELECT dept FROM setop.professor;
