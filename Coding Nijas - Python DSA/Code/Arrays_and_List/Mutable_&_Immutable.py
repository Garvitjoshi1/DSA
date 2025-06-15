# <-------------------------Immutable------------------->
x = 3
a = 3
print(x)
print(id(x))
# this means how 2 variables refer to a single value.
print(id(a))
a = 4
# means that if value of variable is changed then its address/id is also changed.
print(id(a))
# <-------------------------Mutable------------------->
li = [1, 2, 3, 4, 5]
li2 = li
li2[4] = 7
print(li2)
print(id(li2[1]))
print(id(li[1]))
