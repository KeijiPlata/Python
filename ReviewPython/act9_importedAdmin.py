# Activity 9-11 Imported Admin

import moduleAdmin as ma

# creating a instance for admin
miacky = ma.Admin("Miacky", "Plata", 20, "Male")

# display the information about the admin power
miacky.describe_user()

# show privileges
miacky.privileges.show_privileges() 

# creating a list about what admin can do 
admin_power = ["can add post", "can delete a post", "can ban user"]
print("\nWe added the list in this part") 

# giving a value to the list inside the class Privileges
miacky.privileges.privileges = admin_power

# calling out the method from the class priveleges that we moved
miacky.privileges.show_privileges()