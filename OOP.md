# OOP (Object Oriented Programming) 

OOP is a new way of  arranging data.  It includes defining classes (with a **class name, attributes, and methods**). 

Some classes we've already seen are string, boolean, and list... all have specific things in common and can do specific actions (methods, which just means functions that are specific to a class).

- **Object**: an instance of a class.  Each object or instance has its own space in memory & can have distinct attributes.
- **Attribute**: a specific variable defined within a class (example: 'dog' is an object of the string class, and its state or attribute is that it has 3 characters: d-o-g).  Attribute is related to state.   
- **State** includes all the attributes, or variables, within a class.  
- **Behavior**: the functions (aka **methods**) that are defined within a class.

- Side note: in the terminal, use **dir(variable_name)** to get a list of methods available for that class.  Also, **help(class_name)**, ie **help(str)** or **help(list)** will give more info about the class and its methods.

- Give ClassNameWithPascalCase. (FYI: **PascalCase** vs. camelCase vs snake_case)
```
# How to define a class: CapitalizeAndUsePascalCase 

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
```
Another Example, with Class User:
```
class User:

# To initialize attributes (or set the starting values for attributes):
# The __init__ function is called e/time a new object is created for a class:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # This is being given a default value

# Default values do not need to be inluded as a parameter when making a new object

# Once parameters are added to class definition, they must be included
# each time a new object is made (unless default values were given)

user_1 = User("001", "Jenny")
print(user_1)  # <__main__.User object at 0x10add5fd0>
print(f"User 1's username is :{user_1.username}")
```



