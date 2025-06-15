## Read input as specified in the question.
## Print output as specified in the question.

n=int(input())
for i in range(1,n+1):
    #for spaces
    sp = 1
    while (sp <= n - i):
        print(" ", end="")
        sp = sp + 1
    # increasing no
    start = i
    for j in range(1,i+1):
       print(start,end="")
       start=start+1
    # decreasing no
    st = 2 * i - 2
    for k in range(1, i):
        print(st,end="")
        st=st-1
    print()
