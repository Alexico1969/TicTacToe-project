# initialize the game board
def init_board():
  board = [[" " for i in range(3)] for j in range(3)]
  return board

# allow the player to make a move
def make_move(board, player, row, col):
  board[row][col] = player

# check if the game is over
def game_over(board):
  # check if a player has won
  if player_won(board, "X"):
    return True
  if player_won(board, "O"):
    return True

  # check if the game is a draw
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        return False

  return True

# check if a player has won
def player_won(board, player):
  # check rows
  for row in range(3):
    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
      return True

  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True

  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True

  return False

# main game loop
board = init_board()
player = "X"
while not game_over(board):
  # get player's move
  row = int(input("Enter row for player " + player + ": "))
  col = int(input("Enter column for player " + player + ": "))

  # make the move
  make_move(board, player, row, col)