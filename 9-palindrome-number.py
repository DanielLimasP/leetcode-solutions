# Pseudo over engineered stuff
def palindromeNumber(n):
    strnum = str(n)
    l = len(strnum)

    if n < 0:
        return False
    
    if l % 2 == 0:
        pal1 = strnum[0:int(l/2)]
        pal2 = strnum[int(l/2):]
        print("part 1: %r and part 2: %r" %(pal1, pal2))
    else:
        pal1 = strnum[0:int(l/2)]
        pal2 = strnum[int(l/2+1):]
        print("part 1: %r and part 2: %r" %(pal1, pal2))
        print("the middle number is %r" %strnum[int(l/2)])

    if pal1 == pal2[::-1]:
        return True
    else:
        return False

def solutionAgain(n):
    if n < 0:
        return False
    
    strn = str(n)
    if strn == strn[::-1]:
        return True
    else:
        return False

print("The number is a palindrome? %r" %palindromeNumber(981323189))
print(solutionAgain(9813213189))