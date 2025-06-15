import sys


def findUnique(arr, n):
    for i in range(0, len(arr), 1):
        flag = True
        for a in range(0, len(arr), 1):
            if a != i and arr[i] == arr[a]:
                flag = False
                break
        if flag:
            return arr[i]


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


# main
t = int(sys.stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1