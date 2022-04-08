# Exceptions
- [Article on raising exception vs. handling vs returning Errors](https://victoria.dev/blog/do-i-raise-or-return-errors-in-python/)
 - exceptions hold info: What error occured, what line of code it occured on.
 - Silent failures are very difficul bugs to find and fix. By using raise and/or return, you can make sure errors are seen.
 ## Types of Errors
 1. NameError
 2. ZeroDivsionError
 3. Overflow error
 4. SyntaxError
 5. TypeError: ie try to get len() of a bool.
 6. KeyboardInterupt : user hits interrupt key (ie- control + c)

## Raising (aka Throwing) Exceptions: 
- aka 'creating an exception'


## Catching an exception
-- this is when an error is handled with an exception.

## Handling an exception
- Do a Try... except, where except is an alternate code path to follow in cause of an error. 
```
try:
    s = sandwich_or_bust("\U0001F35E")
    print(s)
except ValueError:
    buy_more_jam()
    raise
else:
    print("Congratulations on your sandwich.")
```
-  if your Python code is interacting with other components that do not handle exception classes, you may want to return a message instead. Here’s an example using a try … except statement:
  
  ```
  def share_sandwich(sandwich: int) -> Union[float, Exception]:
    try:
        bad_math = sandwich / 0
        return bad_math
    except Exception as e:
        return e


s = share_sandwich(1)
print(s)
# Prints "division by zero"
  ```

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


