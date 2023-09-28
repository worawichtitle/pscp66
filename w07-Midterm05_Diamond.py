"""Diamond"""
def dia(mond):
    """เพชรแท้มันเป็นอย่างไร"""
    step = 0
    for row in range(mond):
        for col in range(mond):
            if row == int(mond/2):
                print("*", end="")
                step = step * -1
            elif (col == int(mond/2) + step) or (col == int(mond/2) - step):
                print("*", end="")
            else:
                print(" ", end="")
        print()
        step += 1
dia(int(input()))
