def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i - 1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp


array = [5, 66, 2, 4, 78, 9]
insertion_sort(array)
print(array)
