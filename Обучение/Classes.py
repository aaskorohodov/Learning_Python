class Vehicle:
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        print('Created')

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"

# truck = Vehicle('Blue', 5, 4)
# print(truck.brake())


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print(f'Restoran "{self.restaurant_name}" created')

    def describe_restaurant(self):
        print(f'{self.restaurant_name} has {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open')


def classes_restaurant():
    Chang_Wu = Restaurant('Chang Wu Special', 'Korean cuisine')
    Chang_Wu.describe_restaurant()
    Chang_Wu.open_restaurant()

    Big_Bob = Restaurant('Big Bob', 'American cuisine')
    Anastasia = Restaurant('Anastasia', 'Russian cuisine')
    Big_Bob.describe_restaurant()
    Anastasia.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex
        print(f'Congarts {self.first_name}! Your user has been created')

    def describe_user(self):
        print(f'Description:\n'
              f'First Name: {self.first_name}\n'
              f'Last Name: {self.last_name}\n'
              f'Age: {self.age}\n'
              f'Sex: {self.sex}\n')

    def greet_user(self):
        print(f'Gretings {self.first_name} {self.last_name}!')


def uses():
    mike = User('mike', 'schlosberg', 21, 'Male')
    ivan = User('Ivan', 'Petrov', 25, 'Male')
    kate = User('kate', 'Timonova', 24, 'Female')

    mike.describe_user()
    kate.greet_user()


class Super_Users(User):
    pass


david = Super_Users('David', 'Gates', 25, 'Male')

david.greet_user()

print(type(david))
