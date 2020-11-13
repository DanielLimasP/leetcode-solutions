def add_binary(a, b):
    carry = 0
    result = ""
    
    a = list(a)
    b = list(b)
    
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b: 
            carry += int(b.pop())
        result += str(carry % 2)
        carry //= 2
    return result[::-1]

if __name__ == "__main__":
    print(add_binary("1010", "1011"))