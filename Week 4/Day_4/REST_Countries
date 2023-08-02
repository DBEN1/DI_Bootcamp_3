import requests
import random
import sqlite3

# Database connection and cursor setup
conn = sqlite3.connect('countries.db')
cursor = conn.cursor()

# Create a table to store the countries' information if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    name TEXT,
                    capital TEXT,
                    flag TEXT,
                    subregion TEXT,
                    population INTEGER
                )''')
conn.commit()

# API endpoint to get information about all countries
url = 'https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population'

try:
    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Randomly select 10 countries
    random_countries = random.sample(data, 10)

    # Insert the selected countries into the database
    for country in random_countries:
        name = country['name']['common']
        capital = country['capital'][0] if 'capital' in country else 'N/A'
        
        # Check if 'flags' key exists and is a list
        if 'flags' in country and isinstance(country['flags'], list):
            flag = country['flags'][0]
        else:
            flag = 'N/A'
        
        subregion = country['subregion'] if 'subregion' in country else 'N/A'
        population = country['population'] if 'population' in country else 0

        # Insert the country's information into the table
        cursor.execute('''INSERT INTO countries (name, capital, flag, subregion, population)
                          VALUES (?, ?, ?, ?, ?)''', (name, capital, flag, subregion, population))

    conn.commit()
    print("10 random countries successfully added to the database!")

except requests.exceptions.RequestException as e:
    print("Error occurred while making the API request:", e)

finally:
    # Close the database connection
    conn.close()
