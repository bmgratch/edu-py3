class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # This will fail validation if it has non-digits or is too short
        if len(self.card_num.replace(' ','')) < 2 or not self.card_num.replace(' ','').isdigit():
            return False

        strip_num = [int(num) for num in self.card_num.replace(' ', '')[::-1]]

        for idx, num in enumerate(strip_num[1::2]):
            if num * 2 > 9:
                strip_num[idx*2 +1] = num * 2 - 9
            else:
                strip_num[idx*2 +1] = num * 2
        return sum(strip_num) % 10 == 0
