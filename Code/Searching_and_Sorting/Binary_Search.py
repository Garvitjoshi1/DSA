from sys import stdin


def binarySearch(arr, n, x):
    debug = False
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if debug:
            print(start)
            print(end)
            print(mid)
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0:
    x = int(input().strip())
    print(binarySearch(arr, n, x))

    t -= 1
