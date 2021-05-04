-- Transactions

-- turn off autocommit
SET IMPLICIT_TRANSACTIONS OFF;

SELECT * FROM tmp.person;

BEGIN TRANSACTION;

INSERT INTO tmp.person(name, ssn)
                VALUES
                    ('hello', '123456782'),
                    ('hello', '123894832');

select * from tmp.person;
-- the saved state of my db has 4 rows in my person table
COMMIT TRANSACTION;

BEGIN TRANSACTION;
-- transaction made up of 1 statement
UPDATE tmp.person SET name = 'different' WHERE name = 'hello';
-- undo transaction
ROLLBACK;

select * from tmp.person;

