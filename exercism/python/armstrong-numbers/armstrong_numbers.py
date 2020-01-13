def is_armstrong_number(number):
    numString = str(number)
    exp = len(numString)
    total = 0
    for n in numString:
        total += int(n) ** exp
    return(number == total)
