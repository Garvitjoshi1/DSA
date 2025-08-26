n = int(input())
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j = j + 1

    sp = 1
    while sp <= 2 * (n - i):
        print(' ', end='')
        sp = sp + 1

    p = i
    j = 1
    while j <= i:
        print(p, end='')
        p = p - 1
        j = j + 1

    print()
    i = i + 1