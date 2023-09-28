"""Left Arrow"""
def main():
    """You are going to LEFT"""
    star = int(input())
    line = int(input())
    arrow = ""
    space = int((line / 2) * -1)
    for row in range(line):
        arrow = arrow + (" " * abs(space))
        space = space + 1
        if row == (line - 1):
            arrow = arrow + ("*" * star)
        else:
            arrow = arrow + ("*" * star) + "\n"
    print(arrow)
main()
