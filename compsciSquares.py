#I, Gregory Carroll, student number 000101968,
#certify that all code submitted is my own work; that I have not
#copied it from any other source.  I also certify that I have not
#allowed my work to be copied by others.



import random
from random import randint

#game board 3x3 array
board=[["-","-","-"],["-","-","-"],["-","-","-"]]

#Initial Player/Computer variables
player, computer = "",""

def rps_winner(one,two):
    """
    This function takes the RPSLS(Rock,Paper,Scissors,Lizard,Spock) choice of player1 and player2 as arguments and then compares them.
    Based on the camparison, it returns name of whichever move won the round.
    for example: rps_winner("Rock,"Lizard") returns -> "Rock" with the action message (crushes Lizard)
    """
    if ((one == "Rock" and two == "Scissors") or (one == "Scissors" and two == "Rock")):
        return "Rock","Rock crushes (beats) Scissors"
    elif ((one == "Rock" and two == "Lizard") or (one == "Lizard" and two == "Rock")):
        return "Rock","Rock crushes (beats) Lizard"
    elif ((one == "Rock" and two == "Paper") or (one == "Paper" and two == "Rock")):
        return "Paper","Paper covers (beats) Rock"
    elif ((one == "Spock" and two == "Paper") or (one == "Paper" and two == "Spock")):
        return "Paper","Paper disproves (beats) Spock"
    elif ((one == "Paper" and two == "Lizard") or (one == "Lizard" and two == "Paper")):
        return "Lizard","Lizard eats (beats) Paper"
    elif ((one == "Spock" and two == "Lizard") or (one == "Lizard" and two == "Spock")):
        return "Lizard","Lizard poisons (beats) Spock"
    elif ((one == "Rock" and two == "Spock") or (one == "Spock" and two == "Rock")):
        return "Spock","Spock vaporizes (beats) Rock"
    elif ((one == "Scissors" and two == "Spock") or (one == "Spock" and two == "Scissors")):
        return "Spock","Spock smashes (beats) Scissors"
    elif ((one == "Scissors" and two == "Paper") or (one == "Paper" and two == "Scissors")):
        return "Scissors","Scissors cuts (beats) paper"
    elif ((one == "Scissors" and two == "Lizard") or (one == "Lizard" and two == "Scissors")):
        return "Scissors","Scissors decapitates (beats) Lizard"
    else:
        return "WRONG INPUT"

def turn(P1,P2):
    """
    This function takes player1's name and player2's name as arguments.
    it takes input from player1 for the RPSLS game and generates
    a play for player2(computer) randomly, then passes both the inputs into the
    "rps_winner" function which returns who won the RPSLS game. Based on
    the returned string, it decides whose turn it is for the on going
    tic tac toe game.
    """

    options = ["Rock", "Paper", "Scissors","Lizard","Spock"]
    computer = options[randint(0,4)]
    print (" Winner Chooses The Square! ")
    while True:
        computer = options[randint(0,4)]
        player = input("\nrock, paper, scissors, lizard, spock?\nEnter Choice: ").title()
        print(player)
        if player == computer:
            print("RPSLS Tie!") # if there is a tie, take the input of player1 and player2(computer) again. Input remains the same.

        elif rps_winner(player, computer) == "WRONG INPUT":
            print("That's not a valid play. Please Check your spelling!") # Take input again by player1, player2(computer) input remains the same.

        else:
            win, text = rps_winner(player, computer)
            if player == win:
                print ("\n#####",text, " ==> "+P1+" won the turn!")
                return "player" # Player1 won (Rock, Paper, Scissors, Lizard, Spock) game.
            else:
                print ("\n#####",text, " ==> "+P2+" won the turn!")
                return "computer" # Player2 won (Rock, Paper, Scissors, Lizard, Spock) game.


def print_board():
    """
    This function prints the boards 2d array
    """
    print ('\n    0  1  2')
    print ("-----------")
    print("0 |",board[0][0],'',board[0][1],'',board[0][2],"|") 
    print("1 |",board[1][0],'',board[1][1],'',board[1][2],"|") 
    print("2 |",board[2][0],'',board[2][1],'',board[2][2],"|") 
    print ("-----------\n")

def random_XO():
    """
    This function will randomly decide which player is assigned "X" or "O"
    """
    chars=("X","O")
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def didSomebodyWin(x, y):
    """
    This function takes latest turn's row and column (could be either player1's or player2's) as an argument/input and then checks
    that full row/column/diagonal to see if any player won the game. Returns True based on the
    row and column arguments if somebody won the game, otherwise return False.
    """
    if board[0][y] == board[1][y] == board [2][y]: # (If there's a similar character in whole column 'y' --- vertical check)
        return True

    if board[x][0] == board[x][1] == board [x][2]: # (If there's a similar character in whole row 'x' --- horizontal check)
        return True

    if x == y and board[0][0] == board[1][1] == board [2][2]: # (If there's a similar character in the main diagonal --- diagonal check)
        return True

    if x + y == 2 and board[0][2] == board[1][1] == board [2][0]: # (If there's a similar character in the counter diagonal --- antidiagonal check)
        return True

    return False   

def make_move(player):
    """
    This function takes player1's character (X or O) as an argument.
    It takes column and row number of the input from player1 and plays the move
    if it's possible, otherwise it displays an error and takes input again and again
    until it's allowed. 
    """
    legal = False
    while not legal:
        col, row = -1, -1
        # Loop until the column input by player is correct
        while col not in  [0,1,2]:
            try:
                col = int(input("# Enter Column [0-2] : "))
                if (col not in  [0,1,2]):
                    print ("\nNot Valid! Please enter a number between 0-2\n")
            except:
                print("\nIllegal characters entered! Try again...\n")
                continue
        # Loop until the row input by player is correct
        while row not in  [0,1,2]:
            try:
                row = int(input("# Enter Row [0-2] : "))
                if (row not in [0,1,2]):
                    print ("\nNot Valid! Please enter a number between 0-2\n")
            except:
                print("\nIllegal characters entered! Try again...\n")
                continue

        if board[row][col] == '-':
            board[row][col] = player
            legal = True
        else:
            print ("\nIllegal move!!! Please try again\n")
    return (row,col)
# AI goes here
def computer_move(computer):
    """
    This function takes player2's/computer's character (X or O) as argument.
    It randomly generates a move which is then played by the computer/player2.
    """
    legal = False
    while not legal:
        col = randint(0,2)
        row = randint(0,2)

        if board[row][col] == '-':
            board[row][col] = computer
            legal = True

    return (row,col)

def is_full(board):
    """
    This function checks if the board is full and there are no spaces left.
    returns tie game if board is full and there is no winner. 
    """
    res = [pos if pos == "X" or pos =="O" else None for row in board for pos in row]
    board_res = list(filter(lambda x: x != None, res))
    return len(board_res) == len([x for row in board for x in row])
    print("Tie Game")



#-------------------------------------------------------------------------------------------

def Game():
    """
    This is the main function. It returns True if player1 wins the game, otherwise,
    it returns False if it's either a tie or defeat.It takes name input for player1 and player2.
    It randomly assigns X/O to both the players using a 'random_XO' function.
    It plays a loop until the board is full or player1/player2 wins the game.
    """
    P1 = input("Player 1 please enter (your) name: ")
    P2 = input("Player 2 please enter (computer) name: ")

    player, computer = random_XO() # Randomly assign "X" and "O"
    print('\n\nPlayer is ['+ player +'] and computer is ['+ computer +']\n')

    # player who is X has the first turn
    if player == "X":
        check = "player"
        c1 = P1
    else:
        check = "computer"
        c1 = P2

    print_board()
    print (" first turn belongs to 'X', it's "+c1+"'s turn!")
    while not is_full(board):
        if check == "player": # Player 1's turn
            row, col = make_move(player)
            print ("\n"+P1+" played!")
            if didSomebodyWin(row, col): # Player1 wins if it is True that he played the last position
                print_board()
                print('!!! Congrats! You won!!!')
                return True # Player1 won!
        else:                # Player 2's turn
            print ("\n"+P2+" played!")
            row, col = computer_move(computer)
            if didSomebodyWin(row, col): # Player2 wins if True as the latest move was played by him
                print_board()
                print('*** You Lost !!! ***')
                return False # Player2 won!
        print_board() # Print the board after player1's/player2's  move
        check = turn(P1,P2) # whose turn is next

    return False # nobody won and the board is full, it's a tie game

# play again displayed after a win, lose or tie
playing = True
while playing:
    result = Game()
    print(result)
    
    play_again = input("would you like to play again? (y/n):").lower()
    board=[["-","-","-"],["-","-","-"],["-","-","-"]]
    playing = "y" == play_again
    
