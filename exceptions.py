# def is_valid_int(input_num):
#     try:
#         x = int(input_num)
#     except ValueError as err:
#         print(f"{err}. Please enter a valid number.")

# is_valid_int("four")


# def enter_candy(candy_choice):
#     candy_list = ["lollipops", "m&ms", "gummy bears"]
#     try:
#         print(f"Your candy choice is {candy_choice}")
#         print(f"You selected {candy_list[candy_choice]}")
#     except IndexError as error:
#         print(f"A {error} was entered. Please enter 0, 1, or 2.")
# enter_candy(9999)

def do_weird_number_math(apple):
    print("We're entering the do_weird_number_math function! Value of apple:", apple)

    try:
        if apple < 10:
            banana = apple / (apple - 3)

        print("Value of banana:", banana)
        print("Value of carrot:", carrot)
    except ZeroDivisionError as err:
        print(f"apple is 3, so it tried to divide by zero. {err}")
    except UnboundLocalError as err:
        print(f"apple is valid, but banana was never given a value, so we get an error. {err}")
    except NameError as err:
        print(f"We're trying to print carrot, but carrot is never defined before this. {err}")

    print("**************")

# The following line raises a ZeroDivisionError
do_weird_number_math(3)

# The following line raises an UnboundLocalError
do_weird_number_math(5555)

# This line raises a NameError
do_weird_number_math(8)