def binary_Search(a, x, si, ei):
    if si > ei:
        return -1
    mid = (si + ei) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_Search(a, x, si, mid - 1)
    else:
        return binary_Search(a, x, mid + 1, ei)


print(binary_Search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 0, 9))
