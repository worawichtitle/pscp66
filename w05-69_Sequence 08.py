"""Sequence VIII"""
def seq():
    """Sequene 8"""
    num = int(input())
    for row in range(1, num + 1):
        for col in range(num - 1, -1, -1):
            if row - col > 0:
                print("%02d" % (row - col), end=" ")
            else:
                print("  ", end=" ")
        print("")
seq()
