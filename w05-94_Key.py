"""Key"""
def password(idcard):
    """creat key code"""
    num1 = 0
    for num in idcard:
        num1 += int(num)
    num2 = int(idcard[10:]) * 10
    key = num1 + num2
    if key < 1000:
        key += 1000
    print(str(key)[-4:])
password(input())
