import random

def get_words_from_file():
    with open('sowpods.txt', 'r') as f:
        words = f.read().splitlines()
    return words

def get_random_sentence(length):
    words = get_words_from_file()
    # Randomly select words from the list
    random_words = random.choices(words, k=length)
    # Join words into a sentence
    sentence = ' '.join(random_words)
    # Convert sentence to lowercase
    sentence = sentence.lower()
    return sentence

def main():
    print("This program generates a random sentence of a length specified by the user.")

    try:
        length = int(input("Enter the length of the sentence (between 2 and 20): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if length < 2 or length > 20:
        print("Invalid input. Please enter a number between 2 and 20.")
        return

    sentence = get_random_sentence(length)
    print("Here is your sentence:\n" + sentence)

if __name__ == "__main__":
    main()

# Exercise 2
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Parse the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary is:", salary)

# Add a new "birth_date" key at the same level as the "name" key
data["company"]["employee"]["birth_date"] = "1990-07-26"

# Convert the Python dictionary back to a JSON string
updatedJson = json.dumps(data)

# Save the updated JSON string to a file
with open('updated_data.json', 'w') as f:
    f.write(updatedJson)

