'''Sequence N'''
def bign():
    '''Build the N'''
    num = int(input())
    for row in range(num):
        for col in range(num):
            if col == 0 or col == num-1:
                print("*", end="")
            elif col == row:
                print("*", end="")
            else:
                print(" ", end="")
        print()
bign()
