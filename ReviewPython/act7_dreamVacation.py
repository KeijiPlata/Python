# Activity 7-10 Dream Vacaton

dreamVacation = {}
active = True
instruction = 'If you could visit one place in the world, where would you go? '

while active:
    # Prompt
    name = input("What is your name? ")
    vacation = input(instruction)

    # To store something to our dictionary we need key value pair like this
    dreamVacation[name] = vacation

    # This will prompt the user if they want to continue
    loop = input("Would you like to continue? (yes/no) ")
    if loop == 'no':
        active = False

# print all of the items inside the dictionary
for name, dream in dreamVacation.items():
    print(f"{name.title()}, your dream vacation is {dream.title()}.")
