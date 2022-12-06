# Activity 3-4
Friends = ["Jaycee", "Renz", "Andrew", "Zach"]
message = "I would like to invite you to dinner, "

print(f"{message}{Friends[0]}")
print(f"{message}{Friends[1]}")
print(f"{message}{Friends[2]}")
print(f"{message}{Friends[3]}")

# Activity 3-5 remove one and add one
print(f"Mr. {Friends[3]} declines the invitation")
del Friends[3]
Friends.append("Kisses")
print(f"I will invite {Friends[3]} instead")

# Activity 3-6
print("We found a bigger table, so I can invite more")
Friends.insert(0, "Jordan")
Friends.insert(2, "Zach")
Friends.append("Ed")

print(f"{message}{Friends[0]}")
print(f"{message}{Friends[1]}")
print(f"{message}{Friends[2]}")
print(f"{message}{Friends[3]}")
print(f"{message}{Friends[4]}")
print(f"{message}{Friends[5]}")
print(f"{message}{Friends[6]}")


# Activity 3-7
sorryMessage = "Sorry I can't invite you to dinner"
print("\nI can only invite two people")
print(f"{sorryMessage}, {Friends.pop()}")
print(f"{sorryMessage}, {Friends.pop()}")
print(f"{sorryMessage}, {Friends.pop()}")
print(f"{sorryMessage}, {Friends.pop()}")
print(f"{sorryMessage}, {Friends.pop()}")

print(f"{Friends[0]} and {Friends[1]}, you are still invited for dinner")
# there should be no one in list anymore
del Friends[1]
del Friends[0]

print(Friends)