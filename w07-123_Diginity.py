"""Diginity"""
def diginity():
    """Plus untill have only len 1"""
    while True:
        number = str(input())
        if number == "0":
            break
        else:
            while len(number) > 1:
                newnum = 0
                for num in number:
                    newnum += int(num)
                    number = str(newnum)
            print(number)
diginity()
