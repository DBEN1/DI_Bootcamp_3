# Exercise 1 
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create instances of each cat breed
bengal_cat = Bengal('BengalCat', 5)
chartreux_cat = Chartreux('ChartreuxCat', 4)
siamese_cat = Siamese('SiameseCat', 3)

# List containing all cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Sara's pets
sara_pets = Pets(all_cats)

# Walk all cats
sara_pets.walk()

#Exercise 2 
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_dog_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_dog_power:
            return f'{self.name} won the fight'
        elif my_power < other_dog_power:
            return f'{other_dog.name} won the fight'
        else:
            return "It's a tie!"

# Create 3 dog instances
dog1 = Dog('Doggy', 7, 15)
dog2 = Dog('Bully', 5, 20)
dog3 = Dog('Buddy', 6, 18)

# Test the Dog class methods
print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))

print(dog2.bark())
print(dog2.run_speed())
print(dog2.fight(dog3))

print(dog3.bark())
print(dog3.run_speed())
print(dog3.fight(dog1))

#Exercise 3
import random
from dog import Dog  # Import the Dog class

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args])
        print(f'{dog_names} all play together')

    def do_a_trick(self):
        if self.trained:
            tricks = [f'{self.name} does a barrel roll',
                      f'{self.name} stands on his back legs',
                      f'{self.name} shakes your hand',
                      f'{self.name} plays dead']
            print(random.choice(tricks))
