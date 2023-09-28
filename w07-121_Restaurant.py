"""Restaurant"""
def food(price, require, percent, buymore):
    """Find if you should eat more or not"""
    if price + buymore >= require:
        newprice = (price + buymore) * ((100 - percent) / 100)
    else:
        newprice = price + buymore
    if price >= require:
        price = price * ((100 - percent) / 100)
    if price > newprice:
        print("Yes %.03f" % (price - newprice))
    elif price < newprice:
        print("No %.03f" % abs(price - newprice))
    elif price == newprice:
        print("Yes")
food(float(input()), float(input()), float(input()), float(input()))
