# import packages needed
# random is for random numbers
# sys is for the exit of the program
import random, sys

def run_game():
    """Main loop for the game"""
    # initialize the scores
    win = 0
    lose = 0
    ties = 0

    while True:
        print(f"{win} Wins, {lose} Losses, {ties} Ties")
        # userinput
        user = userInput()
        # generate random number
        computer = computerInput()
        # print the versus
        displayVersus(user, computer)
        # checks who is the winner
        result = resultbattle(user, computer)

        # scoring
        if result == "WIN":
            win += 1
        elif result == "LOSE":
            lose += 1
        elif result == "TIE":
            ties += 1
   
def userInput():
    """User will input here, it will not terminate unless condition met"""
    while True:
        print("Enter your move: (r)rock (p)paper (s)scisors or (q)quit")
        playerMove = input()
        if playerMove == 'q':
            print("Thank you for playing the game!")
            sys.exit()
        elif playerMove == 'r' or playerMove == 's' or playerMove == 's':
            return playerMove
        else:
            print("Incorrect Input, Try again")

def computerInput():
    """Generate random number and assign it to rock paper scissor"""
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
    elif randomNumber == 2:
        computerMove = 'p'
    elif randomNumber == 3:
        computerMove = 's'
    
    return computerMove

def conversion(move):
    """Convert characters into string"""
    if move == 'r':
        newMove = "ROCK"
    elif move == 'p':
        newMove = 'PAPER'
    elif move == 's':
        newMove = 'SCISSOR'
    return newMove

def displayVersus(playerMove, computerMove):
    """Display what user and computer choose"""
    player = conversion(playerMove)
    computer = conversion(computerMove)
    print(f"{player} VERSUS {computer}")

def resultbattle(playerMove, computerMove):
    """Check if the user is lose, win or tie"""
    if playerMove == computerMove:
        return "TIE"
    elif (playerMove == 'r' and computerMove == 's') or ( playerMove == 'p' 
        and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        return "WIN"
    elif (playerMove == 'r' and computerMove == 'p') or (playerMove == 'p' 
        and computerMove == 's') or (playerMove == 's' and computerMove == 'r'):
        return "LOSE"
    
# run the game   
run_game()
            