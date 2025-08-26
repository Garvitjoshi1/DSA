s = "Garvit"
print(s[1:4:])
# 1 is start value, 4 is end value, last blank one is increment by 1 which is default.
print(s[-1])
print(s[-5:-1:])
# it does not give error for high slicing value rather than that it provide the element till its end only.
print(s[0:10:])
# to print string in reverse
h = s[::-1]
print(h)
