def classify(number):
    if number < 1:
        raise ValueError('%s is not a natural number.' % number)
    aliquot = 0
    for n in range(1, number):
        if number % n == 0:
            aliquot += n
    if aliquot == number:
        return 'perfect'
    elif aliquot < number:
        return 'deficient'
    else:
        return 'abundant'
