

def primes(limit):
    primes = []
    nonprimes = []
    numbers = [num for num in range(2, limit + 1)]
    while len(numbers) > 0:
        primes.append(numbers[0])
        for num in numbers:
            if num * primes[-1] > max(numbers):
                break
            nonprimes.append(num * primes[-1])
        for n in nonprimes:
            numbers.remove(n)
        numbers.remove(primes[-1])
        nonprimes = []
    return primes
