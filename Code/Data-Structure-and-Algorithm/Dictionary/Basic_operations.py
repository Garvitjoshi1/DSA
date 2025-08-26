a = {1: 2, 3: 4, "list": [1, 2], "dict": {1: 2}}
print(a)
# print(a[0]) is invalid as there is no indexing
print(a["list"])
# is valid as in dict. all work is performed by keys.
print(a.get(1))
print(a.get("li"))  # return None as no value is present
print(a.keys())  # used to print all the keys of dict.
print(a.values())  # to print values
print(a.items())  # to print all keys and values
print("Values using iteration")
for i in a:
    print(i, a[i])
print("Values using iteration")
for i in a.values():
    print(i)
print("li" in a)  # to check given value is present or not in dict.

a['t'] = (1, 2, 3)
print(a)

a[1] = 10  # to update value
print(a)

b = {3: 5, 'the': 4, 2: 100}
a.update(b)
print(a)

a.pop('t')  # we need to provide key here we remove
print(a)

del a[1]  # to delete the provided key
print(a)

a.clear()
# it clears but not delete
print(a)

del a  # will give error as it is clear in prev. line
