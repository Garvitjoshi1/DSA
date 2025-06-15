# Insert and append elements in list
li = [5, 2, 'Garvit', 2.4]
li.append('Hello')
# .append use to add value a last of list
print(li)
li.insert(1, 7)
# .insert use to insert value at the index you want insert(index, value)
print(li)
li.insert(6, 10)
# .insert also add value to last index of list.
print(li)
li.insert(9, 15)
# if our list is till index 6, and we provide value to insert at index 9 it add it at index 7, without providing error.
print(li)
li.append([9, 10, 11])
# used to add list inside the list
print(li)
li.extend((9, 10, 11))
# used to add multiple values to list at a time.
print(li)
