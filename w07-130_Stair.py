"""Stair"""
def stair(foot, steps):
    """Going UP"""
    high = []
    go_up = 0
    going = 0
    for _ in range(steps):
        high.append(int(input()))
    for step in range(len(high)):
        if foot < high[step]:
            go_up = "NO"
            break
        going += high[step]
        if foot == going:
            go_up += 1
            going = 0
        elif foot < going:
            go_up += 1
            going = high[step]
        elif step == len(high) - 1 and foot >= going:
            go_up += 1
            going = 0
    if go_up != "NO" and going != 0 and foot >= going:
        go_up += 1
    print(go_up)
stair(int(input()), int(input()))
