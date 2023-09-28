"""HowLong"""
def long():
    """Find len of number"""
    number = abs(int(input()))
    times = 1
    while True:
        if number // (10 ** times) == 0:
            break
        # if number // (10 ** (times + 6)) >= 1:
        #     times += 6
        # elif number // (10 ** (times + 3)) >= 1:
        #     times += 3
        else:
            times += 1
    print(times)
long()
