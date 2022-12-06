# Activity 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# another way of creatin a list number 1-10
# numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')