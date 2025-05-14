#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Tic-Tac-Toe Game (2 Players, Terminal Based)

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(cell != ' ' for cell in board)

def play_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X | Player 2: O")
    print("Choose positions 1-9 to make a move.")
    
    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position! Try again.")
                continue
            if board[move] != ' ':
                print("Position already taken! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    again = input("Do you want to play again? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
play_game()
 


# In[ ]:




