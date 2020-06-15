SCORES = {
    ('Q', 'Z') : 10,
    ('J', 'X') : 8,
    ('K') : 5,
    ('F', 'H', 'V', 'W', 'Y') : 4,
    ('B', 'C', 'M', 'P') : 3,
    ('D', 'G') : 2
    }

def score(word):
    letterScore = {}
    for k, v in SCORES.items():
        for k0 in k:
            letterScore[k0] = v
    total = 0
    for w in word.upper():
        total+= letterScore.get(w, 1)
    return total
