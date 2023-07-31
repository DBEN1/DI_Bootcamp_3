import math

class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("In geometry, a circle is a closed shape consisting of all points in a plane that are at a given distance from a given point, the centre.")

circle = Circle(5)
print(circle.perimeter())
print(circle.area())
circle.definition()

import random

class MyList:
    def __init__(self, list_of_letters):
        self.list_of_letters = list_of_letters

    def reversed_list(self):
        return self.list_of_letters[::-1]

    def sorted_list(self):
        return sorted(self.list_of_letters)

    def random_list(self):
        return [random.randint(1, 100) for _ in self.list_of_letters]


my_list = MyList(['b', 'a', 'd', 'c'])
print(my_list.reversed_list())  # Prints: ['c', 'd', 'a', 'b']
print(my_list.sorted_list())    # Prints: ['a', 'b', 'c', 'd']
print(my_list.random_list())    # Prints a list of random numbers of length 4
