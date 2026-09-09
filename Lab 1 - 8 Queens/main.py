import numpy as np

board = np.full((8, 8), "0", dtype=str)
queens = []

def print_board():
    board[:] = "0"

    for row, col in queens:
        for i in range(8):
            for j in range(8):
                if i == row or j == col or abs(i - row) == abs(j - col):
                    board[i][j] = "x"

    for row, col in queens:
        board[row][col] = "Q"

    print("\n   0 1 2 3 4 5 6 7")
    print("  ----------------")
    for i in range(8):
        print(i, "|", " ".join(board[i]))
    print()

def is_safe(row, col):
    for q_row, q_col in queens:
        if row == q_row or col == q_col or abs(row - q_row) == abs(col - q_col):
            return False
    return True

print("8 Queens Problem")
print("Place 8 queens safely.")
print("Enter 'u' to undo the last queen.")

while len(queens) < 8:
    print_board()
    print("Queens placed:", len(queens), "/ 8")

    choice = input("Enter row (0-7) or 'u': ").strip().lower()

    if choice == "u":
        if queens:
            removed = queens.pop()
            print("Removed queen:", removed)
        else:
            print("No queen to remove.")
        continue

    try:
        row = int(choice)
        col = int(input("Enter column (0-7): "))

        if row < 0 or row > 7 or col < 0 or col > 7:
            print("Enter values between 0 and 7.")
            continue

        if (row, col) in queens:
            print("A queen is already there.")
            continue

        if is_safe(row, col):
            queens.append((row, col))
            print("Queen placed.")
        else:
            print("Unsafe position.")

    except ValueError:
        print("Enter numbers or 'u'.")

print_board()
print("Congratulations! All 8 queens are placed safely.")
