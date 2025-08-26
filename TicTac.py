import math

def print_board(board):
    print("\n   0   1   2")
    for idx, row in enumerate(board):
        print(idx, " | ".join(row))
        if idx < 2:
            print("  " + "-" * 9)
    print()

def check_winner(board):
    # Rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner == "O": return 1
    elif winner == "X": return -1
    elif is_full(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth+1, False, alpha, beta)
                    board[i][j] = " "
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth+1, True, alpha, beta)
                    board[i][j] = " "
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'. Let's start!\n")

    while True:
        print_board(board)

        # Player move
        try:
            row, col = map(int, input("Enter row and column (0-2): ").split())
        except:
            print(" Invalid input! Enter two numbers between 0 and 2.")
            continue

        if row not in [0,1,2] or col not in [0,1,2]:
            print(" Please enter values between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken. Try again!")
            continue

        board[row][col] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print(" Congratulations! You win!")
            break
        if is_full(board):
            print_board(board)
            print(" It's a draw!")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print(" AI wins! Better luck next time.")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Goodbye ")
            break
