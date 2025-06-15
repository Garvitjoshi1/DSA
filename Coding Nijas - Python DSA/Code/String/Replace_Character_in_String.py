# In this question you need to replace a character with the given character
# char1 = 'a'
# str = "a b c d e"
# char2 = 'e'
# str = "e b c d e"

def replace(str1, char1, char2):
    newStr = ""
    for char in str1:
        if char == char1:
            newStr += char2
        else:
            newStr += char
    return newStr


str = "fsafsavxz"
str = replace(str, 's', 'd')
print(str)
