# Activity 10-11 Favorite Number (Reading)
# Here we will read the file we created 

# to use json file, we need to import it first
import json

filename = 'ReviewPython\\Favorite.json'
with open(filename) as f:
    favoriteNumber = json.load(f)
print(f"I remember your favorite number! its {favoriteNumber}!")