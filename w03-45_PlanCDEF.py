"""PlanCDEF..."""
def cal(arod, newnum, oldnum):
    """Find MAX to min and min to MAX"""
    if arod == 1:
        if newnum > oldnum:
            return newnum
        return oldnum
    else:
        if newnum < oldnum:
            return newnum
        return oldnum

def findmid(val_a, val_b, val_c):
    """Find mid number"""
    if val_a >= val_b >= val_c or val_c >= val_b >= val_a:
        return val_b
    elif val_b >= val_a >= val_c or val_c >= val_a >= val_b:
        return val_a
    elif val_b >= val_c >= val_a or val_a >= val_c >= val_b:
        return val_c

def main(aord):
    """Ascend or Descend"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    most = cal(1, cal(1, num3, num1), num2)
    less = cal(0, cal(0, num3, num1), num2)
    mid = findmid(num1, num2, num3)
    if aord == "Descend":
        print("%.2f, %.2f, %.2f" % (most, mid, less))
    else:
        print("%.2f, %.2f, %.2f" % (less, mid, most))
main(str(input()).capitalize())
