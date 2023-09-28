"""One For All"""
def ofa(people):
    """All Might give One For All"""
    genaration = ""
    for count in range(1, people + 1):
        name = str(input())
        if count == people:
            genaration += name + "_" + str(count)
        elif count % 2 == 1:
            genaration += name + ("*" * count)
        else:
            genaration += name + ("-" * count)
    print(genaration)
ofa(int(input()))
