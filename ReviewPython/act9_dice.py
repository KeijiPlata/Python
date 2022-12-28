# Activity 9-13 Dice 

# importing standard library random
from random import randint

class Dice:
    """ This class will give random number like a dice """
    def __init__(self, sides=6):
        """ Initializing a variable side which has a default value of 6 """
        self.sides = sides

    def roll_die(self):
        """ Picking a random number between 1 and the number of sides """
        print(randint(1, self.sides))

# creating instance for Dice with 6 sides
rollDice6 = Dice()
print("Generate a random number between 1-6")

# initializing a variable so we can loop it 10 times
number = 1
while number <= 10:
    rollDice6.roll_die()
    number += 1

# creating instance for Dice with 10 sides
rollDice10 = Dice(10)
print("Generate a random number between 1-10")

# initializing a variable so we can loop it 10 times
number = 1
while number <= 10:
    rollDice10.roll_die()
    number += 1

# creating instance for Dice with 10 sides
rollDice20 = Dice(20)
print("Generate a random number between 1-20")

# initializing a variable so we can loop it 10 times
number = 1
while number <= 10:
    rollDice20.roll_die()
    number += 1