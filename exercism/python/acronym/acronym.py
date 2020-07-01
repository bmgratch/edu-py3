def abbreviate(words):
    cleanWords = words.replace('\'', '')
    tla = []
    for i in range(0, len(cleanWords)):
        if cleanWords[i].isalpha() and i == 0:
            tla.append(cleanWords[i].upper())
        elif i != 0 and cleanWords[i].isalpha() and not cleanWords[i-1].isalpha():
            tla.append(cleanWords[i].upper())
    return ''.join(tla)
