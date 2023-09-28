"""Table I"""
def price(bowl):
    """Price of noodles"""
    for num in range(1, bowl + 1):
        noodle = 15 * num
        print("15 x %d = %d" % (num, noodle))
price(int(input()))
