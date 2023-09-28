"""SecondConverter"""
def worldtime(time):
    """Change world time to other world time"""
    mpers = int(input())
    hperm = int(input())
    dperh = int(input())
    mins = time // mpers
    sec = time % mpers
    hour = mins // hperm
    mins = mins % hperm
    hour = hour % dperh
    print("%.0f:%.0f:%.0f" % (hour, mins, sec))
worldtime(int(input()))
