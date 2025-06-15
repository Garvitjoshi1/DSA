def f(a, b, c=0):
    return a + b + c


print(f(1, 2, 3))
print(f(6, 7))

# def f(a=0, b, c):
#     return a + b + c
#  but this is not valid as null value can not be at the starting.
#
# print(f(1, 2, 3))
