# Easy to manipulate constant.
SCORES = {
    ('Q', 'Z') : 10,
    ('J', 'X') : 8,
    ('K') : 5,
    ('F', 'H', 'V', 'W', 'Y') : 4,
    ('B', 'C', 'M', 'P') : 3,
    ('D', 'G') : 2
    }

# Construct the dictionary for easier use.
letterScore = {}
for key, val in SCORES.items():
    for key0 in key:
        letterScore[key0] = val

def score(word):
    total = 0
    for letter in word.upper():
        total+= letterScore.get(letter, 1)
    return total
