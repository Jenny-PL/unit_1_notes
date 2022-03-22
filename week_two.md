# Week Two. 

<mark>Need to follow up on: </mark>
1. Download, learn to use 'rectangles' app
2. Learn how to check git status in VS Code
3. Watch Auberon class for TDD?  
4. Practice writing tests for some of the code in Learn?
   
5. Algorithum intro from digital [algo practice](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=22802e07-ea29-40b2-a856-ae5a0014633c)    and [slides](https://docs.google.com/presentation/d/1gpkEZ-UsCVozLJ7E1fH-MZVc0-rwh1kpIYIwCT7CG4w/edit#slide=id.g115ca252154_0_59) and [solutions](https://docs.google.com/presentation/d/1yw9QRWIMabkGjRijNH8Qec9YlBI0_7HouczAv8F_miI/edit#slide=id.g117a86c46dc_0_73)    
6. [zoom room for Algo sessions](aud-digi.adadev.org)
---
## Tuples & Sets, Lists & Dictionaries
1. **Lists:** Mutable, ordered, indexible, can use len()
> Lists use square brackets [1,2,3]
lists.append(new_item)
lists.remove(item_to_remove)

2. **Dictionaries:** Mutable, good for mapping relationships. Good for detecting frequency of data(?)
> Dictionaries use curly brackets {key:value, key:value}
> Each key must be immutable
- access value with dict_name[key]
- add new key:value pair: dict_name[key] = value
   
3. **Tuples:** Immutable-- length cannot change (however the elements within the tuples are mutable), ordered, ie- can index, often used to as a way to return multiple values from a function
> Tuples use parenthesis (data1, data2)  
> tuple_example = tuple([1,3,5,7], "odd numbers")
- Single elment tuple wil have a comma following the single element. 
  - fruit = ('apple',)
- Tuples support concatination (+) and repitition (*)
1. **Sets:** No repeated values, good tool for comparing sets of data, can use len(), should only have **immituable values** within it; it is unordered.
> Sets use curly brackets {data1, data2}
- new set = set() 
- new set = {value1, value2 }
- color_set.add('blue')
- color_set.remove('yellow')
- color_set.discard('orange')
  - Both .remove() and .discard() will remove items, but **remove() will raise KeyError if element is not present**, while discard() will not.
- color_set.pop() Returns a **random** element.
- color_set.clear() Empties a set.




- **union**: all the elements in input sets (union or |)
  - all_students = class_one.union(class_two)
  - new_set = set_a.union(set_b)
  - new_set = set_a | set_b
- **intersection**: all the common elements (only the elements in all inputs:   
    **new_set = set_a.instersection(set_b)  
    new_set = set_a & set_b**  

- **difference**: All the elements of the first set, except any also in the 2nd set (all the district elements in the first set):  
**new_set = set_a.difference(set_b) or  
new_set = set_a - set_b**
- **'disjoint':** No common elements.
  set_a.isdisjoint(set_b) == True or False
- **subset**: all the elements in set_a are contained in set_b?
set_a.issubset(set_b)
- You will get a TypeError if you try to **add a mutable data type (ie- list, dict)** into a set, with msg 'unhashable type'.

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
- Tool for seeing what your code is doing: [Python Tutor](https://cs1110.cs.cornell.edu/tutor/#mode=edit0)
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
- [Good basic summary of git, including common commands](https://www.ayyjohn.com/posts/daily-git)
### Repositories: 'repos' (aka folder, directory)
A directory that stores project files
### Commits:
- An individual change to file(s), identified with a hash (hash = unique ID for the commit)
- should have a commit message, which identifies the main changes.
- Will contain a way to refer to the last commit, its "parent" commit

<mark>Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project.</mark>

To turn any folder into a Git project, run this command in the project root: **$ git init**

### More on Git commits:
- **git diff:** will show changes that have been made.
- good commit size is **one** meaningful change.   
- **git status**: This will tell us what is in the staging area
  
**To make a commit: (1) Put in staging area, (2) then commit.**
- *local changes area* (only on my computer)-->  **git add <file_name>** or **git add .**--> *staging area* --> **git commmit -m "message describing the changes"**

- Alternate: **git add -p** This will allow you to go throught the local changes 'hunk' by 'hunk' and choose y/n about whether to add to the staging area.

Steps:
1. git add
2. git commit
3. git push

### Pushing to github:
  - Copy link from github.
  - git remote add origin [copied web address]
  -     git remote add origin https://github.com/yourname/yourproject.git
  - Push your branch to Github:
  -     git push -u origin main
--- 

## Git example
    echo "# project" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin git@github.com:githubusername/project.git
    git push -u origin master
## Packages 
- a package is a collection of Python modules (ie- pytest, etc)
- Module:  every .py file is a module
- Managing a package: important, to avoid breaking our code!
- pip: packaging installer for python; can use it (in terminal) to install any package in PyPI.
  - We will use <mark> pip3 </mark> to install packages to work with python3.
- PyPI: Python Packaging Index
- To list all packages on the computer: **pip3 list**

### Important concept: installing in virtual environments vs. global 
- requirements.txt will specify the packages and versions required to work collaberatively on a project.
- You can download these packages to a virtual environment so that everyone is working with the same versions/materials.
  - You will have a new virtual environment for new projects
- If a virtual environment is made w/Python3, when we're inside this activated environment, we can use **python3** or **python** as commands to mean Python3.
## Using virtual environments
1. Making:
     - python3 -m venv venv
3. Activating:
   -  $ source venv/bin/activate
   - We know we are in the virtual environment(venv) because the command line changes:   
  <mark>(venv) $ project-root-folder </mark>
3. Install packages in the virtual enir:
   - pip install -r requirements.txt  
   - pip install <package_name> 
4. Deactivating
   - . $ deactivate
   - Command line will change back:   
   - <mark>$ project-root-folder</mark>  

## Iterations
**continue**: skips the rest of the code in that iteration, goes to the next iteration vs.  
**break:** leaves the loop.  