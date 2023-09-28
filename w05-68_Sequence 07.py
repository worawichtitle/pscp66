"""Sequence VII"""
def seq():
    """Sequene 7"""
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            if col <= row:
                print(col, end=" ")
        print("")
    for row in range(num - 1):
        for col in range(num):
            if col > row:
                print(col - row, end=" ")
        print("")
seq()
