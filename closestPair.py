__author__ = "Trang Ha"

import math

def bruteForceClosestPair(lst):
    d = {}
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            cal = (lst[i][0] - lst[j][0])**2 + (lst[i][1] - lst[j][1])**2
            d[cal] = [lst[i], lst[j]]

    minimum = math.sqrt(min(d.keys()))
    print("The distance {0} is the minimum with {1}.".format(d[minimum], minimum))

lst = [(1,1),(3,2),(3,4),(2,5),(2,2),(2,4)]
bruteForceClosestPair(lst)



