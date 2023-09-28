"""Kayak"""
def main():
    """too fat too bad"""
    num_n = int(input())
    people = str(input())
    peoplelist = sorted(people.split(" "))
    checklist = []
    for maa in range(num_n * 2):
        peoplelist[maa] = int(peoplelist[maa])
    for naa in range((num_n * 2) - 1):
        if abs(peoplelist[naa] - peoplelist[naa + 1]) == 0:
            peoplelist.pop(naa)
            peoplelist.pop(naa)
            check = 0
        else:
            check = abs(peoplelist[naa] - peoplelist[naa + 1])
            checklist.append(check)
            break
        checklist.append(check)
    while True:
        for k in checklist:
            if k > 0:
                final = k
                break
            else:
                final = 0
        break
    print(final)
main()
