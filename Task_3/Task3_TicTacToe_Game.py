import random

def print_board(board):
    """Function to print the Tic Tac Toe board"""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Function to check if a player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Function to check if the board is full"""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board, player):
    """Function to get a valid move from the player"""
    while True:
        try:
            if player == 'player':
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
            else:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
            if board[row][col] == " ":
                return row, col
            elif player == 'player':
                print("That position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")

def main():
    """Function to run the Tic Tac Toe game"""
    print("Welcome to Tic Tac Toe!")

    player1 = input("Enter name for player 1: ")
    player2 = input("Enter name for player 2 (or 'computer' for single player mode): ")

    players = [player1, player2]

    # If single player mode, randomly select who goes first
    if player2.lower() == 'computer':
        print("You're playing against the computer!")
        first_player = random.choice(players)
        print(f"{first_player} goes first.")
    else:
        first_player = player1

    player_symbols = {player1: 'X', player2: 'O'}
    board = [[" "]*3 for _ in range(3)]
    current_player = first_player

    while True:
        print("\nCurrent board:")
        print_board(board)
        print(f"{current_player}'s turn")

        player_symbol = player_symbols[current_player]

        if current_player == 'computer':
            row, col = get_player_move(board, 'computer')
        else:
            row, col = get_player_move(board, 'player')

        board[row][col] = player_symbol

        if check_winner(board, player_symbol):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = player1 if current_player == player2 else player2

if __name__ == "__main__":
    main()
