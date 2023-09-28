"""Coke"""
def coke(price, bottle, nprice, want):
    """Cheapest price"""
    if bottle == 0:
        cost = price * want
    else:
        loop = (want - bottle) // (bottle)
        left = (want - bottle) - (bottle * loop) - 1
        if left <= 0:
            cost = price * bottle + ((price * (bottle - 1) + nprice) * loop)
        else:
            cost = price * bottle + ((price * (bottle - 1) + nprice) * loop)\
+ nprice + left * price
    print(cost)
coke(int(input()), int(input()), int(input()), int(input()))
