def first_index(arr, x):
    l = len(arr)
    if l == 0:
        return 1
    if arr[0] == x:
        return 0
    output = first_index(arr[1:], x)
    return output


arr = [1, 2, 3, 4, 5]
x = 4
if first_index(arr, x):
    print('false')
else:
    print('true')
