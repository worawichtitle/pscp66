"""Coke"""
def coke(price, bottle, nprice, want):
    """Cheapest price"""
    if bottle == 0 or want == 0:
        cost = price * want
    else:
        loop = (want - bottle) // (bottle)
        left = nprice + (((want - bottle) - (bottle * loop)) - 1) * price
        if left < 0:
            left = 0
        cost = price * bottle + ((price * (bottle - 1) + nprice) * loop) + left
    print(cost)
coke(int(input()), int(input()), int(input()), int(input()))
