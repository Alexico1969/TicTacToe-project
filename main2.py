#use the random class to generate random numbers
import random

#Copy your code from the 'Complete the Game' exercise in the previous lesson.

#Global Variables
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
player = "X"

#Copy your functions from the previous activities here:
#print_board, is_valid_move, place_player, take_turn
def print_board():
    print("   0     1     2")
    print()
    counter = 0
    for row in board:
        print(str(counter) + " ", end="")
        counter += 1
        for cel in row:
            print(" " + cel + "    ", end="")
        print()
        print()

#returns true if a row,col on the board is open
def is_valid_move(row, col):
    output = False
    if row in [0,1,2] and col in [0,1,2]:
        output = True
    if board[row][col]  != "-":
        print("Error: Cel is occupied!")
        output = False
    return output
        
#places player on row,col on the board
def place_player(player, row, col):
    board[row][col] = player
    
#Asks the user to enter a row and col until the user enters a valid location
#Adds user location to the board, and prints the board
def take_turn(player):
    if player == 'X':
        valid = False
        while not valid:
            row = int(input("Enter a row "))
            col = int(input("Enter a col "))
            valid = is_valid_move(row, col)
    else:
        valid = False
        while not valid:
            row = random.randint(0,2)
            col = random.randint(0,2)
            valid = is_valid_move(row, col)

    place_player(player, row, col)
    print_board()

#Write your check win functions here:
    
def check_col_win(player):
    output = False
    if board[0][0] == board[1][0] == board[2][0] == player:
        output = True
    if board[0][1] == board[1][1] == board[2][1] == player:
        output = True
    if board[0][2] == board[1][2] == board[2][2] == player:
        output = True
    return output

def check_row_win(player):
    output = False
    if board[0][0] == board[0][1] == board[0][2] == player:
        output = True
    if board[1][0] == board[1][1] == board[1][2] == player:
        output = True
    if board[2][0] == board[2][1] == board[2][2] == player:
        output = True
    return output

def check_diag_win(player):
    output = False
    if board[0][0] == board[1][1] == board[2][2] == player:
        output = True
    if board[0][2] == board[1][1] == board[2][0] == player:
        output = True
    return output

def check_win(player):
    return check_col_win(player) or check_row_win(player) or check_diag_win(player)

def check_tie():
    full = True
    for row in board:
        for cel in row:
            if cel == "-":
                full = False
    if not check_win("X") and not check_win("O") and full:
        return True
    else: 
        return False
    



#Start of program
print("\t\tWelcome to Tic Tac Toe!")
print_board()


def flip_player():
    global player, stop
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    else:
        print("Error: Player is not X or O")
        stop = True

stop = False
while not stop:
    print()
    print(f"Player {player} is up...")
    print()
    take_turn(player)
    print(22 * "=")
    print()
    if check_win(player):
        print(f"Player {player} wins !")
        break
    elif check_tie():
        print(f"It's a tie !")
        break
    flip_player()