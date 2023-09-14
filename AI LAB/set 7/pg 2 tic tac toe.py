# Define the Tic-Tac-Toe game board as a 2D list
board = [
    ['0', 'X', '0'],
    ['X', ' ', ' X'],
    [' ', '0 ', '']
]

# Define utility values
utility_values = {
    'X': 1,  # Utility value for X (winning)
    'O': -1,  # Utility value for O (winning)
    ' ': 0,  # Utility value for a tie (draw)
}

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to evaluate the board state
def evaluate_board():
    for player in ['X', 'O']:
        if check_win(player):
            return utility_values[player]  # Player has won

    return utility_values[' ']  # Game is a tie

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win('X'):
        return 1
    elif check_win('O'):
        return -1
    elif depth == 0:
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Find the best move for O
best_move = None
best_eval = -float('inf')
for i in range(3):
    for j in range(3):
        if board[i][j] == ' ':
            board[i][j] = 'O'
            eval = minimax(board, 9, True)
            board[i][j] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = (i, j)

# Print the board and the best move for O
print("Tic-Tac-Toe Board:")
for row in board:
    print(' '.join(row))
print("\nBest Move for O:", best_move)
