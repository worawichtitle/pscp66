"""Parity"""
def eight_bit(text, evod):
    """Already did in Pre Pro"""
    val = 0
    for num in text:
        val += int(num)
    if evod == "Even" and val % 2 == 0:
        final = text + "0"
    elif evod == "Even" and val % 2 != 0:
        final = text + "1"
    elif evod == "Odd" and val % 2 == 0:
        final = text + "1"
    elif evod == "Odd" and val % 2 != 0:
        final = text + "0"
    print(final)
eight_bit(input(), input().capitalize())
