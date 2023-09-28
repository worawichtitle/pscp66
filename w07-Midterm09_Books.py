"""Books"""
def books(book, page, xnum, yunm):
    """I hate reading now"""
    day = 0
    allpage = page
    while book > 0:
        read = ((xnum + day) / (yunm + day)) * page
        if read % 1 > 0:
            read = int(read) + 1
        allpage -= read
        if allpage <= 0:
            book -= 1
            allpage = page
        day += 1
        if read >= page:
            day += book
            break
    print(day)
books(int(input()), int(input()), int(input()), int(input()))
