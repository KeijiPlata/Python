# Activtiy 6-6 Polling

# Dictionary
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

# list of people who participate and not in poll
polls = ['sarah', 'phil', 'jen', 'sarah', 'mario']

# loopint through the list to print their name and languages they like
for name, lang in favorite_languages.items():
    print(f"\nThank you {name.title()} for responding {lang.title()} in our poll")

# looping to check if the list value is inside the dictionary key
for poll in polls:
    # if true
    if poll in favorite_languages.keys():
        print(f"Once again, Thank you {poll.title()} for participating.")

    # if false
    if poll not in favorite_languages.keys():
        print(f"{poll.title()}, please participate in our poll. Thank you.")