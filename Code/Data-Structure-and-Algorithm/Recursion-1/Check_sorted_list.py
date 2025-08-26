def isSorted(a):
    l = len(a)
    if l == 0 | l == 1:
        return True
    if a[0] > a[1]:
        return False
    isSmallerSorted = isSorted(a[1:])
    return isSmallerSorted


a = [1, 2, 3, 4, 5, 6]
print(isSorted(a))
a = [1, 2, 3, 4, 55, 6]
print(isSorted(a))
