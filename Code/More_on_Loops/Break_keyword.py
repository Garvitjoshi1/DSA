i = 1
while i < 10:
    if i == 5:
        break
    print(i)
    i = i + 1
# code means that it will stop working for i == 5;
#  but will work till i== 4.

i = 1
while i < 3:
    j = 1
    while j < 5:
        if j == 3:
            break
        print(j, end=" ")
        j = j + 1
    i = i + 1
