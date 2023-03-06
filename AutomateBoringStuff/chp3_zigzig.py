# import packages needed
import time, sys

def main_loop():
    # enter enter how many indent they want
    indentEnd = int(input("Input number of indent: "))
    indent = 0
    isIndentIncreasing = True
    try:
        while True:
            # print spaces and *
            print(" " * indent, end="")
            print("********")

            # delay 1/10 of a second
            time.sleep(0.1)

            # if true, space will increase by 1
            if isIndentIncreasing:
                indent += 1
                # if indent is equal to user number of indent, return false
                if indent == indentEnd:
                    isIndentIncreasing = False
            # if false, space will decrease by 1
            else:
                indent -= 1
                # if indent is equal to 0, return true
                if indent == 0:
                    isIndentIncreasing = True

    # if user hit ctrl + c, terminate and pring thank you message
    except KeyboardInterrupt:
        print("Thank you for using the program")
        sys.exit()

# run the program
if __name__ == "__main__":
    main_loop()
