"""Calculator"""
def clicktime(num):
    """Find how many time you click"""
    text = ""
    nlen = len(str(num)) + 1
    for count in range(nlen-1):
        text += str(count)
    delete = 9 * int(text)
    if num == 1:
        click = 1
    else:
        click = (num * nlen) - delete
    print(click)
clicktime(int(input()))
