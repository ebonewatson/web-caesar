def alphabet_position(letter):
    alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6,
    'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N':13, 'n':13, 'O':14,
    'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':19, 'T':20, 't':20, 'U':21, 'u':21, 'V':22,
     'v':22, 'W':23, 'w':23, 'X':24, 'x':24, 'Y':25, 'y':25, 'Z':26, 'z':26}
    pos = alphabet_pos[letter]
    return pos


def rotate_character(char, rot):
    initial_char = alphabet_position(char)
    final_char = initial_char + rot
    shift = 97 if char.islower() else 65
    return chr((ord(char) + rot - shift) % 26 + shift)

def encrypt(text, rot):
    results = ""
    for c in text:
        if c.isalpha():
            results = results + rotate_character(c, rot)
        else:
            results = results + c
    return results
    
