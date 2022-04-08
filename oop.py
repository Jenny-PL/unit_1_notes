# # How to define a class: CapitalizeAndUsePascalCase 
# # PascalCase vs. camelCase vs snake_case
# class Car:
#     pass

#     def __init__(self):
#         self.speed = 20 # default speed

#     def race_mode(self):
#         self.speed += 30
#         return f"Race time! My new speed is {self.speed}mph"


# # Creating an instance (aka object) for User
# car_1 = Car()
# # Adding attributes (aka variables) to an object:
# car_1.seats = 5
# car_1.color = "blue"
# print(f"Car 1's color is :{car_1.color}")

# # Calling the race_mode METHOD on object car_1.
# print(car_1.race_mode())


# class User:
# # To initialize attributes (or set the starting values for attributes):
# # The __init__ function is called e/time a new object is created for a class:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0 # This is being given a default value

#         # Default values do not need to be inluded as a parameter when making a new object

# # Once parameters are added to class definition, they must be included
# # each time a new object is made.
# user_1 = User("001", "Jenny")
# print(user_1) # <__main__.User object at 0x10add5fd0>
# print(f"User 1's username is :{user_1.username}")

# # Learn homework:
# class BasketballTeam:
    
#     def __init__(self):
#         self.members = []
        
#     def add_member(self, name):
#         # self.members += [name]
#         self.members.append(name)
#         return True

# class Automobile:
#     def __init__(self):
#         self.speed = 0

#     def accelerate(self, speed_delta):
#         self.speed += speed_delta
#         return self.speed
    
#     def adjust_to_speed_limit(self, speed_limit):
#         if speed_limit == self.speed :
#             return self.accelerate(0)
#         elif speed_limit - self.speed < 0:
#             return self.accelerate(-1)
#         elif speed_limit - self.speed > 5:
#             return self.accelerate(2)
#         else:
#             return self.accelerate(1)



# ## Q 12:
# def get_leading_team(home_team, away_team):
#     pass
#     if self.get_total_score(self,home_team) > self.get_total_score(self,away_team):
#         return self.home_team
#     else:
#         return self.away_team

# class BasketballTeam:

#     def __init__(self, team_name, initial_score_dict):
#         self.team_name = team_name
#         self.score_dict = initial_score_dict

#     def get_total_score(self):
#         return sum(self.score_dict.values())

class Employee:
    # class variable: a variable with scope across all instances of the class:
    num_of_employees = 0

    def __init__(self, first_name, last_name, pay=20000): # __init__ aka 'the constructor'
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." +last_name + '@company.com'
        self.full_name = first_name +" "+ last_name
        # This updates the # of employees with each new instance:
        Employee.num_of_employees +=1 

    def calc_payraise(self, perc_inc):
        new_pay = self.pay * (100+ perc_inc)/100
        return print(f"Your new payrate is ${new_pay:.0f}.  Congrats, you earned a {perc_inc}% raise!")

# Comany prior to adding employees:
print(Employee.num_of_employees)

# first instances of the class, made through instantiation
emp_1 = Employee('Heather', "Marks")
emp_2 = Employee('Tim', "Canner", 5000)

# after instantiating 2 employees:
print(Employee.num_of_employees)

print(emp_1.email)
print(emp_1.full_name)
print(f"{emp_2.first_name} {emp_2.last_name} makes {emp_2.pay} a year. That is our company's base pay")

# Call method beginning with the instance:
emp_2.calc_payraise(5)

# A different way to call this method, beginning with class, passing in the instance:
Employee.calc_payraise(emp_2,5)

# To print out a dictionary for the instance, with key:value pairs being instance variables:values)
print(emp_2.__dict__)
# output: {'first_name': 'Tim', 'last_name': 'Canner', 'pay': 5000,\
#  'email': 'Tim.Canner@company.com', 'full_name': 'Tim Canner'}

@classmethod
def set_rasise_amt(cls, amount):
    cls.raise_amt = amount

@staticmethod
def is_workday(day_weekday):
    if day_weekday == 5 or day_weekday ==6:
        return False
    return True