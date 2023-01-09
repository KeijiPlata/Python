# Activity 10-8 Cats and Dogs

def readFile(filepath):
    """ Read the file and print the names """
    try:
     with open(filepath) as f:
        names = f.read()

    except FileNotFoundError:
        print(f"The filepath {filepath} doesn't exist")

    else:
        print(names)

# filepaths store in list. snake.txt doesn't exist so we can check if 
# except block is working
filepaths = ['ReviewPython\\cats.txt', 'ReviewPython\\dogs.txt', 'ReviewPython\\snake.txt']
for filepath in filepaths:
    readFile(filepath)