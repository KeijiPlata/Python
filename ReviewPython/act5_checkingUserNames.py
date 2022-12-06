# Activity 5-10 checking usernames
# This are the list of current and new users
current_users = ['keiji', 'july', 'jc', 'RENZ', 'Zach']
new_users = ['renz', 'andrew', 'zach']

# The program should be case insensitive so we need to store current_users
# in their lower case form
current_users_lower = []

# This will convert all the current_users in lowercase form
for users in current_users:
    current_users_lower.append(users.lower())

# This will check if the username is duplicate or not
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The name '{new_user}' is already been taken, please input a new username.")
    else:
        print(f"Your Username is available. Hello {new_user}")
