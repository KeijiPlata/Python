# Activity 7-3 multiples of 10

# User input
number = input("Input a number: ")
number = int(number) # convert

if number % 10 == 0:
    print(f"The number {number} is multiple of 10")
else:
    print(f"The number {number} is not multiple of 10")