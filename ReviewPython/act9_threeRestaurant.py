# Activity 9-2 Three Restaurants

# Creating a class called Restaurant()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """ Initialization of attributes"""
        self.name = restaurant_name
        self.ctype = cuisine_type
    
    def describe_restaurant(self):
        """ print the output for attributes"""
        print(f"Restaurant Name: {self.name.title()}")
        print(f"Cuisine Type: {self.ctype.title()}\n")

    def open_restaurant(self):
        """ Prints a message that the restaurant is open """
        print(f"{self.name.title()} is now open!")

# creating three instances 
restaurant = Restaurant("Jollibee", "Fastfood")
restaurant2 = Restaurant("Mcdo", "FastFood")
restaurant3 = Restaurant("Tokyo Tokyo", "Japanes Cuisine")

# calling the method inside the class
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
