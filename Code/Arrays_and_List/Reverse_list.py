def reverse_1(li):
    length = len(li)
    for i in range(length // 2):
        li[i], li[length - i - 1] = li[length - i - 1], li[i]


# we can write the above line also as li[i], li[ - i - 1] = li[ - i - 1], li[i]


li = [1, 2, 3, 4, 5]
reverse_1(li)
print(li)


def reverse_2(li):
    length = len(li)
    for i in range(length // 2):
        li[i], li[- i - 1] = li[- i - 1], li[i]


# we can write the above line also as li[i], li[ - i - 1] = li[ - i - 1], li[i]


li = [1, 2, 3, 4, 5]
reverse_2(li)
print(li)


print(li)
print(li[-1::-1])
print(li[::-1])
