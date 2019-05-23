def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores = []
    for i in range(3):
        top_scores[i] = personal_best(scores)
    return top_scores
