# Activity 5-1 Conditional Test

# This checks if the car is subaru
car = 'subaru'
print("Is car == 'subaru'? I predict it is True")
print(car == 'subaru') # This will return true

# Thic checks if the car is audi
print("\nIs car == 'audi? I predict it is False")
print(car == 'audi') # This will return false

# Activity 5-2
# Test for inequality
print("\nIs car != 'subaru'? I predict it is False")
print(car != 'subaru') # This will return false

print("\nIs car != 'audi? I predict it is False")
print(car != 'audi') # This will return true

car = 'SUBARU' # change the value to capital letter to try lower()
# Test using lower() method
print("\nIs car.lower() == 'audi'? I predict it is False")
print(car.lower() == 'audi') # This will return false

print("\nIs car.lower() == 'subaru'? I predict it is False")
print(car.lower() == 'subaru') # This will return false

# Numerical Test
number = 10
print("\nIs number == 10? I predict it is True")
print(number == 10) # This will return true

print("\nIs number != 5? I predict it is True")
print(number != 5) # This will return True

print("\nIs number == 5? I predict it is False")
print(number == 5) # This will return False

print("\nIs number > 5? I predict it is True")
print(number > 5) # This will return True

print("\nIs number < 5? I predict it is False")
print(number < 5) # This will return False

print("\nIs number >= 5? I predict it is True")
print(number >= 5) # This will return True

print("\nIs number <= 5? I predict it is True")
print(number <= 5) # This will return True

# This will return True since 10 > 5 and 10 < 11
print("\nIs number > 5 and number < 11? I predict it is True")
print(number > 5 and number < 11) 

# This will return False since  10 is not less than 5
print("\nIs number > 5 and number < 5? I predict it is false")
print(number > 5 and number < 5) 

print("\nIs number > 5 or number < 5? I predict it is True")
print(number > 5 or number < 5) # This will return True since there is one true
# 10>5 is true but 10 < 5 is false,since there is one true,the statement is true

# This will return False since there are both false
print("\nIs number > 11 or number < 5? I predict it is False")
print(number > 11 or number < 5) # 10 > 11 false, 10 < 5 is False

# check the list
lists = ['keiji', 'july']
isInList = 'keiji'

# checks if there is keiji in the list: return True
print("\nis there keiji in the list?")
print(isInList in lists)

# checks if there is no keiji in the list : return false
print("\nis there not keiji in the list?")
print(isInList not in lists)
