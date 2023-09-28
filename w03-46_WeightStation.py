"""WeightStation"""
def checkbalance(bal, aver, num):
    """Check balance"""
    if bal == True:
        state = aver + (aver / 2) > num > aver / 2
        return state
    return False

def main():
    """Check Weight"""
    average = float(input())
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    lostnum = (average * 4) - (num1 + num2 + num3)
    balance = checkbalance(True, average, num1)
    balance = checkbalance(balance, average, num2)
    balance = checkbalance(balance, average, num3)
    balance = checkbalance(balance, average, lostnum)
    if num1 + num2 + num3 + lostnum > 15000:
        print("Overweight")
    elif balance == False:
        print("Unbalance")
    else:
        print("Pass %.2f" % lostnum)
main()
