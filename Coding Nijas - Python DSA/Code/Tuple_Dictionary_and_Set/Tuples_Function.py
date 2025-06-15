a = (1, 2, 3)
b = 4, 5
# for loop
# for i in a:
#     print(i)
print(1 in a)
print(7 in a)
# used to check value is present in tuple and provide answer in True and False
print(len(a))
# concatenation of tuples
c = a+b
print(c)
# or to present in form of tuple of tuples
d = (a, b)
print(d)
# to print a tuple multiple times
print(a*4)
# for minimum and maximum value of tuple
print(min(a))
print(max(a))
# also, for float and int we can find min and max but not in string and int
a = (1, 2.2)
print(max(a))
print(min(a))
# list to tuple
li = [1, 2, 3, 4, 5]
x = tuple(li)
print(x)
