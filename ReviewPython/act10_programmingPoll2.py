# Activity 10-5 Programming Poll
# Altenative way

# so we can end the loop
flag = True
responses = []

while flag:
    # prompt a message
  
    prompt1 = "Why do you like programming? \nReason: "
    prompt2 = "Do you want to quit? y or n: "

    # user will input here
   
    reason = input(prompt1)
    exit = input(prompt2)

    # storing reasons into list
    responses.append(reason)

    # To know if the user still want to continue the program
    if exit == 'y' or exit == 'Y':
        flag = False

# prompt that the user ends.
print("Thank you for using the program!!")

 # appending user input into the text file
file_path = 'ReviewPython\\reasons2.txt'
with open(file_path, 'a') as fileObj:
    for response in responses:
        fileObj.write(f"{response} \n")

