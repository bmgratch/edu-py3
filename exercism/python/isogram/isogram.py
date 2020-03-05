def is_isogram(string):
    iso = []
    for c in string.lower():
        if c.isalpha():
            if c not in iso:
                iso.append(c)
            else:
                return False
    return True

