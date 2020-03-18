class PhoneNumber:
    def __init__(self, number):
        phone = ''
        for n in number:
            if n.isnumeric():
                phone += n
        if phone[0] == '1':
            phone = phone[1:]
        print(phone)
        self.number = phone
