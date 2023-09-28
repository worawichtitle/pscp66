"""Century"""
def century(years):
    """What Century is this?"""
    for _ in range(years):
        year = str(input()).upper()
        adyear = int(year[5:])
        if year[:4] == "B.E.":
            adyear = int(adyear) - 543
        elif year[:4] not in ("A.D.", "B.E."):
            adyear = -9999
        adyear = int(adyear) / 100
        if adyear % 1 > 0 and adyear >= 0:
            adyear = int(adyear) + 1
        if adyear < 0:
            print("ERROR")
        else:
            print(int(adyear))
century(int(input()))
