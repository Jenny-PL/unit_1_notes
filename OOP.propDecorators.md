# Design Patterns & Property Decorators: getters, setters

## Setter  
**@property** allows you to use method as an attribute
```
@property
   def email(self):
   return(f"{first}{last}@email.com")
```

```
@fullname.setter
def fullname(self,name):
    first, last = name.split(' ')
    self.first = first
    self.last = last

employee_1.fullname = 'jen luong'

print(employee_1.full_name) # jen luong
```

# Design patterns
- **iterator**: responsible to know how to iterate
- **factory**: to create instances of a class:   
  - ie, if `__init__` (constructor) is changed, only need to change the factory, not each line that calls the constructor
- **adapter**: allows two classes to communicate
- **observer**: watches for changes
- **decorator**: alter/extend the behavior of a function/class.  
  - example: calculator that has simple math function; it can be wrapped with functions that check validity of input, calculates, then prints the results.
- **strategy**: responsible to represent an algorithm

Note: Design patterns can complicate the code and/or make it less maintainable-- choose carefully adn think about whether they help/hurt

# Decorator pattern:
- **wrapped function**: function beding extended (aka the decorated function.)
- def wrapper_function() will take at least one parameter, the function being wrapped.
```
def wrapper_function(wrapped_function):
    def inner():
    # wrapper logic
    wrapped_function()
    #wrapper logic
    return inner
```
syntax to set up a decorator:
```
@wrapper_function
def wrapped_function():
    pass
```
This is the same as this, however the above is more explicit/readable:
```
wrapped_function = wrapper_function(wrapped_function)
```
