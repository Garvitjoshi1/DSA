from sys import stdin


def rotate(arr, n, d):
    t = arr[0:d]
    i = 0
    j = d
    while j < n:
        arr[i] = arr[j]
        i += 1
        j += 1
    for k in range(len(t)):
        arr[i] = t[k]
        i += 1


# Taking Input Using Fats I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)

    t -= 1