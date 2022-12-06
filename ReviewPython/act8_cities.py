# Activity 8-5 Describe_city

def describe_city(city, country = "Philippines"):
    """ This will print the city and the country of your choice. """
    print(f"{city} is in {country}")

# Function call
# default values
describe_city("Manila")
describe_city("Batangas")

# keyword argument
describe_city(city = "Tokyo", country = "Japan")