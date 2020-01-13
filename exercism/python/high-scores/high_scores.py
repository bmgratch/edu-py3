def latest(scores):
    return(scores[-1])


def personal_best(scores):
    scores.sort()
    return(scores[-1])


def personal_top_three(scores):
    scores.sort()
    scores.reverse()
    top3 = []
    for a in scores:
        top3.append(a)
        if len(top3) == 3:
            break
    return(top3)
