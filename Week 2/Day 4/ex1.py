# # Exercise 1 
# def display_message():
#     print("I am learning Python programming in this course.")

# display_message()

# # Exercise 2 
# def favorite_book(title):
#     print("One of my favorite books is " + title)

# # Call the function and provide a book title as an argument
# favorite_book("Alice in Wonderland")

# # Exercise 3 
# def describe_city(city, country="Unknown"):
#     print(city + " is in " + country)

# # Call the function without specifying the country
# describe_city("Reykjavik")

# # Call the function with both city and country
# describe_city("Paris", "France")

#Exercise 4 

# import random
# def compare_numbers(user_number):
#     # Generate a pseudo-random number based on the user input
#     random_number = random.randint(1,101)

#     if user_number == random_number:
#         print("Success! The numbers match.")
#     else:
#         print("Fail! The numbers don't match.")
#         print("User number:", user_number)
#         print("Random number:", random_number)


# user_input = int(input("Enter a number between 1 and 100: "))


# compare_numbers(user_input)

# Exercise 5

# def make_shirt(size="large", message="I love Python"):
#     print("The size of the shirt is", size, "and the text is", message)

# # Call the function with default arguments
# make_shirt()

# # Call the function with medium size and default message
# make_shirt("medium")

# # Call the function with small size and a custom message
# make_shirt("small", "Hello, World!")

# # Call the function using keyword arguments
# make_shirt(size="extra large", message="Coding is fun!")

#Exercise 6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians():
#     for magician in magician_names:
#         print(magician)

# def make_great():
#     for i in range(len(magician_names)):
#         magician_names[i] += " the Great"

# make_great()
# show_magicians()

#Exercise 7 
# import random

# def get_random_temp(season):
#     if season == 'winter':
#         lower_limit = -10
#         upper_limit = 16
#     elif season == 'spring':
#         lower_limit = 17
#         upper_limit = 23
#     elif season == 'summer':
#         lower_limit = 24
#         upper_limit = 32
#     elif season == 'autumn' or season == 'fall':
#         lower_limit = 33
#         upper_limit = 40
#     else:
#         print("Invalid season entered.")
#         return

#     temperature = round(random.uniform(lower_limit, upper_limit), 1)
#     return temperature

# def main():
#     month = int(input("Enter the number of the month (1-12): "))
#     if month in (1, 2, 12):
#         season = 'winter'
#     elif month in (3, 4, 5):
#         season = 'spring'
#     elif month in (6, 7, 8):
#         season = 'summer'
#     elif month in (9, 10, 11):
#         season = 'autumn'
#     else:
#         print("Invalid month entered.")
#         return

#     temperature = get_random_temp(season)
#     if temperature is not None:
#         print("The temperature right now is", temperature, "degrees Celsius.")
        
#         if temperature < 0:
#             print("Brrr, that's freezing! Wear some extra layers today.")
#         elif temperature < 16:
#             print("Quite chilly! Don't forget your coat.")
#         elif temperature < 23:
#             print("Enjoy the mild weather!")
#         elif temperature < 32:
#             print("It's getting warm. Stay hydrated.")
#         else:
#             print("It's hot outside! Stay cool.")

# # Call the main function
# main()

# Exercise 8 
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def take_quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question in data:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": question["question"],
                "user_answer": user_answer,
                "correct_answer": question["answer"]
            })

    show_results(correct_answers, incorrect_answers, wrong_answers)

def show_results(correct_answers, incorrect_answers, wrong_answers):
    print("Quiz Results:")
    print("Correct Answers:", correct_answers)
    print("Incorrect Answers:", incorrect_answers)

    if incorrect_answers > 0:
        print("\nQuestions Answered Incorrectly:")
        for wrong_answer in wrong_answers:
            print("Question:", wrong_answer["question"])
            print("Your Answer:", wrong_answer["user_answer"])
            print("Correct Answer:", wrong_answer["correct_answer"])
            print()

    if incorrect_answers > 3:
        play_again = input("You had more than 3 incorrect answers. Do you want to play again? (yes/no) ")
        if play_again.lower() == "yes":
            take_quiz()

# Start the quiz
take_quiz()

