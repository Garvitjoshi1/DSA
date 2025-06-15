def fib(n):
    if n == 1 or n == 2:
        return 1
    fib_n = fib(n - 1) + fib(n - 2)
    return fib_n


n = int(input())
print(fib(n))
