ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def encode(plain_text):
    cipher = []
    for char in plain_text.lower():
        if char.isalpha():
            cipher.append(ALPHA[-1 - ALPHA.index(char)])
        elif char.isnumeric():
            cipher.append(char)
    for idx, char in enumerate(cipher):
        if idx % 5 == 4:
            cipher[idx] = char + ' '
    return ''.join(cipher).strip()

def decode(ciphered_text):
    cipher = []
    for char in ciphered_text.replace(' ',''):
        if char.isalpha():
            cipher.append(ALPHA[-1 - ALPHA.index(char)])
        else:
            cipher.append(char)
    return ''.join(cipher)
