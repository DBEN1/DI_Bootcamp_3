-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

-- CREATE DATABASE "Hollywood"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

-- Count how many actors are in the table:

SELECT COUNT(*) FROM actors;

-- Try to add a new actor with some blank fields.
INSERT INTO actors (first_name, last_name, age, number_oscars) 
VALUES ('', 'Doe', '1970-01-01', 1);

-- I won't be able to insert a new actor with blank fields in the first_name 
-- last_name or age columns. Those fields have been defined as NOT NULL 
-- meaning that they cannot be left empty. 
-- However empty string ('') will work / technically a value.