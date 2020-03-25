def square(number):
    if number < 1 or number > 64:
        raise ValueError('Square must be positive.')
    return 2 ** (number - 1)


def total():
    return sum(square(n) for n in range(1, 65))
