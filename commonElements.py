__author__ = "Trang Ha"

def commonElements(lst1, lst2):
    commonLst = []
    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2:
                commonLst.append(item1)
                break
            else:
                continue
    return commonLst

lst1 = [2,5,5,5]
lst2 = [2,2,3,5,5,7]

print(commonElements(lst1, lst2))
