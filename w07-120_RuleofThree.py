"""RuleofThree"""
def deal(count):
    """Find the best deal"""
    money_best = 1
    val_best = 0
    for _ in range(count):
        money = float(input())
        value = float(input())
        bestdeal = best(money_best, val_best)
        if bestdeal < best(money, value):
            money_best = money
            val_best = value
        elif bestdeal == best(money, value):
            if money < money_best:
                money_best = money
                val_best = value
    print("%.2f %.2f" % (money_best, val_best))

def best(money, val):
    """Find Gram per bath"""
    good = val / money
    return good

deal(int(input()))
