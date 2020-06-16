from random import randint

ABILITIES = [
    self.strength,
    self.dexterity,
    self.constitution,
    self.intelligence,
    self.wisdom,
    self.charisma]

class Character:
    def __init__(self):
        self.strength = sum(rollStats()[1:])
        self.dexterity = sum(rollStats()[1:])
        self.constitution = sum(rollStats()[1:])
        self.intelligence = sum(rollStats()[1:])
        self.wisdom = sum(rollStats()[1:])
        self.charisma = sum(rollStats()[1:])
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return ABILITIES[randint(0, len(stats))]

def modifier(stat):
    return (stat - 10) // 2

def rollStats():
    return sorted([randint(1, 6) for d in range(4)])
