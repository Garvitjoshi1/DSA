## Read input as specified in the question.
## Print output as specified in the question.
n1 = 0
n2 = 1
count = int(input())
i = 2
n3 = 0
if count == 1:
    print(count)
else:
    while i <= count:
        i = i+1
        n3 = n1+n2
        n1 = n2
        n2 = n3
    print(n3)
