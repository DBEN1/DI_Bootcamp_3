class Family:
    def __init__(self, last_name):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = last_name

    def born(self, **kwargs):
        print('Congratulations on the new family member!')
        kwargs['is_child'] = True
        self.members.append(kwargs)

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(member['name'])

# Create a Family instance
my_family = Family('Smith')

# Add a child to the family
my_family.born(name='John', age=0, gender='Male')

# Check if a family member is over 18
print(my_family.is_18('John'))

# Present the family
my_family.family_presentation()

class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
        ]

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] < 18:
                    raise Exception(f"{name} is not over 18 years old!")
                else:
                    print(f"{name}'s power is {member['power']}")

    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(f"{member['incredible_name']} has the power to {member['power']}")

# Create an instance of TheIncredibles
my_incredible_family = TheIncredibles('Incredible')

# Use the born method to add Baby Jack
my_incredible_family.born(name='Jack', age=0, gender='Male', power='Unknown Power', incredible_name='Baby Jack')

# Call the incredible_presentation method
my_incredible_family.incredible_presentation()
