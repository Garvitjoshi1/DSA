# To print multiples of 3.
# a = int(input())
# b = int(input())
# for i in range(a, b + 1, 1):
#     if i % 3 == 0:
#         print(i)

# more efficient code could be-->
# To print multiples of 3 from any starting number
a = int(input())
b = int(input())
if a % 3 == 0:
    s = a
elif a % 3 == 1:
    s = a + 2
else:
    s = a + 1
for i in range(s, b + 1, 3):
    print(i)
