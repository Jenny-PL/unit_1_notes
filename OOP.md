# OOP (Object Oriented Programming) 
Note: this is in contrast to **Procedural Programming** which is step by step and oriented around functions.

OOP is a new way of  arranging data.  It includes defining classes (with a **class name, attributes, and methods**).    

Some classes we've already seen are string, boolean, and list... all have specific things in common and can do specific actions (methods, which just means functions that are specific to a class.   

When to make a class?  
- A concept that will be used often, can do things.    
- A class should be a singular name (not plural), ie: House, Car, Traveler.    
- Should make your code more readable  
- Is reusable, can be used often in your code.  

---


- **Object**: an instance of a class.  Each object or instance has its own space in memory & can have distinct attributes.
- **Attribute**: a specific variable defined within a class (example: 'dog' is an object of the string class, and its state or attribute is that it has 3 characters: d-o-g).  Attribute is related to state.   
- **State** includes all the attributes, or variables, within a class.  
- **Behavior**: the functions (aka **methods**) that are defined within a class.   
- **instantation**: Creating a new object or instance

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
---
## Organizing files

- Each class definition should have its own **.py** file
- Create the __init__.py file in each package folder and subfolder, even if it is empty!
- Python package names cannot contain hypens (-)
- When we write our own modules, it is a best practice to gather them together into a package. 

Sample Project set up:
```
project_name/
├── README.md
├── requirements.txt
├── main.py
├── project_package_name
│   ├── __init__.py
│   ├── example_class_a.py
│   └── example_class_b.py
└── tests
    ├── __init__.py
    ├── example_class_a_test.py
    └── example_class_b_test.py
```
-- When can import an entire package. Example:

    import random

However, to call a method, we then have to use dot notation:

    number = random.randint(0, 5)

alternative way:   
```
from random import randint
```
Then when call the function:   

    number = randint(0.5)