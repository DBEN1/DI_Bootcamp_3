# # Exercise 1 
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f"{self.amount} {self.currency}s"

#     def __int__(self):
#         return self.amount

#     def __repr__(self):
#         return str(self)

#     def __add__(self, other):
#         if isinstance(other, int):
#             return Currency(self.currency, self.amount + other)
#         elif isinstance(other, self.__class__):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             raise TypeError("Unsupported operand type for +")

#     def __radd__(self, other):
#         return self.__add__(other)

#     def __iadd__(self, other):
#         result = self.__add__(other)
#         self.amount = result.amount
#         return self

# # Exercise 2 

# # File: exercise_one.py



# from func import add_numbers
# add_numbers(5, 7)

# #exercise 3
# import random

# def guess_and_roll(guess):
#     if not 1 <= guess <= 100:
#         print("Guess must be between 1 and 100.")
#         return
#     roll = random.randint(1, 100)
#     if roll == guess:
#         print("Success! Your guess was correct.")
#     else:
#         print(f"Sorry, your guess was incorrect. The rolled number was {roll}.")

# # Call the function with a number between 1 and 100
# guess_and_roll(50)


# #Exercise 4 
# import random
# import string

# def generate_random_string(length):
#     # Combine all the letters
#     letters = string.ascii_letters  # this contains both lower case and upper case letters
#     # Choose `length` random characters from `letters`
#     result_str = ''.join(random.choice(letters) for _ in range(length))
#     return result_str

# # Generate a random string of length 5
# print(generate_random_string(5))

# #Exercise 5
# from datetime import datetime

# def display_current_date():
#     # Get the current date
#     current_date = datetime.today().date()
#     # Display the date
#     print(current_date)

# # Call the function
# display_current_date()

# #Exercise 6
# from datetime import datetime, timedelta

# def time_until_new_year():
#     now = datetime.now()
#     current_year = now.year
    
#     # Check if January 1st has already passed this year
#     if now.month == 1 and now.day == 1:
#         new_year = datetime(current_year + 1, 1, 1)
#     else:
#         new_year = datetime(current_year + 1, 1, 1)

#     # Calculate the time difference
#     diff = new_year - now

#     days, seconds = diff.days, diff.seconds
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60

#     print(f"The 1st of January is in {days} days and {hours}:{minutes}:{seconds} hours.")

# # Call the function
# time_until_new_year()


#Exercise 7
from datetime import datetime

def calculate_minutes_lived(birthdate_str):
    # Parse the birthdate string into a datetime object
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    
    # Calculate the difference between now and the birthdate
    lived = datetime.now() - birthdate

    # Convert the difference to minutes (1 day = 24*60 minutes)
    minutes_lived = lived.total_seconds() / 60

    print(f"You have lived for approximately {int(minutes_lived)} minutes.")

# Call the function with a birthdate
calculate_minutes_lived('1994-01-21')

#Exercise 5
from faker import Faker

# Create a Faker instance
fake = Faker()

# Create an empty list of users
users = []

def add_user():
    # Create a new user with fake data
    user = {
        "name": fake.name(),
        "address": fake.address().replace('\n', ', '),
        "language_code": fake.language_code(),
    }
    # Add the new user to the list
    users.append(user)

# Add a few users
for _ in range(10):
    add_user()

# Print the list of users
for user in users:
    print(user)
