"""Sequence III"""
def seq():
    """Sequene 3"""
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            print(col + row, end=" ")
        print("")
seq()
