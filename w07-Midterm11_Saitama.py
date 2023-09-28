"""ฉันจะเป็น Saitama ให้ได้เลย"""
def training(wit, sit, lok, wig):
    """How to train to be Saitama"""
    floor = perday(wit, int(input()))
    upp = perday(sit, int(input()))
    run = perday(wig, int(input()))
    nang = perday(lok, int(input()))
    print(int(fast(fast(fast(floor, upp), run), nang)))

def perday(need, done):
    """Find how many day this job take"""
    plus = 0
    if need % done != 0:
        plus = 1
    day = (need / done) + plus
    return day

def fast(long, new):
    """Find Max to get Fastest day"""
    if long > new:
        return long
    else:
        return new
training(int(input()), int(input()), int(input()), int(input()))
