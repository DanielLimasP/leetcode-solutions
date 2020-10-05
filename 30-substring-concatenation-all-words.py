# Substring with Concatenation of All Words
def solution_problem_30(s, L):
    # We have to obtain the length of the words in list
    word_size = len(L[0])
    word_count = len(L)
    size_l = word_size * word_count
    res = []

    # Size of the list cannot be greater than the string 
    if size_l > len(s):
        return res

    hash_map = {}

    # We need to check the occurrences of each word in list 
    # to concatenate said word that many times
    for word in L:
        if word in hash_map:
            hash_map[word] += 1
        else:
            hash_map[word] = 1

    # Iterate through every size_l characters to find the indices that yield a result
    for i in range(len(s) - size_l + 1):
        temp_hash_map = hash_map.copy()
        j = i 
        count = word_count

    # Iterate the current size_l chars, one word_size at a time
        while j < i + size_l:
            word = s[j:j + word_size]

            if (word not in hash_map or temp_hash_map[word] == 0):
                break

            else:
                temp_hash_map[word] -= 1
                count -= 1
            j += word_size
        
        if count == 0:
            res.append(i)

    return res

if __name__ == "__main__":
    test_string_1 = "barfoothefoobarman"
    test_string_2 = "capcodcodcapthecodcapcapcod"
    word_list_1 = ["foo", "bar"]
    word_list_2 = ["cap", "cod"]
    print(solution_problem_30(test_string_2, word_list_2))