# TODO: Solve a bunch of edge cases
def myAtoi(s):
    cont = 0
    negative = False
    num = 0
    strnum = ""
    for c in s:
        if s[0].isalpha():
            return 0
        if c == " ":
           continue
        if c == "-":
            negative = True
        if c.isnumeric():
            strnum += c

        cont += 1    
    num = int(strnum)
    if negative:
        num = num * -1

    #print(strnum)    
    return num

print(myAtoi("   myatoifunct -365"))