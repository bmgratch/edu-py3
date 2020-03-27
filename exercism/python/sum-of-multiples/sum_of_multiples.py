def sum_of_multiples(limit, multiples):
    results = []
    for factor in multiples:
        for x in range(1, limit):
            if x * factor < limit:
                results.append(x * factor)
            else:
                break
    return sum(set(results))
