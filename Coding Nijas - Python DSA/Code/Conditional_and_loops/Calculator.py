# Write your code here
while True:
    n = int(input())
    if n <= 6:
        if n == 1:
            a = int(input())
            b = int(input())
            sum = a + b
            print(sum)
        elif n == 2:
            a = int(input())
            b = int(input())
            sub = a - b
            print(sub)
        elif n == 3:
            a = int(input())
            b = int(input())
            pro = a * b
            print(pro)
        elif n == 4:
            a = int(input())
            b = int(input())
            val = a // b
            print(val)
        elif n == 5:
            a = int(input())
            b = int(input())
            rem = a % b
            print(rem)
        else:
            break
    else:
        print("Invalid Operation")
