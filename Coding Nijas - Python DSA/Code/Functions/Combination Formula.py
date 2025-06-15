def fact(j):
    n_factorial = 1
    for i in range(1, j + 1):
        n_factorial = n_factorial * i
    return n_factorial


n = int(input())
r = int(input())
n_fact = fact(n)
r_fact = fact(r)
n_r_fact = fact(n - r)
ans = n_fact // (r_fact * n_r_fact)
print(ans)


def nCr(a, b):
    n__fact = fact(a)
    r__fact = fact(b)
    n__r__fact = fact(a - b)
    return n__fact // (r__fact * n__r__fact)


print(nCr(5, 2))
