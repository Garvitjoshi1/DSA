from sys import stdin


def getCompressedString(input):
    n = len(string)
    li = []
    i = 1
    li.append(string[0])
    while i < n:
        if string[i] != string[i - 1]:
            li.append(string[i])
        i += 1

    count = [0] * 256
    var = -1
    char = []
    i = 0
    for i in string:
        count[ord(i)] += 1

    return count[ord(i)].join(li)


# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)