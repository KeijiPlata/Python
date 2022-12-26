""" importing a  module inside of module to inherit from other class """
from moduleUser import User

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