# Activity 7-4 pizza toppings

prompt = "Please enter many toppings as you like. "

active = True

while active:
    toppings = input(prompt)

    if toppings == "quit":
        active = False
        print("We are now delivering you pizza.")
        print("Loop terminated.")
    else:
        print(f"{toppings.title()}. We are adding this topping to your pizza.")