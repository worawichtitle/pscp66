"""Sequence IV"""
def seq():
    """Sequene 4"""
    num = int(input())
    for row in range(num):
        for col in range(1, num + 1):
            print(col + (num * row), end=" ")
        print("")
seq()
