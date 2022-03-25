# Big O notation
Big O gives relative information about how long a program will take to run + how much space it will use.  

-The syntax use for Big O complexities is O(...)

## Some common Big O complexity curves (from fastest to slowest):

1. **O(1) Constant**: no change with increased input size <mark>*Ideal</mark>
2. **O(log n): Logarithmic**: complexity increases by 1 when input size is doubled. <mark>*Very good</mark>
3. **O(n): Linear**: Proportional change in complexity (ie- if input size doubles, complexity doubles)
4. **O(n logn): Log linear**: input size is multiplied by base-2 log of input size.
5. **O(n^2): Quadratic**: complexity is proportional to size of input squared (often involves two nested loops)
6. **O(2^n): Exponential**: Complexity doubles with each input increase of 1. <mark>*Bad. very slow </mark>(This is the opposite of logarithmic)