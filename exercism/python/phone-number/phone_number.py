class PhoneNumber:
    def __init__(self, number):
        # convert to simple string
        phone = ''
        for n in number:
            if n.isnumeric():
                phone += n
        if phone[0] == '1':
            phone = phone[1:]

        # break up number
        self.number = phone
        self.area_code = self.number[:3]
        #self.phone = self.number[3:] #unnecessary in tests, but I think it should exist if area-code is pulled out too

        # test for valid number
        self.is_valid()        

    def pretty(self):
        return "({}) {}-{}".format(self.number[:3], self.number[3:6], self.number[6:])

    def is_valid(self):
        if int(self.number[0]) < 2:
            raise ValueError('Incorrect digit in area code')
        elif int(self.number[3]) < 2:
            raise ValueError('Incorrect digit in exchange code')
        elif len(self.number) != 10:
            raise ValueError('Incorrect number of digits')
