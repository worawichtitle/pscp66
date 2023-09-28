"""Sequence XXX"""
def sequence(star, box):
    """Why XXX is blue"""
    for row in range(star):
        for _ in range(box):
            for col in range(star):
                if col == 0 or row == 0 or col == star - 1 or row == star - 1\
or row == col or col == star - 1 - row:
                    print("*", end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        print()
sequence(int(input()), int(input()))
