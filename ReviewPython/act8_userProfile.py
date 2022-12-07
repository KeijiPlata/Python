# Activity 8-13 User profiles

# This accepts arbitrary arguments but this time using empty dictionary
# we can create empty dictionary using ** to parameters name

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# function call
user_profile = build_profile('keiji', 'plata',
                            gender='male',
                            status='single')
# this will output the dictionary
print(user_profile)