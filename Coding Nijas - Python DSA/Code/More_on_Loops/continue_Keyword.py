n = int(input())
for i in range(2, n + 1, 2):
    if i % 7 == 0:
        continue
    print(i, i, end=' ')
    print()
