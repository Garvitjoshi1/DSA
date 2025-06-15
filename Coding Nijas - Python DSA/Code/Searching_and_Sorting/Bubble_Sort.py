# Bubble sort in Python
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr


input = [-2, 45, 0, 11, -9]
bubbleSort(input)
print('Sorted Array in Ascending Order:')
print(input)
