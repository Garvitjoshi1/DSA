li = [1, 2, 3, 4, 5]
# li[0] or any positive index provide value from starting
print(li[0])
# but li[-1] or any negative index provide value from last of list.
print(li[-1])
print(li[-5])
print(li[-3])
# Sequencing in list is done by-->
#             list[start:end:step]
# runs till start to end-1.
print(li[1:5:1])
# [2, 3, 4, 5] is the ans to the above one.
print(li[1:5:2])
# [2, 4] is the ans to next one.
print(li[1:])
# have by default increment of 1, and runs till the last index.
print(li[:3])
# this means its start is index 0 to 2 and default increment by 1.
print(li[-1:])
print(li[-3:-1])
