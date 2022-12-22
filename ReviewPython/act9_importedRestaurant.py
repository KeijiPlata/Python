""" Activity 9-10 Imported Restaurant """
# I created  new module for icecreamstand and import the class and change name
from moduleIceCreamStand import Restaurant as rt

jollibee = rt("Jollibee", "Filipino Fastfood")
jollibee.increment_number_served(100)
jollibee.increment_number_served(200)
jollibee.describe_restaurant()
jollibee.open_restaurant()
