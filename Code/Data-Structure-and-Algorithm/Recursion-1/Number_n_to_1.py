def num_n_to_1(n):
    if n == 0:
        return 0
    print(n)
    num_n_to_1(n-1)


n = int(input())
num_n_to_1(n)
