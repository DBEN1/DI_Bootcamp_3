# Exercise 1 

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Dict1 = dict(zip(keys, values))
print(Dict1)

# Exercise 2 
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

ticket_prices = {
    "free": 0,
    "child": 10,
    "adult": 15
}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = ticket_prices["free"]
    elif age >= 3 and age <= 12:
        price = ticket_prices["child"]
    else:
        price = ticket_prices["adult"]
    
    print(f"{name} has to pay ${price}")
    total_cost += price

print(f"\nTotal cost for the movies: ${total_cost}")

# Exercise 3
# Step 2: Create the 'brand' dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# Step 3: Change the number of stores to 2
brand["number_stores"] = 2

# Step 4: Print a sentence describing Zara's clients
print(f"Zara's clients are men, women, and children.")

# Step 5: Add a key 'country_creation' with a value of 'Spain'
brand["country_creation"] = "Spain"

# Step 6: Check if 'international_competitors' key is in the dictionary and add 'Desigual' if it is
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Step 7: Delete the information about the date of creation
del brand["creation_date"]

# Step 8: Print the last international competitor
last_competitor = brand["international_competitors"][-1]
print(f"The last international competitor is {last_competitor}.")

# Step 9: Print the major clothes colors in the US
us_colors = brand["major_color"]["US"]
print("The major clothes colors in the US are:", ", ".join(us_colors))

# Step 10: Print the amount of key-value pairs in the dictionary
num_pairs = len(brand)
print(f"The dictionary has {num_pairs} key-value pairs.")

# Step 11: Print the keys of the dictionary
print("Keys of the dictionary:", list(brand.keys()))

# Step 12: Create the 'more_on_zara' dictionary
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Step 13: Add the information from 'more_on_zara' to the 'brand' dictionary
brand.update(more_on_zara)

# Step 14: Print the value of the key 'number_stores'
print("The value of the key 'number_stores' is:", brand["number_stores"])

Exercise 4 : 
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Recreate the 1st result using a for loop
disney_users_A = {}
for index, user in enumerate(users):
    disney_users_A[user] = index
print(disney_users_A)

# Recreate the 2nd result using a for loop
disney_users_B = {}
for index, user in enumerate(users):
    disney_users_B[index] = user
print(disney_users_B)

# Recreate the 3rd result using the sorted() method
disney_users_C = {}
sorted_users = sorted(users)
for index, user in enumerate(sorted_users):
    disney_users_C[user] = index
print(disney_users_C)

# Recreate the 1st result for names containing the letter "i"
disney_users_A_filtered = {}
for index, user in enumerate(users):
    if 'i' in user.lower():
        disney_users_A_filtered[user] = index
print(disney_users_A_filtered)

# Recreate the 1st result for names starting with "m" or "p"
disney_users_A_filtered_2 = {}
for index, user in enumerate(users):
    if user[0].lower() in ['m', 'p']:
        disney_users_A_filtered_2[user] = index
print(disney_users_A_filtered_2)
