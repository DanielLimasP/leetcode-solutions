def plus_one(digits):
    if not digits:
        return [1]

    elif digits[-1] == 9:
        digits = plus_one(digits[:-1])
        digits.extend([0])
    else:
        digits[-1] += 1

    return digits

if __name__ == "__main__": 
    print(plus_one([0]))
