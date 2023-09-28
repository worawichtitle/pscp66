"""Triangle I"""
def cal(newnum, oldnum):
    """Find max num"""
    if newnum > oldnum:
        return newnum
    return oldnum

def triangle():
    """Find right triangle"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    most = cal(cal(num1, num2), num3)
    if most + 0.01 >= (num1 ** 2 + num2 ** 2 + num3 ** 2 - most ** 2) ** 0.5 >= most - 0.01:
        print("Yes")
    else:
        print("No")
triangle()
