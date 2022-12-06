# Activity 6-5

rivers = {
    'nile' : 'egypt', 
    'amazon': 'america', 
    'congo' : 'africa'
    }

for river, place in rivers.items():
    print(f"The {river.title()} runs through {place.title()}.")

print("\nTheses are the rivers that included in the dictionary:")
for river in rivers.keys():
    print(river)

print("\nThese are the places that included in the dictionary:")
for place in rivers.values():
    print(place)
