# Activity 4-1 Pizzas
pizzas = ["Hawaiian Pizza", "Pepperoni Pizza", "Cheesy Pizza", "All toppings", "Beef pizza"]
friends_pizza = pizzas[:] # Copying the list

# Appending new list
pizzas.append("Burger Pizzas")
friends_pizza.append("Ice cream Pizza")

print("Original Pizza:")
for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love eating pizza.")

print("Friends list:")
for pizza in friends_pizza:
    print(pizza)

