"""GraderMachine"""
def grader():
    """Build Mr.White machine"""
    start = int(input())
    end = int(input())
    step = 1 if start < end else -1
    number = ""
    value = 0
    for num in range(start, end + step, step):
        if num == 0:
            continue
        if num % 2 == 0:
            if value == 0:
                number += str(num)
            else:
                number += " " + str(num)
            value = value + num
    print("pass : %s\nSum : %d" % (number, value))
grader()
