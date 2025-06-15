from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    i = n - 1
    j = m - 1
    carry = 0

    k = len(output) - 1
    if n == 0 and m == 0:
        return 0
    while i >= 0 and j >= 0:
        output[k] = (arr1[i] + arr2[j] + carry) % 10
        carry = (arr1[i] + arr2[j] + carry) // 10
        k = k - 1
        i = i - 1
        j = j - 1

    while j >= 0:
        output[k] = (arr2[j] + carry) % 10
        carry = (arr2[j] + carry) // 10
        k = k - 1

        j = j - 1

    while i >= 0:
        output[k] = (arr1[i] + carry) % 10
        carry = (arr1[i] + carry) // 10
        k = k - 1
        i = i - 1

    output[0] = carry


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
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = (1 + max(n, m))
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1