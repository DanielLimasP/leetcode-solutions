def spiralOrder(matrix):
    row = len(matrix)
    col = len(matrix[0])
    seen = [[False] * row for i in range(col)]
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1 ,0]
    r = c = di = 0
    result = []

    for i in range(row * col):
        result.append(matrix[r][c])
        seen[r][c] = True
        cr = r + d_row[di]
        cc = c + d_col[di]
        if (0 <= cr < row) and (0 <= cc < col) and not seen[cr][cc]:
            r = cr
            c = cc
        else:
            di = (di + 1) % 4
            r = r + d_row[di]
            c = c + d_col[di]
    
    return result

if __name__ == "__main__":
    print(spiralOrder([
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]))