def first_n_numbers(n):
    if n == 0:
        return
    first_n_numbers(n - 1)
    print(n)


n = int(input())
print(first_n_numbers(n))
