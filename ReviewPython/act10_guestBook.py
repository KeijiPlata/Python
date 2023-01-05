# Activity 10-4 Guest Book

# so we can end the loop
flag = True

while flag:
    # prompt a message
    prompt = "Hello Guest, Please input your name and I will put in a text file.\
            \nName: "

    # user will input here
    guest = input(prompt)
    exit = input("Do you want to quit? y or n: ")

    # appending user input into the text file
    file_path = 'ReviewPython\\guest_book.txt'
    with open(file_path, 'a') as fileObj:
        fileObj.write(f"{guest} \n")

    # To know if the user stillw ant to continue the program
    if exit == 'n' or exit == 'N':
        flag = False

# prompt that the user ends.
print("Thank you for using the program!!")