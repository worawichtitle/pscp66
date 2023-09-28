"""Right Arrow"""
def arrow(star, high):
    """Similar to Left arrow"""
    space = 0
    step = 1
    for row in range(high):
        if row >= int(high / 2):
            step = -1
        print(space * " " + star * "*")
        space += step
arrow(int(input()), int(input()))
