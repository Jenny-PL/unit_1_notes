# Unit 1 lightening Talks
1. **Slicing**: New_sequence = [start:stop:step] start: inclusive, stop: exclusive.  This makes a shallow copy-- ie, does not effect the original.  Can also use **slice(start, stop, step)**   
2. **Ternary Operator**: Something composed of 3 components: ___ if ___ else ____, aka condional expressions  
3. **DRY: Don't repeat Yourself**
4. **YAGNI: You Aint Gonna Need It**
5. **Optional Parameters & Named arguments**:
   - Optional parameters: default value that is used if no arguments are given.  
```
def return_boolean(bool= True):
        return boolean

def func_mult(x, y = 1, z = 1):
    return x*y*z
```
Call with: **positional arguments**
```
func_mult(6) where x =6, y =1, z = 1 
or
func_mult(5,6) where x = 5, y = 6, z =1
```

or **named arguments**:
```
func_mult(z = 6, x = 5) where x = 5, y =1, z = 6
```
6. **Default Parameters & Danger of mutables as default parameters**:
- Default paraemters are part of the funtion definition (ie- This becomes an optional parameter for the funtion, as there is already a default value provided.)  It is dangerous to use a mutable(ie- list, dict) as a defualt parameters, because the defualt provided is used only the 1st time,then this vaue will changed based on prior value, and based on how it is modified in the function.  if the output value is different, this is the value that will then feed into the function next time that function is called.
7. **\*args and \*kwargs: unknown # of parameters**
   - args: passed trhu as a tuple
   - kwargs: passed trhu as a dictionary(keyword-args)
```
  def add(*num):
    sum = a+b
    return sum
```
8. **Lambda**: A function that is not named... no need to define it with a function signature.  Often used inside other functions, for brief issues that do not need to be repeated often. 
- It is a single-line function.
- Can be used as an argument inside calling a function
- example for squaring:
```
lambda x: x*x
```
1.  **docstrings**:
 Describe what a function does.     
 """ One line docstring""" 
 No need for empty line before or after. Longer docstring:

 """
 summary line: what does Fx do
 Description. Input:  
 Output:  
 """   
     
- To get more docstring info: **print(module.__doc__)** or **help(module)** for any modules imported into your file.   
- Print func's docstring with: **print(func_name.__doc__)**   

10. **Floating numbers**:  Use binary-floating point (not precise... so this can give errors)  
- Decimal module can be inported to get around this, and using **pytest.approx()** is a helpful way in tests.    
11. **Technical debt**: Making work for yourself later (ie- doing things quickly rather than well, making more work in the long run... ie, not writing any tests). **code smell**   
12. **EAFP**: Easiear to Ask For Forgiveness Than Permission, aka holding an optimistic view for the code you are working on, and if an exception is thrown catch it and deal with it later.  **This is more pythonic**
13. **LBYL**: Look Before You Leap: Using lots of conditional statements, trying to think of all possible errors. More cautious. More common with Java and C.  
14. **Python type hints**: Newer python feature. You can add hints to function signature or variables, however Python will not enforce.  It can be helpful to improve understanding, acts as additional documentation.
```
def add(num1:int, num2: int)
    return num1 + num2
```
- This can be helpful as Python allows variables to change data types (dynamic type)... example:
```
a = 10 where type(a)= int
a = "ten" where type(a)= str
```
15. **Assembly language**: This is in opposition to a more high level lagnuage.<mark>???????</mark>
16. **compiled vs. interpreted languages**: 
- Compiled: C  
  Translated to assembly language --> binary
  Two steps
- Interpreted: Python
  Translated while the program is running.
  One step. Slower
17. **Static vs. Dynamic Typing**:
    - Checking data type can happen BEFORE runtime or during runtime (ie- give a runtime error, or throw an error before this.) <mark> ??? </mark>
18.  **VIM**: A text editor
19.  **Short circuiting**:  for a statement **if A and B**, if A is False, B will not be evaluated... Similarly, **if A or B**... Python will get only as much info as it needs to evaluate the expression.
20.  **opening and closing files** 
- something about Pickle module
- import pickle
- pickle.dump()
- pickle.load() converts info from binary
21. **CSV**: Comma separated value **.csv** will be file extesion. Often used to convert tables (ie in excel)--> text data
22. **map**
syntax: **map(function_name, iterables):** This must then be assigned to some data type to hold it... ie: list
```
output = list(map(func, num_list)):
```
Above, **map** will apply the function **func** to all the iterables in **num_list** and will place the results into a **list**.
- When to use **map** vs. **for loop**:
  - Map is helpful if you want to apply a func to **each** iterable 
  - for loop: may be more readable. Can be useful if you want ot iterate over only some parts... ie use a conditional or specific range.

23. **zip** and **enumerate**:
24.    
