# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


#The code performs a binary search to find a specified number within a given range, 
# keeping track of the number of tries, and returning the final guess and number of tries.
import math


def binary_search(low, high, actual_number):

    tries = 0
    guess = 0


    while low <= high:
        guess = math.floor((low + high) / 2) 
        print(f"Guess: {guess}")
        tries += 1

        if guess == actual_number:
            break  

        if guess < actual_number:
            low = guess + 1  
        else:
            high = guess - 1  

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
