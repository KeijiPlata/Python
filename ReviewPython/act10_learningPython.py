# Activity 10-1 Learning python

# getting access to the file we want to manipulate
file_path = 'ReviewPython\\learning_python.txt'
with open(file_path) as fileObject:
    lines = fileObject.read()
print(lines)

# here we read the text file line by line and print it
# we will use here rstrip() so we can eliminate new line 
with open(file_path) as fileObject:
    for a in fileObject:
        print(a.rstrip())
        
# new line
print()

# storing the text in list and print it
# it is importan to user readlines() here so we can store it in list
# rstrip() eliminates the new line
with open(file_path) as fileObject:
    linesList = fileObject.readlines()

for line in linesList:
    print(line.rstrip())
