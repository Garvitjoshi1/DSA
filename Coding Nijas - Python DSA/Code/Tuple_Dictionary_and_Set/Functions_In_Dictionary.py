a = {1: 2, 3: 4, 'list': [1, 23], "dict": {1: 2}}
a["tuple"] = (1, 2, 3)  # we can add different data types in dictionary with any name
print(a)
a[1] = 10  # we can also update the values here.
print(a)
b = {3: 5, "the": 4, 2: 100}
c = a.update(b)
print(c)  # used when any of both the dictionary have them in common
print(a)
# also add all the value of b in a and vice_versa
print(a.pop(1))
