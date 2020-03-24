def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Minimum factor must not be larger than maximum factor.")
    highest = min_factor
    factors = []
    for n1 in range(min_factor, max_factor+1):
        for n2 in range(n1, max_factor +1):
            product = n1 * n2
            if product == highest:
                factors.append((n1, n2))
            elif str(product) == str(product)[::-1] and product > highest:
                highest = product
                factors = [(n1, n2)]
    if not factors:
        return (None, factors)
    else:
        return (highest, factors)
    


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Minimum factor must not be larger than maximum factor.")
    lowest = (max_factor +1) ** 2
    factors = []
    for n1 in range(min_factor, max_factor+1):
        for n2 in range(n1, max_factor +1):
            product = n1 * n2
            if product == lowest:
                factors.append((n1, n2))
            elif str(product) == str(product)[::-1] and product < lowest:
                lowest = product
                factors = [(n1, n2)]
    if not factors:
        return (None, factors)
    else:
        return (lowest, factors)
