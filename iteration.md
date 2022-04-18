# Iteration (aka loops)

Uses of loops:
1. Finding an element:
   1. often used to find the 1st of a type of element.
2. To operate on each item of a list

## Iterating over Lists: 'for loops' vs. 'while loops':
## For loops: Most commmon
   1. Predetermined/known number of iterations
   2. sytax: for ___ in ____:
      - for elem in list
      - for index in range(len(list)
      - for index, elem in enumerate(list)
      - for key in dict
      - for item in dict.items()
      - for key, value in dict.items()
   3. range(start, stop, step): 
      - start: incluse
      - stop: exclusive for the range
      - Only stop is required
   4. "for else" loop: possible, but don't do it!
      - The else clause at the end of the loop will run once the loop finishes as long as the loop did not exit because of a break statement.
## while loop
   1. Loops until some condition is met -- unkown # of loops
      - while with a counter (iterate over a list)


## Continue vs. break
**continue**: skips the rest of the code in that iteration, goes to the next iteration (stays in the loop)  
**break:** leaves the loop. 