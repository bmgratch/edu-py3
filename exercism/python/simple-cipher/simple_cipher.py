class Cipher:
    
    def __init__(self, key=None):
        if not key:
            self.key = 'd'
        else:
            self.key = key
    
    def encode(self, text):
        newText = []
        tKey = self.key
        while len(tKey) < len(text):
            tKey += self.key
        for i, c in enumerate(text):
            if c.islower():
                newText.append(chr(self.cton(c) + self.cton(tKey[i]) % 26 + 97))
            elif c.isupper():
                newText.append(chr(ord(c) + self.cton(tKey[i]) % 26 + 96))
            else:
                newText.append(c)
        return ''.join(newText)

    def decode(self, text):
        pass

    def cton(self, char):
        return ord(char) - 97

ci = Cipher('d')
print(ci.key)
print(ci.encode('iamapandabear'))
print(ci.cton('d'))
