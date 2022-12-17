# Activity 9-6 Ice Cream Stand
# I copied activity 9-4 here

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

# Using inheritance, we create here a new class which is the child
class IceCreamStand(Restaurant):
    """ A class that inherits the class Restaurant"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """ Get all the attributes from the class Restaurant """
        super().__init__(restaurant_name, cuisine_type)
        self.iceCream = flavors
        # You can also just initialize the list easily
        # self.iceCream = [] # we initialize a list here with no value

    def displayFlavors(self):
        """ Display all the flavor of ice cream in a list"""
        print("\nFlavors of Icecream:")
        for flavor in self.iceCream:
            print(f"* {flavor.title()}")

# creating the instance 
restaurant = Restaurant("Jollibee", "Fastfood")
restaurant.describe_restaurant()

# creating a list of ice Cream
flavors_icecream = ["McFlurry", "Sundae", "Ice cream in cone", "Coffee crumble"]
icecreamstand = IceCreamStand("Mcdonalds", "Fastfood", flavors_icecream)

# You can also just change the list we created forcefully so we can add value
# icecreamstand.iceCream = ['vanilla', 'chocolate', 'black berry']

# Calling the method in the class icecreamstand 
icecreamstand.displayFlavors()


