"""GO NUT"""
def da_donut(price, pay_donut, free_donut, want):
    """Get me some Nut"""
    donut_round = want // (pay_donut + free_donut)
    left_donut = want % (pay_donut + free_donut)
    if left_donut >= pay_donut:
        all_price = (pay_donut * (donut_round + 1)) * price
        all_donut = (pay_donut + free_donut) * (donut_round + 1)
    else:
        all_price = ((pay_donut * donut_round) + left_donut) * price
        all_donut = ((pay_donut + free_donut) * donut_round) + left_donut
    print(all_price, all_donut)
da_donut(int(input()), int(input()), int(input()), int(input()))
