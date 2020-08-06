class Clock:
    def __init__(self, hour, minute):
        self.hour = ((minute // 60) + hour) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'{self.hour:0>2}:{self.minute:0>2}'

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        new_min = self.minute + minutes
        new_hr = self.hour
        if new_min > 60:
            new_hr += new_min // 60
            new_min %= 60
        return Clock(new_hr, new_min)

    def __sub__(self, minutes):
        new_min = self.minute - minutes
        new_hr = self.hour
        if new_min > 60:
            new_hr -= new_min // 60
            new_min %= 60
        return Clock(new_hr, new_min)

## tests
clock = Clock(6,15)
print (clock - 3005)
