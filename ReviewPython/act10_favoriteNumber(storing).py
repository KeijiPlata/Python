# Activity 10-11 Favorite Number (Storing numbers)

# to use json file, we need to import it first
import json

# user input
number = input("Hello user! Can I ask your favorite numbers is? ")

# storing data to json file
filename = 'ReviewPython\\Favorite.json'
with open(filename, 'w') as f:
    # json dump will store the value inside the json file
    # it needs two argument, the value we need to store and the file object
    json.dump(number, f)
    print(f"Your favorite number is {number}, I will be remembering it next time!")
