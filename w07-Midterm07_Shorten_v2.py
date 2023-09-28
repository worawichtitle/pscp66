"""Shorten"""
def shirt():
    """Size of Shirt"""
    size = ""
    fnum = 0
    count = 0
    cnum = 0
    while True:
        num = int(input())
        if fnum == 0:
            fnum = num
            cnum = num
        elif cnum != fnum and fnum + count != num:
            if size != "":
                size += ", "
            size += str(fnum) + "-" + str(cnum)
            fnum = num
            count = 0
        elif cnum == fnum and fnum + count != num:
            if size != "":
                size += ", "
            size += str(cnum)
            fnum = num
            count = 0
        cnum = num
        count += 1
        if num == -1:
            break
    print(size)
shirt()
