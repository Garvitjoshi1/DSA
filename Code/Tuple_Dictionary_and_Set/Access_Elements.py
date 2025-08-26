a = {1: 2, 3: 4, 'list': [1, 23], "dict": {1: 2}}
print(a["list"])
b = a.get("list")
print(b)
print(a.get("li"))  # output: None because "li" is not present
print(a.get("li", 0))  # to avoid non we have on method we can pass the value we want.
print(a.keys())   # to get all keys at a time
print(a.values())  # to get all value at a time
print(a.items())  # to get the complete items we have in a list
# to get all the keys printed one by one:
for i in a:
    print(i, a[i])
for i in a.values():
    print(i)
# how to check if a key exist or not in key of dictionary
print("list" in a)
print("li" in a)
