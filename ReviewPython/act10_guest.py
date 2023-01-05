# Activity 10-3 Guest

# prompt a message
prompt = "Hello Guest, Please input your name and I will put in a text file.\
        \nName: "

# user will input here
guest = input(prompt)

# creating a new file if the file is not existing
# and overwrite if it exist
with open("ReviewPython\\guest.txt", 'w') as fileObj:
    fileObj.write("Welcome this is a guest list where you are the only guest!\n")
    fileObj.write(guest)

# prompt user that the name is inserte to the text file
print(f"Your name '{guest.title()}' is successfully inserted!")
