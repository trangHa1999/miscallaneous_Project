__author__ = "Trang Ha"

lst = [(1,1),(3,2),(3,4),(2,5),(2,2),(2,4)]
newLst = []
for p1 in range(0, len(lst) - 1):
    for p2 in range(p1 + 1, len(lst)):
        a = lst[p2][1] - lst[p1][1]
        b = lst[p1][0] - lst[p2][0]
        c = lst[p1][0] * lst[p2][1] - lst[p1][1] * lst[p2][0]
        foundProblem = False
        for p3 in range(p2 + 1, len(lst)):
            check = a*lst[p3][0] + b*lst[p3][1] - c
            if check == 0:
                foundProblem = True
                break
        if foundProblem:
            newLst.append([lst[p1], lst[p2]])
print newLst

