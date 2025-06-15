def multi(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        n = a * b
        return n


a = int(input())
b = int(input())
print(multi(a, b))
