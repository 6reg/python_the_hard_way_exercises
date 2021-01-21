# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('too low')
    elif guess > secretNumber:
        print('too high')
    else:
        break # this condition is the correct guess

if guess == secretNumber:
    print('you guessed it in ' + str(guessesTaken) + ' guesses')
else: 
    print('nope. it was ' + str(secretNumber))
