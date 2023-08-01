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

-- Get a list of all the languages, from the language table:
SELECT * FROM language;
-- Get a list of all films joined with their languages:
SELECT film.title, film.description, language.name AS language_name 
FROM film
INNER JOIN language ON film.language_id = language.language_id;
-- Get all languages, even if there are no films in those languages:
SELECT film.title, film.description, language.name AS language_name 
FROM language
LEFT JOIN film ON language.language_id = film.language_id;
-- Create a new table called new_film and add some films:
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO new_film (name) VALUES ('Film1'), ('Film2'), ('Film3');
-- Create a new table called customer_review:
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255),
    score INTEGER CHECK(score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Add 2 movie reviews:
INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
VALUES 
(1, 1, 'Great Film', 8, 'I really enjoyed this film. Great acting and plot.'),
(2, 1, 'Not My Cup of Tea', 4, 'The film was too slow for my liking.');
-- Delete a film that has a review from the new_film table:
DELETE FROM new_film WHERE id = 1;
-- What happens to the customer_review table?"
-- the ON DELETE CASCADE clause in the customer_review table's 
-- definition means that if a row in the new_film table is deleted, 
-- then all related rows in the customer_review table 
-- (i.e., reviews of the deleted film) are also automatically deleted.

-- Change the language of some films
UPDATE film
SET language_id = 3
WHERE film_id IN (1, 2);
-- To identify which foreign keys are defined for the customer table
SELECT conname, confrelid::regclass 
FROM pg_constraint 
WHERE confrelid = 'customer'::regclass;
-- dropping the customer review table
DROP TABLE customer_review;
-- To find out how many rentals are still outstanding:
SELECT COUNT(*) 
FROM rental 
WHERE return_date IS NULL;
-- To find the 30 most expensive movies which are outstanding:
SELECT film.title, film.replacement_cost 
FROM film 
JOIN inventory ON film.film_id = inventory.film_id 
JOIN rental ON inventory.inventory_id = rental.inventory_id 
WHERE rental.return_date IS NULL 
ORDER BY film.replacement_cost DESC 
LIMIT 30;
 -- find 1st film : 
 SELECT film.title 
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id 
JOIN actor ON film_actor.actor_id = actor.actor_id 
WHERE film.description LIKE '%sumo wrestler%' AND actor.first_name = 'Penelope' AND actor.last_name = 'Monroe';
-- 2nd film
SELECT title 
FROM film 
WHERE length < 60 AND rating = 'R';
-- 3rd film
SELECT film.title 
FROM film 
JOIN inventory ON film.film_id = inventory.film_id 
JOIN rental ON inventory.inventory_id = rental.rental_id 
JOIN payment ON inventory.inventory_id = payment.rental_id 
JOIN customer ON rental.customer_id = customer.customer_id 
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND payment.amount > 4.00 AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';
-- 4th film:
SELECT film.title 
FROM film 
JOIN inventory ON film.film_id = inventory.film_id 
JOIN rental ON inventory.inventory_id = rental.rental_id 
JOIN customer ON rental.customer_id = customer.customer_id 
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND (film.title LIKE '%boat%' OR film.description LIKE '%boat%') AND film.replacement_cost > (SELECT AVG(film.replacement_cost) FROM film);
