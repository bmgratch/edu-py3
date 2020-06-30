def abbreviate(words):
    tla = []
    for i in range(0, len(words)):
        if words[i].isalpha() and i == 0:
            tla.append(words[i].upper())
        elif i != 0 and words[i].isalpha() and not words[i-1].isalpha():
            tla.append(words[i].upper())
    return ''.join(tla)
