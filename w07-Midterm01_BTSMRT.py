"""BTSMRT"""
def train(day, age, hight):
    """Find if this guy free to go or not"""
    if age < 14 and hight < 90:
        print("FREE")
    elif age < 14 and hight <= 140 and day == "Children Day":
        print("FREE")
    elif age >= 60 and day == "Senior Day":
        print("FREE")
    else:
        print("PAY")
train(str(input()), float(input()), float(input()))
