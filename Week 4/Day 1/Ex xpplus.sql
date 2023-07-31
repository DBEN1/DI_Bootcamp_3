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


CREATE TABLE bootcamp.students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE
);

INSERT INTO bootcamp.students (first_name, last_name, birth_date)
VALUES 
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03'),
('Dan', 'Benguira', '1994-01-21');

-- Fetch all of the data from the table
SELECT * FROM bootcamp.students;
-- Fetch all of the students first_names and last_names:
SELECT first_name, last_name FROM bootcamp.students;
-- Fetch the student which id is equal to 2:
SELECT first_name, last_name FROM bootcamp.students WHERE id = 2;
-- Fetch the student whose last_name is Benichou AND first_name is Marc:
SELECT first_name, last_name FROM bootcamp.students WHERE last_name = 'Benichou' AND first_name = 'Marc';
-- Fetch the students whose last_names are Benichou OR first_names are Marc:
SELECT first_name, last_name FROM bootcamp.students WHERE last_name = 'Benichou' OR first_name = 'Marc';
-- Fetch the students whose first_names contain the letter 'a':
SELECT first_name, last_name FROM bootcamp.students WHERE first_name LIKE '%a%';
-- Fetch the students whose first_names start with the letter 'a':
SELECT first_name, last_name FROM bootcamp.students WHERE first_name LIKE 'a%';
-- Fetch the students whose first_names end with the letter 'a':
SELECT first_name, last_name FROM bootcamp.students WHERE first_name LIKE '%a';
-- Fetch the students whose second to last letter of their first_names are 'a' (Example: Leah):
SELECT first_name, last_name FROM bootcamp.students WHERE first_name LIKE '%a_';
-- Fetch the students whose ids are equal to 1 AND 3:
SELECT first_name, last_name FROM bootcamp.students WHERE id IN (1, 3);
-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info):
SELECT * FROM bootcamp.students WHERE birth_date >= '2000-01-01';

 
