"""Lift"""
def lift(people, limit):
    """How SAFE the Lift is?"""
    allwight = 0
    safe = "Not Safe"
    for _ in range(people):
        age = int(input())
        wigth = float(input())
        if age >= 12:
            safe = "Safe"
        allwight += wigth
    if people == 0:
        safe = "Safe"
    if limit < allwight:
        safe = "Not Safe"
    print(safe)
lift(int(input()),float(input()))
