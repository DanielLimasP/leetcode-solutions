# Leetcode problem #51: N-Queens problem
# https://leetcode.com/problems/n-queens/discuss/873235/Python-easiest-to-understand-dfs-solution
def n_queens(n):
    board = [['.' for i in range(n)] for j in range(n)]
    queens_in_col = [0]*n # To keep track of the number of queens in each queens_in_col
    queens_in_left_d = [0]*(2*n-1) # This represents the number of queens in the left diagonal
    queens_in_right_d = [0]*(2*n-1) # ibid
    result = []
    backtrack(n, 0, board, result, queens_in_col, queens_in_left_d, queens_in_right_d)
    return result

def backtrack(n, row, board, result, col_queens, left_queens, right_queens):
    if row == n:
        res = []
        for i in range(n):
            res.append(''.join(board[i]))
        result.append(res)
        return 
    for col in range(n):
        if not col_queens[col] and not left_queens[row-col] and not right_queens[row+col]:
            board[row][col] = 'Q'
            col_queens[col] = 1
            left_queens[row-col] = 1
            right_queens[row+col] = 1
            backtrack(n, row+1, board, result, col_queens, left_queens, right_queens)
            board[row][col] = '.'
            col_queens[col] = 0
            left_queens[row-col] = 0
            right_queens[row+col] = 0

if __name__ == "__main__":
    for solution in solveNQueens(8):
        for row in solution:
            print(row)
        print()

    