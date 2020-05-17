__author__ = "Trang Ha"

import math

def rootOfEquation(a, b, c):
    delta = b * b - 4 * a * c
    x1 = 0
    x2 = 0

    if delta < 0:
        print ("There is no value for x!")
    elif delta == 0:
        x1 = -b / (2 * a)
        x1 == x2
        print ("x1= {0} |  x2= {1}".format(x1, x2))
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print ("x1= {0} |  x2= {1}".format(x1, x2))
    return

print (rootOfEquation(3,5,2))
