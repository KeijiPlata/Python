""" A class that represent a user. This is the parent """
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