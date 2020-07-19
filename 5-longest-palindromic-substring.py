def longestPalindrome(s):
    # We create the aux variable that will hold the current substring
    aux = ""
    #print(s, n)
    # We iterate through the length of the word
    for i in range(len(s)):
        # j will keep track of the coming characters
        j = i + 1
        # while j is less or equal of the lenght of the word
        # and m is less or equal than the remaining substring
        while j <= len(s) and len(aux) <= len(s[i:]):
            # if we find a palindrome (substring from i to j that is equal when reversed)
            # and it's length is greater than the last palindrome, we update the palindrome
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(aux):
                aux = s[i:j]
            # regardless of the circumstances, we update j
            j += 1
    # We return the greater palindrome
    return aux

testWord1 = "forgeekskeegrof"
print(longestPalindrome(testWord1))



















