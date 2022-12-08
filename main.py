import random

def init_vars():
    global possible_choices, players, current_player, row1, row2, row3, board
    possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    players = ["Player 1", "Player 2"]
    current_player = random.choice(players) 
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    board = [row1, row2, row3]
    print("Player 1 is X")
    print("Player 2 is O")

def print_intro_text():
    global current_player
    print()
    print("***********************")
    print("Welcome to Tic Tac Toe!")
    print("***********************")
    print()
    print("This is a 2 player game.")
    print("Player 1 is X")
    print("Player 2 is O")
    print("To make a move, enter the row and column, e.g. A1")
    print()
    print("Player {} goes first".format(current_player))


def draw_board():
    global possible_choices, players, current_player, row1, row2, row3, board
    print()
    print("    A   B   C")
    print("  +---+---+---+")
    print("1 | {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
    print("  +---+---+---+")
    print("2 | {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print("  +---+---+---+")
    print("3 | {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print("  +---+---+---+")
    print()

def player_choice():
    global possible_choices, players, current_player, row1, row2, row3, board
    print()
    print("Player to make a move: {}".format(current_player))
    print()
    valid_choice = False
    while not valid_choice:
        choice = input("Enter your choice: ").upper()
        if choice in possible_choices:
            valid_choice = True
        else:
            print("Invalid choice. Please try again.")
    return choice

def process_choice(choice):
    global possible_choices, players, current_player, row1, row2, row3, board
    if current_player == players[0]:
        player = "X"
    else:
        player = "O"
    if choice == "A1":
        board[0][0] = player
    elif choice == "A2":
        board[1][0] = player
    elif choice == "A3":
        board[2][0] = player
    elif choice == "B1":
        board[0][1] = player
    elif choice == "B2":
        board[1][1] = player
    elif choice == "B3":
        board[2][1] = player
    elif choice == "C1":
        board[0][2] = player
    elif choice == "C2":
        board[1][2] = player
    elif choice == "C3":
        board[2][2] = player

    possible_choices.remove(choice)
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]

def check_win():
    global possible_choices, players, current_player, row1, row2, row3, board
    if board[0][0] == board[0][1] == board[0][2] != " ": # top row
        print("Player {} wins!".format(current_player))
        return True
    elif board[1][0] == board[1][1] == board[1][2] != " ": # middle row
        print("Player {} wins!".format(current_player))
        return True
    elif board[2][0] == board[2][1] == board[2][2] != " ": # bottom row
        print("Player {} wins!".format(current_player))
        return True
    elif board[0][0] == board[1][0] == board[2][0] != " ": # left column
        print("Player {} wins!".format(current_player))
        return True
    elif board[0][1] == board[1][1] == board[2][1] != " ": # middle column
        print("Player {} wins!".format(current_player))
        return True
    elif board[0][2] == board[1][2] == board[2][2] != " ": # right column
        print("Player {} wins!".format(current_player))
        return True
    elif board[0][0] == board[1][1] == board[2][2] != " ": # diagonal
        print("Player {} wins!".format(current_player))
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ": # diagonal
        print("Player {} wins!".format(current_player))
        return True
    elif len(possible_choices) == 0:
        print("It's a draw!")
        return True
    else:
        return False



init_vars()
print_intro_text()
draw_board()

while True:
    choice = player_choice()
    process_choice(choice)
    draw_board()
    if check_win():
        break