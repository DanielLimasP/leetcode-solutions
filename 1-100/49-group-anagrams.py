def group_anagrams(strs):
    res = {}
    for word in strs:
        sorted_word = str(sorted(word))
        if sorted_word in res:
            res[sorted_word].append(word)
        else:
            res[sorted_word] = [word]
    return res.values()

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))