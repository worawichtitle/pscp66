"""SurprisingVote"""
def score(all_score, most_score):
    """Find is it will surprist ejudge or not"""
    if all_score > most_score * 2:
        less_score = all_score - (most_score * 2)
    else:
        less_score = 0
    if most_score - less_score > 2:
        print("Surprising")
    else:
        print("Not surprising")
score(float(input()), float(input()))
