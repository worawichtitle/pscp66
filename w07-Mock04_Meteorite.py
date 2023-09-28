"""Meteorite"""
def defence(wight, muti, safe):
    """Destroy meteor till it not dangerous"""
    missile = 0
    count = 1
    while True:
        if wight >= safe:
            wight = wight / muti
            missile += count
            count = count * muti
        else:
            print(missile)
            break
defence(float(input()), int(input()), float(input()))
