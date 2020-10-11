# This is obviously way to hard to code by myself
# https://medium.com/daily-python/solving-sudoku-puzzle-using-backtracking-in-python-daily-python-29-99a825042e

# Straightforward function to form a new sudoku grid, based off of a puzzle string with
# format "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
def form_grid(puzzle_string):
    global grid
    print("The sudoku problem")
    for i in range(0, len(puzzle_string), 9):
        row = puzzle_string[i:i+9]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)
    printGrid()

# Function to print the grid that we just created
def printGrid():
    global grid
    for row in grid:
        print(row)

# This function uses the logic behind the sudoku checker program to see if the current block is actually
# solvable. 
def has_solution(row, col, digit):
    global grid
    for i in range(0, 9):
        if grid[row][i] == digit:
            return False
    for i in range(0, 9):
        if grid[i][col] == digit:
            return False
    
    # Magic numbers
    square_row = (row//3)*3
    square_col = (col//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[square_row+i][square_col+j] == digit:
                return False

    return True

# The way that solve function works is: 
def solve():
    global grid
    # Got to check every possible position with nested loops
    for row in range(9):
        for col in range(9):
            # If current position is empty
            if grid[row][col] == 0:
                # Check for every possible number that we can place 
                # in said position
                for digit in range(1, 10):
                    # Wheter or not curr block is solvable
                    # if it is, change the current position to be
                    # digit and recursively call solve. If the grid is not
                    # solvable anymore, simply return and change the last value to 0.
                    # If the program makes it until the end, it won't return anything, 
                    # given that this function edits global grid in-place until it has solved
                    # it in it's entirety 
                    if has_solution(row, col, digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0
                return 
    print('\n The solution')
    printGrid()

if __name__ == "__main__":
    puzzle_string = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
    grid = []
    form_grid(puzzle_string)
    solve()