board = []
player = "X"

    
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

def get_available_moves():
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                moves.append((i, j))
    return moves


def minimax(player):
    if check_tie():
        return 0
    elif check_win("X"):
        return -10
    elif check_win("O"):
        return 10

    if player == "O":
        best = -10000
        for move in get_available_moves():
            board[move[0]][move[1]] = "O"
            score = minimax("X")
            board[move[0]][move[1]] = "-"
            best = max(best, score)
        return best

    if player == "X":
        worst = 10000
        for move in get_available_moves():
            board[move[0]][move[1]] = "X"
            score = minimax("O")
            board[move[0]][move[1]] = "-"
            worst = min(worst, score)
        return worst


def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")
    count = 0
    for item in board:
        row = ""
        for space in item:
            row += "\t" + space + "\t"
        print(count,row + "\n")
        count+= 1
        
board.append(["O","X","O"])
board.append(["-","O","X"])
board.append(["X","X","-"])
print("Calling minimax('O') on this board:")
print_board()
print("Minimax should return 10:", minimax("O"))
board.clear()
board.append(["O","X","O"])
board.append(["-","X","X"])
board.append(["X","O","-"])
print("Calling minimax('O') on this board:")
print_board()
print("Minimax should return 0:", minimax("O"))
board.clear()
board.append(["O","X","-"])
board.append(["-","X","X"])
board.append(["X","O","O"])
print("Calling minimax('O') on this board:")
print_board()
print("Minimax should return -10:", minimax("O"))