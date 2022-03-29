# How to define a class: CapitalizeAndUsePascalCase 
# PascalCase vs. camelCase vs snake_case
class Car:
    pass

    def __init__(self):
        self.speed = 20 # default speed

    def race_mode(self):
        self.speed += 30
        return f"Race time! My new speed is {self.speed}mph"


# Creating an instance (aka object) for User
car_1 = Car()
# Adding attributes (aka variables) to an object:
car_1.seats = 5
car_1.color = "blue"
print(f"Car 1's color is :{car_1.color}")

# Calling the race_mode METHOD on object car_1.
print(car_1.race_mode())


class User:
# To initialize attributes (or set the starting values for attributes):
# The __init__ function is called e/time a new object is created for a class:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # This is being given a default value

        # Default values do not need to be inluded as a parameter when making a new object

# Once parameters are added to class definition, they must be included
# each time a new object is made.
user_1 = User("001", "Jenny")
print(user_1) # <__main__.User object at 0x10add5fd0>
print(f"User 1's username is :{user_1.username}")

