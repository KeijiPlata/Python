# Activity 10-5 Programming Poll

# so we can end the loop
flag = True

while flag:
    # prompt a message
    prompt = "Hello User, Please input your name and I will put in a text file.\
            \nName: "
    prompt2 = "Why do you like programming? \nReason: "
    prompt3 = "Do you want to quit? y or n: "

    # user will input here
    guest = input(prompt)
    reason = input(prompt2)
    exit = input(prompt3)

    # appending user input into the text file
    file_path = 'ReviewPython\\reasons.txt'
    with open(file_path, 'a') as fileObj:
        fileObj.write(f"{guest} - {reason} \n")

    # To know if the user still want to continue the program
    if exit == 'y' or exit == 'Y':
        flag = False

# prompt that the user ends.
print("Thank you for using the program!!")


