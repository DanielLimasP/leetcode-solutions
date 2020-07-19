def longestCommonPrefix(words):
        # Compare first two words
        lcp = ""
        cont = 0
        wordCount = 0

        for word in words:
            lcp = ""
            #print("Current word %r" %word)
            firstWord = words[wordCount]
            secondWord = words[wordCount+1]
            cont = 0
            while cont < len(secondWord) and cont < len(firstWord):
                if firstWord[cont] == secondWord[cont]:
                    lcp += firstWord[cont]
                    #print(lcp)
                else:
                    return lcp
                cont += 1
            if wordCount < len(words) - 2:
                wordCount += 1

        return lcp

testList1 = ["doggogogogog", "doggo", "dogog"]
testList2 = ["flo", "fl", "fp"]
testList3 = ["flowe", "flow", "flowe"]
testList4 = ["dog","racecar","car"]
testList5 = ["race","racecar","car"]
print("The longest common prefix of the words in the list is %r" %longestCommonPrefix(testList1))
print("The longest common prefix of the words in the list is %r" %longestCommonPrefix(testList2))
print("The longest common prefix of the words in the list is %r" %longestCommonPrefix(testList3))
print("The longest common prefix of the words in the list is %r" %longestCommonPrefix(testList4))

