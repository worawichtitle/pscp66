"""Harshad Number"""
def harshad():
    """12: 1 + 2 = 3: 12 % 3 == 0: 12 is Harshad Number"""
    for _ in range(10):
        hars = 0
        number = abs(int(input()))
        for num in str(number):
            hars += int(num)
        if number != 0 and number % hars == 0:
            print("Yes")
        else:
            print("No")
harshad()
