"""Longer"""
import math
def long(rad, aval, bval):
    """What longer circle or box"""
    circle = 2 * math.pi * rad
    box = 2 * (aval + bval)
    if circle == box:
        print("Equal")
        print("%.5f" % (box - circle))
    elif circle < box:
        print("Rectangle is longer")
        print("%.5f" % (box - circle))
    else:
        print("Circle is longer")
        print("%.5f" % (circle - box))
long(float(input()),float(input()),float(input()))
