"""Largest Number"""
def cal(newnum, oldnum):
    """Find Max num"""
    if newnum > oldnum:
        return newnum
    return oldnum

def chungus(num1, num2, num3):
    """Biggest number"""
    val_1 = int((num1) + (num2) + (num3))
    val_2 = int((num1) + (num3) + (num2))
    val_3 = int((num2) + (num1) + (num3))
    val_4 = int((num2) + (num3) + (num1))
    val_5 = int((num3) + (num1) + (num2))
    val_6 = int((num3) + (num2) + (num1))
    final = cal(cal(val_1, val_2), cal(val_3, val_4))
    final = cal(cal(final, val_5), val_6)
    print(final)
chungus((input()), (input()), (input()))
