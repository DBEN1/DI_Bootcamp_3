# lenght = input('Tell me something... I\'m listening :')
# if len(lenght) < 10 :
#     print('string not long enough')
# elif len(lenght) > 10 :
#     print('string too long')
# else :
#     print('perfect string')

# Last_and_first = input('I will help you to find the first and the last character of what you will tell me :')
# first_character = Last_and_first[0]
# last_character = Last_and_first[-1]
# print(f'the first character is {first_character}, and the last character is {last_character}')

user_input = input("Enter a string: ")

for i in range(0, len(user_input)):
    substring = user_input[:i]
    print(substring)
