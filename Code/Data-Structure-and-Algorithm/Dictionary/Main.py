a = {"the":1, "a":5, 1000:"abc"}
print(type(a))
print(a)
print(len(a))
b = a.copy()
print(b)
# dict used to make given data to dictionary
c = dict([("the", 3), ("an", 23), (1000, "abc")])
print(c)
# first element is key second is value
d = dict.fromkeys(["abc", 32, 4], 10)
print(d)
# typecasting
myList= [("a",1),("b",2),("c",2)]
myDictionary= dict(myList)
print(myDictionary)
