"""Sequence IX"""
def peramit(high):
    """Sequence 09"""
    space = high - 1
    for row in range(1, high + 1):
        step = 1
        print("   " * space, end="")
        for col in range(1, row * 2):
            if col > row:
                col = col - (step * 2)
                step += 1
            print("%02d" % col, end=" ")
        print()
        space = abs(space - 1)
peramit(int(input()))
