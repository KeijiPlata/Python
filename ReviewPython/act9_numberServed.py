# Activity 9-4 Number Served
# Started at activity 9-1

# Creating a class called Restaurant()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """ Initialization of attributes"""
        self.name = restaurant_name
        self.ctype = cuisine_type
        # Adding a attribute aclled number_served with a default value 0
        self.number_served = 0

    def describe_restaurant(self):
        """ print the output for attributes"""
        print(f"Restaurant Name: {self.name.title()}")
        print(f"Cuisine Type: {self.ctype.title()}")
        print(f"Number Served: {self.number_served}\n")

    def open_restaurant(self):
        """ Prints a message that the restaurant is open """
        print(f"{self.name.title()} is now open!")

    def set_number_served(self, userinput):
        """ Let user set the number for how many is served """
        self.number_served = userinput

    def increment_number_served(self, userinput):
        """ This will increment the value of number served"""
        self.number_served += userinput

# creating the instance 
restaurant = Restaurant("Jollibee", "Fastfood")
restaurant.describe_restaurant()

# set the number of served 
restaurant.set_number_served(300)
restaurant.describe_restaurant()

# increment the value of number_served
restaurant.increment_number_served(100)
restaurant.describe_restaurant()


