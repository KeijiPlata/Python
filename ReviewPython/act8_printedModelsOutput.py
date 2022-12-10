# Activity 8-15 Printing models (Output)

# importing the mdoule as pm <-- pm is the new nickname
import act8_printedModelsModule as pm 

# trying function from another module with alias
from act8_printedModelsModule import printing_models as pms

# creating the lists needed
unprintedDesigns = ['robot', 'pokemon', 'toy']
completeDesigns = []

# This is a function call
pms(unprintedDesigns, completeDesigns)
pm.showModels(completeDesigns)
