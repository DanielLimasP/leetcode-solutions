def set_matrix_zeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    zeros_rows = [False] * m
    zeros_cols = [False] * n
    
    # Mark the zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros_rows[i] = True
                zeros_cols[j] = True
                
    for i in range(m):
        for j in range(n):
            if zeros_rows[i] or zeros_cols[j]:
                matrix[i][j] = 0
                    