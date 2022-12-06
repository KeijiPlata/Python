# Activity 6-2 favorite numbers

# use dictionary to store people's favorite numbers

faveNumbers = {
    'keiji': [24, 15, 4],
    'july': [5, 25, 50],
    'zach': [2, 3, 4], 
    'andrew': [69, 420, 34], 
    'kisses': [100, 300, 600]
    }

# looping to the dictionary and list
for name, numbers in faveNumbers.items():
    print(f"\nNames: {name.title()}")
    print("Favorite Numbers:")
    for number in numbers:
        # the end is used to eliminate newline and replace with 
        # something else like space or comma
        print(number, end=" ") 

# print(f"Keiji's Favorite number: {faveNumbers['keiji']}")
# print(f"July's Favorite number: {faveNumbers['july']}")
# print(f"Zach's Favorite number: {faveNumbers['zach']}")
# print(f"Andrew's Favorite number: {faveNumbers['andrew']}")
# print(f"Kisses's Favorite number: {faveNumbers['kisses']}")



