# sum function code for 2 values
# def sum(a, b):
#     return a + b
#
#
# print(sum(1, 2))
# <================================================================>
# sum function code for n variables
def sum2(a, b, *more):
    print(a)
    print(b)
    ans = a + b
    for i in more:
        ans = ans + i
    return ans


print(sum2(2, 3, 4, 5))


def sum_diff(a, b):
    return a + b, a - b


d, e = sum_diff(4, 1)
print(d, e)
print(d)
print(e)
