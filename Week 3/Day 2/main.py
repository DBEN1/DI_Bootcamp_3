class Employee:
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def get_fullname(self):
        return self.firstname + " " + self.lastname

    def happy_birthday(self):
        self.age += 1
        return self.age

    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount
        return self.salary

    def show_info(self):
        print(f"Name: {self.get_fullname()}\nAge: {self.age}\nJob: {self.job}\nSalary: {self.salary}")


# Create two Employee objects
lea = Employee("Lea", "Smith", 30, "developer", 50000)
david = Employee("David", "Schwartz", 20, "teacher", 40000)

# Print their full names
print(lea.get_fullname())
print(david.get_fullname())

# Celebrate their birthdays
print(lea.happy_birthday())
print(david.happy_birthday())

# Give them promotions
print(lea.get_promotion(5000))
print(david.get_promotion(4000))

# Show their info
lea.show_info()
david.show_info()

class Developer(Employee):
    def __init__(self, firstname, lastname, age, job='developer', salary=15000, coding_skills=[]):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = coding_skills

    def add_skills(self, *skills):
        self.coding_skills.extend(skills)

    def coding(self):
        print(f"{self.get_fullname()} can code in: {', '.join(self.coding_skills)}")

    def coding_with_partner(self, other_developer):
        print(f"{self.get_fullname()} is coding with {other_developer.get_fullname()}. They know {', '.join(self.coding_skills + other_developer.coding_skills)}")

    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount
        return self.salary


# Create two Developer objects
tom = Developer("Tom", "Cruiz", 30)
angelina = Developer("Angelina", "Jolie", 23)

# Add skills to developers
tom.add_skills('Python', 'Java')
angelina.add_skills('JavaScript', 'HTML', 'CSS')

# Developers coding
tom.coding()
angelina.coding()

# Developers coding with partner
tom.coding_with_partner(angelina)

# Developers getting promotions
print(tom.get_promotion(1.2))
print(angelina.get_promotion(1.1))

# Show their info
tom.show_info()
angelina.show_info()
