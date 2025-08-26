# syntax of list
li = [1, 2, 3]
print(type(li))
# or
li = [1, 2, ]
# or
# Due to storing different data at a time its a heterogeneous data
li = [1, 2, "Garvit", 2.4]
print(li)
# Access and change element in list
print(li[0], li[1], li[2])
# print(li[4]) line will give error saying item out of range
li[0] = 5
print(li)
# Slicing of list
# means it will print list value form index 1 to index 3-1, i,e till n-1.
print(li[1: 3])
