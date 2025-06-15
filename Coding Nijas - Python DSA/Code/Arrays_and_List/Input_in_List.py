# n = int(input('Element you need in list: '))
# li = []
# for i in range(n):
#     curr = int(input())
#     li.append(curr)
# print('Your desired list is: ', li)
# c = input()
# # c is a string input
# a = c.split(' ')
# # c.split is used to split the string with a space.
# print(a)
# c = input()
# a = c.split()
# print(a)
# c = input()

# to print this all-in-one line
# li = [int(x) for x in input().split()]
# print(li)

# Sum of array/List :
n = int(input())
sum = 0
li = [int(x) for x in input().split()]
for ele in li:
    sum = sum+ele
print(sum)
