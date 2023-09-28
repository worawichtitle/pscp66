"""Lotto"""
def lotto():
    """Check if your gamber give you any money"""
    prize1 = str(input())
    last2 = str(input())
    front3_1 = str(input())
    front3_2 = str(input())
    last3_1 = str(input())
    last3_2 = str(input())
    buy = str(input())
    money = 0
    if prize1 == "000000":
        dclose = "999999"
    else:
        dclose = "%06d" % (int(prize1) - 1)
    if prize1 == "999999":
        uclose = "000000"
    else:
        uclose = "%06d" % (int(prize1) + 1)
    if buy == prize1:
        money += 6000000
    if buy[4::] == last2:
        money += 2000
    if buy[:3:] == front3_1:
        money += 4000
    if buy[:3:] == front3_2:
        money += 4000
    if buy[3::] == last3_1:
        money += 4000
    if buy[3::] == last3_2:
        money += 4000
    if buy in (str(dclose), str(uclose)):
        money += 100000
    print(money)
    # print(dclose, uclose)
lotto()
