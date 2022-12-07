# Activity 8-12 Sandwiches

# using *toppings, we can input many arguments as we like
# the asterisk in toppings means it is empty tuples

def itemsSandwich(*toppings):
    """ This function accepts abritrary arugments. """
    print("\nThe following is your sandwich toppings: ")
    for topping in toppings:
        print(f"* {topping}")

# function calls
itemsSandwich('tomato', 'pickles')
itemsSandwich('bacon', 'cheese', 'hotdog')