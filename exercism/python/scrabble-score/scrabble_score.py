SCORES = {
    ('Q', 'Z') : 10,
    ('J', 'X') : 8,
    ('K') : 5,
    ('F', 'H', 'V', 'W', 'Y') : 4,
    ('B', 'C', 'M', 'P') : 3,
    ('D', 'G') : 2
    }

def score(word):
    total = 0
    for w in word.upper():
        total+= letterScore(w)
    return total

def letterScore(letter):
    for key in SCORES:
        if letter in key:
            return SCORES[key]
    return 1
