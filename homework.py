import pdb

number_list = [4, 9, 0, 0, 1, 8, 0, 0, 11, 5, 0, 10] 

def sidewinder(number_list):
    next_index = 0

    # find index of value 0; returns that position
    while number_list[next_index] != 0:
        next_index = number_list[next_index]
        # pdb.set_trace()
    return next_index
    
answer = sidewinder(number_list)
print(answer)