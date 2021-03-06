def betterSolution(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    sym = [
        "M", "CM", "D", "CD",
        "C", "XC", "L" , "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman = ""
    i = 0

    while n > 0: 
        for digit in range(n // val[i]):
            roman += sym[i]
            n -= val[i]
        i += 1

    return roman



def int2roman(n):
    numString = str(n)
    cont = 0
    rom = ""
    for c in numString[::-1]:
        #print(c)
        # The most stupid way I could ever think of...
        # Continue doing this until you finish
        if c == "0" and cont == 0:
            rom += ""
        if c == "1" and cont == 0:
            rom += "I"
        if c == "2" and cont == 0:
            rom += "II"
        if c == "3" and cont == 0:
            rom += "III"
        if c == "4" and cont == 0:
            rom += "VI"
        if c == "5" and cont == 0:
            rom += "V"
        if c == "6" and cont == 0:
            rom += "IV"
        if c == "7" and cont == 0:
            rom += "IIV"
        if c == "8" and cont == 0:
            rom += "IIIV"
        if c == "9" and cont == 0:
            rom += "XI"
        if c == "1" and cont == 1:
            rom += "X"
        if c == "2" and cont == 1:
            rom += "XX"
        if c == "3" and cont == 1:
            rom += "XXX"
        if c == "4" and cont == 1:
            rom += "LX"
        if c == "5" and cont == 1:
            rom += "L"
        if c == "6" and cont == 1:
            rom += "XL"
        if c == "7" and cont == 1:
            rom += "XXL"
        if c == "8" and cont == 1:
            rom += "XXXL"
        if c == "9" and cont == 1:
            rom += "CX"
        if c == "1" and cont == 2:
            rom += "C"
        if c == "2" and cont == 2:
            rom += "CC"
        if c == "3" and cont == 2:
            rom += "CCC"
        if c == "4" and cont == 2:
            rom += "DC"
        if c == "5" and cont == 2:
            rom += "D"
        if c == "6" and cont == 2:
            rom += "CD"
        if c == "7" and cont == 2:
            rom += "CCD"
        if c == "8" and cont == 2:
            rom += "CCCD"
        if c == "9" and cont == 2:
            rom += "MC"
        if c == "1" and cont == 3:
            rom += "M"
        if c == "2" and cont == 3:
            rom += "MM"
        if c == "3" and cont == 3:
            rom += "MMM"
        cont += 1
    return rom[::-1]

print(int2roman(1994))
print(betterSolution(1))
print(betterSolution(4000))
print(betterSolution(2020))