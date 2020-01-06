# robot names should be random!
import random

class Robot:
    
    def __init__(self):
        self.name = self.gen_name()

    def gen_name(self):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        a = alpha[random.randint(0, 25)]
        b = alpha[random.randint(0, 25)]
        name = str(a) + str(b)
        for n in range(0, 3):
            name += str(random.randint(0, 9))
        return(name)
    
    def reset(self):
        old_name = self.name
        while old_name == self.name:
            self.name = self.gen_name()
