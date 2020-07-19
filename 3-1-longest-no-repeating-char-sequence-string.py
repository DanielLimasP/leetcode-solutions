def findSubsequence(word):
    wordDict = {}
    longSub = ""
    index = 0
    for i in word:
        if i in wordDict:
            wordDict[i] = False
        else:
            wordDict[i] = True
            #print(dict)
            index += 1
            longSub = longSub + i
    print(longSub)
    #print(wordDict)
    #print(word)

testWord = "pwwkew"
#print(findSubstring(testWord)) 
findSubsequence(testWord)