n = int(input())
i = 1
p = 1
while i <= n:
    j = 1
    while j <= i:
        print(p, end=' ')
        p = p+1
        j = j+1
    print()
    i = i+1