class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        strip_num = self.card_num.replace(' ', '')[::-1]
        if len(strip_num) < 2 or not strip_num.isdigit():
            return False
        checksum = 0
        for idx, num in enumerate(strip_num):
            if idx % 2 == 0:
                checksum += int(num)
            elif int(num) * 2 > 9:
                checksum += (int(num) * 2) - 9
            else:
                checksum += int(num) * 2
            print(checksum)
        return checksum % 10 == 0
