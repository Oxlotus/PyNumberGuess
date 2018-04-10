##
# Author: Alex Metz (alex.tar.gz@gmail.com)
##

# Import Section
from random import *

# Logic Section
def guessing_game(tooLow, tooHigh, guesses):
    print("\nGuess a value between {} and {}: ".format(tooLow,tooHigh))
    randomNumber = randint(tooLow, tooHigh)

    for _ in range(guesses):
        guess = int(input("Enter a number: "))

        try:
            if guess == randomNumber:
                print('Your guess is correct! It took you {}/{} ({}%) guess(es) to get {}.'.format((_+1),guesses,"{0:.2f}".format((float(_+1)/int(guesses))*100),randomNumber))
                return
            elif guess < int(tooLow) or guess > int(tooHigh):
                print('Your guess is out of bounds. Try again.')
            elif guess < randomNumber:
                print('Your guess is too low. Try again.')
            elif guess > randomNumber:
                print('Your guess is too high. Try again.')
        except ValueError:
            print("Your guess isn't a number.")

    print("\nYou didn't guess correctly within the chosen {} round(s). You lose.".format(guesses,guesses=guesses))
    print("Correct number: {}".format(randomNumber))

tooLow = int(input("What minimum value do you want? "))
tooHigh = int(input("What maximum value do you want? "))
guesses = int(input("How many attempts would you like? "))
guessing_game(tooLow, tooHigh, guesses)
