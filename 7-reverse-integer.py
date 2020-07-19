# Most easy of the bunch so far...
def reverseInteger(n):
    s = str(n)
    rev = int(s[::-1])
    return rev

print(reverseInteger(765))