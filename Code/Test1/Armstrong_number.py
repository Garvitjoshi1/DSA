def checkarmstrong(n):
    temp = n
    num = n
    # count digit
    dig = 0
    while n != 0:
        dig = dig + 1
        n = n // 10
    sum = 0
    while num != 0:
        ch = num % 10
        sum = sum + (ch ** dig)
        num = num // 10
    if temp == sum:
        return True
    else:
        return False


n = int(input())
if checkarmstrong(n):
    print('true')
else:
    print('false')
