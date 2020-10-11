# https://www.tutorialspoint.com/valid-sudoku-in-python
def is_valid_sudoku(grid):
    for i in range(9):
        row = {}
        col = {}
        block = {}
        row_cube = 3 * (i // 3)
        col_cube = 3 * (i % 3)
        for j in range(9):
            if grid[i][j] != "." and grid[i][j] in row:
                return False
            row[grid[i][j]] = 1
            if grid[j][i] != "." and grid[j][i] in col:
                return False
            col[grid[j][i]] = 1
            rc = row_cube + j // 3 
            cc = col_cube + j % 3
            if grid[rc][cc] in block and grid[rc][cc] != ".":
                return False
            block[grid[rc][cc]] = 1
    return True

def sudoku_grid_render(grid):
    for row in grid:
        for col in row:
            print(" | ", end="") 
            print(col, end=" | ")
        print(" ")  
        
if __name__ == "__main__":
    grid = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    sudoku_grid_render(grid)
    print(sudoku_solver(grid))
