n = int(input())
i = 1
while i <= n:
    j = 1
    Start = 'A' + i - 1
    while j <= i:
        print(chr(Start))
        j = j + 1
        Start = Start + 1
        print()
    i = i + 1
