# Tic Tac Toe

# Global variables
board = [' '] * 9
current_player = 'X'

# Function to display the Tic Tac Toe board
def display_board():
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

# Function to get the position from the player
def player_input(player):
    while True:
        position = input("Player " + player + ", enter your move (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9:
            position = int(position) - 1
            if board[position] == ' ':
                return position
            else:
                print("That position is already filled. Try again.")
        else:
            print("Invalid input. Try again.")

# Function to check whether there is a winner or not
def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True

    return False

# The main function to play the game
def play():
    global current_player  # Add this line to access the global variable

    print("Welcome to Tic Tac Toe!")

    while True:
        display_board()
        position = player_input(current_player)
        board[position] = current_player

        if check_win():
            display_board()
            print("Player " + current_player + " wins!")
            break

        if ' ' not in board:
            display_board()
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play()
