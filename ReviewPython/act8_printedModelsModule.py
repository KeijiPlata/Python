""" This functions are for printing models. """
# Activity 8-15 Printing Models (Module)

def printing_models(unprintedModels, printedModels):
    """ This will print the value and remove it from the list,
        After removing, it will be stored in another list. """
    
    while unprintedModels:
        currentModel = unprintedModels.pop()
        print(f"Printing {currentModel} ...")
        printedModels.append(currentModel)

def showModels(printedModels): 
    for printedModel in printedModels:
        print(f"{printedModel} is printed successfully.")
