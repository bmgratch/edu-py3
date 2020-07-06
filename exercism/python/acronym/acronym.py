def abbreviate(words):
    cleanWords = words.replace('\'', '').upper()
    tla = []
    for i in range(0, len(cleanWords)):
        if cleanWords[i].isalpha():
            if i == 0:
                tla.append(cleanWords[i])
            elif not cleanWords[i-1].isalpha():
                tla.append(cleanWords[i])
    return ''.join(tla)
