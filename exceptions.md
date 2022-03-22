# Exceptions
 - exceptions hold info: What error occured, what line of code it occured on.
 ## Types of Errors
 1. NameError
 2. ZeroDivsionError
 3. Overflow rror
 4. SyntaxError
 5. TypeError: ie try to get len() of a bool.
 6. KeyboardInterupt : user hits interrupt key (ie- control + c)

## Rasing Exceptions: 
- aka 'creating an exception'

## Catching an exception
- 
## Handling an exception
- Do a Try... except 
---
In below examples, **err** is a variable, which can they be accessed in 

    def calculate_circumference(radius):
    try:
        circumference = 2*3.14*radius
        print(f"Circumference of circle is: {circumference}")
        return circumference
    except TypeError as err:
        print(f"Calculation input has an incorrect data type, {err}.")


    calculate_circumference("Some text that is definitely not a valid radius value.")

     print("Notice how the program hasn't crashed. This is because exceptions change the flow of how programs execute rather than completely stop it.")
---


