# Activity 4-10 using slices
# I will just create new list

pizzas = ["Pepporoni", "Hawaiian", "Cheesy", "All toppings", "Beef"]

print("The first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("The first three items in the middle:")
for pizza in pizzas[1:4]:
    print(pizza)

print("The last three items in the list")
for pizza in pizzas[-3:]:
    print(pizza)