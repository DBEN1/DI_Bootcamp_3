# username = "Tom"
# hobby = "football"
# age = 233
# sentence = username + " plays " + hobby

# print(sentence)

# sentence2 = f'{username} is {age} years old'
# # print(sentence2)
# city = "tlv"
# my_age = 29 + 123879
# first_name = 'Dan'
# last_name = 'Benguira'


# user_answer = input("Where do you live")
# print(city == user_answer.lower())

# sentence3 = "hello world how ar3 you"
# sentence_list = sentence3ddd
# print(sentence3, sentence_list)

# sentence4 = "hello, world, how, ar3, you"
# sentence_list = sentence4.split(",")
# print("sentence: " + sentence4 + "\n list: " + sentence_list)


# # Exercise
# # ask a user for a number of miles, to convert kilometers and display it.
# user_answer3 = input("number of miles please")
# user_answer3_km = float(user_answer3) * 1.60934
# print (f'{user_answer3_km} kilometers my man')

# Ask the user for a number between 1 and 100

# # user_answer2 = input("number between 1 and 100 PLSSSSSSSSSSSSSS")
# user_answer2 = input("Welcome to FizzBuzz : Please give me a number between 1 and 100 ! \n")
# # # If the number is a multiple of three, print "Fizz"
# if type(int(user_answer2) / 3) == int: print('Fizz')
# # # If the number is a multiple of five, print "Buzz".
# elif type(int(user_answer2) / 5) == int: print('Buzz')

# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.
# price = 0
# user_answer4 = input("Please Give Me the number of Guests !  \n")
# if int(user_answer4) < 50 :
#    price = 4000
# elif 50 < int(user_answer4) < 100 :
#    price = 10000
# elif 100 < int(user_answer4) < 200 :
#    price = 15000
# else : price = 20000
# print(f"The price is {int(price)}")


# name = 'John rfffffffDoe'
# if len(name) > 20 :
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = 'long'
# elif len(name) > 15 :
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = 'semi long'
# elif len(name) > 10:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = 'semi long'
# elif len(name) > 8:
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = 'semi short'
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = 'short'


# user_answer2 = input("Welcome to FizzBuzz: Please give me a number between 1 and 100!\n")
# number = int(user_answer2)
# if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz!")
# elif number % 3 == 0:
#         print("Fizz")
# elif number % 5 == 0:
#         print("Buzz")
# else : print(number)

# list of 15 number 
for number in range(0,14):
        if number % 2 == 0 :
                print(f'The number {number} is even')
        else : 
                print(f'the number {number} is odd')


