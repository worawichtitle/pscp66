"""Sequence VI"""
def seq():
    """Sequene 6"""
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            if col <= row:
                print(col, end=" ")
        print("")
seq()
