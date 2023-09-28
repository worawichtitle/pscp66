"""EuclideanDistance2D"""
def distance(num1, num2):
    """Find Distance"""
    answer = (num1 - num2)**2
    return answer

def main():
    """Distance"""
    q_1 = float(input())
    q_2 = float(input())
    p_1 = float(input())
    p_2 = float(input())
    final = (distance(q_1, p_1) + distance(q_2, p_2))**0.5
    print(final)
main()
