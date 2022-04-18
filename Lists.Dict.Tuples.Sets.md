### Week Two. 
<mark>Need to follow up on: </mark>
1. Download, learn to use 'rectangles' app
2. Learn how to check git status in VS Code
3. Watch Auberon class for TDD?  
4. Practice writing tests for some of the code in Learn?
5. Algorithum intro from digital [algo practice](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=22802e07-ea29-40b2-a856-ae5a0014633c)    and [slides](https://docs.google.com/presentation/d/1gpkEZ-UsCVozLJ7E1fH-MZVc0-rwh1kpIYIwCT7CG4w/edit#slide=id.g115ca252154_0_59) and [solutions](https://docs.google.com/presentation/d/1yw9QRWIMabkGjRijNH8Qec9YlBI0_7HouczAv8F_miI/edit#slide=id.g117a86c46dc_0_73)    
6. [zoom room for Algo sessions](aud-digi.adadev.org)
---
# Tuples & Sets, Lists & Dictionaries

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
