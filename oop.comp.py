# Example from Learn: 

# import random

# class ExampleComponent:

#     def __init__(self, name):
#         self.name = name

#     def get_random_num(self):
#         print("***************************************************")
#         print("I'm inside Component's instance method get_random_num")
#         random_num = random.randint(0, 999)
#         print("Now, I'm going to leave Component's instance method")
#         print("***************************************************")
#         return random_num

# class ExampleComposite:

#     def __init__(self, name, component):
#         self.name = name
#         self.component = component

#     def read_fruits(self):
#         print("I'm inside Composite's instance method read_fruits")
#         print("I can read self.component here:", self.component)
#         print("Now, I'm going to call self.component's instance method")

#         result_from_component = self.component.get_random_num()

#         print("This is what Component's method returned:", result_from_component)

# ExampleComponent:
class Student:
    def __init__(self, name):
        self.name = name
        self.id = self.get_ID_num()
    
    def get_ID_num(self):
        for i in range(5000):
            stud_id = f" {self.name}+{i}"

        print(stud_id)
        return stud_id

# instantiating 3 students
student_one = Student("Heather")
student_two = Student("Timothy")
student_three = Student("Mark")

# adding students into a list
students = [student_one, student_two, student_three]

# Example Composite:
class AnatomyClass:
    
    # def __init__ (self, name, component(s))
    def __init__(self, teacher, students):
        self.teacher = teacher
        self.students = students
    
    def class_roster(self):
        class_roster = []
        for student in self.students:
            class_roster.append((f"Name: {student.name}, Id #: {student.id}"))
        return class_roster

# instantiating an anatomy class
one_class = AnatomyClass("Prof Green", students)

print(one_class.class_roster())