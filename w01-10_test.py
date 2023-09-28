"""Kayak"""

def main():
    """main Function"""

    volume = int(input())
    lst = input().split(" ")
    for k in range(2*volume):
        lst[k] = int(lst[k])
    lst = sorted(lst)
    check = 0
    ans = 0
    num_diff = 0

    while True:
        if len(lst) > 2:
            for i in range(len(lst) - 1):
                if abs(lst[i] - lst[i+1]) == num_diff:
                    ans += num_diff
                    lst.pop(i)
                    lst.pop(i)
                    check = 1
                    break
        else:
            break

        if check == 1:
            check = 0
        else:
            num_diff += 1

    print(ans)

main()