def climbing_stairs(n):
    a = b = 1
    for _ in range(n):
        # Calculation has to be in one line, otherwise, it doesn't work
        a, b = b, a + b
    return a

if __name__ == "__main__":
    for i in range(49):
        print(climbing_stairs(i))