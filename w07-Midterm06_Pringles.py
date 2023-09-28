"""Pringles"""
def pbottle():
    """It's a mash potato not chip"""
    top = str(input())
    middle = str(input())
    bottom = str(input())
    willeat = int(input())
    chip = middle[:-1]
    eat = chip[:willeat]
    left = chip[willeat:]
    print(eat.count(")"))
    if left.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(top)
    print(" " * len(eat) + left + "|")
    print(bottom)
pbottle()
