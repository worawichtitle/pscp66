'''FOR!F-Ball'''
def balls():
    '''ball'''
    var = input()
    ball = 1
    for text in var:
        if text == "A" and ball == 1:
            ball = 2
        elif text == "B" and ball == 2:
            ball = 3
        elif text == "C" and ball == 3:
            ball = 1
        elif text == "A" and ball == 2:
            ball = 1
        elif text == "B" and ball == 3:
            ball = 2
        elif text == "C" and ball == 1:
            ball = 3
    print(ball)
balls()
