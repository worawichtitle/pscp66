"""Inflation"""
def inflation(price, year):
    """Find the Price after Inflation"""
    new_price = int(price * 100)
    for _ in range(year):
        new_price += (new_price * 381) // 10000
    if str(new_price)[:-2] == "":
        new_price = "00" + str(new_price)
    print("%d.%s" % (int(str(new_price)[:-2]), str(new_price)[-2:]))
inflation(float(input()), int(input()))
