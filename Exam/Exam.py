# Exam
# Python Basics

# Data Types
# Q: Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set
# Answer: c) Tuple

# Lists and Loops
# Q: Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.
squares_of_even = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares_of_even)

# Q: Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
numbers = [x for x in range(1, 11) if x % 2 == 0 and x % 3 == 0]
print(numbers)

# Q: Loop through the provided list of dictionaries and print the names and ages:
student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]
for student in student_list:
    print(student["name"], student["age"])

# Function Behavior with *args and **kwargs
# Q: Write a function combine_words that accepts any number of positional arguments and key-value arguments. 
# The function should return a single sentence combining all the words provided.
def combine_words(*args, **kwargs):
    sentence = " ".join(args) + "."
    additional_words = " ".join([kwargs[key] for key in sorted(kwargs.keys())])
    return sentence + " " + additional_words
print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# Object-Oriented Programming (OOP)

# Q: Create a class Vehicle with string attributes type, brand, and integer attribute year. 
# Ensure instances of the vehicle cannot be created if any of these attributes are missing 
# and include a method to display the vehicle’s info. Use dunder method.
class Vehicle:
    def __init__(self, type, brand, year):
        if not all([type, brand, year]):
            raise ValueError("All attributes must be provided!")
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.type} - {self.brand} ({self.year})"

# OOP Inheritance and Decorators

# Q: Create a class Car with string attributes brand, model, and integer attribute mileage. 
# Implement a method to return the car’s details.
class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def details(self):
        return f"{self.brand} {self.model} with {self.mileage} miles"

# Q: Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. 
# Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.
class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if value > 0:
            self.__battery_capacity = value

    def details(self):
        base_details = super().details()
        return f"{base_details} and a battery capacity of {self.__battery_capacity} kWh"

# OOP Inheritance and Decorators

# Q: Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. 
# Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created 
# and a static method for a bank policy message. Ensure the balance is non-negative.

class BankAccount:
    _accounts_created = 0

    def __init__(self, account_holder, initial_balance=0.0):
        self._account_holder = account_holder
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative!")
        self._balance = initial_balance
        BankAccount._accounts_created += 1

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount!")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount!")
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount

    def view_balance(self):
        return self._balance

    @classmethod
    def get_accounts_created(cls):
        return cls._accounts_created

    @staticmethod
    def bank_policy():
        return "This bank ensures the safety and security of its customers' funds."

# Test
account = BankAccount("John Doe", 100)
account.deposit(50)
account.withdraw(30)
print(account.view_balance())  # Expected: 120
print(BankAccount.bank_policy())  # Expected: This bank ensures the safety and security of its customers' funds.
print(BankAccount.get_accounts_created())  # Expected: 1

# Data Science

# Numpy and Pandas Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q: Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().
array_3x3 = np.arange(1, 10).reshape(3, 3)
print(array_3x3)

# Q: Provided pandas DataFrame df:
df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})

# Replace non-numeric values in column “A” with the mean of numeric values. 
# Plot a histogram of the “A” column using matplotlib.
df['A'] = pd.to_numeric(df['A'], errors='coerce')
mean_A = df['A'].mean()
df['A'].fillna(mean_A, inplace=True)
plt.hist(df['A'])
plt.title("Histogram of Column A")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.
plt.plot(df['A'], label='A')
plt.plot(df['B'], label='B')
plt.title("Plot of Columns A and B")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.show()

