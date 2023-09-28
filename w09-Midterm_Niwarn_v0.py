"""Niwarn World"""
import math
def x_find(nval):
    """Find X position"""
    xval = 2 + ((math.log((nval**2), 2)) / ((2*nval) * math.log((nval), 2)))
    return xval
 
def y_find(nval, sval):
    """Find Y position"""
    yval = (math.sin(math.radians(30)) + (2*sval)**0.5) / (x_find(nval) + 3)
    return yval
 
def z_find(kval):
    """Find Z position"""
    zval = (y_find(kval, kval))**2 + (8456 * (x_find(kval))**4) / (24 * kval)
    return zval
 
def long(nval, sval, kval):
    """It might be a Neither in Minecraft"""
    x_pos = x_find(nval)
    y_pos = y_find(nval, sval)
    z_pos = z_find(kval)
    print("X: %.1f, Y: %.1f, Z: %.1f" % (x_pos, y_pos, z_pos))
long(float(input()),float(input()),float(input()))