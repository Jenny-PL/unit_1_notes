# Lists & Memory

An array, or list, has an id #  
- This ID # contains an array of references and metadata (ie- info about length of list):
- each element in the list refers to a different object in memory. 
- You can check this by comparing the id(data) vs. id(data[index]).
```
list = [3,5,"something", 6]
>>> id(list)
4487426560
>>> id(list[1])
4485650864
```
Q: **?? Is reference address the same as id?**  

 Per this lesson, reference address = start_point_of_list + size_of_refence*index#

 start_of_items_collection + size_of_reference * index_number   
 So if:

The items collection started at the memory address 100
Each reference is 8 units in size
We could find a reference to index 3 of a list with:

reference_address = 100 + 8 * 3

<mark> Q from class re: memory & lists </mark>
- Class example frm 3/30/22:
```
within a for loop:
    movie = {}
    movie['title] = title
    move_list.append(title) # this is appending a dict with key:value of 'title': #'indiv_movie_title' to a list of movies
```
Q: In the example, a new list was created each time, with just one dictinary entry.
My Q: Why didn't it just empty out the existing list and replace it, since its the same variable name?
