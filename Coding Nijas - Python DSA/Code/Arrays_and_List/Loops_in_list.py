li = [1, 2, 'Garvit', 9, 10, 11, 'Ankush']
# basic code
for i in range(len(li)):
    print(li[i])
# this code is to print from any index value you want.
for i in range(2, len(li)):
    print(li[i])
# Easiest code to print all element
for ele in li:
    print(ele)
# using concept of slicing, to print from desired index.
for ele in li[2:]:
    print(ele)
for ele in li[2:5]:
    print(ele)
