def partition(a, si, ei):
    pivot = a[si]
    # find number of elements smaller than pivot
    count = 0
    for i in range(si, ei + 1):
        if a[i] < pivot:
            count = count + 1
    a[si + count], a[si] = a[si], a[si + count]
    pivot_index = si + count

    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i = i + 1
        elif a[j] >= pivot:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    return pivot_index


def quickSort(a, si, ei):
    if si >= ei:
        return
    pivot_index = partition(a, si, ei)
    quickSort(a, si, pivot_index - 1)
    quickSort(a, pivot_index + 1, ei)


a = [6, 10, 9, 8, 7, 1, 3, 5, 4, 2]
print(partition(a, 0, len(a) - 1))
print(quickSort(a, 0, len(a) - 1))
