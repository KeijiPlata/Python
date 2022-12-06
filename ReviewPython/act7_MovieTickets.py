# Activity 7-5 Movie Tickets

prompt = "Please input your age to determine the ticket price. "

# We can also use flag here to easily terminate the program when we have
# multiple test
while True:
    # getting the user input
    age = input(prompt)

    # checking if the user typed quit so we can terminate the program
    if age == 'quit':
        break
    
    # converting age into integer
    age = int(age)

    if age < 3:
        # print("Your ticket is free")
        ticket = 0
    elif age < 12:
        # print("Your ticket is 10")
        ticket = 10
    elif age >= 12:
        # print("Your ticket is 15")
        ticket = 15
    
    print(f"You ticket is {ticket}")
    
  
