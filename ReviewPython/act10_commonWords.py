# Activity 10-10 Common words

def readSomeLines(filepath, word):
    """ Read the lines, count the word you want and then print """
    with open(filepath, encoding='utf-8') as f:
        lines = f.read()
    wordcount = lines.lower().count(word)
    print(f"The word '{word.lower()}' appears {wordcount} in text file.")

# user input and filepath
word = input("Please input the word you want to count: ")
filepath = 'ReviewPython\\ThetrainingofteachersintheUnitedStatesofAmerica.txt'
readSomeLines(filepath, word)

