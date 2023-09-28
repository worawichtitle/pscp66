"""RockPaperScissor"""
def play():
    """Find whoi win in RockPaperScissor"""
    game = input()
    gamelis = []
    a_score = 0
    b_score = 0
    for text in game:
        gamelis += [text]
    for num in range(0, len(game), 2):
        temp_a = gamelis[num]
        temp_b = gamelis[num + 1]
        if temp_a + temp_b in ("PR", "RS", "SP"):
            a_score += 1
        elif (temp_a + temp_b)[::-1] in ("PR", "RS", "SP"):
            b_score += 1
    if a_score == b_score:
        print("DRAW %d" % a_score)
    elif a_score > b_score:
        print("A win %d-%d" % (a_score, b_score))
    else:
        print("B win %d-%d" % (b_score, a_score))
play()
