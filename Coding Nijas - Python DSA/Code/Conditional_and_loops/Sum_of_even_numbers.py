n = int(input())
s = 0
if n == 1:
    print(0)
while n > 0:
    s = s + n
    n -= 2
print(s)
