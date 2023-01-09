# Actvity 10-6 Addition

def addition():
    """ User will input here """
    num1  = input("Enter first Number: ")
    num2 = input("Enter Second Number: ")

    # try to execute the block then except will check for value error
    try:
        answer = int(num1) + (num2)
    except ValueError:
        print("This input should not contain characters!")
    else:
    # if there is no error else block is the continuation for try block
        print(f"{num1} + {num2} = {answer}")

addition()
