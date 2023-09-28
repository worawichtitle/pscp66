"""BootSequence"""
def main():
    """Put "_" between"""
    final = int(input())
    word = "1"
    for num in range(2, final + 1):
        word += "_" + str(num)
    print(word)
main()

"""The other way"""
# def second():
#     final = int(input())
#     print(*range(1, final + 1), sep="_")
# second()

# def third():
#     final = int(input())
#     for num in range(1, final + 1):
#         if num == final:
#             print(num, end="")
#         else:
#             print(num, end="_")
# third()