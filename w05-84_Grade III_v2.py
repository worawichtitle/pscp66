"""Grade III"""
def score():
    """Find average score"""
    subjects = int(input())
    all_score = 0
    for _ in range(subjects):
        sub_score = float(input())
        if 100 >= sub_score >= 95:
            all_score += 4
        elif 95 > sub_score >= 90:
            all_score += 3.5
        elif 90 > sub_score >= 85:
            all_score += 3
        elif 85 > sub_score >= 80:
            all_score += 2.5
        elif 80 > sub_score >= 75:
            all_score += 2
        elif 75 > sub_score >= 70:
            all_score += 1.5
        elif 70 > sub_score >= 65:
            all_score += 1
        elif 65 > sub_score >= 60:
            all_score += 0.5
        elif 60 > sub_score >= 0:
            all_score += 0
    ave_score = int((all_score / subjects) * 100)
    print("%.2f" % (ave_score / 100))
score()
