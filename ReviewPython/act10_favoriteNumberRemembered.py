# Activity 10-12 Favorite number remembered!

# import json so we can store a value inside a json file
import json

def dumpFavoriteNumber():
    """ This will let the user input a value inside the json file """
    # user input
    number = input("Hello user! Can I ask your favorite number is? ")

    # storing data to json file
    filename = 'ReviewPython\\Favorite.json'
    with open(filename, 'w') as f:
        # json dump will store the value inside the json file
        # it needs two argument, the value we need to store and the file object
        json.dump(number, f)
    return number

def readFavoriteNumber():
    """ This will read the json file and check if the json file is existing """
    # file path
    filename = 'ReviewPython\\Favorite.json'

    # this block of code will try to read the json file
    # if the json file is not existing, it will return none
    # else it will return favorite number
    try:
        with open(filename) as f:
            favoriteNumber = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favoriteNumber

def printFavoriteNumber():
    """Print the user favorite number """
    # storing the the value of readFavoriteNumber into a variable
    # if the variable number is empty, it will return false. It means the file
    # is not existing
    # if the number is not existing, it will run the function dumpFavoriteNumber
    # and generate new favorite number for the user
    # if there is a value inside the variable number, it will just copy the 
    # number that the function read and display it.
    number = readFavoriteNumber()
    if number:
        print(f"I remember your favorite number! its {number}!")
    else:
        number = dumpFavoriteNumber()
        print(f"Your favorite number is {number}, I will be remembering it next time!")

# calling the function
printFavoriteNumber()
