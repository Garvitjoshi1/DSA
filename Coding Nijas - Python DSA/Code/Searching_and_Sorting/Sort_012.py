from sys import stdin


def sort012(arr, n):
    # Your code goes here
    a = arr.sort()
    return a


# Taking Input Using Fast I/O
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

    sort012(arr, n)
    printList(arr, n)

    t -= 1