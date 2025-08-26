def lastIndex(a, x):
    l = len(a)
    if l == 0:
        return -1
    small_list = a[1:]
    output = lastIndex(small_list, x)
    if output != -1:
        return output + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1


a = [1, 2, 4, 5, 6, 7, 8, 9, 4]
x = 4
print(lastIndex(a, x))
