from sys import stdin


def leftRotate(arr, c, e):
    c = c % e
    g_c_d = gcd(c, e)
    for i in range(g_c_d):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + c
            if k >= e:
                k = k - e
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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
    arr, e = takeInput()
    c = int(stdin.readline().rstrip())
    leftRotate(arr, c, e)
    printList(arr, e)

    t -= 1
