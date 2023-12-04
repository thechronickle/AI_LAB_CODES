import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def is_valid_move(board, move):
    row, col = move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "


def make_move(board, move, player):
    row, col = move
    if is_valid_move(board, move):
        board[row][col] = player
        return True
    return False


def get_player_move():
    try:
        move = input("Enter row and column (e.g., '1 2'): ")
        row, col = map(int, move.split())
        return row, col
    except (ValueError, IndexError):
        print("Invalid input. Please enter two space-separated numbers.")
        return get_player_move()


def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells) if empty_cells else None


def play_tic_tac_toe():
    board = initialize_board()
    players = ["X", "O"]
    current_player = players[0]

    while True:
        print_board(board)

        if current_player == "X":
            row, col = get_player_move()
        else:
            print("Computer's move:")
            row, col = get_computer_move(board)

        if make_move(board, (row, col), current_player):
            if is_winner(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = players[1] if current_player == players[0] else players[0]
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    play_tic_tac_toe()
