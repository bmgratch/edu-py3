def steps(number):
    if number < 1:
        raise ValueError("The Collatz Conjecture is only applicable on positive integers.")
    count = 0
    num = number
    while num != 1:
        if num %2 == 0:
            num /=2
        else:
            num = 3 * num + 1
        count += 1
        print(count, num)
    return count
