# Activity 3-8 Seeing the world

# Store the location you want to visit in a list and print it

locations = ["Japan", "Korea", "Italy", "Spain"]
print("Original")
print(locations)

# Use sorted() to sort temporarily
print("Sort the list temporarily")
print(sorted(locations))

# Print again the original 
print("Print again the original")
print(locations)

# Use sorted again but not in reverse order
print("Print again sorted temporarily in reverse order")
print(sorted(locations, reverse=True))

# Print again the original 
print("Print again the original")
print(locations)

# Make the list in reverse order
print("List in reverse order")
locations.reverse()
print(locations)

# Reverse again to redo our reverse in previous
print("Reverse order again to redo what we did")
locations.reverse()
print(locations)

# Using sort to permanently change the order
print("Using sort to permanent change the list")
locations.sort()
print(locations)

# Using sort again but in reverse order
print("permanent change of list but in reverse")
locations.sort(reverse=True)
print(locations)
