# Activity 8-3 T shirt

# The value inside the parameter called default values
def make_shirt(size = "Large", message = "I love python"):
    """ This will print the summary of your shirt. """
    print(f"Size: {size}")
    print(f"Message: {message}")

# Positional arguments
make_shirt("Medium", "To the moon")

# Keyword argument
make_shirt(message = "San Ka punta?", size = "Small")

# Trigerring the defaul value for message
make_shirt("Small")

# Trigerring the default value for Size
make_shirt(message="I also love you!")