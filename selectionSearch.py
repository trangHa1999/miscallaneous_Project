__author__ = "Trang Ha"

# Input: an unordered list
# Output: finding the nth smallest value of the list using partition method

class QuickSelect():
    def __init__(self, lst, k):
        self.lst = lst
        self.k = k
        self.leftMark = -1

    def partition(self, lst):
        self.leftMark += 1
        p = self.lst[self.leftMark]
        s = self.leftMark
        for i in range(1, len(lst)):
            if lst[i] < p:
                s += 1
                self.lst[s], self.lst[i] = self.lst[i], self.lst[s]
        self.lst[self.leftMark], self.lst[s] = self.lst[s], self.lst[self.leftMark]
        self.leftMark = s
        return s

    def quickSelect(self, lst):
        s = self.partition(lst)
        if s == self.k-1:
            print("The {0} smallest number is {1}".format(self.k, self.lst[s]))
        elif s > self.k-1:
            self.leftMark = -1
            self.quickSelect(self.lst[:s])
        else:
            self.quickSelect(self.lst[self.leftMark+1:len(self.lst)])


def main(lst, k):
    obj = QuickSelect(lst, k)
    print("Orginal list: {}".format(lst))
    obj.quickSelect(lst)

# Ordered list = [1,2,4,7,8,9,10,12,15]
main([4,1,10,8,7,12,9,2,15],5)

# Ordered list = [11,56,61,90,93]
main([61,93,56,90,11],1)
main([61,93,56,90,11],2)
main([61,93,56,90,11],3)

# Ordered list = [-5,1,2,5,12,14,16]
main([5,1,12,-5,16,2,12,14],4)

# Ordered list = [2,11,32,56,65,89,90]
main([65,32,11,89,90,2,56],5)
