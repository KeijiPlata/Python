# Activity 9-3 Users

# Creating a class called User

class User:
    """ A simple class for describing user"""

    def __init__(self, first_name, last_name, age, gender):
        """ Initialization of attributes """
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """ Printing information about the user """
        print(f"Name: {self.first.title()} {self.last.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}\n")

    def greet_user(self):
        """ Greeting the user """
        print(f"Good day! {self.first}!\n")

# Creating a instance
keiji = User("keiji", "Plata", 20, "Male")
Andrew = User("andrew", "De Guzman", 21, "Male")
Kisses = User("kisses", "ureta", 22, "Female")

# calling the method inside the class
keiji.describe_user()
keiji.greet_user()
Andrew.describe_user()
Andrew.greet_user()
Kisses.describe_user()
Kisses.greet_user()