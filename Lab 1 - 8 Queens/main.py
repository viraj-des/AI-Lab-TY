# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# def printBoard():
#     for row in board:
#         print(row)

# queenPosition_i = int(input("Queens position [i]: "))
# queenPosition_j = int(input("Queens position [j]: "))

# board[queenPosition_i][queenPosition_j] = "Q"

# for j in range(len(board[queenPosition_i])):
#     if board[queenPosition_i][j] == "Q":
#         continue
#     else:
#         board[queenPosition_i][j] = "x"

# for i in range(len(board)):
#     if board[i][queenPosition_j] == "Q":
#         continue
#     else:
#         board[i][queenPosition_j] = "x"

# printBoard()

import numpy as np

def print_board(move_history):
    """Calculates all attack paths and prints the board with 'Q' and 'x'."""
    # Start with a clean board for rendering
    render_board = np.full((8, 8), "0", dtype=str)
    
    # 1. First, calculate and place the 'x' blocks for all active queens
    for q_row, q_col in move_history:
        for i in range(8):
            for j in range(8):
                # Mark rows, columns, and diagonals as under attack
                if i == q_row or j == q_col or abs(i - q_row) == abs(j - q_col):
                    render_board[i, j] = "x"
                    
    # 2. Layer the actual 'Q' marks on top so they aren't hidden by 'x'
    for q_row, q_col in move_history:
        render_board[q_row, q_col] = "Q"

    # 3. Print the rendered grid with labels
    print("\n   0 1 2 3 4 5 6 7")
    print("  ----------------")
    for i, row in enumerate(render_board):
        row_str = " ".join(cell for cell in row)
        print(f"{i} | {row_str}")
    print("-" * 22)

def is_safe(move_history, row, col):
    """Checks if a new position clashes with any existing queens."""
    for q_row, q_col in move_history:
        if row == q_row or col == q_col or abs(row - q_row) == abs(col - q_col):
            return False
    return True

# The Stack: Only tracks the coordinates of valid Queens placed by the user
move_history = []

print("--- Interactive 8-Queens Puzzle Game ---")
print("Place 8 queens safely. Type 'u' at any time to manual backtrack (undo).")

while len(move_history) < 8:
    print_board(move_history)
    print(f"Queens placed: {len(move_history)}/8")

    # Get user input
    user_input = input("Enter row (0-7) or 'u' to undo last move: ").strip().lower()

    # --- HANDLE BACKTRACK (UNDO) ---
    if user_input == "u":
        if len(move_history) == 0:
            print("❌ No moves to undo!")
        else:
            last_row, last_col = move_history.pop()  # Pop strips the last queen out
            print(f"↩️ Backtracked! Removed Queen from [{last_row}, {last_col}]")
        continue

    # --- HANDLE MOVE PLACEMENT ---
    try:
        row = int(user_input)
        col = int(input("Enter column (0-7): "))

        # Validate range boundaries
        if not (0 <= row < 8 and 0 <= col < 8):
            print("❌ Out of bounds! Choose numbers between 0 and 7.")
            continue

        # Check if a queen is already there
        if (row, col) in move_history:
            print("❌ There is already a Queen at this position!")
            continue

        # Check attack paths using the referee function
        if is_safe(move_history, row, col):
            move_history.append((row, col))  # Push move onto our stack history
            print(f"✅ Queen placed at [{row}, {col}]")
        else:
            print("💥 UNSAFE! That position is marked with an 'x' and is under attack!")

    except ValueError:
        print("❌ Invalid input! Enter integers or 'u'.")

# Game Over Screen
print_board(move_history)
print("🎉 Congratulations! You successfully placed all 8 queens safely!")
