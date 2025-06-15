def sum_digit(n):
    if len(n) == 0:
        return 0
    else:
        sum1 = sum_digit(n - 1)
        return sum1


n = int(input())
print(sum_digit(n))
