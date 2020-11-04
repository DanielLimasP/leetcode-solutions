def last_word_lenght(s):
    if s == "":
        return 0
    
    words = s.split()
    
    if len(words) == 0:
        return 0
    
    return len(words[-1])

if __name__ == "__main__":
    print(last_word_lenght("Hello World"))