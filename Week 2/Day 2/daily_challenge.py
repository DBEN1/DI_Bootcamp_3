# number = int(input("Enter a number: "))
# length = int(input("Enter the desired length: "))

# multiples = []
# count = 0
# current_multiple = number

# while count < length:
#     multiples.append(current_multiple)
#     current_multiple += number
#     count += 1

# print(multiples)

user_word = input("Enter a word: ")

new_word = ""
prev_char = ""

for char in user_word:
    if char != prev_char:
        new_word += char
    prev_char = char

print("New word:", new_word)
