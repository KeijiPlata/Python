# Activity 6-1 Person

# Storing all of the information about the person in dictionary
# proper format of storing dictionary
person = {
    'firstName': 'Lord Miacky Keiji',
    'lastName': 'Plata',
    'age' : 20, 
    'city': 'Cainta, Rizal'
    }

person2 = {
    'firstName': 'Sherwin',
    'lastName': 'Esternon',
    'age' : 19, 
    'city': 'Cainta, Rizal'
    }

# storing dictionary inside the list
people = [person, person2]

# looping through the list
for onePeople in people:
    print(f"Fullname: {onePeople['firstName']} {onePeople['lastName']}")
    print(f"Age: {onePeople['age']}")
    print(f"City: {onePeople['city']}")

# # print each information in the dictionary
# print(f"First Name: {person['firstName']}")
# print(f"Last Name: {person['lastName']}")
# print(f"Age: {person['age']}")
# print(f"City: {person['city']}")



