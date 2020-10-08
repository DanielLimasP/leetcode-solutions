def needleHaystack(needle, haystack):
    nLen = len(needle)
    hLen = len(haystack)
    i = 0
    j = 0
    flag = False

    if needle == "":
        return 0

    while i < hLen:
        if haystack[i] == needle[0]:
            while j < nLen:
                if haystack[i] == needle[j]:
                    j += 1
                    flag = True
                else:
                    flag = False
                    break
                if j == nLen - 1:
                    return i
        i += 1

    if flag == False:
        return -1


if __name__ == "__main__":
    print(needleHaystack("ll", "hello"))
    print(needleHaystack("aa", "aaaaa"))
    print(needleHaystack("baa", "aaaaa"))