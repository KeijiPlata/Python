# Activity Lottery Analysis
# I will be creating the Lottery in different approach

# importing standard library for picking a random value in list
from random import choice

# creating the list of numbers and letters to be picked
randomNumLetters = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]

# my ticket
myTicket = ["a", 4, 9, "b"]

# flag 
won = False

# this is noting how many plays we already played to win
plays = 0

def getWinningTicket(randomNumLetters):
    """ Generate a winning ticket """
    # creating the list where we store the 4 picked numbers
    winningTicket = []

    # This while loop will check if the length of the list is less than 4
    while len(winningTicket) < 4:
        currentPicked = choice(randomNumLetters)

    # checks if the current pick is not in winning ticket
        if currentPicked not in winningTicket:
            winningTicket.append(currentPicked)

    return winningTicket

def checkTicket(myticket, winningticket):
    """ Checks if the ticket is winning or not """
    for element in myticket:
        if element not in winningticket:
            return False

    return True

while not won:
    ticket = getWinningTicket(randomNumLetters)
    won = checkTicket(myTicket, ticket)
    plays += 1 # add 1 to number of plays
    print(f"Current Ticket: {ticket}")

if won:
    print("YOU WIN!!")
    print(f"Your Ticket: {myTicket}")
    print(f"Winning ticket: {ticket}")
    print(f"Number of plays: {plays}")
        
    