"""Password"""
import math
def password(text):
    """Find a STRONG<oOo> password"""
    l_val = len(text)
    r_val = pool(text)
    entropy = int(math.log((r_val**l_val), 2))
    print(entropy)
    print(strong(entropy))
"""Bonus"""
def bonus(sala, year, moth):
    """Find bonus"""
    if moth >= 10:
        year += 1
    if year > 20:
        year = 20
    money = sala * year
    if money > 1000000:
        money = 1000000
    elif money < 5000:
        money = 5000
    print(money)
bonus(int(input()),int(input()),int(input()))
