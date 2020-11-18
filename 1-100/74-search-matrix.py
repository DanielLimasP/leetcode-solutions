def search_in_matrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False

def binary_search(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    lo = 0
    hi = rows * cols - 1

    while lo <= hi:
        mid = (lo + hi)/2
        n = matrix[mid / cols][mid % cols]
        if n == target:
            return True
        elif n < target:
            hi = mid + 1
        else:
            lo = mid - 1
    
    return False

if __name__ == "__main__":
    print([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13)