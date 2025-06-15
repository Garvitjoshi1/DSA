from sys import stdin


def removeAllOccurrencesOfChar(string, ch):
    arr = string.split()
    n = len(arr)
    for i in range(n):
        if arr[i] == ch:
            string.replace(ch, i)
    return ''.join(arr)


# main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
