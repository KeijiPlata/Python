# Activity 7-2 Restaurant Seating

count = input("How many people ? ")
count = int(count) # convert the input into integer

if count > 8:
    print("You have to wait for a table.")
else:
    print("The table is ready")