# Activity 11-1 City, Country (functions) and Activity 11-2 Populations

def cityCountry(cityName, countryName, population=0):
    """ combines two variables: city name and country also checks
            if user input a value to population"""
    # if the populaiton is equal to 0 it will return false
    # if the population is non zero, it will print the population

    if population:
        combineName = f"{cityName.title()}, {countryName.title()} - Population {population}"
    else:
        combineName = f"{cityName.title()}, {countryName.title()}"
    
    return combineName