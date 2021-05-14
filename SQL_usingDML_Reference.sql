USE Practice_DB;

-- *********** INSERT COMMAND ************************************************

-- insert is used to add new rows of data

-- insert by stating table(col1, col2, etc.) VALUES (val1, val2, etc.)
INSERT INTO tmp.person(name,ssn, dob, gender)
                VALUES('hello', '123456780', GETDATE(), 'F');

select * from tmp.person

-- can remove columns if not required for inserting a new row (id, dob, gender)
INSERT INTO tmp.person(name, ssn)
                VALUES('hello', '123456781');
select * from tmp.person



-- mutli inserts --> inserts with a single statement
INSERT INTO tmp.person(name, ssn)
                VALUES
                    ('hello', '123456782'),
                    ('hello', '123894832');

select * from tmp.person;


-- *********** UPDATE COMMAND ************************************************

-- update used to modify existing data in a table

--updating one record
UPDATE tmp.person
SET name = 'world'
WHERE p_id = 2;

select * from tmp.person;

-- update multiple columns
UPDATE tmp.person
SET name = 'hi', gender = 'M'
WHERE name = 'hello';

select * from tmp.person;


-- *********** DELETE COMMAND ************************************************

-- removing a row of data from table

DELETE FROM tmp.person
WHERE p_id = 4;

select * from tmp.person;


-- if you don't specify a where clause, everything gets deleted
-- DELETE FROM tmp.person;

-- this gives you an empty table

-- a delete can be undone, a truncate is permanent (can't recover that data)
-- deleting a whole table takes longer than truncating it
