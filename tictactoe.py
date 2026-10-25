import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
            
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
        
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    if winner == "X":  # Human wins
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                score = minimax(board, 0, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    move = (r, c)
    board[move[0]][move[1]] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("--- Tic-Tac-Toe AI Game ---")
    print("You are 'X' and AI is 'O'.")
    print("Enter row and column numbers from 0 to 2 (e.g., 0 1).\n")
    
    while True:
        print_board(board)
        
        # Human turn
        try:
            r, c = map(int, input("Your turn (row and col: 0, 1 or 2): ").split())
            if board[r][c] != " ":
                print("Spot already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2 separated by a space.")
            continue
            
        board[r][c] = "X"
        
        if check_winner(board) == "X":
            print_board(board)
            print("Congratulations! You won!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
            
        # AI turn
        print("AI is thinking...")
        ai_move(board)
        
        if check_winner(board) == "O":
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()