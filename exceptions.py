__author__ = 'Jeffrey'

# try:
#     numerator = int(input("Enter the numerator:"))
#     denominator = int(input("Enter the denominator"))
#     fraction = numerator / denominator
# except ValueError:
#     print("Numerator and denominator must be valid numbers")
# except ZeroDivisionError:
#     print("You cheeky bastard, you know you can't divide by zero!")
# print("Finished.")

# 1. When a value entered for the two integers is not valid, such as a letter,\
#         any non-decimal character.
# 2. When a cheeky shit tries to divide by 0 of course.
# 3. Yes, just make sure there a check on each value before the division method


def get_integer():
    finished = False
    result = 0
    while not finished:
        try:
            prompt = int(input("Please enter a number."))
            finished = True
        except ValueError:
            print("You must enter a valid number.")
    return result

get_integer()

# def get_number(value_type=int):
