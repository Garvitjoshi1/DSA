def checkNumber(arr, x):
    if x == arr[0]:
        return 'true'
    else:
        s = checkNumber(arr[1:], x)
        return s


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
