## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
n1 = (n + 1) / 2
n2 = n1 - 1
i = 1
while i <= n1:
    spaces = 1
    while spaces <= n1 - i:
        print(" ", end="")
        spaces = spaces + 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1
k = n2
while k >= 0:
    spaces = 0
    while spaces < n2 - k + 1:
        print(" ", end="")
        spaces = spaces + 1
    l = 0
    while l < 2 * k - 1:
        print("*", end="")
        l = l + 1
    print()
    k = k - 1
