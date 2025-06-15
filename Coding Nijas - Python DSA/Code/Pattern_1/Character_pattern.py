# k = int(input())
# x = ord('A')
# asciiTarget = x + k - 1
# targetChar = chr(asciiTarget)
# print(targetChar)
# <--------------------------------------------------->
# This was the basic concept of how you print the character pattern .


n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        x = chr(ord('A') + j - 1)
        print(x, end=' ')
        j = j + 1
    print()
    i = i + 1
