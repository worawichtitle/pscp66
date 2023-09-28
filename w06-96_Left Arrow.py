"""Left Arrow"""
def arrow(star, row):
    """build left arrow"""
    for num in range(row):
        space = abs(num - (row // 2))
        for _ in range(space):
            print(" ", end="")
        for _ in range(star):
            print("*", end="")
        print()
arrow(int(input()), int(input()))
