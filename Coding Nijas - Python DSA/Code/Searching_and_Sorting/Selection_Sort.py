def selection_sort(arr1):
    for i in range(len(arr1)):
        min_value = i
        for j in range(i + 1, len(arr1)):
            if arr1[j] < arr1[min_value]:
                min_value = j
            arr1[i], arr1[min_value] = arr1[min_value], arr1[i]

    return arr1


arr = [5, 6, 2, 1, 3, 4]
print(selection_sort(arr))
