"""[Midterm 2021] iPhone 13 Again"""
def buyiphone(model, size):
    """Find how much price you have to pay"""
    price = 0
    giga = 1
    if size == "1 TB":
        giga = 1024 - 256
    elif size.find("GB") >= 0:
        giga = "".join(filter(str.isdigit, size))
        print(giga)
    if not str(giga).isdigit() or int(giga) % 128 != 0:
        price = "Not Available"
    if model.find("iPhone 13") >= 0 and price != "Not Available":
        giga = (int(giga) // 128) * 4000
        if model == "iPhone 13 mini" and giga <= 16000:
            price = 21900 + giga
        elif model == "iPhone 13" and giga <= 16000:
            price = 25900 + giga
        elif model == "iPhone 13 Pro":
            price = 34900 + giga
        elif model == "iPhone 13 Pro Max":
            price = 38900 + giga
        else:
            price = "Not Available"
    else:
        price = "Not Available"
    print(price)
buyiphone(model=input(), size=input().upper())
