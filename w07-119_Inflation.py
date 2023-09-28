"""Inflation"""
def inflation(price, year):
    """Find the Price after Inflation"""
    new_price = int(price * 100) / 100
    for _ in range(year):
        new_price = int(new_price * 100) / 100
        new_price += new_price * 0.0381
    new_price = int(new_price * 100) / 100
    if str(new_price)[-2:].isdigit() > 0:
        decimal = str(new_price)[-2:]
    else:
        decimal = ".00"
    print(str(new_price)[:-2] + decimal)
inflation(float(input()), int(input()))
