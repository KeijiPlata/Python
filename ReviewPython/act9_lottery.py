# Activity 9-14 Lottery

# import standard library random
from random import choice

# creating a function that pick 4 random numbers
def pick_randomNumber(numbers, letters):
    """ Picking a random number and letter from a list """
    print("Any ticket matching these four numbers and  two letters wins a prize")
    # choosing 4 random numbers and print it
    i = 1
    while i <= 4:
        # pick a number from list
        chosen = choice(numbers)
        print(chosen) 

        # deletes from list so i can't be duplicated
        numbers.remove(chosen) 

        # loop
        i += 1

    # choosing 2 random letters and print it
    i = 1
    while i <= 2:
        chosen = choice(letters)
        print(chosen)
        letters.remove(chosen) 
        i += 1

# creating a list containing series of 10 numbers and five letters
numbersList = list(range(1,11))
lettersList = ["a", "b", "c", "d", "e"]

# [:] the colon here is to make a copy of the list and keep the original
pick_randomNumber(numbersList[:], lettersList[:])
pick_randomNumber(numbersList[:], lettersList[:])
pick_randomNumber(numbersList[:], lettersList[:])
