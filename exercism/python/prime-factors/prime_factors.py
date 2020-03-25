def factors(value):
    primes = []
    while value > 1:
        for num in range(2, value+ 1):
            if value % num == 0:
                primes.append(num)
                value //= num
                break
    return sorted(primes)
