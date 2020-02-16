def is_isogram(string):
    iso = ''
    for c in string.lower():
        if not c.isalpha():
            continue
        elif c not in iso:
            iso += c
        else:
            return False
    return True

