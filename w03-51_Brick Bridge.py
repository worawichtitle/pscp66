"""Brick Bridge"""
def bridge(small, big, goal):
    """Built Brick Bridge"""
    if goal // 5 <= big:
        big = goal // 5
    if goal <= (big * 5) + small:
        small = goal - (big * 5)
        print(small)
    else:
        print(-1)
bridge(int(input()), int(input()), int(input()))
