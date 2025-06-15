# Problem: Remove x from string
def removeX(string):
    if len(string) == 0:
        return string
    smallop = removeX(string[1:])
    if string[0] == 'x':
        return smallop
    else:
        return string[0] + smallop


string = input()
print(removeX(string))
