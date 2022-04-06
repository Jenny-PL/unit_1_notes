# Nested lists & dicts

## Nested lists (aka 2D arrays)
1. Acccess data within the nested list: my_list[0][2]= this will look at the FIRST value within outside list, then access the 3rd value in the next list.
2. Modify a data point?  my_list[0][2] = "new_value"


## Nested dictionaries
### Dictonaries containing lists
1. Access data in a **list** within a **dict**: 
- my_dictioary[key][index for list] = 'movie'

### Lists containing dicts
1. To acess data in a **dict** within a **list**:
- my_list[index][key] = dict_value

### Dictionaries containing dictionaries
1. Dictionaries can have dictionaries as the value pair-- but cannot be used as a key. 
- Dictionary keys must be immutable (ie- string, int, float, tuple...)
---
## Some examples
```
pet_shelters = [
    {
        'shelter_name': 'Seattle Animal Shelter', 
        'cats': ['Boots', 'Constance', 'Mr. Fussy'],
        'lizards': ['Bagon', 'Buddy'],
    },
    {
        'shelter_name': 'Seattle Humane',
        'birds': ['Tweety'],
        'cats': ['Maru', 'Lil Bub']
    }
]
```
## How do I add a new bird to Seattle Humane shelter?
```
# forcing the new name by replacing the prior list
pet_shelters[1]['birds']= ['Tweety', 'Jonathon Lingston']

# Much better way to add a name to the list:
pet_shelters[1]['birds'].append("Jon Ling")
```
## Create a new list containing all of the cats across all the shelters?
```
cats = []

for shelter in pet_shelters:
    cats.append(shelter['cats'])

print(cats) 
# [['Boots', 'Constance', 'Mr. Fussy'], ['Maru', 'Lil Bub']]
# Problem: creates nested list rather than single list
```
```
cats = []

for shelter in pet_shelters:
    cats.extend(shelter['cats'])
print(cats) 
# ['Boots', 'Constance', 'Mr. Fussy', 'Maru', 'Lil Bub']
# Fixes the nested loop problem!
```
Alternate way to avoid creating a nested list, do a nested for-loop to isolate the individual list items:
```
for shelter in pet_shelters:
    for cat in shelter['cats']:
        cats.append(cat)
print(cats)
# ['Boots', 'Constance', 'Mr. Fussy', 'Maru', 'Lil Bub']
```
More ways to do this:
```
new_cat_list = []
for i in range(len(pet_shelters)):
   new_cat_list.extend(pet_shelters[i]['cats']) 

# print output: ['Boots', 'Constance', 'Mr. Fussy', 'Maru', 'Lil Bub']

# need to use extend rather than append, as append will create a nested list.
```
Using '+' to add to the new list
<mark> Why does this one not create a nested list, too? </mark> Because adding a list to a list just adds the contents.
```
cat_list_3 = []
for shelter in pet_shelters:
    cat_list_3 += shelter['cats']

print(f"Adding to a list: {cat_list_3}")
# ['Boots', 'Constance', 'Mr. Fussy', 'Maru', 'Lil Bub']
```

Using nested list comprehensions to do this:
```
another_list = [cat for i in range(len(pet_shelters)) for cat in pet_shelters[i]['cats'] ]

# print output: ['Boots', 'Constance', 'Mr. Fussy', 'Maru', 'Lil Bub']
```
