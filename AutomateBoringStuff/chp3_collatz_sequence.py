"""
Collatz Sequence
"""
def collatz(number):
    """check if even or odd, divide by 2 if even, multiply
    by 3 + 1 if odd
    """
    while number != 1:
        if number%2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)

def main_loop():
    """Main loop for the program"""
    flag =  True
    while flag:
        try:
            userinput = int(input("Enter number: \n"))
        except ValueError:
            print("This should be a number!")
        else:
            collatz(userinput)
            flag = validation(flag)

def validation(flag):
    """check if the user still want to continue"""
    userinput = input("Press any key to continue, q to quit: ")
    if userinput == "q":
        flag = False
        print("Thank you for using the program")
    return flag

if __name__ == "__main__":
    main_loop()
