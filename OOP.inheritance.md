# Inheritance:  
A way to **pass on attributes and methods to related objects**.  The **parent class (aka super class)** will pass on all of their attributes and methods to the **child class (aka sub class)**.  
- The child class may also have additional attributes/methods, and **may override** some of those they inherited.  
- Example: Dessert is the parent class... it is sweet, is usually eaten at the end of a meal, and you will feel ill if you eat way too much.  Chocolate is a child class. All of the dessert traits are true, but chocolate also has its own distinct traits    
- other examples: animal (parent class); snake & dog (child classes))  
- **Inheritance is an "is a" relationship.**  Chocolate "is a" dessert.  
- **Note**: <mark>Object class</mark> is a super class to all other classes (for example: this is where __init__() comes from)
---
Syntax:
```
import ExampleParentClass

# Parent class is added into the () when   # constructing a subclass:
class ExampleChildClass(ExampleParentClass):
    pass
```
---
## When to use super()  ?
- If the child class has its own constructor method `__init__`, then **the child class with only call its own constructor method, unless told it also needs to call the parent (aka super class) constructor** as well.  This is because the `__init__` functions have the same name, so the constructor class has essentially overrides the inherited info.  
- To also call the parent's constructor method, one needs to include `
super().__init__(parameters, excluding 'self')`
- Example:  
```
class Truffle(Candy):
    def __init__(self, name, price, grams_of_sugar, coating, filling, topping):
        super().__init__(name, price, grams_of_sugar)  # new addition
        self.coating = coating
        self.filling = filling
        self.topping = topping
```
- If another method exists in the child class with the **same name**, to include the parents' info, it must be included in the function definition.  
Example: 
```
    def build_description(self):
     # added to also included parent class' build_description method
        first_line = super().build_description() 
        second_line = f"{self.coating}-coated {self.filling}, topped with {self.topping}"
        return f"{first_line}\n{second_line}"
```