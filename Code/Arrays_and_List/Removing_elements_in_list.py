li = [5, 7, 2, 'Garvit', 2.4, 'Hello', 10, 15, [9, 10, 11], 9, 10, 11]
li.remove(2)
# use to remove values.
print(li)
li.append(5)
print(li)
li.remove(5)
# this line tell the first occurring value in list is removed first
print(li)
li.pop()
# .pop used to remove the last most value form the list.
print(li)
li.pop(2)
# .pop(index) we can also provide the index number of the value we want to delete
print(li)
# li.pop(18) like this type of value provide error because li index is not till 18.
print(len(li))
# .len used to print the length of list.
