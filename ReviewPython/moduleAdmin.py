""" Module for activity 9-11 imported admin"""
# copy of Activity 9-8 Privileges 


# Creating a class called User
class User:
    """ A simple class for describing user"""

    def __init__(self, first_name, last_name, age, gender):
        """ Initialization of attributes """
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """ Printing information about the user """
        print(f"Name: {self.first.title()} {self.last.title()}") 
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Login Attempts: {self.login_attempts}\n")
    
    def increment_login(self):
        """ Increment the value of login_attempts """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Return the value of login_attempts to 0"""
        self.login_attempts = 0

    def greet_user(self):
        """ Greeting the user """
        print(f"Good day! {self.first}!\n")

class Privileges:
    def __init__(self, priveleges=[]):
        self.privileges = priveleges

    def show_privileges(self):
        """ This shows the power of the admin user """
        # adding a condtion so we can know if the list doesn't have values
        if self.privileges:
            print(f"\nBelow are the administrator can do")
            for privilege in self.privileges:
                print(f"* {privilege}")
        else:
            print("You don't have priveleges")

class Admin(User):
    """ This class inherits the methods and attributes of user """
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)

        # Initializing that this value is a list
        self.privileges = Privileges()



# # Creating an instance for admin
# miacky = Admin("Miacky", "Plata", 20, "Male")

# # Display the information about the admin_power
# miacky.describe_user()

# # show the priveleges of the user, which is none because we didn't pass 
# # anything yet
# miacky.privileges.show_privileges() 

# # creating a list about what admin can do 
# admin_power = ["can add post", "can delete a post", "can ban user"]

# # now we added the list
# print("\nWe added the list in this part") 

# # giving a value to the list inside the class Privileges
# miacky.privileges.privileges = admin_power

# # calling out the method from the class priveleges that we moved
# miacky.privileges.show_privileges()

# # I learn to pay attention to your spelling. I spent my f*king time debugging