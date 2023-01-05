# Activity 10-2 Learning C 

# here im going to use the method replace()

# storing the the value of text file into a list
file_path = "ReviewPython\\learning_python.txt"
with open(file_path) as fileObj:
    lines = fileObj.readlines()

# looping through the list and replace the word python with C
# and dogs with cat
# We used rstrip() here so we can eliminate new lines
for line in lines:
    line = line.replace("python", "C")
    line = line.replace("dogs", "cat")
    print(line.rstrip())