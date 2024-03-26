--  a script that lists all the tables of a database in your MySQL server.
USE INFORMATION_SCHEMA;

SELECT TABLE_NAME
FROM TABLES
WHERE TABLE_SCHEMA = 'mysql';

