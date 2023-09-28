"""ChristmasTree"""
def tree(leaf, log):
    """Let create the ChristmasTree"""
    space = leaf - 1
    for num in range(1, leaf * 2, 2):
        print(" " * space, end="")
        print("*" * num, end="\n")
        space -= 1
    for _ in range(log):
        space = leaf - 2
        print(" " * space + "---", end="\n")
tree(int(input()), int(input()))
