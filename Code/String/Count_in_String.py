# count number of vowels, consonant, digits, and special character in string
def countInString(str):
    v, c, d, s = 0, 0, 0, 0
    for char in str:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            char = char.lower()
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                v += 1
            else:
                c += 1
        elif '0' <= char <= '9':
            d += 1
        else:
            s = s + 1
    return v, c, d, s

str = "hsdbadhxnjbws1235@$%^&% vbdsfu&^&$"
v, c, d, s = countInString(str)
print(v, c, d, s)
