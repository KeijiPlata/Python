# Activity 8-14 Cars

# first solution
def informationCar(manufacturer, modelName, **CarInfo):
    """ This will accept manufacturer, modelname and additional info """
    # this will put key value pair into dictionary
    CarInfo['Manufacturer'] = manufacturer
    CarInfo['ModelName'] = modelName
    return CarInfo

# second solution
def informationCar2(manufacturer, modelName, **CarInfo):
    """ This is the same as the first function but in different way """
    # this will build dictionary inside the funciton
    carDetails = {
        'Manufacturer': manufacturer.title(),
        'Model': modelName.title()
    }

    # This for loop will get no matter how many arbitrary key value arguments we pass
    for option, value in option.items:
        carDetails[option] = value

    return carDetails

# funciton calls
car = informationCar('subaru', 
                    'outback', 
                    color = 'blue', 
                    tow_package = True )

car2 = informationCar('honda', 
                    'outback', 
                    color = 'black', 
                    tow_package = False )

# printing the dictionary
print(car)
print(car2)
