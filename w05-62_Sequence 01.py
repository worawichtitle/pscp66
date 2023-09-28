"""Sequence I"""
def seq():
    """Sequene 1"""
    num = int(input())
    for _ in range(num):
        for col in range(num):
            print(col + 1, end=" ")
        print("")
seq()
