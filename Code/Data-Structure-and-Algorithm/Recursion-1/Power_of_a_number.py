def power(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * power(a, b - 1)


base, exp = input().split()
base = int(base)
exp = int(exp)
print(power(base, exp))
