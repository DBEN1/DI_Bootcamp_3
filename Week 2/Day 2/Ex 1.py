# # Exercise 1 : Set 
# my_fav_numbers = {23,32,44,99,339,99444444444444}
# print(my_fav_numbers)
# my_fav_numbers.update([88888,8883838383883]) 
# print(my_fav_numbers)
# my_fav_numbers.discard(44)
# print(my_fav_numbers)
# friend_fav_numbers = {1,11,111,1111,11111,111111} # my friend is so dumb
# print(friend_fav_numbers) 
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# #Exercise 2 : 
# tuple = (1,3323223,32,3223,323223,323232234382843284)
# print(tuple)
# # Not possible to add something in the tuple, as REBBEI said : 'Tuples are immutable lists, which means items can’t be changed'

#Exercise 3 : 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0,"Apples")
# print(basket)
# count = basket.count("Apples")
# print(count)
# basket.clear()
# print(basket)

# Exercise 4 : 
# Float is a decimal, int is not
# sequence = [x / 2 for x in range(3, 11)]
# print(sequence)
#
# sequence = []
# for i in range(3, 11):
#     sequence.append(i / 2)

# print(sequence)

# Exercise 5: For Loop

# for num in range(1, 21):
#     print(num)

# # 
# for i in range(1, 21, 2):
#     print(i)

# Exercise 6 : While Loop
# name = 'dan'
# while True:
#   user_name = input('What is your name')
#   if user_name.lower() == name.lower():
#     print('Congrats! You win!')
#     break
#   else:
#     user_name
    
# # Exercise 7: Favorite Fruits
# Favourite_Fruit = input('What is your favorite fruit(s) my friend? /n')
# Favourite_Fruit = Favourite_Fruit.split()
# Second_question = input('Nooooooooow, do you remember one of your favourite fruits ???????????????????????? \n')
# if Second_question.lower() in [fruit.lower() for fruit in Favourite_Fruit]:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#    print('You chose a new fruit. I hope you enjoy')

# Exercise 8 : 
# toppings = []
# price_per_topping = 2.5

# while True:
#     topping = input("Enter a pizza topping (or 'quit' to finish): ")
#     if topping.lower() == 'quit':
#         break
#     toppings.append(topping)
#     print("Adding", topping, "to your pizza.")

# total_price = 10 + len(toppings) * price_per_topping

# print("\nToppings on your pizza:")
# for topping in toppings:
#     print("- ", topping)

# print("\nTotal price:", total_price)

# Exercise 9: Cinemax
# family_size = int(input("Enter the number of people in the family: "))
# total_cost = 0

# for person in range(1, family_size + 1):
#     age = int(input(f"Enter the age of person {person}: "))

#     if age < 3:
#         ticket_cost = 0
#     elif 3 <= age <= 12:
#         ticket_cost = 10
#     else:
#         ticket_cost = 15

#     total_cost += ticket_cost

# print("Total cost for the family's tickets:", total_cost)

# teenagers = ["Alice", "Bob", "Charlie", "David", "Emma"]
# allowed_ages = range(16, 22)

# print("Teenagers' Movie Selection:")

# for teenager in teenagers:
#     age = int(input(f"Enter the age of {teenager}: "))
#     if age not in allowed_ages:
#         teenagers.remove(teenager)

# print("\nFinal List of Teenagers Allowed to Watch the Movie:")
# print(teenagers)

# Exercise 10 :
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# # Removing all occurrences of "Pastrami sandwich" from sandwich_orders
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")

# finished_sandwiches = []

# # Preparing the orders of the clients
# while sandwich_orders:
#     sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(sandwich)
#     print("I made your", sandwich.lower())

# print("\nList of sandwiches that were made:")
# for sandwich in finished_sandwiches:
#     print(sandwich)

