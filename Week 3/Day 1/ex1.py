# # Exercise 1 
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# cat1 =Cat('Bob',10)
# cat2 =Cat('Bill',22)
# cat3 =Cat('Ben',11)

# def oldest_cat(cat_list:list[Cat]) -> Cat | None :
#     if len(cat_list) == 0 :
#         return None

#     oldest_cat = cat_list[0]

#     for cat in cat_list:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat 
#     return oldest_cat
# oldest = oldest_cat([cat1, cat2, cat3])
# print(f"{oldest.name} is the oldest cat and is {oldest.age} years old")

# # Exercise 2 

# class Dog:
#     def __init__(self, name: str, height: int):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")


# # Create David's dog
# davids_dog = Dog("Rex", 50)
# print(f"David's dog's name is {davids_dog.name} and his height is {davids_dog.height} cm.")
# davids_dog.bark()
# davids_dog.jump()

# # Create Sarah's dog
# sarahs_dog = Dog("Teacup", 300)
# print(f"Sarah's dog's name is {sarahs_dog.name} and his height is {sarahs_dog.height} cm.")
# sarahs_dog.bark()
# sarahs_dog.jump()

# # Compare dogs
# if davids_dog.height > sarahs_dog.height:
#     print(f"The bigger dog is {davids_dog.name}.")
# elif sarahs_dog.height > davids_dog.height:
#     print(f"The bigger dog is {sarahs_dog.name}.")
# else:
#     print("Both dogs are the same height.")

# #Exercise 3 

# class Song:
#     def __init__(self, lyrics: list):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)


# stairway = Song(["There’s a lady who's sure",
#                  "all that glitters is gold",
#                  "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

#Exercise 4

class Zoo:
    def __init__(self, zoo_name: str):
        self.animals = []
        self.name = zoo_name
        self.sorted_animals = {}

    def add_animal(self, new_animal: str):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold: str):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.sorted_animals = {}
        current_letter =  ''
        for animal in self.animals:
            if animal[0] != current_letter:
                current_letter = animal[0]
                self.sorted_animals[len(self.sorted_animals) + 1] = [animal]
            else:
                self.sorted_animals[len(self.sorted_animals)].append(animal)

    def get_groups(self):
        for key, value in self.sorted_animals.items():
            print(f"Group {key}: {value}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

# Adding animals
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

# Get animals
ramat_gan_safari.get_animals()

# Sell an animal
ramat_gan_safari.sell_animal("Bear")

# Check animals after selling
ramat_gan_safari.get_animals()

# Sort animals
ramat_gan_safari.sort_animals()

# Get groups of animals
ramat_gan_safari.get_groups()
