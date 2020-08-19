def findSubsequence(word):
    wordDict = {}
    longSub = ""
    index = 0
    for letter in word:
        if letter in wordDict:
            wordDict[letter] = False
        else:
            wordDict[letter] = True
            #print(dict)
            index += 1
            longSub = longSub + letter
    print(longSub)
    #print(wordDict)
    #print(word)

testWord = "pwwkew"
#print(findSubstring(testWord)) 
findSubsequence(testWord)