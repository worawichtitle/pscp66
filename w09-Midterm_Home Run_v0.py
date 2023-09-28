"""Home Run"""
def hrun(place, batter):
    """How many time he can hit a Home run"""
    count = 0
    for _ in range(place):
        lenge = float(input())
        if batter > lenge:
            count += 1
    print(count)
hrun(int(input()),float(input()))