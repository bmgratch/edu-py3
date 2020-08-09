MIN, MAX = 0, 999
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEEN = ['ten', 'eleven','twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['teen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def say(number):
    if number > MAX or number < MIN:
        return "ERROR:" + str(number) + " out of limits!"
    if number > 99:
        return hundreds(number)
    return ones(number)

def ones(num):
    if num < 10:
        return ONES[num]
    if num < 20:
        return TEEN[num%10]
    if num % 10 != 0:
        return TENS[num//10] + "-" + ONES[num%10]
    return TENS[num//10]

def hundreds(num):
    if num % 100 > 0:
        return ONES[num//100] + ' hundred ' + ones(num%100)
    return ONES[num//100] + ' hundred'



## TEST CASES
tests = [0, 7, 11, 50, 25, 100, -1, 14, 101, 721]
for test in tests:
    print(say(test))
