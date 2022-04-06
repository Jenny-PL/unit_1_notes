# Composition: 
- When an instance of a class contains another class.
- Composition is a **"has a"** relationship.  
-  A bookclub "has a " member.
- A class Bookclub could have an attribute that is self.members, which could be made up of instances of the class Member.
- This allows a class to use the attributes& methods of a class, or multiple classes, within its own defintion.
- The **composite class** has a (or multiple) **component class**(es)
---
- **one-to-one** relationship
- **one-to-many** relationship
---
## Magic Methods (aka Special Methods)
- `__init__` is a special method.
- Some other ones to include are `__repr__` and `__str__ `.  
- If we use dunder str (aka `__str__`) within our class definition, we are re-writing the rules for what we want Python to do when we call str() for an object of that class.  **We are also re-writing the rules for what to print when we `print(object)`.  Instead of giving us something like `<object class ......09090-9-0999->` it will give us the more useful info we asked it to print.**
- Note: if `__repr__` is defined, and` __str__` is not, the object will behave as though `__str__=__repr__` 
- `__repr__` is more for the developers. It's goal is to be unambigious.  
  - **In general, it is helpful to return something that can be used to recreate the object, aka ClassName(argument1, argument2, argument3)**
- `__str__` is more for the end users... a readable version