# Activity 6-8 pets

# the list is not working since you can't put a title method to a list
# that is why it has a error

pet1 = {
    'animal': 'dog',
    'name': 'chewy',
    # 'color': ['white', 'brown'],
    'owner': 'shella'
}

pet2 = {
    'animal': 'cat',
    'name': 'tom',
    # 'color': ['black', 'brown'],
    'owner': 'mercy'
}

pet3 = {
    'animal': 'cat',
    'name': 'alex',
    # 'color': ['black', 'white'],
    'owner': 'deleck'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\n")
    for key, value in pet.items():
        print(f"{key.title()} : {value.title()}")



