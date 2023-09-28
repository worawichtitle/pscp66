"""Ball"""
def balls(high):
    """Thomas give me da สูตร"""
    bounce = 0
    while True:
        high = high / (5 / 3)
        if high < 0.01:
            print(bounce)
            break
        else:
            bounce += 1
balls(float(input()))
