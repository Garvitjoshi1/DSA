# replace with given char
def replace_char(s, a, b):
    if len(s) == 0:
        return s
    output = replace_char(s[1:], a, b)
    if s[0] == a:
        return b + output
    else:
        return s[0] + output


s = 'garvit'
a = 'a'
b = 'x'
print(replace_char(s, a, b))
