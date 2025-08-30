s = "IceCreAm"
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = list(s)
l, r = 0, len(s)-1
while l < r:
    if s[l] not in v:
        l += 1
    elif s[r] not in v:
        r -= 1
    else:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
print(''.join(s))