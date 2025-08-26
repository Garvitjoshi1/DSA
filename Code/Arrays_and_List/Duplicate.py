import sys


def duplicateNumber(arr, n):
    for i in range(0, n - 1):
        for a in range(i + 1, n):
            if arr[i] == arr[a]:
                return arr[i]


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


# main
t = int(sys.stdin.readline().strip())
while t > 0:
    arr, n = takeInput()
    print(duplicateNumber(arr, n))
    t -= 1
