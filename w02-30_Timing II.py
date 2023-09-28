"""Timing II"""
def main():
    """Find day:hours:minutes:seconds"""
    sec = int(input())
    minut = sec // 60
    sec = sec % 60
    hour = minut // 60
    minut = minut % 60
    day = hour // 24
    hour = hour % 24
    if day <= 9999:
        print("%04d:%02d:%02d:%02d" % (day, hour, minut, sec))
    else:
        print("ERR_:__:__:__")
main()
