"""Calculator"""
def clicktime(num):
    """Find how many time you click"""
    nlen = len(str(num)) + 1
    if num == 1:
        click = 1
    elif num < 10:
        click = num * nlen
    elif num < 100:
        click = (num * nlen) - 9
    elif num < 1000:
        click = (num * nlen) - 108
    elif num < 10000:
        click = (num * nlen) - 1107
    elif num < 100000:
        click = (num * nlen) - (1107 + 9999)
    print(click)
clicktime(int(input()))
