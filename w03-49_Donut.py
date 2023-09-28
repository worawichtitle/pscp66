"""GONUT"""
def da_donut(price, pay_donut, free_donut, want):
    """Get me some donut"""
    donut_round = want // (pay_donut + free_donut)
    if (pay_donut + free_donut) * donut_round >= want:
        all_price = (pay_donut * donut_round) * price
        all_donut = (pay_donut + free_donut) * donut_round
    else:
        left_donut = want - (pay_donut + free_donut) * donut_round
        if left_donut // pay_donut == 1:
            all_price = (pay_donut * (donut_round + 1)) * price
            all_donut = (pay_donut + free_donut) * (donut_round + 1)
        else:
            all_price = ((pay_donut * donut_round) + left_donut) * price
            all_donut = ((pay_donut + free_donut) * donut_round) + left_donut
    print("%d %d" % (all_price, all_donut))
da_donut(int(input()), int(input()), int(input()), int(input()))
