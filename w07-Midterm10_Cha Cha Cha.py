"""Cha Cha Cha"""
def salary(days):
    """Find how much money he have"""
    money = 0
    for _ in range(days):
        hours = float(input())
        if hours != int(hours):
            hours = int(hours) + 1
        money += 8720 * hours
    print(int(money))
salary(int(input()))
