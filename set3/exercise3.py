"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

# The code defines a guessing game where the user is prompted to enter a lower and upper bound, 
# and then attempts to guess a randomly generated number within that range, 
# with feedback provided after each guess.
def limit_integer_value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please use integer.")

def advancedGuessingGame():
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    while True:
        try:
            lowerBound = limit_integer_value("Enter a lower bound: ")
            upperBound = limit_integer_value("Enter an upper bound: ")
            break
        except ValueError:
            print("Please use integer datatype entry.")

    print(f"OK then, a number between {lowerBound} and {upperBound}?")

    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False

    while not guessed:
        guessedNumber = limit_integer_value("Guess a number: ")
        print(f"You guessed {guessedNumber},")

        if guessedNumber < lowerBound or guessedNumber > upperBound:
            print("Your Guessed number is outside the Bound")
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        elif guessedNumber > actualNumber:
            print("Too big, try again :'(")
        else:
            print(f"You got it!! It was {actualNumber}")
            guessed = True

    return "You got it!"

if __name__ == "__main__":
    print(advancedGuessingGame())