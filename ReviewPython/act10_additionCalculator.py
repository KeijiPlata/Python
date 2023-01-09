# Activity 10-7 Addition Calculator
# copy of 10-6
flag = True
def addition():
    """ User will input here and program will add two numbers """
    num1  = input("Enter first Number: ")
    num2 = input("Enter Second Number: ")

    # try to execute the block then except will check for value error
    try:
             answer = int(num1) + int(num2)  
    except ValueError:
        print("This input should not contain characters!")
    else:
    # if there is no error else block is the continuation for try block
            print(f"{num1} + {num2} = {answer}")

while flag:
    addition()

    # validation to break the loop if user want's to quit.
    prompt = "Do you want to quit? press q, press anything to continue: "
    validation = input(prompt)
    if validation == "q" or validation == "Q":
        flag = False
