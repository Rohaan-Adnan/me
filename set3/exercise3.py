"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

# The code defines a guessing game where the user is prompted to enter a lower and upper bound, 
# and then attempts to guess a randomly generated number within that range, 
# with feedback provided after each guess.
def advancedGuessingGame():
    print("Welcome to the guessing game!")
    lowerBound = not_number_rejector("Enter a lower bound: ")
    upperBound = not_number_rejector("Enter an upper bound: ")
    print(f"OK then, a number between {lowerBound} and {upperBound}?")

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = not_number_rejector("Guess a number: ")
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


def not_number_rejector(message):
    while True:
        response = input(message)
        try:
            number = int(response)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


advancedGuessingGame()


if __name__ == "__main__":
    print(advancedGuessingGame())
