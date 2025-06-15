## Read input as specified in the question.
## Print output as specified in the question.
s = input().split()
l = []
for i in s:
    l.append(len(i))
print(s[l.index(min(l))])
