# import the package needed
import random 

def getSecretNummber():
    """ Get the secret number for the game """
    secretNumber = random.randint(1, 20)
    return secretNumber

def askPlayer(secretNumber):
    """Ask player 6 times to guess the number """
    print("I am thinking of a number between 1 and 20")
    for guessTaken in range(1, 7):
        # user input
        print("Take a guess: ")
        guess = int(input())

        # condition to know if the number is high or low
        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('You guess is too high')
        else:
            # if user got it right, return guess, and number of guesses
            return guess, guessTaken
    
    # return guess if the use didn't get it right
    return guess, guessTaken
            
def displayNumber(secretNumber, guess, guesstaken):
    if guess == secretNumber:
        print(f"Good Job! you guessed my number in {guesstaken}")
    else:
        print(f'Nope. The number I was thinking of was {secretNumber}')

secret = getSecretNummber()
guess, guesstaken = askPlayer(secret)
displayNumber(secret, guess, guesstaken)
