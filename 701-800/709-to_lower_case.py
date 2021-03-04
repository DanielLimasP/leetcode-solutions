def to_lowercase(s):
    char_dict = {
        'A': 'a',
        'B': 'b',
        'C': 'c',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g',
        'H': 'h',
        'I': 'i',
        'J': 'j',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'O': 'o',
        'P': 'p',
        'Q': 'q',
        'R': 'r',
        'S': 's',
        'T': 't',
        'U': 'u',
        'V': 'v',
        'W': 'w',
        'X': 'x',
        'Y': 'y',
        'Z': 'z',
    }

    new_s = []

    for c in str:
        if c in char_dict:
            new_s.append(char_dict[c])
        else:
            new_s.append(c)

    return "".join(new_s)

if __name__ == "__main__":
    print(to_lowercase("HELLO"))
             
