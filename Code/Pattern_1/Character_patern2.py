n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        x = chr(ord('A') + j - 1)
        print(x, end='')
        j = j + 1
    print()
    i = i + 1

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         x = chr(ord('A') + i - 1)
#         print(x, end='')
#         j = j + 1
#     print()
#     i = i + 1
