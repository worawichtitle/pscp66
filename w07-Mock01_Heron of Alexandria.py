"""Heron of Alexandria"""
def triangle(num_a, num_b, num_c):
    """Find area of Triangle"""
    val_s = (num_a + num_b + num_c) / 2
    area = (val_s * (val_s - num_a) * (val_s - num_b) * (val_s - num_c)) ** 0.5
    print("%.3f" % area)
triangle(float(input()), float(input()), float(input()))
