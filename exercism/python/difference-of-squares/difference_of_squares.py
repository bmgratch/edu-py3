# I could just import the Math module,
# but I'm trying to do this without importing.

def square_of_sum(number):
    sum_number = (number * (number + 1)) // 2
    return sum_number ** 2

def sum_of_squares(number):
    return (number * (number + 1) * ((number * 2) + 1)) // 6

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
