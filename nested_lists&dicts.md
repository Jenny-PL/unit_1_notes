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