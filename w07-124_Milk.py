"""Milk"""
def milk():
    """Find the MILK your DAD gonna get"""
    price = float(input())
    cap = int(input())
    free = int(input())
    money = float(input())
    bottle = money // price
    newbottle = bottle
    if cap != 0:
        while True:
            newcap = newbottle % cap
            newbottle = (newbottle // cap) * free
            bottle += newbottle
            newbottle += newcap
            if newbottle // cap == 0:
                break
    print(int(bottle))
milk()
