# We are lacking some terms in our dict...
def roman2int(s):
    symbols_dict = {
        "M":    1000,
        "CM":   900, 
        "D":    500,
        "CD":   400,
        "C":    100,
        "XC":   90,
        "L":    50,
        "XL":   40,
        "X":    10, 
        "IX":   9,
        "V":    5,
        "IV":   4,
        "I":    1
    }

    i = 0
    number = 0

    while i < len(s):
        if i+2 <= len(s) and s[i:i+2] in symbols_dict:
            number += symbols_dict[s[i:i+2]]
            i += 2
        else:
            number += symbols_dict[s[i]]
            i += 1
    return number

print(roman2int("III"))
print(roman2int("CDXLIII"))