n = int(input())
k = 0
while k <= n:
    d = 2
    flag = False
    while d < k:
        if k % d == 0:
            flag = True
            break
        d = d + 1
    if not flag:
        print(k)
    k = k + 1
