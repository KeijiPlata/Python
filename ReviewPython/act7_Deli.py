# Activity 7-8 Deli

sandwiches_orders = ["cheese sandwich", "Pastrami", "peanut butter sandwich", "Pastrami", "vegan sandwich", "Pastrami"]
finished_sandwich = []

# This will delete all the pastrami in the list
print("Deli has run out of pastrami")
while 'Pastrami' in sandwiches_orders:
    sandwiches_orders.remove('Pastrami')

# this will loop through the list and if the list still not empty
# It will continiously run
while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()    
    print(f"I made your {current_sandwich.title()}.")
    finished_sandwich.append(current_sandwich)

# Print the sandwiches
for sandwich in finished_sandwich:
    print(f"{sandwich.title()} is finished.")