# Activity 8-7 Album

def make_album(artistName, albumTitle, numberOfSongs=None):
    """ This function will store information to dictionary"""
    # store the value inside the dictionary
    album = {
        'ArtistName' : artistName, 
        'AlbumTitle': albumTitle
        }
    # condtion if the user will input the number of songs
    if numberOfSongs:
        album['NumberOfSongs'] = numberOfSongs

    # return the actual dictionary but doesn't give an output
    return album
    
# function calls
print(make_album("Joji", "Nectar"))
print(make_album("Post Malone", "Stoney"))
print(make_album("Ed Sheeran", "x", 12))

# you can also store it in a variable and print it
PostMalone = make_album("Post Malone", "Stoney")
print(PostMalone)

