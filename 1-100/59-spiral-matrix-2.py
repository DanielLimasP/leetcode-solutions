# Intuition behid the solution is have 0s matrix n*n
# and walk through it, 1 - n^n. Write the number to 
# current pos and make turns on edges

def spiral_matrix_2(n):
    zeros = [[0] * n for i in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        for row in zeros:
            print(row)
        zeros[i][j] = k + 1
        # This line right here basically checks for
        # the next position in the spiral
        # If we hit a corner, this piece of code 
        # will properly update the direction
        # of the spiral
        if zeros[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return zeros
    

if __name__ == "__main__":
    print(spiral_matrix_2(3))