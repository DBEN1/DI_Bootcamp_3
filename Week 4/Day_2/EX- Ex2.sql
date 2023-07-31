-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

-- CREATE DATABASE dvdrental
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
	
-- Select all the columns from the “customer” table:
SELECT * FROM customer;
-- Display the names (first_name, last_name) using an alias named “full_name”:
SELECT first_name || ' ' || last_name AS full_name FROM customer;
-- Select all the create_date from the “customer” table (there should be no duplicates):
SELECT DISTINCT create_date FROM customer;
-- Get all the customer details from the customer table, it should be displayed in descending order by their first name:
SELECT * FROM customer ORDER BY first_name DESC;
-- Get the film ID, title, description, year of release, and rental rate in ascending order according to their rental rate:
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
SELECT address, phone FROM address JOIN customer ON address.address_id = customer.address_id WHERE district = 'Texas';
-- Retrieve all movie details where the movie id is either 15 or 150:
SELECT * FROM film WHERE film_id IN (15, 150);
-- Check if your favorite movie exists in the database (I'm using 'Titanic' as an example):
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Notting Hill';
-- Get the film ID, title, description, length, and the rental rate of all the movies starting with 'Ti':
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Ti%';
-- Find the 10 cheapest movies:
SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;
-- Find the next 10 cheapest movies:
SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10;
-- Join the data in the customer table and the payment table:
SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date 
FROM customer 
JOIN payment ON customer.customer_id = payment.customer_id 
ORDER BY customer.customer_id;
--Get all the movies which are not in inventory:
SELECT * FROM film WHERE film_id NOT IN (SELECT film_id FROM inventory);
-- Find which city is in which country:
SELECT city.city, country.country FROM city JOIN country ON city.country_id = country.country_id;
-- Get the customer’s id, names (first and last), the amount, and the date of payment ordered by the id of the staff member who sold them the DVD:
SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date 
FROM customer 
JOIN payment ON customer.customer_id = payment.customer_id 
ORDER BY payment.staff_id;

