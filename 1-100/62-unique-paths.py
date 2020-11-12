import math
def unique_paths(m, n):
    return int(math.factorial(m+n-2)/(math.factorial(m-1) * math.factorial(n-1)))

if __name__ == "__main__":
    print(unique_paths(7, 3))