# Week Two. 

<mark>Need to follow up on: </mark>
1. Download, learn to use 'rectangles' app
2. 
---
## Tuples & Sets, Lists & Dictionaries
1. **Lists:** Mutable, ordered, indexible, can use len()
> Lists use square brackets [1,2,3]
lists.append()
lists.remove()

2. **Dictionaries:** Mutable, good for mapping relationships. Good for detecting frequency of data(?)
> Dictionaries use curly brackets {key:value, key:value}
> Each key must be immutable
- access value with dict_name[key]
- add new key:value pair: dict_name[key] = value
   
3. **Tuples:** Immutable-- length cannot change (however the elements within the tuples are mutable), ordered, ie- can index, often used to as a way to return multiple values from a function
> Tuples use parenthesis (data1, data2)
   
4. **Sets:** No repeated values, good tool for comparing sets of data, can use len(), should only have immituable values within it; it is unordered.
> Sets use curly brackets {data1, data2}
- new set = set() 
- new set = {value1, value2 }
- **union**: all the elements in input sets (union or |)
- **intersection**: all the common elements (only the elements in all inputs:   
    **new_set = set_a.instersection(set_b)  
    new_set = set_a & set_b**  

- **difference**: All the elements of the first set, except any also in the 2nd set (all the district elements in the first set):  
**new_set = set_a.difference(set_b) or  
new_set = set_a - set_b**
- 'disjoint': No common elements.
  set_a.isdisjoint(set_b) == True or False
- subset: all the elements in set_a are contained in set_b?
set_a.issubset(set_b)
- You will get a TypeError if you try to add a mutable data type into a set.

---
## JSON: JavaScript Object Notation
   Language-indep way to store data. holds values as ordered lists of values/arrays, name/value pairs, or 'objects'.
   - Arrays are similar to python lists
   - objects are similar to python dictionaries
   - Uses nested data
   - 'true', 'false, 'null'
  
(Other options: XML, YAML, SOAP)

---
## Variables & Memory
- Scope: Where in your code can you access yoru variable? (local vs. global)

---
## Tests
- Automated Tests
- Unit tests (aka Test Case): Specifically designed to test **one function**.
- Test output: pass, fail, or gives an error
- Nominal vs. Edge Cases
  - Edge Cases: Positive vs. Negative
  - Positive: ??  
  - Negative: ??  
- Run tests from the terminal with the command **pytest**

### Anatomy of a test function:
**Test name**  
**Arrange**: set up variables  
**Act**: call the tested function  
**Assert**: Assertion statement: compare result of function with expected outcome.  

**Assert statement:** checks for truthin-ess.    
- **If truthy --> pass**, moves on to next line.  
- **if falsy --> fail**; the test execution will leave that test, and move on to the next test.  

### Test Naming
- Must start wtih: **test_** or end with **_test** to be recognized by pytest.
- Example name: **test_calculate_non_numbers_returns_type_error()**  
- A name should include:  
  - the tested function
  - context (possibly the kinds of arguments)
  - its expected outcome (usually the return value)
---

## Git
Git is a version control system (VCS) that has widespread use.  A VCS makes snapshots of files to be later referenced as a version; the files are organized into repositiories.
- In order to use Git to compare versions, sometimes we will need to tell Git to track different files in a project.  
- ??? Q about the above: isn't that the main purpose of git?

### Repositories: 'repos' (aka folder, directory)
A directory that stores project files
### Commits:
- An individual change to file(s), identified with a hash (hash = unique ID for the commit)
- should have a commit message, which identifies the main changes.
- Will contain a way to refer to the last commit, its "parent" commit

<mark>Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project.</mark>

To turn any folder into a Git project, run this command in the project root: **$ git init**