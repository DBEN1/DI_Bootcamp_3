-- -- Database: Bootcamp

-- -- DROP DATABASE IF EXISTS "Bootcamp";

-- CREATE DATABASE "Bootcamp"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- COMMENT ON DATABASE "Bootcamp"
--     IS 'ex 1+';

-- creating 2 tables:
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INTEGER UNIQUE REFERENCES Customer(id)
);

-- insert customers:
INSERT INTO Customer (first_name, last_name) VALUES ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

-- customer profiles
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
SELECT true, id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe';

INSERT INTO CustomerProfile (isLoggedIn, customer_id)
SELECT false, id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu';

-- To get the first_name of the loggedIn customers:

SELECT C.first_name
FROM Customer C
INNER JOIN CustomerProfile CP ON C.id = CP.customer_id
WHERE CP.isLoggedIn;

--To get all customers' first_name and isLoggedIn columns:
SELECT C.first_name, CP.isLoggedIn
FROM Customer C
LEFT JOIN CustomerProfile CP ON C.id = CP.customer_id;

-- And finally, to get the number of customers that are not loggedIn:
SELECT COUNT(*)
FROM Customer C
LEFT JOIN CustomerProfile CP ON C.id = CP.customer_id
WHERE CP.isLoggedIn IS NULL OR CP.isLoggedIn = false;


