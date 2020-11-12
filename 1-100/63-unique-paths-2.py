def unique_paths_2(og):
    m = len(og)
    n = len(og[0])

    og[0][0] = 1 - og[0][0]

    # find obstacles in rows
    for i in range(1, m):
        if not og[i][0]:
            og[i][0] = og[i-1][0]
        else:
            og[i][0] = 0

    # find obstacles in columns
    for j in range(1, m):
        if not og[0][j]:
            og[0][j] = og[0][j-1]
        else:
            og[0][j] = 0

    # Loop through the matrix to find no of possible routes
    for i in range(1, m):
        for j in range(1, n):
            if not og[i][j]:
                og[i][j] = og[i][j-1] + og[i-1][j]
            else:
                og[i][j] = 0 

    return og[-1][-1]

if __name__ == "__main__":
    print(unique_paths_2([[0,0,1,0],[0,0,0,0],[1,1,1,0],[0,0,0,0]]))
 
    