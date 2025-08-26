from sys import stdin


def arrayRotateCheck(arr, n):
    if len(arr) == 0:
        return 0
    a = min(arr)
    b = arr.index(a)
    return b


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1
