def valid_number(s):
    s = s.strip()
    dot = exp = dig = False
    for i, c in enumerate(s):
        if c in ['+', '-']:
            if i > 0 and s[i-1] != 'e':
                return False
        elif c == '.':
            if dot or exp:
                return False
            dot = True
        elif c == 'e':
            if exp and not dig:
                return False
            exp = True
            digit = False
        elif c.isdigit():
            digit = True
        else:
            return False
    
    return digit

if __name__ == "__main__":
    print(valid_number("53.5e93"))
