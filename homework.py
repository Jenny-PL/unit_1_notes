
# Iterating over Data.
# Prob Set: While loops. #10.
def sidewinder(number_list):
    start_index = 0
    next_index = number_list[0]
    
  # find index of value 0; returns that position 
    while next_index != 0:
        value = number_list[next_index]
        if value == 0:
            return next_index
        else:
            next_index = number_list[next_index]
  