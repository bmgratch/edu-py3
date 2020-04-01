from random import randint

class Cipher:
    
    def __init__(self, key=None):
        if not key:
            self.key = self.keygen()    # default generation if none provided
        else:
            self.key = key
    
    def encode(self, text):
        newText = []
        tKey = self.key # tKey repeats the key if it's shorter than the message
        while len(tKey) < len(text):
            tKey += self.key
        for i, c in enumerate(text):
            if c.islower():
                newText.append(chr((self.cton(c) + self.cton(tKey[i])) % 26 + 97)                               )
            elif c.isupper():
                newText.append(chr((self.cton(c) + self.cton(tKey[i])) % 26 + 65))
            else:
                newText.append(c)
        return ''.join(newText)

    def decode(self, text):
        newText = []
        tKey = self.key # tKey repeats the key if it's shorter than the message
        while len(tKey) < len(text):
            tKey += self.key
        for i, c in enumerate(text):
            if c.islower():
                newText.append(chr((self.cton(c) - self.cton(tKey[i])) % 26 + 97))
            elif c.isupper():
                newText.append(chr((self.cton(c) - self.cton(tKey[i])) % 26 + 65))
            else:
                newText.append(c)
        return ''.join(newText)

    # alpha char to number
    def cton(self, char):
        if char.isupper():
            return ord(char) - 65
        return ord(char) - 97
    
    # generates a random 100-character lowercase key
    def keygen(self):
        return ''.join(chr(randint(0, 25) + 97) for i in range(100))
