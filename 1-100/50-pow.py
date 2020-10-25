def powxn(x, n):
    # Alternatively you can do return x**n
    res = 1.0
    if n >= 0:
        for i in range(n):
            res *= x
    else:
        for i in range(n, 0):
            res /= x
    return res

if __name__ == "__main__":
    print(powxn(2, -3))