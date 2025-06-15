from sys import stdin


def pushZerosAtEnd(arr, n):
    # Your code goes here
    i, k = 0, 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k += 1
        else:
            i += 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1