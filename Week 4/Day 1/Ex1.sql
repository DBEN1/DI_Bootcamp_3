-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--    OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- COMMENT ON DATABASE public
--     IS 'Ex1 ';


CREATE TABLE public.items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    item_description TEXT,
    item_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE public.customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20)
);

INSERT INTO public.items (item_id, item_name, item_price)
VALUES (1, 'Small Desk', 100.00);

INSERT INTO public.items (item_id, item_name, item_price)
VALUES (2, 'Large Desk', 300.00);

INSERT INTO public.items (item_id, item_name, item_price)
VALUES (3, 'Fan', 80.00);

INSERT INTO public.customers (customer_id, first_name, last_name)
VALUES (1, 'Greg', 'Jones');

INSERT INTO public.customers (customer_id, first_name, last_name)
VALUES (2, 'Sandra', 'Jones');

INSERT INTO public.customers (customer_id, first_name, last_name)
VALUES (3, 'Scott', 'Scott');

INSERT INTO public.customers (customer_id, first_name, last_name)
VALUES (4, 'Trevor', 'Green');

INSERT INTO public.customers (customer_id, first_name, last_name)
VALUES (5, 'Melanie', 'Johnson');


-- fetching
-- All the items
SELECT * FROM public.items;
-- All the items with a price above 80 (80 not included):
SELECT * FROM public.items WHERE item_price > 80;
-- All the items with a price below 300 (300 included):
SELECT * FROM public.items WHERE item_price <= 300;
-- All customers whose last name is 'Smith':
SELECT * FROM public.customers WHERE last_name = 'Smith';
-- All customers whose last name is 'Jones':
SELECT * FROM public.customers WHERE last_name = 'Jones';
-- All customers whose first name is not 'Scott':
SELECT * FROM public.customers WHERE first_name != 'Scott';


