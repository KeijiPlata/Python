# Activity 4-5 adding a miliion
miliion = []
for count in range (1, 1_000_001):
    miliion.append(count)

print(f"This is the highest number in the list: {max(miliion)}")
print(f"This is the lowest number in the list: {min(miliion)}")
print(f"Adding the highest and the lowest number in the list: {max(miliion) + min(miliion)}")

# Another method:
print("\nAnother Method(Right answer):\n")
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))
