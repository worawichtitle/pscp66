"""Shorten"""
def shirt():
    """Size of Shirt"""
    size = ""
    fnum = 0
    count = 0
    cnum = 0
    while True: #1 2 3 5 == 1-3, 5
        number = int(input())
        if fnum == 0:
            fnum = number
        elif cnum != fnum and fnum + count != number:
            if size != "":
                size += ", "
            size += str(fnum) + "-" + str(cnum) + ", " + str(number)
            fnum = number
            count = 0
        elif cnum == fnum and fnum + count != number:
            if size != "":
                size += ", "
            size += str(cnum)
            fnum = number
            count = 0
        cnum = number
        count += 1
        if number == -1:
            break
    print(size)
shirt()
