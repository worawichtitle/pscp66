"""Ticket Fare"""
def train():
    """Just reading this make me want to ride a PAIN Train"""
    station = int(input())
    astate = int(input())
    price1 = int(input())
    cstate = int(input())
    price2 = int(input())
    price3 = int(input())
    start = int(input())
    end = int(input())
    goto = abs(start - end)
    if goto <= astate:
        final = price1
    elif goto <= (astate + cstate):
        final = price1 + price2 * (goto - astate)
    else:
        final = price1 + price2 * cstate + price3 * (goto - (astate + cstate))
    if end > station or start > station:
        final = "Error"
    print(final)
train()