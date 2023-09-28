"""CompositeFunction"""
def find_f(num):
    """Function f(x)"""
    answer = 2 * num
    return answer
def find_g(num):
    """Function g(x)"""
    answer = num / 2 + 1
    return answer

def main():
    """Find function answer"""
    valinput = int(input())
    print("%.2f\n%.2f" % (find_f(find_g(valinput)), find_g(find_f(valinput))))
main()
