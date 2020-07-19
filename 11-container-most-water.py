# I coded this solution myself without any kind of help whatsoever and I'm kind of proud 
def mostWater(h):
    cont = 0
    vol = 0
    biggest = max(h)
    bDict = {}

    for n in h:
        if n == biggest:
            bDict[cont] = n
        cont += 1
        
    for i in bDict:
        cont = 0
        #print(i)
        for j in h:
            if cont >= i:
                if j * (cont - i) > vol:
                    vol = j * (cont - i)
            else:
                if j * (i - cont) > vol:
                    vol = j * (i - cont)
            cont += 1

    return vol

#mostWater([8, 6, 2, 5, 4, 8, 3, 7])
print('''
The highest volume that a container can contain 
within this list is %r
''' 
%mostWater([8, 6, 2, 5, 4, 8, 3, 7]))