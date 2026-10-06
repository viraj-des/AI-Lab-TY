grid = [[0 for _ in range(6)] for _ in range(6)]


def print_grid():
    for row in grid:
        print(" ".join(str(x) if x != 0 else "." for x in row))


def valid_move(row, col, num):
    row -= 1
    col -= 1

    if num < 1 or num > 6:
        return False

    for i in range(6):
        if grid[row][i] == num:
            return False

    for i in range(6):
        if grid[i][col] == num:
            return False

    start_row = (row // 2) * 2
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve():
    for row in range(6):
        for col in range(6):

            if grid[row][col] == 0:

                for num in range(1, 7):

                    if valid_move(row + 1, col + 1, num):
                        grid[row][col] = num

                        if solve():
                            return True

                        grid[row][col] = 0

                return False

    return True


# Enter Sudoku values
n = int(input("Enter number of values in the Sudoku: "))

for i in range(n):
    print("\nEnter value", i + 1)

    row = int(input("Enter row (1-6): "))
    col = int(input("Enter column (1-6): "))
    num = int(input("Enter value (1-6): "))

    if row < 1 or row > 6 or col < 1 or col > 6 or num < 1 or num > 6:
        print("Invalid input. Try again.")
        i -= 1
        continue

    if grid[row - 1][col - 1] != 0:
        print("This cell is already filled. Try again.")
        i -= 1
        continue

    if valid_move(row, col, num):
        grid[row - 1][col - 1] = num
    else:
        print("Invalid Sudoku move. Try again.")
        i -= 1


# Show initial Sudoku
print("\nInitial Sudoku:")
print_grid()


# Solve Sudoku
if solve():
    print("\nFinal Sudoku:")
    print_grid()
else:
    print("\nNo solution exists for this Sudoku.")
