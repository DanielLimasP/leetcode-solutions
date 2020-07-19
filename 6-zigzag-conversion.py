# The string "PAYPALISHIRING" is written in a zigzag pattern. See problem for reference
# And then read line by line: "PAHNAPLSIIGYIR. Write the code that will take a string 
# and make the conversion given number of rows...
# Author: Myself, given that no other goood solution is given!

def zigzagConversion(s, rows):
    if rows == 1:
        return s
    n = len(s)
    result = ""
    # According to leetcode, cyclelen is the magic number were the 
    # next char lies within the string. 
    cyclelen = 2*rows-2
    for i in range(rows):
        print("<--------- Iteration %r --------->" %i)
        j = 0
        while j + i < n:
            # Code Magic
            result = result + s[j+i]
            print("j = ", j)
            print("Result: ", result)
            if i != 0 and i != rows - 1 and j + cyclelen - i < n:
                result = result + s[j+cyclelen-i]
                print("Result if: ", result)
            j += cyclelen 
    return result

tests = "PAYPALISHIRING"
rows = 4
print(zigzagConversion(tests, rows))