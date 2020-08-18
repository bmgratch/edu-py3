class Clock:
    def __init__(self, hour, minute):
        self.hour = ((minute // 60) + hour) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'{self.hour:0>2}:{self.minute:0>2}'

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
