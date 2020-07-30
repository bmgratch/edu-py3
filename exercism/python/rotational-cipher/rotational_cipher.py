UPPER = 65
LOWER = 97
def rotate(text, key):
    cipher = []
    for char in text:
        if char.isupper():
            cipher.append(chr(((ord(char) - UPPER) + key)%26 + UPPER))
        elif char.islower():
            cipher.append(chr(((ord(char) - LOWER) + key)%26 + LOWER))
        else:
            cipher.append(char)
    return ''.join(cipher)
