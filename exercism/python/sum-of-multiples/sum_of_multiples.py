def sum_of_multiples(limit, multiples):
    results = []
    for x in range(1, limit):
        for m in multiples:
            if m < 1:
                continue
            elif x % m == 0:
                results.append(x)
                continue
    return sum(set(results))
