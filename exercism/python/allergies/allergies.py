allergens = [
    'eggs',         # 1
    'peanuts',      # 2
    'shellfish',    # 4
    'strawberries', # 8
    'tomatoes',     # 16
    'chocolate',    # 32
    'pollen',       # 64
    'cats']         # 128

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        all_list = []
        aller = self.score % 256
        counter = 7
        while counter >= 0:
            if aller >= 2 ** counter:
                all_list.append(allergens[counter])
                aller = aller % 2 ** counter
            counter -= 1
        return all_list
