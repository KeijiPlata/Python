# Activity 9-1 Restaurant

# Creating a class called Restaurant()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """ Initialization of attributes"""
        self.name = restaurant_name
        self.ctype = cuisine_type
    
    def describe_restaurant(self):
        """ print the output for attributes"""
        print(f"Restaurant Name: {self.name.title()}")
        print(f"Cuisine Type: {self.ctype.title()}")

    def open_restaurant(self):
        """ Prints a message that the restaurant is open """
        print(f"{self.name.title()} is now open!")

# creating the instance 
restaurant = Restaurant("Jollibee", "Fastfood")

# printing the two attributes 
print(restaurant.name.title())
print(restaurant.ctype.title())

# calling the method inside the class
restaurant.describe_restaurant()
restaurant.open_restaurant()