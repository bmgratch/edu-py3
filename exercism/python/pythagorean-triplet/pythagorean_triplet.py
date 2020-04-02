def triplets_with_sum(number):
    pyth = []
    for a in range(1, number // 3):
        for b in range(a + 1, number // 2):
            if is_triplet([a, b, number - (a + b)]):
                pyth.append([a, b, number-(a+b)])
    return pyth


def triplets_in_range(start, end):
    pyth = []
    for num in range(start, end):
        pyth.extend(triplets_with_sum(num))
    return pyth


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
