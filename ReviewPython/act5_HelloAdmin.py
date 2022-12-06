# Activity 5-8 hello admin and Activity 5-9

# 'keiji', 'july', 'admin'
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again.")
else:
    print("We need some users!")