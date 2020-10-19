def count_and_say(n):   
    s = "1"
    for i in range(n-1):
        count = 1 
        temp = []
        for j in range(1, len(s)):
            if s[j] == s[j-1]:
                count += 1
            else:
                temp.append(str(count))
                temp.append(s[j-1])
                #print(temp)
        temp.append(str(count))
        temp.append(s[-1])
        #print(temp)
        s = "".join(temp)
    return s

if __name__ == "__main__":
    print(count_and_say(4))