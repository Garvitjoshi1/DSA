d = {1: "hi", "hello": 2, "How are you": 3, 1000: "good"}
print(len(d))
print(d[1])
print(d[1000])

b = d.copy()  # .copy is to print th dictionary to another dictionary and form a new one.
print(b)

d = dict.fromkeys(["abc", "Hl", "Garvit"])
print(d)
d = dict.fromkeys(["abc", "Hl", "Garvit"], 10)
print(d)
