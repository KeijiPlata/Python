# Activity 8-8 User Album

# declaration of variables
flag = True

def make_album(artistName, albumTitle):
    """ This function will store information to dictionary"""
    # store the value inside the dictionary
    album = {
        'ArtistName' : artistName, 
        'AlbumTitle': albumTitle
        }
    # return the actual dictionary but doesn't give an output
    return album

# this will loop until the user doesn't enter q  
while flag:
    # user input
    print("Please enter the following:\n")
    ArtistName = input("Artist Name: ")
    AlbumTitle = input("Album Title: ")

    # put the value to the dictionary
    Album = make_album(ArtistName, AlbumTitle)

    # output
    print(Album)

    # checks if the user wants to quit
    quit = input("Do you want to quit? press q and press anything if not: ")
    if quit == "q":
        flag = False
        print("\nThank you for responding!")
