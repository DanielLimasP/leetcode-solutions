# Find the longest substring within a string without repeating chars

def findSubstring(word):
    subLength = 0
    subDict = {}
    auxDict = {}
    substring = ""
    for i in word:
        if i in subDict:
            subDict = {}
            auxDict[substring] = subLength
            subLength = 0
            substring = ""
        else: 
            subDict[i] = True
            subLength += 1
            substring = substring + i
            auxDict[substring] = subLength
            #print(substring)
    print("The longest substring is: "+max(auxDict, key = auxDict.get))
    #print(auxDict)
testWord1 = "abcabcbb"
testWord2 = "bbbbb"
testWord3 = "pwwkew"
#print(findSubstring(testWord)) 
findSubstring(testWord1)