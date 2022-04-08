# Big O notation
Big O gives relative information about how long a program will take to run + how much space it will use.  

-The syntax use for Big O complexities is O(...)

## Some common Big O complexity curves (from fastest to slowest):

1. **O(1) Constant**: no change with increased input size <mark>*Ideal</mark>
2. **O(log n): Logarithmic**: complexity increases by 1 when input size is doubled.  **aka Binary search**  <mark>*Very good</mark>
3. **O(n): Linear**: Proportional change in complexity (ie- if input size doubles, complexity doubles)
4. **O(n logn): Log linear**: input size is multiplied by base-2 log of input size.
5. **O(n^2): Quadratic**: complexity is proportional to size of input squared (often involves two nested loops)
6. **O(n^3): Cubic**: Complexity is proportional to the size of input cubed.
7. **O(2^n): Exponential**: Complexity doubles with each input increase of 1. <mark>*Bad. very slow </mark>(This is the opposite of logarithmic)
8. **O(n!): factorial**: Available options decreases by 1 with each iteration... example all the possible orders for visiting a list of cities, one time each: 5 cities: 5*4*3*2*1, or O(5!), aka O(n!)
---
**Dominant order**: Part of the complexity that has the greatest effect(drop the constants-- these have a fixed value.  if O(n + n^2), O(n^2) presents the dominant order.  
**Tips:**  
- Identify all the variables (count only when initialized, not when re-assigned)
- Identify which variables have a variable size
- identify all the operations
- Idenity which operations are related to the variable size
---
**For loops**:
1. Count how many times a loop will run
2. Mulitply whatever is nested inside the loop
3. Add consecutive loops, multiply nested loops
---
**Lists**:  
**Time complexity**
1. list.append(x)  --> O(1), aka constant
2. list[i] = x     --> O(1), aka constant
3. x in list       --> O(n), aka linear  
   
**Space complexity**   
space = len(list)* size of item in list

---
**Dicts**:  
**Time complexity**
1. dict[key] = value --> O(1), aka constant
2. key in dict       --> O(1), aka constant
   
**Space complexity**   
space = O(# of key:values)* size of key + O(# of values)* size of value

---
**Str**:  
**Time complexity**
1. str = "something"   --> O(# of char), aka constant
- ?? O(9)
1. str += str2         --> O(# of char in str1 + # of char in str2), aka constant
   
**Space complexity**   
space = O(# of char)