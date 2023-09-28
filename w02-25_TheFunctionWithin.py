"""TheFunctionWithin"""
def find_f(num):
    """Function f(x)"""
    answer = 2 * num
    return answer
def find_g(num):
    """Function g(x)"""
    answer = (3 * num**4) - (num**3) + (2 * num**2) + 10
    return answer
def find_h(numx, numy, numz):
    """Function h(x, y, z)"""
    answer = (numz + numx)**2 - (numx * numy) + numy**2
    return answer
def find_i(numa, numb, numc, numd):
    """Function i(a, b, c, d)"""
    answer = (numa**2 + numb**2 - numc**2) / (numd**2 - (2 * numa * numd) + (2 * numa))
    return answer

def main():
    """Find function answer"""
    input_a = float(input())
    input_b = float(input())
    input_c = float(input())
    input_d = float(input())
    print(float(find_f(find_f(input_a))))
    print(float(find_g(find_f(input_a - input_b))))
    print(float(find_h(find_f(input_a + input_b), find_f(input_a + input_c),\
    find_g(find_f(input_d**2)))))
    print(float(find_i(find_h(find_f(input_a + input_b), find_f(input_a - input_c),\
    find_g(find_f(input_d**2))),\
    find_g(find_f(input_a - input_b)),\
    find_f(find_f(find_f(find_f(find_f(input_c))))), input_d ** 8)))
main()
