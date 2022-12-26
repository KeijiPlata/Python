from modulePrivilegesAdmin import Admin

# creating instance for admin
miacky = Admin("Miacky", "Plata", 20, "Male")

# incrementin login
miacky.increment_login()
miacky.increment_login()
miacky.increment_login()
miacky.increment_login()

# describe and greet user 
miacky.describe_user()
miacky.greet_user()

# show privileges
miacky.privileges.show_privileges() 

# creating a list about what admin can do 
admin_power = ["can add post", "can delete a post", "can ban user"]
print("\nWe added the list in this part") 

# giving a value to the list inside the class Privileges
miacky.privileges.privileges = admin_power

# calling out the method from the class priveleges that we moved
miacky.privileges.show_privileges()