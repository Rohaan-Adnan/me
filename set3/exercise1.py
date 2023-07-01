# -*- coding: UTF-8 -*-
"""Set 3.

Modify each function until the tests pass.
"""

#Used a while loop to generate a list of numbers with parameters provided
def loop_ranger(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    result = []
    while start < stop:
        result.append(start)
        start += step

    return result


#generates a range of numbers between the start and stop values, 
#with a step size of 2
def two_step_ranger(start, stop):
    
     return loop_ranger(start, stop, step=2)

#This code repeatedly prompts for a valid number within a given range.
def stubborn_asker(low, high):
    while True:
        response = input("Enter a number between {} and {}: ".format(low, high))
        try:
            number = int(response)
            if low <= number <= high:
                return number
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
 

#repeatedly prompts the user to enter a number, only accepts numbers as a input 
# and returns the valid number.
def not_number_rejector(message):

    while True:
        response = input(message)
        try:
            number = float(response)  
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#The super_asker function repeatedly prompts for a valid number within a specified range and returns it.
def super_asker(low, high):
    while True:
        response = input("Enter a number between {} and {}: ".format(low, high))
        try:
            number = float(response)
            if low <= number <= high:
                return number
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
