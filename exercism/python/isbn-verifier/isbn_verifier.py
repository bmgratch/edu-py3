def is_valid(isbn):
    checksum = 0
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    for d in range(len(isbn)):
        if d == 9 and isbn[d] == 'X':
            checksum += 10
        elif isbn[d].isnumeric():
            checksum += (10-d) * int(isbn[d])
        else:
            return False
    return (checksum % 11) == 0
