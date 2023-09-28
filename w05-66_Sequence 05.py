"""Sequence V"""
import math
def seq():
    """Sequene 5"""
    num = int(input())
    for _ in range(math.ceil(num / 7)):
        for _ in range(7):
            if num == 0:
                break
            print(num, end=" ")
            num -= 1
        print("")
seq()
