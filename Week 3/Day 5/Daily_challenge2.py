

# 1. **What is a class?**
# In Python, a class is a blueprint or a template that defines the structure and behavior of objects. 
# It acts as a user-defined data type, encapsulating data (attributes) and methods (functions) 
# that operate on that data. Classes allow you to create objects based on the defined blueprint, 
# and each object created from a class is referred to as an instance of that class.

# 2. **What is an instance?**
# An instance, also known as an object, is a specific occurrence of a class. 
# When you create an object using a class, you are creating an instance of that class with its own unique
#  set of attributes and methods. Each instance can have different values for its attributes
#  but shares the methods defined in the class.

# 3. **What is encapsulation?**
# Encapsulation is one of the four fundamental principles of object-oriented programming (OOP). 
# It refers to the bundling of data (attributes) and methods (functions) that operate on that data 
# within a single unit, i.e., the class. It provides the concept of access control, 
# where you can specify which data members and methods are accessible from outside the class 
# and which are hidden or private.

# 4. **What is abstraction?**
# Abstraction is another important OOP principle that allows you to represent the essential features
# of an object while hiding unnecessary details. It involves creating a simplified 
# and generalized view of an object, focusing on its essential characteristics and behaviors. 
# Abstract classes and interfaces in Python enable you to achieve abstraction.

# 5. **What is inheritance?**
# Inheritance is a mechanism in object-oriented programming that allows a class 
# (called the child or subclass) to inherit the properties and behaviors (attributes and methods) 
# of another class (called the parent or superclass). This helps in reusing code
#  and establishing a hierarchical relationship between classes.

# 6. **What is multiple inheritance?**
# Multiple inheritance is a feature in Python
# that allows a class to inherit from more than one parent class. 
# In other words, a class can have multiple superclasses, 
# and it inherits attributes and methods from all of them. 
# However, it is essential to handle potential conflicts or ambiguity that might arise 
# due to multiple inheritance.

# 7. **What is polymorphism?**
# Polymorphism is the ability of a class to take on multiple forms. 
# In Python, polymorphism allows objects of different classes to be treated as objects
# of a common superclass, as long as they support the same interface (methods). 
# This concept enables code to be written in a more generic and flexible way, 
# facilitating code reusability.

# 8. **What is method resolution order or MRO?**
# Method Resolution Order (MRO) is the order in which Python searches for methods and attributes 
# in a class hierarchy. When you call a method on an instance, Python looks for the method 
# in the instance's class first, and if not found, it follows a specific sequence to search 
# through the inheritance chain. The MRO is determined using the C3 linearization algorithm. 
# You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

# Example usage:
if __name__ == "__main__":
    deck = Deck()
    print("Deck before shuffling:")
    for card in deck.cards:
        print(card)

    print("\nShuffling the deck...")
    deck.shuffle()

    print("\nDeck after shuffling:")
    for card in deck.cards:
        print(card)

    print("\nDealing a card:")
    card_dealt = deck.deal()
    print("Card dealt:", card_dealt)

    print("\nDeck after dealing a card:")
    for card in deck.cards:
        print(card)
