__author__ = "Trang Ha"

def findRoot(n):
    root = 1
    for i in range(root, n/2):
        if root*root == n:
            print ("Sqrt({0}) = {1}".format(n, root))
        else:
            root += 1
            continue
        return root

n = 16
findRoot(n)
