# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):
    l = -2147483648
    sl = -2147483648

    for i in arr:
        if i > l:
            sl = l
            l = i
        elif i > sl and i != l:
            sl = i

    return sl


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1