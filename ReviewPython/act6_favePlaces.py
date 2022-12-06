# Activity 6-9 favorite places

favorite_places = {
    'keiji': ['japan', 'korea', 'paris'],
    'shella': ['korea', 'singapore', 'malaysia'],
    'deleck': ['taiwan', 'china', 'russia']
}

for name, places in favorite_places.items():
    print(f"\nName: {name.title()}")
    print("Favorite Places: ")
    for place in places:
        print(place.title(), end=" ")

