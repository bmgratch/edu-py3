import random

def collatz(number):
    number = int(number)
    if number  % 2 == 0:
        nn = number // 2
        print(nn)
        return nn
    else:
        nn = 3 * number +1
        print(nn)
        return nn

def validateNumber():
    valid = False
    print("Please input a starting number.")
    while not valid:
        num = input()
        try:
            num = int(num)
            valid = True
        except ValueError:
            print('Error: Please input a *number*.')
    return num

print('Hey! Let\'s Collatz!')
num = validateNumber()

while num > 1:
    num = collatz(num)
