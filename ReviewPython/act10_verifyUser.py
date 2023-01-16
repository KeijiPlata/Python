# Activity 10-13 Verify user
# copy the file from the book and add verification to validate 
# if the user is still the one who is using the program

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'ReviewPython\\username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
         return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'ReviewPython\\username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

def validate_user():
    """ This will checks if user who is using the program is correct """
    # asks the user if the username given is correct
    # if not, it will ask for new username and edit the json file
    validation = input("Is your username is correct? Y or N: ")
    if validation == 'Y' or validation == 'y':
        print("Thank you for using the program!")
    elif validation == 'N' or validation == 'n':
        print("Sorry for inconvinience, can i ask")
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
validate_user()
