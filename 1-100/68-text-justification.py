def justify_text(words, max_width):
    result = []
    current_words = []
    no_letters = 0

    for word in words: 
        if no_letters + len(word) + len(current_words) > max_width:
            for i in range(max_width - no_letters):
                current_words[i%(len(current_words)-1 or 1)] += ' '
            result.append(''.join(current_words))
            current_words = []
            no_letters = 0
        current_words.append(word)
        no_letters += len(word)
    
    return result + [" ".join(current_words).ljust(max_width)]

if __name__ == "__main__":
    print(justify_text(["This", "is", "an", "example", "of", "text", "justification."], 16))
        
