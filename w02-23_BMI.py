"""BMI"""
def bmi():
    """calculate BMI"""
    name = str(input()).capitalize()
    weight = float(input())
    tall = float(input()) / 100
    dabmi = weight / (tall ** 2)
    answer = ("%s's  BMI = %.2f" % (name, dabmi))
    return answer

def main():
    """Are you too fat or ok"""
    final = []
    final.append(bmi())
    final.append(bmi())
    final.append(bmi())
    final.append(bmi())
    final.append(bmi())
    print("%s\n%s\n%s\n%s\n%s"\
    % (final[0], final[1], final[2], final[3], final[4]))
main()
