def geometric_sum(k):
    if k == 0:
        return 1.00000
    geometricSum = geometric_sum(k - 1) + (1 / pow(2, k))
    return geometricSum


k = int(input())
if k <= 5:
    c = format(geometric_sum(k), '.5f')
    print(c)
else:
    print(round(geometric_sum(k), k - 1))
