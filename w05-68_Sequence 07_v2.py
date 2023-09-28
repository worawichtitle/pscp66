"""Sequence VII"""
def main():
    """Start"""
    num1_ = int(input())
    num2_ = 1
    backward = False
    for _ in range((2*num1_)-1):
        for i in range(num2_):
            print(i+1, end=" ")
        print()
 
        if num2_ == num1_:
            backward = True
        if not backward:
            num2_ += 1
        if backward:
            num2_ -= 1
 
main()
