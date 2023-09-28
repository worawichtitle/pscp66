"""Stepper II"""
def step():
    """Step 2"""
    start = int(input())
    end = int(input())
    num = start
    if start < end:
        for _ in range(start, end + 1):
            print(num)
            num += 1
    else:
        for _ in range(end, start + 1):
            print(num)
            num -= 1
step()
