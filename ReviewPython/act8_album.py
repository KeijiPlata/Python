# Activity 8-7 Album

def make_album(artistName, albumTitle, numberOfSongs=None):
    """ This function will store information to dictionary"""
    # store the value inside the dictionary
    album = {'ArtistName' : artistName, 'AlbumTitle': albumTitle}

    # condtion if the user will input the number of songs
    if numberOfSongs:
        album['NumberOfSongs'] = numberOfSongs

    # return the actual dictionary
    return album
    
# function calls
make_album("Joji", "Nectar")
make_album("Post Malone", "Stoney")
make_album("Ed Sheeran", "x", 12)
