"""SumOfNumber"""
def main():
    """Find sum of all number"""
    want_num = int(input())
    sum_num = 0
    while True:
        if sum_num == want_num:
            break
        num = int(input())
        if num == -1:
            break
        sum_num += num
    print(sum_num)
main()
