# Activity 9-7 Admin
# copy of activity 9-5

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

class Admin(User):
    """ This class inherits the methods and attributes of user """
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)

        # Initializing that this value is a list
        self.privileges = []

    def show_privileges(self):
        """ This shows the power of the admin user """
        print(f"\nBelow are the administrator ({self.first.title()}) can do")
        for privilege in self.privileges:
            print(f"* {privilege}")

# Creating a instance
keiji = User("keiji", "Plata", 20, "Male")

print("No vallue:")
# calling the method inside the class
keiji.describe_user()
keiji.greet_user()

print("Calling the instance 5 times")
# calling the new method we created
keiji.increment_login()
keiji.increment_login()
keiji.increment_login()
keiji.increment_login()
keiji.increment_login()

# printing
keiji.describe_user()

# reset_login_attempts
keiji.reset_login_attempts()

print("Reset the attempts")
# print again
keiji.describe_user()

# creating a list about what admin can do 
admin_power = ["can add post", "can delete a post", "can ban user"]

# Creating an instance for admin
miacky = Admin("Miacky", "Plata", 20, "Male")

# Display the information about the admin_power
miacky.describe_user()

# changing the value of priveleges in the class admin
miacky.privileges = admin_power

# calling the method so we can show the power of the admin_power
miacky.show_privileges()