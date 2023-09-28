"""Largest Number"""
def cal(catagory, newnum, oldnum):
    """Find Max num or min num"""
    if catagory == 1:
        if int(str(newnum)[0]) > int(str(oldnum)[0]):
            return newnum
        elif int(str(newnum)[0]) == int(str(oldnum)[0]) and newnum > oldnum:
            return newnum
        return oldnum
    else:
        if int(str(newnum)[0]) < int(str(oldnum)[0]):
            return newnum
        elif int(str(newnum)[0]) == int(str(oldnum)[0]) and newnum < oldnum:
            return newnum
        return oldnum

def chungus():
    """Biggest number"""
    final_num = []
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    most = cal(1, num1, cal(1, num2, num3))
    less = cal(0, num1, cal(0, num2, num3))
    mid = (num1 + num2 + num3) - (most + less)
    final_num.append(str(most))
    final_num.append(str(mid))
    final_num.append(str(less))
    print("".join(final_num))
chungus()
